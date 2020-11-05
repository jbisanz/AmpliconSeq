# Protocol 7 - Loading MiSeq
## Theory

While many platforms can be used for sequencing of the amplicons, MiSeq is among the most common due to its relatively longer read lengths and accuracy. While the NextSeq will provide many more reads, the cost of running and shorter read lengths make it less desirable for some applications. If ultra high-depth is desired perhaps HiSeq V2 Rapid run 2x250 would be appropriate.

Because we are using an illumina-compatible barcoding strategy, it is  unnecessary to add custom sequencing primers as the built in Illumina primers will suffice. Also, we can now provide a sample sheet such that the sequencer demultiplexes our reads for us. The sample sheet will be automatically created for you in the **TrackingSheet.xlsx** file you created during DNA extraction under the SampleSheet tab.  The sample sheet can always be changed after the fact, however it is important that the reads are set up for at least 270x12x12x270 to ensure both barcodes are sequenced.

## Materials
- [ ] MiSeq Reagent Kit (Version 3, 600 cycles, $1,377.00 each)
- [ ] Buffer HT1 (Included with MiSeq Kit)
- [ ] Incorperation buffer (Included with MiSeq Kit)
- [ ] Phix174 Illumina Spike in Control (FC-110-3001)
- [ ] 1N NaOH
- [ ] Dilution Buffer (10 mM Tris-HCl pH 8, 0.05% Tween, note can be prepared from Qiagen EB + Tween)

## Protocol
- [ ] Thaw MiSeq reagent kit overnight in fridge (or in room temp water bath)
- [ ] Prepare fresh 0.2 N NaOH (20 µL 1N NaOH and 80µL molecular-grade H2O)
- [ ] Using the molarity of your sample calculated via qPCR in Protocol 6, dilute library to 2 nM in Dilution Buffer. Transfer 10 µL of 2 nM library to a new 1.5mL microfuge tube.
- [ ] In a separate tube, prepare 10 µL of 2 nM PhiX by combining 2µL of Phix174 Illumina Spike in Control with 8µL Dilution Buffer.
- [ ] To both tubes, add 10 µL freshly prepared 0.2 N NaOH and incubate at room temperature for 5 min.
- [ ] Add 980 μl of Illumina’s HT1 buffer to both tubes to bring the samples to 20 pM.
- [ ] Dilute each to 8 pM by mixing 400 μl of 20 pM sample and 600 μl of Illumina’s HT1 buffer in clean 1.5 ml microfuge tubes.
- [ ] In a fresh tube, combine 850 µL of the 8 pM sequencing library, and 150 µL of the 8 pM PhiX (This will results in a 15% spike-in)
- [ ] Add 600 μl of the combined 8 pM library (15% PhiX) to the sample well of the MiSeq cartridge and initiate sequencing. 
- [ ] Double check that sequencing will be 270 x 12 x 12 x 270 cycles

## QC
- An ideal clustering density from 500-900 clusters/mm2
- % Aligned ~ 15%
- >80% AVG%Q30
- High quality sequencing across all reads. See example in **Figure 1**.

## Figures
![fig1](https://github.com/jbisanz/AmpliconSeq/raw/master/images/basespace.png)
**Figure 1.** Basespace Qscore plot of sequencing run by cycle. The first 270 cycles are the forward read where quality starts to drop off mildly towards the end of the read. The next 24 cycles are the indexing reads. Note some low quality on the start of the first index read (i7), this happens quite frequently on the MiSeq and can be partially addressed using the error correcting barcodes. The remaining 270 cycles are the reverse read which deteriorates at a rate higher than the forward as to be expected.
