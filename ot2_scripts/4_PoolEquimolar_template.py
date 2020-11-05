from opentrons import protocol_api
import csv

# metadata
metadata = {
    'protocolName': 'PoolEquimolar', 
    'author': 'J Bisanz, jordan.bisanz@gmail.com',
    'description': 'Cherry picking protocol to generate equimolar pools of amplicon libraries. All volumes are transfered to 1.5mL Eppendorf tube',
    'apiLevel': '2.7'
}


# The data below is taken from a CSV wherein the first column defines the well from an indexing plate (biorad 96 well) and the second column is the volume (in µL) to transfer.
# Lines 17-20 are to be replaced with the users data
loadings = '''
indexing_well,transfer_volume
A1,5
B1,6
C1,7
'''

def run(protocol: protocol_api.ProtocolContext):

    # define labware
    tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', '1') # 20ul filter tips on deck position 1
    amplicons = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2') # skirted 96 well plate of amplicons on deck position 2
    epitube = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '3') # eppendorf microcentrifuge tube in rack on position 3

    # define pipettes
    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips])

	#loop through every well
    loadings_parsed = loadings.splitlines()[1:] # Discard the blank first line.
    for row in csv.DictReader(loadings_parsed):
        left_pipette.pick_up_tip()
        left_pipette.aspirate(float(row['transfer_volume']), amplicons[row['indexing_well']])
        left_pipette.dispense(float(row['transfer_volume']), epitube['A1'])
        left_pipette.drop_tip()     
