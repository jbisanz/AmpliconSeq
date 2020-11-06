# Protocol 4 - Equimolar pooling of amplicons

## Theory
Any given sequencing run produces a set number of reads: for example ~15 million from a MiSeq with v3 600 cycle reagents. In an ideal world, we would evenly distribute these reads among all samples. For example, if sequencing 150 samples, we should get 100,000 reads per sample. To get as close to this as possible, we need to pool equimolar amounts of each sample's individual sequencing library. While we have used manual pooling and Sequal plates in the past, manual pooling is prone to human error and is time consuming and Sequal plates provide inconsistent and irratic results. This protocol will use the OT-2 to pool equal molar concentrations of each sample based on quantification using Pico-green dye which specifically quantifies dsDNA (allowing direct quantification of PCR amplicons). This is the same approach that the Qubit uses, but in a higher throughput format (Quant-iT). The dsDNA concentration of each product is used to **Note: all quantification and pooling should be done at the same time to avoid batch effects leading to poor normalization.**

## Materials
- [ ] Quant-iT dsDNA Assay kit, high sensitivity (Life Tech Q33120)
- [ ] 2 x 96 well black flat bottom NBS microplate (Corning 3650)
- [ ] Generic 50mL reservoirs (ex. VistaLab Reagent Reservoirs 50mL 2138127G)
- [ ] 200 µL multichannel pipette
- [ ] 10 ul multichannel pipette
- [ ] 1x 200ul filter tips (USA scientific 120-8710)
- [ ] 1x 10ul filter tips (USA scientific 1121-2710)
- [ ] Fluorescent plate reader (ex ***XXXXXXX***)

## Protocol
- [ ] For 96 well plate, prepare 110 reactions (11mL dsDNA HS buffer, 55µL dsDNA HS reagent dye) in a reagent reservoir.
- [ ] Fill each well of 96 well plate with 100 µL reaction mix (sample plate)
- [ ] Fill 1 column of second plate with 90 µL reaction mix (standard plate)
- [ ] To full 96 well black plate (sample plate), transfer 1 µL of eached indexed PCR product and mix by pipetting
- [ ] to standards plate (1 column filled), transfer 10 µL of the kit's dsDNA HS standards (0, 0.5, 1, 2, 4, 6, 8, 10 ng/ul)
- [ ] Start by measuring flourescence on standard plate by setting the gain to automatic (Ex=480nm, Em=530nm).
- [ ] Copy the gain setting and flourescence values to the Picogreen tab of TrackingSheet.xlsx
- [ ] Repeat measurement on full sample plate being sure to set gain to match the standard plate.
- [ ] Copy and paste results into Picogreen template as per **Figure 1**.
- [ ] Move to Loading.csv tab, and click File > Save As > File Format: CSV UTF-8
- [ ] For each plate you wish to pool, download a copy of ot2_scripts/4_PoolEquimolar_template.py and copy and paste the pooling volumes at Line 17-19 saving as many copies as you have plates.
- [ ] Set up OT-2 as described in **Figure 2**.
- [ ] Upload scripts to OT-2 using Opentrons App.
- [ ] Calibrate all deck positions
- [ ] Run protocol. **Estimated time of completion: XXXXXXXX**
- [ ] when pooling is done, load the next plate's protocol and continue pooling into the same 1.5 mL eppendorf tube.



## Figures
![](https://github.com/jbisanz/AmpliconSeq/raw/master/images/picogreen.png)

**Figure 1.** PicoGreen Normalization Tab. Note: in this case I did not run all standards but it would not hurt in future.

![](https://github.com/jbisanz/AmpliconSeq/raw/master/images/ot2pico.png)

**Figure 2.** OT-2 deck layout. **Position 1:** 20µL filter tips. **Position 2:** Indexing PCR plates (in 96 well biorad plates). **Position 3:** Eppendorf tube in position A1 of tube rack. Left Pipette is loaded with p20 single channel.
