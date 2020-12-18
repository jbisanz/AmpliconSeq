# Optional Protocol 4 - Ampure XP amplicon clean up

## Theory
If significant primer dimer formation has occured, these will be quantified by the picogreen assay and lead to poor normalization. If >=25 cycles of PCR have been run during primary PCR, or if during QC, significant primer dimers are observed then this protocol is recommended. Depending on the ratio of beads to DNA volume, a size selection is possible which will remove small DNA. This protocol is set up to use a 0.7x volume; however, this can be adjusted in the script. The defaults in the script will assume you have 20ul amplicon to clean up and will use 14ul beads (0.7x).

## Automated Method

### Materials
- [ ] Ampure XP clean up beads (A63881) *Note: these can be made from scratch for significantly cheaper but may have less consistent size-selection properties*
- [ ] [Opentrons OT2](https://opentrons.com/ot-2)
- [ ] [Opentrons 8-channel 300ul pipette head mounted on right (gen2)](https://shop.opentrons.com/collections/ot-2-robot/products/8-channel-electronic-pipette)
- [ ] [Opentrons Magnetic Capture Module (Gen2)](https://opentrons.com/modules/magnetic-module/)
- [ ] 4 x [Opentrons filter 200ul tips](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-200ul-filter-tips)
- [ ] 1 x USA Scientific 12 Well Reservoir 22 mL (USA Scientific 1061-8150) 
- [ ] 1 x Agilent 1 well 290 mL reservoirs (Agilent 201252-100) **OR** use an empty tip box lid
- [ ] 100% Ethanol
- [ ] Nuclease Free Water
- [ ] Bio-Rad 96 Well Plate 200 µL skirted PCR plate  (Biorad hsp9601) 

### Protocol
- [ ] Prepare fresh 80% ethanol and put in columns 2 and 3 of the 12 well reservoir.
- [ ] Add appropriate volume of beads to well 1 and ensure they are well mixed (bead volume/sample * Nsamples * 1.2)
- [ ] Add appropriate volume of water to well 4 (elution volume * Nsamples * 1.2)
- [ ] Set up OT2 according to Figure 1 below.
- [ ] Obtain a copy of scripts/O4_AmpureXPWash.py
- [ ] Modify lines 15-28 as required with close attention to desired bead volumes and elution volumes.
- [ ] Calibrate all deck positions and run method. **Estimated run time X min**
- [ ] After execution dispose of waste and clean out tip container

## Manual Method
### Materials
- [ ] Ampure XP clean up beads (A63881) *Note: these can be made from scratch for significantly cheaper but may have less consistent size-selection properties**
- [ ] 8x200ul multichannel
- [ ] 5 boxes of 200µL filtered tips (USA Scientific 1120-8710)
- [ ] 100% Ethanol
- [ ] Nuclease Free Water
- [ ] Bio-Rad 96 Well Plate 200 µL skirted PCR plate  (Biorad hsp9601) OR  TemPlate Semi-Skirt 0.2mL PCR Plate (USA Scientific 1402-9200)
- [ ] 96 well plate magnetic stand (Life Tech DynaMag-96 side 12331D)
- [ ] Disposable nuclease free reservoirs

### Protocol
- [ ] Prepare fresh 80% ethanol
- [ ] Add 0.7x volume to each well and mix by pipette (ex 14ul beads to 20ul amplicons)
- [ ] Incubate 5 min at room temperature
- [ ] Capture on magnetic stand for 2 minutes or until clear
- [ ] Discard of supernatant
- [ ] Add 200µL ethanol to each well and let stand at least 30 seconds
- [ ] Remove superantant
- [ ] Add 200µL ethanol to each well and let stand at least 30 seconds
- [ ] Remove superantant
- [ ] Air dry for 10 minutes or until beads are dry
- [ ] Add 30uL nuclease free water and pipette to mix
- [ ] Incubate for 2 minutes at RT
- [ ] Capture beads for 2 minutes or until cleared
- [ ] Remove supernatant (containing DNA) to new 96 well plate to carry forward.

## Figures
![Fig1](../images/ampurelayout.png)
<br>**Figure 1.** OT-2 deck layout. Deck positions are sequentially numbered 1-11 from the bottom left to the top right. **Position 1**: Amplicons to be cleaned in 96 well biorad PCR plate sitting on top of magnetic module. **Position 2**: 12 well reservoir, first column contains magbeads, second and 3rd 80% ethanol, 4th nuclease free water. **Position 3**: Empty 96 well biorad PCR plate to collect final DNA. **Positions 4-7**: 200ul filter tips. **Position 11**: Waste container (either an upside down tip lid or a single channel reservoir. **Pipettes*: 300ul multichannel on right mount.
