# covid_hospital
COVID hospital bed management system

A hospital have n numbers of bed available

Type of bed:
############
	1.) general(50%) 	index (0,2,4) 
	2.) semi-private(25%) 	index (1,5,9) 
	3.) private(25%) 		index (3,7,11) 

Assign Bed to Patient:
######################
If any patient comes and asks for a specific bed: assign them particular bed if bed available else: show the message "not available as of now"

Status of bed:
##############
	1.) input- bed_number
	1.) output- patient_name, bed_type

Patient Checkout:
################
	1.) customer leave the bed so the bed is again free for use

Utility Function:
#################
	1.) get the name of all patients which opt for a specific type of bed
	2.) status of types of beds: empty or full
	3.) list of beds which are free/occupy

*One customer can get an only a single bed of any type
*Customer can give priority based on FCFS mode.
