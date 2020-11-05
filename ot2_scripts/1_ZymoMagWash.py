from opentrons import protocol_api

# metadata
metadata = {
	'protocolName': 'Zymo Mag Wash', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Carryout washing and elution steps of zymobiomics 96 MAgBead DNA Kit (D4608/4302). Tip usage has been optimized to allow the protocol to run without intervention and as such dirty tips will be returned to boxes. Dispose of tip boxes after use.',
	'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):

	# set tweakable variables
	wash_speed = 100 # speed with which to draw large volumes of magbeads in ul/s
	elution_speed = 20 # speed with which to draw up liquid from captured beads in ul/second
	elution_volume = 50 # ul of water to add to final beads
	elution_to_plate = 40 # ul to transfer to final elution plate
	wells_to_extract = [ 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12' ]

	# define deck layout
	MagModule = protocol.load_module('magnetic module gen2', 1)
	BindingPlate = MagModule.load_labware('usascientific_96_wellplate_2.4ml_deep')
	BeadsAndWater = protocol.load_labware('usascientific_12_reservoir_22ml', '2') # magbeads in A1 (5.5 mL), water in A2 (cleaning tips; 10mL) and water in A3 (elution; 15mL)
	ElutionPlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '3') # an empty biorad 96 well plate
	BindingBuffer = protocol.load_labware('agilent_1_reservoir_290ml', '4') # reservoir with 132 mL binding buffer
	MagWash1 = protocol.load_labware('agilent_1_reservoir_290ml', '5') # reservoir with 110 mL magwash1
	MagWash2 = protocol.load_labware('agilent_1_reservoir_290ml', '6') # reservoir with 210 mL magwash1
	tips_binding = protocol.load_labware('opentrons_96_filtertiprack_1000ul', '7')
	tips_wash1 = protocol.load_labware('opentrons_96_filtertiprack_1000ul', '8')
	tips_wash2 = protocol.load_labware('opentrons_96_filtertiprack_1000ul', '9')
	tips_elution = protocol.load_labware('opentrons_96_filtertiprack_200ul', '10')
	tips_wash2rep = protocol.load_labware('opentrons_96_filtertiprack_1000ul', '11')


	# define pipettes
	left_pipette = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips_binding, tips_wash1, tips_wash2, tips_wash2rep])
	right_pipette = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tips_elution])


	### Prerun setup ########################################
	MagModule.disengage()
	left_pipette.flow_rate.aspirate = wash_speed
	right_pipette.flow_rate.aspirate = elution_speed

	### MAG BINDING ######################################
	# add 25uL beads to each well
	protocol.comment('Adding mag beads')
	right_pipette.pick_up_tip(tips_elution['A1'])
	right_pipette.mix(20, 100, BeadsAndWater['A1']) # mix beads 20 x by pulling up 100ul
	for i in range(1, 13): 
		right_pipette.aspirate(25, BeadsAndWater['A1'])
		right_pipette.dispense(25, BindingPlate['A'+str(i)])
	right_pipette.mix(20, 100, BeadsAndWater['A2']) # wash tips in water so can reuse them for elution later
	right_pipette.return_tip() 
	# add 600ul mag binding buffer, mix and return to tip box
	protocol.comment('Adding binding buffer')
	for i in range(0, 96): 
		left_pipette.pick_up_tip(tips_binding[wells_to_extract[i]])
		left_pipette.aspirate(600, BindingBuffer['A1'])
		left_pipette.dispense(600, BindingPlate[wells_to_extract[i]])
		left_pipette.mix(10, 300, BindingPlate[wells_to_extract[i]])
		left_pipette.return_tip() 
	MagModule.engage()
	protocol.delay(minutes=5)
	# using dirty tips from before to move liquid back to reservoir
	for i in range(0, 96): 
		left_pipette.pick_up_tip(tips_binding[wells_to_extract[i]])
		left_pipette.aspirate(600, BindingPlate[wells_to_extract[i]])
		left_pipette.dispense(600, BindingBuffer['A1'])
		left_pipette.return_tip() 
	MagModule.disengage()

	
	### MagWash 1 ########################################
	# add 500ul magwash 1, mix and return to tip box
	protocol.comment('Adding magwash 1')
	for i in range(0, 96): 
		left_pipette.pick_up_tip(tips_wash1[wells_to_extract[i]])
		left_pipette.aspirate(500, MagWash1['A1'])
		left_pipette.dispense(500, BindingPlate[wells_to_extract[i]])
		left_pipette.mix(10, 300, BindingPlate[wells_to_extract[i]])
		left_pipette.return_tip() 
	# engage capture
	MagModule.engage()
	protocol.delay(minutes=5)
	# using dirty tips from before to move liquid back to reservoir
	for i in range(0, 96): 
		left_pipette.pick_up_tip(tips_wash1[wells_to_extract[i]])
		left_pipette.aspirate(500, BindingPlate[wells_to_extract[i]])
		left_pipette.dispense(500, MagWash1['A1'])
		left_pipette.return_tip() 
	MagModule.disengage()	
	
	### MagWash 2 - first time ########################################
	# add 500ul magwash 2, mix and return to tip box
	protocol.comment('Adding magwash 2- first time')
	for i in range(0, 96): 
		left_pipette.pick_up_tip(tips_wash2[wells_to_extract[i]])
		left_pipette.aspirate(500, MagWash2['A1'])
		left_pipette.dispense(500, BindingPlate[wells_to_extract[i]])
		left_pipette.mix(10, 300, BindingPlate[wells_to_extract[i]])
		left_pipette.return_tip() 
	# engage capture
	MagModule.engage()
	protocol.delay(minutes=5)
	# using dirty tips from before to move liquid back to reservoir
	for i in range(0, 96): 
		left_pipette.pick_up_tip(tips_wash2[wells_to_extract[i]])
		left_pipette.aspirate(500, BindingPlate[wells_to_extract[i]])
		left_pipette.dispense(500, MagWash1['A1']) # disposing into magwash 1 to not dirty the magwash 2 which is needed again
		left_pipette.return_tip() 
	MagModule.disengage()	
	
	### MagWash 2 - second time time ########################################
	# add 500ul magwash 2, mix and return to tip box
	protocol.comment('Adding magwash 2- first time')
	for i in range(0, 96): 
		left_pipette.pick_up_tip(tips_wash2rep[wells_to_extract[i]])
		left_pipette.aspirate(500, MagWash2['A1'])
		left_pipette.dispense(500, BindingPlate[wells_to_extract[i]])
		left_pipette.mix(10, 300, BindingPlate[wells_to_extract[i]])
		left_pipette.return_tip() 
	# engage capture
	MagModule.engage()
	protocol.delay(minutes=5)
	# using dirty tips from before to move liquid back to reservoir
	for i in range(0, 96): 
		left_pipette.pick_up_tip(tips_wash2rep[wells_to_extract[i]])
		left_pipette.aspirate(500, BindingPlate[wells_to_extract[i]])
		left_pipette.dispense(500, MagWash2['A1'])
		left_pipette.return_tip() 
	MagModule.disengage()	

	### Airdry ########################################
	protocol.delay(minutes=15)

	### Elution ########################################
	protocol.comment('Eluting DNA')
	# pipette water in and mix
	for i in range(1, 13): 
		right_pipette.pick_up_tip(tips_elution['A'+str(i)])
		right_pipette.aspirate(elution_volume, BeadsAndWater['A3'])
		right_pipette.dispense(elution_volume, BindingPlate['A'+str(i)])
		right_pipette.mix(10, 25, BindingPlate['A'+str(i)])
		right_pipette.return_tip() 
	# capture
	protocol.delay(minutes=5) # wait five minutes to elute
	MagModule.engage()
	protocol.delay(minutes=5)
	# transfer to elution plate
	for i in range(1, 13): 
		right_pipette.pick_up_tip(tips_elution['A'+str(i)])
		right_pipette.aspirate(elution_to_plate, BindingPlate['A'+str(i)])
		right_pipette.dispense(elution_to_plate, ElutionPlate['A'+str(i)])
		right_pipette.return_tip() 
