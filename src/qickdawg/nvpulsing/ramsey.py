'''
Ramsey
=======================================================================
An NVAveragerProgram class acquires data for ramsey, i.e. 
a mw pluse sequence pi/2 - delay - pi/2 . This measurement is
performed twice with an alternative phase of 0 and 180 for the last pi/2 pulse 
'''


from .nvaverageprogram import NVAveragerProgram
from .nvqicksweep import NVQickSweep

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


class Ramsey(NVAveragerProgram):
    '''
    An NVAveragerProgram class that generates and executes a sequence used
    to measure ramsey

    Parameters
    ----------
    soccfg : `qick.QickConfig`
    cfg : `.NVConfiguration`
        instance of `.NVConfiguration` class with attributes:
        .adc_channel : int
            ADC channel for gathering data, usually 0 or 1
        .mw_channel : int
            qick channel that provides microwave excitation
            0 or 1 for RFSoC4x2
            0 to 6 for ZCU111 or ZCU216
        .mw_nqz : int
            nyquist zone for microwave generator (1 or 2)
        .mw_gain : int
            gain of micrwave channel, in register values, from 0 to 2**15-1

        .pre_init : bool
            boolian value that indicates whether to pre-pulse the laser to initialize
            the spin state

        .relax_delay_treg : int
            Time between on/off cycles and reps in register units
        .readout_length_treg : int
            Time for which the adc accumulates data in register units
        .laser_readout_offset_treg : int
            Time offset between initial laser triggering and readout start

        .laser_gate_pmod : int
            PMOD channel used to trigger laser source usually 0 to 6

    Returns
    `.Ramsey`
        An instance of Rmasey with compiled assembly language

    Methods
    -------
    initialize
        method that generates the assembly code that setups the adcs &  mw generators,
        and performs other one-off setps
    body
        method that generates the assembly code that exectues in the middle of each sweep
        and rep
    plot_sequence
        generates a plot labeled with self.cfg attributes or the required inputs
    time_per_rep
        returns the approximatetime for one rep to complete
    total_time
        returns the approximate total time for the entire program to complete
    '''
    required_cfg = [
        "adc_channel",
        "readout_integration_treg",
        "mw_channel",
        "mw_nqz",
        "mw_pi2_treg",
        "mw_gain",
        "delay_start_treg",
        "delay_end_treg",
        "nsweep_points",
        "pre_init",
        "laser_gate_pmod",
        "laser_on_treg",
        "relax_delay_treg",
        "reps",
        "readout_reference_start_treg",
        "laser_readout_offset_treg",
        "mw_readout_delay_treg"]

    def initialize(self):
        '''Method that generates the assembly code that is sets up adcs and sources.

        For Ramsey this:
        1. Configures the adc to acquire points for self.cfg.readout_integration_t#. 
        2. Configures the microwave channel 
        3. Configures the sweep parameters
        4. Initiailzes the spin state with a laser pulse
        '''
        self.check_cfg()

        self.setup_readout()
        # Get registers for mw

        self.declare_gen(ch=self.cfg.mw_channel, nqz=self.cfg.mw_nqz)        

        # Setup pulse defaults microwave
        self.default_pulse_registers(
            ch=self.cfg.mw_channel,
            style='const',
            freq=self.cfg.mw_freg,
            length=self.cfg.mw_pi2_treg,
            gain=self.cfg.mw_gain)

        self.set_pulse_registers(ch=self.cfg.mw_channel,
                                 phase=0)

        # Addd loops
        self.delay_register = self.new_gen_reg(self.cfg.mw_channel,
                                               name='delay', 
                                               init_val=self.cfg.delay_start_treg)

        self.mw_time_register = self.get_gen_reg(self.cfg.mw_channel, 
                                                 name='t')

        self.add_sweep(NVQickSweep(
            self, 
            self.delay_register,
            self.cfg.delay_start_treg, 
            self.cfg.delay_end_treg,
            self.cfg.nsweep_points))

        self.synci(100)  # give processor some time to configure pulses
        if (self.cfg.ddr4 is True) or (self.cfg.mr is True):
            self.trigger(ddr4=self.cfg.ddr4, mr=self.cfg.mr, adc_trig_offset=0)
        self.synci(100)

        if self.cfg.pre_init:
            self.trigger(
                pins=[self.cfg.laser_gate_pmod],
                width=self.cfg.laser_on_treg,
                adc_trig_offset=0
            )           
            self.sync_all(self.cfg.laser_on_treg + self.cfg.relax_delay_treg)

    def body(self):
        '''
        Method that generates the assembly code that is looped over or repeated. 
        For Ramsey this peforms four measurements at a time and does two pulse
        sequences differing only by the phase of the final pulse.  The sequences is:
        1. Set pulse phase to 0
        2. Pulse mw for pi/2
        5. delay by variable delay time
        6. pulse mw for pi/2 (on second sequence change the phase to 180 degrees)
        7. Perform readout
        8. Loop over delay times
        9. Loop over reps
        10. Loop over rounds
        '''

        self.set_pulse_registers(ch=self.cfg.mw_channel, phase=self.deg2reg(0))
        ## Pulse Sequence 1
        # first reset phase to x
        # pi/2 - x
        self.pulse(ch=self.cfg.mw_channel)
        self.sync_all()
        # delay
        self.sync(self.delay_register.page, self.delay_register.addr)
        # pi/2 - x
        self.pulse(ch=self.cfg.mw_channel)
        self.sync_all(self.cfg.mw_readout_delay_treg)
        # Readout           
        self.ttl_readout()

        ## Pulse sequence 2
        # Second pi/2 pulse is in the -x direction
        # pi/2 - x
        self.pulse(ch=self.cfg.mw_channel)
        self.sync_all()
        # delay
        self.sync(self.delay_register.page, self.delay_register.addr)
        # pi/2 - x
        self.set_pulse_registers(ch=self.cfg.mw_channel, phase=self.deg2reg(180))
        self.pulse(ch=self.cfg.mw_channel)
        self.sync_all()
        self.sync_all(self.cfg.mw_readout_delay_treg)

        # Readout           
        self.ttl_readout()

    def acquire(self, raw_data=False, *arg, **kwarg):

        data = super().acquire(readouts_per_experiment=4, *arg, **kwarg)

        if raw_data is False:
            data = self.analyze_pulse_sequence(data)

        return data

    def time_per_rep(self):

        pass

    def plot_sequence(cfg=None):
        '''
        Function that plots the pulse sequence generated by this program

        Parameters
        ----------
        cfg: `.NVConfiguration` or None(default None)
            If None, this plots the squence with configuration labels
            If a `.NVConfiguration` object is supplied, the configuraiton value are added to the plot
        '''
        graphics_folder = os.path.join(os.path.dirname(__file__), 'graphics')
        image_path = os.path.join(graphics_folder, 'Ramsey.png')

        if cfg is None:
            plt.figure(figsize=(12, 12))
            plt.axis('off')
            plt.imshow(mpimg.imread(image_path))
            plt.text(500, 700, "config.reps", fontsize=14)
            plt.text(270, 365, "delay", fontsize=10)
            plt.text(400, 385, "  config.readout_reference_start", fontsize=10)
            plt.text(200, 340, "mw_pi2", fontsize=10)

            plt.text(310, 340, " mw_pi2", fontsize=10)
            plt.text(260, 465, "config.laser_readout_offset", fontsize=10)
            plt.text(390, 340, "config.readout_integration", fontsize=10)
            plt.text(650, 340, "config.readout_integration", fontsize=10)
            plt.text(850, 340, "config.relax_delay", fontsize=10)
            plt.text(400, 430, "config.laser_on", fontsize=10)

            string = "Sweep delay linearly from config.delay_start to config.delay_end in config.nsweep_points \n"
            string += "                            with scaling given by config.scaling_mode"
            plt.text(220, 605, string, fontsize=12)

            plt.title("             Ramsey Pulse Sequence", fontsize=20)
        else:
            plt.figure(figsize=(12, 12))
            plt.axis('off')
            plt.imshow(mpimg.imread(image_path))
            plt.text(450, 700, "Repeat {} times".format(cfg.reps), fontsize=14)
            plt.text(270, 365, "delay", fontsize=10)
            plt.text(385, 385, "  readout_reference_start = {} us".format(cfg.readout_reference_start_tus), fontsize=10)
            plt.text(200, 340, "pi/2", fontsize=12)
            plt.text(310, 340, " pi/2", fontsize=12)
            plt.text(240, 465, "laser_readout_offset = {} treg".format(cfg.laser_readout_offset_treg), fontsize=10)
            plt.text(390, 337, "readout_integration = {} us".format(str(cfg.readout_integration_tus)[:4]), fontsize=10)
            plt.text(650, 357, "readout_integration \n = {} us".format(
                str(cfg.readout_integration_tus)[:4]), fontsize=10)
            plt.text(850, 357, "relax_delay \n = {} us".format(str(cfg.relax_delay_tus)[:4]), fontsize=10)
            plt.text(400, 430, "laser_on = {} us".format(cfg.laser_on_tus), fontsize=12)

            string = f"    Sweep delay linearly from {int(cfg.delay_start_tns)} "
            string += "to { int(cfg.delay_end_tns)}          \n"
            string += "                     in {cfg.nsweep_points} steps"
            plt.text(375, 605, string, fontsize=12)
            plt.title("               Ramsey Pulse Sequence", fontsize=20)
