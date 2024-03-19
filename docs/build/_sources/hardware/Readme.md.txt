
<p align="center">
    <img src="./../_static/QD_logo.png"
        alt="QD logo"
        width="300x"/>
</p>




# Hardware Setup
In this document we outline the hardware setup for an all-in-one RFSoC4x2 enclosure. We show:

1. Enclosure Overview 

    a. Components list 

2. Enclosure Modification 

    a. Drill Holes

    b. 3D Printed Cages 

    c. Low-Frequency Differential Amplifier 

    d. BNC to PMOD TTL 

3. Assembly 

    a. Power 

    b. Securing the RFSoC4x2

    c. Securing 3D printed cages 

    d. Front Panel Assembly

    e. Input Signal Assembly 

    f. Router and Ethernet Connection



## 1. Enclosure Overview

<p align="center">
    <img src="./../_static/Enclosure_Schematic.png"
        alt ="Fully assembled RFSoC4x2 Enclosure"
        width="1000x"/>
    
</p>

***1a. Components***
- [Bud Industries CH-14404 Enclosure](https://www.digikey.com/en/products/detail/bud-industries/CH-14404/428959)
- [RFSoC4x2 FPGA](https://www.xilinx.com/support/university/xup-boards/RFSoC4x2.html) 
- [Router](https://www.amazon.com/TP-Link-Integrated-Lightening-Protection-TL-R605/dp/B08QTXNWZ1/ref=asc_df_B08QTXNWZ1/?tag=hyprod-20&linkCode=df0&hvadid=475692076734&hvpos=&hvnetw=g&hvrand=3761702075041011209&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1022494&hvtargid=pla-1149738264234&psc=1)
- [DC Voltage Supply](https://www.digikey.com/en/products/detail/cui-inc/PYB30-Q24-T315-U/4477530) 
- Low-Frequency Differential Amplifier [Texas Instruments LMH5401EVM](https://www.digikey.com/en/products/detail/texas-instruments/LMH5401EVM/5031896?s=N4IgTCBcDaIDIFkASBWALABgIwFEBqCIAugL5A)
- 3D printed Router Cage
- 3D printed Low-Frequency Differential Amplifier Holder
- [Ethernet Pass-Through](https://www.digikey.com/en/products/detail/amphenol-ltw/RCP-5SPFFH-TCU7001/5253168)
- [Power Pass-Through](https://www.digikey.com/en/products/detail/tensility-international-corp/54-00151/9829987)
- [6 SMA Pass-Through](https://www.digikey.com/en/products/detail/amphenol-rf/132170/1011921) 
- [8 BNC Pass-Through](https://www.digikey.com/en/products/detail/adam-tech/RF1-106-D-00-50-HDW/9830449)
- [Pig Tail Power Cord](https://www.digikey.com/en/products/detail/tensility-international-corp/10-02937/9686418)
- [1 x Flexible SMA Cable](https://www.digikey.com/en/products/detail/cinch-connectivity-solutions-johnson/415-0025-012/457078) 
- [2 x Rigid SMA Cable](https://www.digikey.com/en/products/detail/cinch-connectivity-solutions-johnson/415-0081-006/1014585) 
- [1' Ethernet Cord](https://www.digikey.com/en/products/detail/panduit-corp/UTP28CH1/7981686) 
- [1.64' Ethernet Cord](https://www.digikey.com/en/products/detail/metz-connect-usa-inc/13084U0533-E/13402445) 
- [16 x 4-40 Screws (0.25")](https://www.digikey.com/en/products/detail/keystone-electronics/9900/317321)
- [8 x 4-40 0.5" Hex Standoff Pilar](https://www.digikey.com/en/products/detail/keystone-electronics/1450C/303581)
- [Wire](https://www.amazon.com/AWG-Stranded-Wire-Kit-Pre-Tinned/dp/B07T4SYVYG/ref=sr_1_5?crid=1PFWR4LYQI3YD&keywords=wire+set&qid=1704903898&sprefix=wire+set+soldering%2Caps%2C624&sr=8-5)
- [Heat Shrink](https://www.amazon.com/Ginsco-580-pcs-Assorted-Sleeving/dp/B01MFA3OFA/ref=sr_1_3?crid=14F6I0UNEEKPJ&keywords=heat+shrink+tubing&qid=1704903836&sprefix=heat+sh%2Caps%2C422&sr=8-3
) 
- PMOD Connectors 
- [Solder](https://www.amazon.com/MAIYUM-63-37-Solder-Electrical-Soldering/dp/B075WB98FJ/ref=sr_1_5?keywords=solder&qid=1704903785&sr=8-5
)
- [Zip Ties with Adhesive Mounts](https://www.amazon.com/Adhesive-Backed-Mounts-holder-Anchor-Holders/dp/B07Z79LHJC/ref=asc_df_B07Z79LHJC?tag=bingshoppinga-20&linkCode=df0&hvadid=80127002044380&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=&hvtargid=pla-4583726547458434&th=1)


<!-- - Laser Cut Voltage Divider 
    - [1 SMA Side Mount](https://www.digikey.com/en/products/detail/mueller-electric-co/BU-1420701801/9950116)
    - 15 Ohm Resistor 
    - 2 x 56 Ohm Resistors
    - 68 Ohm Resistor 
    - 270 Ohm Resistor    
    - 390 Ohm Resistor 
    - [Double Sided Proto Board Copper Clad 5" X 3"](https://www.digikey.com/en/products/detail/mg-chemicals/540/2177370) -->


`parts_all.xlsx` lists the source, quantity, and cost for hardware modification components. `parts_digikey.xlsx` can be uploaded directly into the [Digikey shopping cart](https://www.digikey.com/ordering/ShoppingCart) for easy purchase of Digikey items. 

## 2. Enclosure Modification ##

### 2a. Drilling Holes ###
Drill holes are made in the main body of the CH-14404 enclosure to secure 3D printed cages, the RFSoC4x2, an ethernet pass-through, and a power pass-through. Drill holes are also made in the front panel of the CH-144-4 enclosure for 6 SMA pass-throughs and 8 BNC pass-throughs. The schematic below shows the position and purpose of each drill hole. `Enclosure_Main.STEP` and `Enclosure_Front.STEP` give the exact size and position of each drill hole (found in the hardware folder). 

<p align="center">
    <img src="./../_static/Enclosure.png"
        alt ="Enclosure CAD diagram"
        width="700px"
        />
        <figcaption>
        Bud Industries CH-14404 Enclosure Screw Hole CAD Schematic <br> 
        <li><b>A = RFSoC4x2</b> with the PMOD oriented toward the enclosure front <br></li>
        <li><b>B = Router</b> with the ethernet ports facing the RFSoC4x2 <br></li>
        <li><b>Optional</b><br></li>
        <ul>
            <li><b>C = DC Power Supply</b> supply with voltage outputs orientated towards the RFSoC4x2</li>
            <li><b>D = Voltage Divider</b></li>
            <li> An external power supply can be used rather than C) DC Power Supply and D) Voltage Divider
        </ul>
        <li><b>E = Low-Frequency Differential Amplifier </b> with V+ and V- facing the RFSoC4x2</li>
        <li><b>F = Ethernet Pass-Through</b></li>
        <li><b>G = Power Pass-Through</b></li>
        </figcaption>
</p>
<p align="center">
    <img src="./../_static/Front_Panel.png"
        alt ="Enclosure Front Panel CAD Schematic",
        width="1000px"
        />
        <figcaption>CH-14404 Enclosure Front Panel pass-through schematic. 6 SMA pass-throughs (Left) and 8 BNC pass-throughs (Right). <br> 
</figcaption>
</p>


### 2b. 3D Printed Cages ###
The router and low-frequency differential amplifier are secured in the enclosure using 3D printed cages. It is especially important to immobilize the low-frequency differential amplifier since the wires and solder for the RFSoC4x2 to low-frequency differential amplifier connection are very delicate. 

The 3D printed low-frequency differential amplifier holder is made of `Low_Freq_Diff_Amp_Base.STEP` and `Low_Freq_Diff_Amp_Top.STEP` in the main hardware folder. Print these parts at 0.16mm tolerance. The low-frequency differential amplifier sits in the 3D printed base with the loops for V+, V-, and ground pointing down. The 3D printed top should be snug over the top of the 3D printed base. In a later step, the 3D printed low-frequency differential amplifier holder will be secured to the enclosure base with screws. 

<div style="display: flex; justify-content: center;">
    <div style="text-align: center;">
        <div style="display: flex;">
            <div style="margin-right: 10px;">
                <img src="./../_static/low_frequency_diff_amp-1.png" alt="Diff Amp Holder Base" style="width: 75%;">
                <figcaption> 3D printed low-frequency differential amplifier holder base</figcaption>
            </div>
            <div>
                <img src="./../_static/low_frequency_diff_amp_top-1.png" alt="Diff Amp Holder Top" style="width: 75%;">
                <figcaption> 3D printed low-frequency differential amplifier holder top</figcaption>
            </div>
        </div>
    </div>
</div>


<br></br>

`Router_Holder.STEP` is the CAD part for the router holder and is found in the main hardware folder. Printing tolerance of 0.2mm is adequate for the router holder. The holder sits over the router and is held in place by screws from the underside of the enclosure into the part's legs. 


<div style="text-align: center;">
    <img src="./../_static/router_holder-1.png" alt="Router Holder" width="300px">
    <figcaption style="text-align: center;">3D printed router holder</figcaption>
</div>




### 2c. Low-Frequency Differential Amplifier ###
to bypass the high-pass filter inherent to the analog to digital converters (ADCs) on the RFSOC4x2. 
Recall from the installation readme that the balun and capacitors on the analog-to-digital converters (ADCs) act as a high-pass filter, which filters our the low-frequency experimental defect data. The balun and capacitor need to be removed from one ADC to read in experiment data. Additionally, a low-frequency differential amplifier is required to process the low-frequency signal input after the balun has been removed. Follow step 1a in the installation readme to remove or bypass the balun and capacitors for one of the ADCs if not yet done. Now follow the modified step 1b to connect the low-frequency differential amplifier with the 3D printed holder for the low-frequency differential amplifier.  

### Modified Installation Readme 1b. <br> Connect the low-frequency differential amplifier 

<div style="text-align: center;">
    <img src="./../_static/differential_amp.PNG"
        alt="Diff Amp Circuit Schematic"
        width="450px"/>
    <p style="text-align: center;">Texas Instruments LMH5401EVM low-frequency differential amplifier schematic with bias voltage for the RFSoC4x2</p>
</div>

To connect the low-frequency differential amplifier to the RFSoC4x2,

- solder a 3.3 V input wire to the red V+ post on the low-frequency differential amplifier
- solder a -1.8 V input wire to the yellow V- post on the low-frequency differential amplifier
- solder a ground wire to either the TPG1 or TPG2 post on the low-frequency amplifier
- screw a 0.7 V SMA wire to the Vcm (V common) SMA head on the top of the low-frequency differential amplifier
- `MODIFIED - with the posts facing down, feed the soldered V+, V-, and ground wires through the base of the low-frequency differential amplifier 3D printed holder, and push the low-frequency differential amplifier down so that it is snug in the base`
- cut a semi-flexible SMA cable in half and strip the insulation off of both ends to expose the center conductor 
- screw the SMA heads of the cut SMA cable to Vp and Vm SMA heads on the low-frequency differential amplifier--screwing on the SMA cables now will limit the torsion on our delicate soldering in the next steps
- take the SMA cables attached to the low-frequency differential amplifier and solder them to the RFSoC4x2
    - Vp should be solder to the top right solder pad
    - Vm should be soldered to the middle right solder pad 

The image below is the circuit diagram for the RFSoC4x2. The top right solder pad--the pad for Vp--is labeled `6`. The middle right solder pad--the pad for Vm--is labeled `5`


<div style="text-align: center;">
    <img src="./../_static/balun_surgery_2.PNG"
        alt="Balun Surgery"
        width="1000px"/>     
    <p style="text-align: center;">(Top Left) 6 contact pads underneath the balun (Bottom Left) Vm input soldered to pad 5 and Vp input soldered to pad 6 (Right) Inputs from low-frequency differential amplifier soldered to RFSoC4x2 ADC D</p>
</div>



Note that you can instead leave the balun in place and directly solder coax cables to the capacitor terminals, however, this is more difficult and it is easy to destroy the capacitor terminals with the solder iron. 

### 2d. BNC to PMOD TTL ###

To use the PMOD to control a laser with digital TTLs we need to connect the PMOD to BNC on the front panel of the enclosure. To do so,
- select a BNC pass-through to be inserted to the front panel
- take a PMOD male to male connector and cut off one end
- strip the insulation from the cut end of the PMOD connector 
- solder the exposed PMOD connector wire to the cup of the BNC connector 
- secure the BNC pass-through to the enclosure front panel using the provided washer and nut
- the remaining PMOD connector male end can be plugged into the RFSoC4x2 PMOD 


<div style="display: flex; align-items: center;">
    <div style="flex: 1; text-align: center;">
        <img src="./../_static/BNC_to_ttl.jpg" alt="BNC to TTL Physical" style="max-width: 300px;">
        <p>BNC to TTl connection in the RFSoC4x2 enclosure</p>
    </div>
    <div style="flex: 1; text-align: center;">
        <img src="./../_static/BNC_to_ttl_handdrawn.png" alt="BNC to TTL Drawing" style="max-width: 300px;">
        <p>Schematic for soldering PMOD cable to BNC head. Single ended male PMOD soldered to BNC cup. </p>
    </div>
</div>


## 3. Assembling the Components ##



### 3a. Power 
A single power source is plugged into the power pass-through in the back of the enclosure and pig-tail power splitters are used to power the RFSoC4x2, router, and optional internal low-frequency differential amplifier voltage supply. The power cord supplied with the RFSoC4x2 provides more voltage than necessary thus this source can be used to power the RFSoC4x2, router, and optional internal low-frequency differential amplifier voltage supply. To create the single power plug in:

- remove the hex nut and washer from the power pass-through jack (1 in schematic below)
- push the power pass-through jack through drill hole G (schematic 2a above) from the outside of the enclosure to the inside
- place washer back on the power pass-through jack and tighten the hex nut, the pass-through should be secured to the wall of the enclosure now
- measure and trim the two or three pigtail power cords (2 in schematic below). The power cords need to reach the router power input, RFSoC4x2 power input, and optional voltage supply. Refer to  schematic 2a above. to estimate distances. 
- solder two or three pigtails to the head of the power pass-through, connecting positive wires to the center jack and negative wires to the outer loop (3 and 4, respectively, in schematic below)


<div style="text-align: center;">
    <div style="display: inline-block; text-align: center; margin-right: 20px;">
        <img src="./../_static/pig_tail_power_passthrough.jpg"
            alt="Power Split Physical"
            width="500px"/>    
        <p>Power pass-through and pig-tail power splitting in the RFSoC4x2 enclosure. Power is split to the RFSoC4x2, router, and voltage source.</p>
    </div>
    <div style="display: inline-block; text-align: center;">
        <img src="./../_static/power_pass_through_hand_drawn.png"
            alt="Power Split Diagram"
            width="500px"/>    
        <p>Schematic for soldering pigtail power wires to the power pass-through. 1) hex nut washer 2) pig-tail power cords 3) power pass-through center jack 4) power pass-through ground ring </p>
    </div>
</div>



### 3b. Securing the RFSoC4x2
Screws and hex standoff pillars are used to support and secure the RFSoC4x2 in the enclosure. To do so,
- pass a screw through an edge screw hole in the RFSoC4x2 into a hex pillar placed underneath the board, repeat for each of the 8 perimeter screw holes
- place the RFSoC4x2 in the enclosure in spot A (schematic 2a) with the PMODs facing the open end of the enclosure
- screw 8 x 4-40 0.25" up through the bottom of the enclosure into the bottom of the 8 x 0.5" hex pillars 
- tighten the screws until the RFSoC4x2 is secure 


### 3c. Securing 3D Printed Cages

To secure the 3D printed cage for the router,
- place the router inside enclosure in spot B (schematic 2a above) with the ethernet ports facing the RFSoC4x2
- place the 3D printed router cage on top of the router
- screw 4 4-40 0.25" screws through the bottom of the enclosure into the legs of the 3D printed router cage. Tighten the screws until the router is secure

To secure the 3D printed support for the low-frequency differential amplifier,
- place the low-frequency differential amplifier in the 3D printed base in the enclosure in spot E (schematic 2a above))
- screw 4 4-40 0.25" screws through the bottom of the enclosure into the legs of the 3D printed low-frequency differential amplifier. Tighten the screws until the router is secure 

### 3d. Front Panel Assembly

With the holes drilled in the CH-14404 enclosure front panel BNC and SMA pass-throughs can be secured in place. To do so, 
- remove the washers and nuts from 6 SMA pass-throughs and 8 BNC pass-throughs
- through the front pass of the panel, place 6 SMA in the smaller left hand drill holes and 8 BNC in the right hand drill holes (schematic 2a)
- from the backside of the panel put the washers and nuts back on the SMA and BNC pass-throughs and tighten to secure

The SMA and BNC pass-throughs should be secured in place on the front enclosure panel now. 


<div style="text-align: center;">
    <img src="./../_static/enclosure_front_real.jpg"
        alt="Front Panel Real"
        width="800px"/>     
    <img src="./../_static/Front_Panel.png"
        width="800px"/>
    <p>Front panel of the RFSoC4x2 enclosure. Silk-screening was used to label SMA and BNC ports</p>
</div>


### 3e. Input Signal Assembly 

To connect the input signal to the RFSoC4x2, 

- screw one end of a rigid SMA cable to the inside end of a SMA pass through on the front panel
- screw the other end of the rigid SMA cable to the signal in SMA head on the low-frequency differential amplifier (IN+)

<div style="display: flex; align-items: center;">
    <div style="flex: 1; text-align: center;">
        <img src="./../_static/input_and_diff_hookup.jpg" alt="Input/Output Connection Physical" style="max-width: 400px;">
        <p>Input and output connections inside the RFSoC4x2 enclosure</p>
    </div>
    <div style="flex: 1; text-align: center;">
        <img src="./../_static/connection_hand_drawn.png" alt="Input/Output Connection Drawing" style="max-width: 474.5px;">
        <p>Schematic of input and output connections in the RFSoC4x2 enclosure</p>
    </div>
</div>


### 3f. Router and Ethernet Connection 

To add the ethernet pass-through to the enclosure:
- remove the washer from the ethernet pass-through base
- push the base of the ethernet pass-through through drill hole F from the outside of the enclosure
- screw the washer back on the ethernet-pass through from the inside of the enclosure

The ethernet-pass through should now be secured to the wall of the enclosure. To connect the lab control computer to the RFSoC4x2, 

- connect the router from the lab control computer to the ethernet pass through 
- connect an ethernet cord from the ethernet pass through to the router
- connect an ethernet cord from the router to the RFSoC4x2

Now the lab control computer can be used to communicate with and control with RFSoC4x2. 

