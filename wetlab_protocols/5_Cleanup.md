# Protocol 5: Pool cleanup

## Theory
Before sequencing, it is crucial to remove any free adapter and/or primer dimers which will cause a loss of reads during sequencing and/or resulting in enhanced barcode hoping. For more on the idea of barcode hoping, see [here](https://www.illumina.com/techniques/sequencing/ngs-library-prep/multiplexing/index-hopping.html). This protocol can be accomplished in one of two ways: Ampure XP bead cleanup (**Protocol A**) or gel extraction (**Protocol B**). *Note: an automated size selection method such as a pippin prep can be used as well if available*.

## Materials
**Protocol A**
- [ ] MinElute Gel Extraction Kit (Qiagen 28604)
- [ ] TBE or TAE (BioRad 1610773)
- [ ] Agarose for Molecular Biology (BioRad 1613100)
- [ ] Quick-Load 100bp DNA Ladder (NEB N0467S)

**Protocol B**
- [ ] Ampure XP beads (Beckman A63881)
- [ ] Freshly made 80% ethanol
- [ ] Nuclease Free Water
- [ ] Magnetic capture rack

## Protocol A: Gel purification
- [ ] Prepare 50mL of 1% agarose (0.5g) in the microwave.
- [ ] Add 5 µL of SYBR Safe stain to the gel and mix before pouring into freshly cleaned (with RNase Away or similar) gel mold. Use the smallest lane width possible.
- [ ] Mix 24ul library with loading buffer (according to concentration of buffer).
- [ ] Load gel along with 5µL of ladder leaving a space between wells.
- [ ] Run for ~45 minutes at 80V.
- [ ] Using blue light tray, excise the band at 435bp into a empty preweighed tube
- [ ] Weigh mass of gel and add 3 volumes buffer QG.
- [ ] Incubate for 10min @ 50˚C or until gel has dissolved
- [ ] Add 1 volume isopropanol (ex, if gel was 100mg, add 100µL).
- [ ] Add mixture to MinElute column.
- [ ] Wash with 500µL buffer QG.
- [ ] Wash with 750µL buffer PE
- [ ] Spin empty column for 2 min at 10,000 g.
- [ ] Elute in 12 µL buffer EB.
- [ ] Quantify by Nanodrop and/or Qubit.

## Protocol B: Magnetic Capture
- [ ] Mix 100ul of pooled library with 80µL ampure XP beads (0.8x bead volume has been picked to remove adapter dimers and free adapter)
- [ ] Incubate 10 min at room temperature
- [ ] Capture for ~ 3 min
- [ ] Discard supernatant
- [ ] Add 200 ul fresh 80% ethanol, briefly mix and recapture
- [ ] Discard ethanol
- [ ] Add 200 ul fresh 80% ethanol, briefly mix and recapture
- [ ] Discard ethanol
- [ ] briefly centrigue, recapture, and use pipette to remove any ethanol at bottom of tube
- [ ] Airdry beads for ~ 5 min at room temperature until no visible ethanol remains
- [ ] Add 35ul nuclease free water and mix well
- [ ] Capture beads
- [ ] Transfer supernatant to fresh tube and quantify using Nanodrop and/or Qubit
