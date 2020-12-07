from opentrons import protocol_api
import csv
import numpy

# metadata
metadata = {
    'protocolName': 'PoolEquimolar', 
    'author': 'J Bisanz, jordan.bisanz@gmail.com',
    'description': 'Cherry picking protocol to generate equimolar pools of amplicon libraries. All volumes are transferred to a single 1.5mL Eppendorf tube',
    'apiLevel': '2.7'
}


#fix disposing first tip, and protocol comment instead of print, add tip touch on both sides?

# The data below is taken from a CSV wherein the first column defines the plate number, the second is the well from an indexing plate (biorad 96 well) and the third column is the volume (in µL) to transfer.
# Note: Ensure that total volumes to be transferred do not exceed 1.4mL!!!!! If so, program will pause and ask you to replace the tube when it is full. After run merge all tubes.
# Lines 17-114 are to be replaced with the users data taken from the loadings.csv of the tracking sheet.
loadings = '''
plate,well,volume
Plate4,A1,3.712893132
Plate4,B1,2.332358945
Plate4,C1,3.536277844
Plate4,D1,3.436969095
Plate4,E1,4.955626648
Plate4,F1,3.117195854
Plate4,G1,3.537629477
Plate4,H1,4.024917919
Plate4,A2,5.765140072
Plate4,B2,10
Plate4,C2,3.803682242
Plate4,D2,3.913241092
Plate4,E2,3.270436918
Plate4,F2,3.26668549
Plate4,G2,4.469798496
Plate4,H2,4.6696602
Plate4,A3,3.442882119
Plate4,B3,3.303559478
Plate4,C3,3.350953096
Plate4,D3,4.046916333
Plate4,E3,4.467640919
Plate4,F3,3.250052672
Plate4,G3,4.205755052
Plate4,H3,6.734701302
Plate4,A4,5.546616327
Plate4,B4,4.312304897
Plate4,C4,3.254910235
Plate4,D4,4.963599555
Plate4,E4,4.953968849
Plate4,F4,3.037528101
Plate4,G4,4.118726846
Plate4,H4,3.505140974
Plate4,A5,2.802001105
Plate4,B5,2.634136623
Plate4,C5,4.477637212
Plate4,D5,2.522243872
Plate4,E5,5.916703957
Plate4,F5,5.632692805
Plate4,G5,6.605527504
Plate4,H5,3.633990008
Plate4,A6,4.19979127
Plate4,B6,3.200325029
Plate4,C6,2.687485935
Plate4,D6,2.674768084
Plate4,E6,3.059745283
Plate4,F6,3.590116561
Plate4,G6,5.629266958
Plate4,H6,5.765588986
Plate4,A7,2.890266371
Plate4,B7,3.623497631
Plate4,C7,3.001086234
Plate4,D7,3.681876044
Plate4,E7,2.844520253
Plate4,F7,3.496038604
Plate4,G7,6.198536675
Plate4,H7,3.152498787
Plate4,A8,4.729311975
Plate4,B8,4.522212857
Plate4,C8,5.102471161
Plate4,D8,4.524423479
Plate4,E8,4.601464136
Plate4,F8,4.086899886
Plate4,G8,4.220859175
Plate4,H8,3.580568102
Plate4,A9,2.962660649
Plate4,B9,3.672380272
Plate4,C9,5.517683354
Plate4,D9,3.045774648
Plate4,E9,6.604938272
Plate4,F9,4.001426688
Plate4,G9,5.030368086
Plate4,H9,10
Plate4,A10,5.020476797
Plate4,B10,2.433704527
Plate4,C10,3.87656803
Plate4,D10,2.910832082
Plate4,E10,2.569241553
Plate4,F10,3.291224764
Plate4,G10,4.10616446
Plate4,H10,10
Plate4,A11,5.632264346
Plate4,B11,4.900525501
Plate4,C11,3.401600559
Plate4,D11,3.368024599
Plate4,E11,10
Plate4,F11,3.195215204
Plate4,G11,5.174862319
Plate4,H11,10
Plate4,A12,7.912881783
Plate4,B12,5.838327131
Plate4,C12,5.599044191
Plate4,D12,7.779855843
Plate4,E12,5.813573694
Plate4,F12,7.529081591
Plate4,G12,6.330494853
Plate4,H12,10
'''

# Tweakable parameters
ChangeTip = True #should tips be changed between samples? 
ChangeFrequency = 8 # how frequently should tips be changed if ChangeTip = true. 1 = every sample, 8 = every column.
newtube_volume = 1200 # pause protocol when tube gets to this volume in ul

#Don't edit below this line unless you want to change the functionality of the script
loadings_parsed = loadings.splitlines()[1:] # Discard the blank first line.
whichplates = [row["plate"] for row in csv.DictReader(loadings_parsed)]
whichplates = numpy.unique(whichplates)

def run(protocol: protocol_api.ProtocolContext):

    # define labware, only load the plates that are specified in the csv file
    if 'Plate1' in whichplates: Plate1 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '1')
    if 'Plate2' in whichplates: Plate2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2')
    if 'Plate3' in whichplates: Plate3 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '3')
    if 'Plate4' in whichplates: Plate4 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '4')
    if 'Plate5' in whichplates: Plate5 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5')
    if 'Plate6' in whichplates: Plate6 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '6')

    epitube = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '7') # eppendorf microcentrifuge tube in rack on position 3
    tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10') # 20ul filter tips on deck position 1

    # define pipettes
    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips])

	#loop through every line in the csv to be transferred
    left_pipette.pick_up_tip()
    i=0 # a counter to know when to change tips
    total_volume = 0 # tracking the total volume in the tube
    for transfer in csv.DictReader(loadings_parsed):
        check = i % ChangeFrequency #checking the remainder to know when to change tips
        if ChangeTip and check == 0 and i != 0:
            left_pipette.drop_tip()
            left_pipette.pick_up_tip()
        if transfer['plate'] == 'Plate1': left_pipette.aspirate(float(transfer['volume']), Plate1[transfer['well']])
        if transfer['plate'] == 'Plate2': left_pipette.aspirate(float(transfer['volume']), Plate2[transfer['well']])
        if transfer['plate'] == 'Plate3': left_pipette.aspirate(float(transfer['volume']), Plate3[transfer['well']])
        if transfer['plate'] == 'Plate4': left_pipette.aspirate(float(transfer['volume']), Plate4[transfer['well']])
        if transfer['plate'] == 'Plate5': left_pipette.aspirate(float(transfer['volume']), Plate5[transfer['well']])
        if transfer['plate'] == 'Plate6': left_pipette.aspirate(float(transfer['volume']), Plate6[transfer['well']])
        left_pipette.dispense(float(transfer['volume']), epitube['A1'])
        i=i+1
        total_volume = total_volume + float(transfer['volume'])
        if total_volume > newtube_volume:
            protocol.pause("Please insert new 1.5mL eppendorf tube")
            total_volume = 0
    protocol.comment("Total volume in tube is " + str(total_volume) + " ul")
    left_pipette.drop_tip()