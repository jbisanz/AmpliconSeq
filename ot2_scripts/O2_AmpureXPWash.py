from opentrons import protocol_api

# metadata
metadata = {
	'protocolName': 'Ampure XP wash', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Carry out bead cleanup of PCR amplicons using ampure XP beads',
	'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):

	# set tweakable variables
	#columns_to_extract = [1,2,3,4,5,6,7,8,9,10,11,12] # which columns should be cleaned up?
	columns_to_extract = [1,2] # which columns should be cleaned up?
	bead_volume = 18 # 0.9x volume already in wells for size selection, 1.8x for other uses
	aspirate_speed = 20 # speed with which to draw liquids off beads
	wash_volume = 150 # ul of ethanol for bead washes
	elution_volume = 50 # ul of water to add to final beads
	elution_to_plate = 40 # ul to transfer to final elution plate
	incubation_time = 3 #number of minutes for capturing DNA on beads
	capture_time = 3 #number of minutes to capture on stand
	wash_time = 0.16 #time to pause before removing Etoh
	dry_time = 10 #number of minutes to dry beads
	reservoir = False #If the using the 12 channel reservoirs, go True, otherwise dispense into 96-well deep well plate along similar columns.
	
	# define deck layout
	MagModule = protocol.load_module('magnetic module gen2', 1)
	BindingPlate = MagModule.load_labware('biorad_96_wellplate_200ul_pcr')
	if reservoir:
		BeadsAndWater = protocol.load_labware('usascientific_12_reservoir_22ml', '2') # magbeads in A1 (Nsamples * bead_volume * 1.2), 80% Ethanol in A2 (Nsamples * wash_volume * 1.2), 70% Ethanol in A3 (Nsamples * wash_volume * 1.2), water in A4 (Nsamples * elution_volume * 1.2))
	else:
		BeadsAndWater =  protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '2') #This is an alternate using USA scientific deep well 2mL plates
	ElutionPlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '3') # an empty biorad 96 well plate
	tips_bind = protocol.load_labware('opentrons_96_filtertiprack_200ul', '4')
	tips_wash1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '5')
	tips_wash2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '6')
	tips_elute = protocol.load_labware('opentrons_96_filtertiprack_200ul', '7')


	# define pipettes
	right_pipette = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tips_bind, tips_wash1, tips_wash2, tips_elute])

	### Prerun setup ########################################
	MagModule.disengage()

	### Binding ########################################
	#mix up beads
	protocol.comment('-----------------------> Mixing beads')
	right_pipette.pick_up_tip(tips_bind['A1'])
	right_pipette.mix(5, 100, BeadsAndWater['A1']) # mix beads 10 x by pulling up 100ul
	right_pipette.blow_out()
	right_pipette.touch_tip()
	right_pipette.return_tip() 
	# add defined volume of beads to each well
	
	
	protocol.comment('-----------------------> Adding beads')
	for i in columns_to_extract: 
		right_pipette.pick_up_tip(tips_bind['A'+str(i)])
		right_pipette.aspirate(bead_volume, BeadsAndWater['A1'])
		right_pipette.touch_tip()
		right_pipette.dispense(bead_volume, BindingPlate['A'+str(i)])
		right_pipette.mix(10, 20, BindingPlate['A'+str(i)])
		right_pipette.return_tip()
	protocol.delay(minutes=incubation_time)
	# capture beads
	protocol.comment('-----------------------> Capturing beads')
	MagModule.engage()
	protocol.delay(minutes=capture_time)
	# Remove buffer
	protocol.comment('-----------------------> Removing buffer')
	right_pipette.flow_rate.aspirate = aspirate_speed
	for i in columns_to_extract: 
		right_pipette.pick_up_tip(tips_bind['A'+str(i)])
		right_pipette.aspirate(wash_volume+10, BindingPlate['A'+str(i)])
		right_pipette.drop_tip() 
	
	
	
	### Wash 1 ########################################
	protocol.comment('-----------------------> Adding EtOH: Wash 1')
	for i in columns_to_extract: 
		right_pipette.pick_up_tip(tips_wash1['A'+str(i)])
		right_pipette.aspirate(wash_volume, BeadsAndWater['A2'])
		right_pipette.dispense(wash_volume, BindingPlate['A'+str(i)])
		protocol.delay(minutes=wash_time)
		right_pipette.aspirate(wash_volume+10, BindingPlate['A'+str(i)])
		right_pipette.drop_tip()
		
	### Wash 2 ########################################
	protocol.comment('-----------------------> Adding EtOH: Wash 2')
	for i in columns_to_extract: 
		right_pipette.pick_up_tip(tips_wash2['A'+str(i)])
		right_pipette.aspirate(wash_volume, BeadsAndWater['A3'])
		right_pipette.dispense(wash_volume, BindingPlate['A'+str(i)])
		protocol.delay(minutes=wash_time)
		right_pipette.aspirate(wash_volume+10, BindingPlate['A'+str(i)])
		right_pipette.drop_tip()	
	
	### Drying ########################################
	protocol.comment('-----------------------> Drying beads')
	protocol.delay(minutes=dry_time)

	### Elution ########################################
	MagModule.disengage()
	right_pipette.flow_rate.aspirate = 80 #temp turning speed back up with the purposes of mixing
	for i in columns_to_extract:
		right_pipette.pick_up_tip(tips_elute['A'+str(i)])
		right_pipette.aspirate(elution_volume, BeadsAndWater['A4'])
		right_pipette.dispense(elution_volume, BindingPlate['A'+str(i)])
		right_pipette.mix(10, elution_volume*0.5, BindingPlate['A'+str(i)])
		right_pipette.blow_out()
		right_pipette.touch_tip()
		right_pipette.return_tip()

	MagModule.engage()
	protocol.delay(minutes=capture_time)
	right_pipette.flow_rate.aspirate = aspirate_speed
	for i in columns_to_extract:
		right_pipette.pick_up_tip(tips_elute['A'+str(i)])
		right_pipette.aspirate(elution_to_plate, BindingPlate['A'+str(i)])
		right_pipette.dispense(elution_to_plate, ElutionPlate['A'+str(i)])
		right_pipette.drop_tip()	
