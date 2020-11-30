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


# The data below is taken from a CSV wherein the first column defines the plate number, the second is the well from an indexing plate (biorad 96 well) and the third column is the volume (in µL) to transfer.
# Note: Ensure that total volumes to be transferred do not exceed 1.4mL!!!!! If so, program will pause and ask you to replace the tube when it is full. After run merge all tubes.
# Lines 17-20 are to be replaced with the users data taken from the loadings.csv of the tracking sheet.
loadings = '''
plate,well,volume
Plate1,A1,1
Plate1,B2,1
Plate2,B1,2
Plate3,C3,3
Plate4,D4,4
Plate5,E5,5
Plate6,F6,6
Plate6,H12,2
'''

# Tweakable parameters
ChangeTip = True #should tips be changed between samples? 
ChangeFrequency = 8 # how frequently should tips be changed if ChangeTip = true. 1 = every sample, 8 = every column.
newtube_volume = 1200 # pause protocol when tube gets to this volume in ul

#Don't edit below this line
loadings_parsed = loadings.splitlines()[1:] # Discard the blank first line.
whichplates = [row["plate"] for row in csv.DictReader(loadings_parsed)]
whichplates = numpy.unique(whichplates)

def run(protocol: protocol_api.ProtocolContext):

    # define labware
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
        if ChangeTip and check == 0:
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
    print("Total volume in tube is " + str(total_volume) + " ul")
    left_pipette.drop_tip()