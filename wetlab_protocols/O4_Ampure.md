# Optional Protocol 4 - Ampure XP amplicon clean up

## Theory
If significant primer dimer formation has occured, these will be quantified by the picogreen assay and lead to poor normalization. If >=25 cycles of PCR have been run during primary PCR, or if during QC, significant primer dimers are observed then this protocol is recommended. Depending on the ratio of beads to DNA volume, a size selection is possible which will remove small DNA. This protocol is set up to use a 0.9x volume; however, this can be adjusted in the script.

## Materials
- [ ] Ampure XP clean up beads (A63881) *Note: these can be made from scratch for significantly cheaper but may have less consistent size-selection properties**
- [ ] Opentrons OT2 with gen 2 300ul pipette mounted on right and magnetic module gen2 in position 1.
- [ ] 4 x Opentrons filter 200ul tips (https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-200ul-filter-tips)
- [ ] 1 x USA Scientific 12 Well Reservoir 22 mL (USA Scientific 1061-8150) 
- [ ] 1 x Agilent 1 well 290 mL reservoirs (Agilent 201252-100) **OR** use an empty tip box lid
- [ ] 100% Ethanol
- [ ] Nuclease Free Water
- [ ] Bio-Rad 96 Well Plate 200 µL skirted PCR plate  (Biorad hsp9601) 

## Protocol
- [ ] Prepare fresh 80% ethanol and put in columns 2 and 3 of 12 well reservoir.
- [ ] Add appropriate volume of beads to well 1 and ensure they are well mixed (bead volume/sample * Nsamples * 1.2)
- [ ] Add appropriate volume of water to well 4 (elution volume * Nsamples * 1.2)
- [ ] Set up OT2 according to Figure 1 below.
- [ ] Obtain a copy of scripts/O4_AmpureXPWash.py
- [ ] Modify lines 15-28 as required with close attention to desired bead volumes and elution volumes.
- [ ] Calibrate all deck positions and execture method. **Estimated run time Xmin**
- [ ] After execution dispose of waste and clean out tip container

## Figures
![Fig1](../images/ampurelayout.png)
<br>**Figure 1.** OT-2 deck layout. Deck positions are sequentially numbered 1-11 from the bottom left to the top right. **Position 1 (BINDINGPLATE)**: Amplicons to be cleaned in 96 well biorad PCR plate sitting on top of magnetic module gen2. **Position 2**: 12 well reservoir, first column contains magbeads, second and 3rd 80% ethanol, 4th nuclease free water. **Position 3 (ELUTIONPLATE)**: Empty 96 well biorad PCR plate to collect final DNA. **Positions 4-7**: 200ul filter tips. **Position 11**: Waste container (either an upside down tip lid or a single channel reservoir. **Pipettes*: 300ul multichannel on right mount.
