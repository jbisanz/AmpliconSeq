# Protocol 4 - Equimolar pooling of amplicons

## Theory
Any given sequencing run produces a set number of reads: for example ~15 million from a MiSeq with v3 600 cycle reagents. In an ideal world, we would evenly distribute these reads among all samples. For example, if sequencing 150 samples, we should get 100,000 reads per sample. To get as close to this as possible, we need to pool equimolar amounts of each sample's individual sequencing library. While we have used manual pooling and Sequal plates in the past, manual pooling is prone to human error and is time consuming and Sequal plates provide inconsistent and irratic results. This protocol will use the OT-2 to pool equal molar concentrations of each sample based on quantification using Pico-green dye which specifically quantifies dsDNA (allowing direct quantification of PCR amplicons). This is the same approach that the Qubit uses, but in a higher throughput format (Quant-iT). The dsDNA concentration of each product is used to **Note: all quantification and pooling should be done at the same time to avoid batch effects leading to poor normalization. Also, if significant primer dimer formation has occured, a bead cleanup is reccomended, see Optional Protocol 4: Ampure XP Wash.**

## Materials
- [ ] Quant-iT Picogreen dsDNA Assay Kit (Life Tech P7589)
- [ ] well black flat bottom NBS microplates (Corning 3650)
- [ ] Generic 50mL reservoirs (ex. VistaLab Reagent Reservoirs 50mL 2138127G)
- [ ] 200 µL multichannel pipette
- [ ] 10 ul multichannel pipette
- [ ] 1x 200ul filter tips (USA scientific 120-8710)
- [ ] 1x 10ul filter tips (USA scientific 1121-2710)
- [ ] Fluorescent plate reader
- [ ] Nuclease free 1.5 mL microcentrifuge tube (eppendorf or alternative)
- [ ] Opentrons OT2
- [ ] Opentrons Gen2 20ul single channel
- [ ] 1 box 20ul opentrons filter tips

## Protocol
- [ ] For 96 well plate, prepare 110 reactions (11mL QuantIt buffer (1xTE), 55µL QuantIt reagent dye) in a reagent reservoir.
- [ ] Fill each well of 96 well plate with 100 µL reaction mix (samples plate)
- [ ] Fill 1st column of second plate with 90 µL reaction mix (standards plate)
- [ ] To full 96 well black plate (sample plate), transfer 1 µL of eached indexed PCR product and mix by pipetting
- [ ] to standards plate, transfer 10 µL of the kit's dsDNA HS standards (0, 1.56, 3.125, 6.25, 12.5, 25, 50, 100 ng/ul)
- [ ] Start by measuring flourescence on standard plate by setting the gain to automatic (Ex=480nm, Em=530nm).
- [ ] Copy the gain setting and flourescence values to the Picogreen tab of TrackingSheet.xlsx
- [ ] Repeat measurement on full sample plate being sure to set gain to match the standard plate.
- [ ] Copy and paste results into Picogreen template as per **Figure 1**.
- [ ] Manually edit the value in C140 to the desired ng of DNA to withdrow from each sample. Select a value such that most samples end up having less than 20 ul of volume withdrawn and pooled. For those that have more than 20 ul, manually edit these to the max volume to draw up.
- [ ] Move to Loading.csv tab, and click File > Save As > File Format: CSV UTF-8
- [ ] Remove lines which do not have a loading volume from the resulting csv file
- [ ] Download a copy of ot2_scripts/4_PoolEquimolar_template.py and copy and paste the pooling volumes from the CSV file into the python (.py) script.
- [ ] Set up OT-2 as described in **Figure 2**. *Note: Up to 6 plates can be pooled simnultaneously from plates in deck positions 1-6. Place your plate in the corresponding deck position matching its number from the spread sheet*
- [ ] Add 20ul nuclease free water to the eppendorf tube in the A1 position of the tube rack to ensure consistent delivery of volumes.
- [ ] Upload scripts to OT-2 using Opentrons App.
- [ ] Calibrate all deck positions
- [ ] Run protocol. **Estimated time of completion: 13 minutes/plate**
- [ ] Note, if the total volume to be pooled is over 1200ul, the protocol will pause and ask you to insert a fresh 1.5mL eppendorf tube.
- [ ] At completion of pooling, mix all pooled 1.5mL eppendorf tubes together (if pooling >1200ul)


## Figures
![](https://github.com/jbisanz/AmpliconSeq/raw/master/images/picogreen.png)

**Figure 1.** PicoGreen Normalization Tab.

![](https://github.com/jbisanz/AmpliconSeq/raw/master/images/poolinglayout.png)

**Figure 2.** OT-2 deck layout. **Position 1-6:** Indexed PCR products. *Note: you may use any combination of plates 1-6 however ensure that their deck positions matches the loading.csv file.* **Position 7:** Eppendorf tube in position A1 of tube rack. **Position 8:** 20ul filter tips. Left Pipette is loaded with p20 single channel.
