welcome_message =	"""
		Welcome to Nokia 3310 Where we help you to
		Welcome Welcome 




		1.-> Phone Book
		2.-> Message
		3.-> Chat
		4.-> Call Register
		5.->Tone
		6.-> Settings
		7.-> Call Divert
		8.-> Games
		9.-> Calculator
		10.-> Remainder
		11.-> Clock
		12.-> Profile
		13.-> SIM Service
		"""
print(welcome_message)
USERINPUT = int(input("Enter a option\n"))
match(USERINPUT) :
	case 1 :
		print("""
		1->.Search
		2->.Service Nos
		3->. Add Name
		4->. Erase
		5->. Edit
		6->.Assign tone
		7->.send b'card
		8->.Options
		9->.Speed Dials
		10->.Voice Tags
		""")
		PHONEBOOK_INPUT = int(input("Choose an option from Phonebook"))
		match(PHONEBOOK_INPUT):
			case 1 : print("Search")
			case 2 : print("Service Nos")
			case 3 : print("Add Name")
			case 4 : print("Erase")
			case 5 : print("Edit")
			case 6 : print("Assign Tone")
			case 7 : print("Send b' Card")
			case 8 : print("""
				Options
					1->.Type Of View
					2-->.Memory Status
					""")
		INPUT_OPTIONS = int(input("Enter your options"))
		match (INPUT_OPTIONS) :
			case 1 : print("Type Of View")
			case 2 : print("Memory Status")
			#case _ : print("Invalid Output") 






			case 9 : print("Speed Dials")
			case 10 : print("Voice Tags")
			case _ : print("Invalid Output")
	case 2:
		print("""
		1->.Write Messages
		2->.Inbox
		3->. Outbox
		4->. Picture Messages
		5->. Templates
		6->.Smileys
		7->.Mesage Settings
		8->.Info Services
		9->.Voice Mailbox
		10->.Service command editor
		""")
		MESSAGE_INPUT = int(input("Enter Input for Message Options"))
		match(MESSAGE_INPUT) :
			case 1 : print("Write messages")
			case 2 : print("Inbox")
			case 3 : print("Outbox")
			case 4 : print("Picture Messgae")
			case 5 : print("Template")
			case 6 : print("Smileys")
			case 7 : print("Message Settings")
		MESSAGE_SETTTINGS = int(input("Enter your options"))
		match (MESSAGE_SETTTINGS) :
			case 1 : print("Set")
			case 2 : print("Common")
			


			case 8 : print("Info Services")
			case 9 : print("Voice Mailbox")
			case 10 : print("Service Command Editor")
			case _ : print("INVALID INPUT")
	case 3 :
		print("Chat")
	case 4 : 
		print("""
		1->.Missed call
		2->. Dialled numbers
		3->. Erase recent calls
		4->. Received Calls
		5->.Show call duration
		6->.Show Call cost
		7->.Call Cost settings
		8-->.Prepaid Credits
		""")
		CALL_REGISTER = int(input("Enter options to pick from Call Options"))
		match (CALL_REGISTER) :
			case 1 : print("Missed Calls")
			case 2 : print("Dialled Calls")
			case 3 : print("Erase recent calls")
			case 4 : print("Recived Calls")
			case 5 : print("Show Call Duration")
		SHOW_CALL_DURATION = int(input("Enter Call Duration"))
		match(SHOW_CALL_DURATION) :
			case 1 : print("Last Call Duration")
			case 2 : print("AlL Calls Duration")
			case 3 : print("Call Duration")
			case 4 : print("Dialled Calls Duration")
			case 5 : print("Show Call Timers")
				

			case 6 : print("Show Call Cost")
		SHOW_CALL_SETTINGS = int(input("Enter Your Call Cost Options"))
		match(SHOW_CALL_SETTINGS) :
			case 1 : print("Call Cost Setting")
			case 2 : print("ALL Cost Settings")
			
			case 7 : print("Call Cost Setting")
		SHOW_CALL_COST = int(input("Enter Your Call Cost Settings"))
		match(SHOW_CALL_COST) : 
			case 1 : print("Call Cost Limit")
			case 2 : print("Show Cost Settings") 
 

			
			case 8 : print("Prepaid Credits")
			case _ : print("Invalid Input")	
	case 5 :
		print("""
		1->.Ringing tone
		2->. Ringing Volume
		3->. Incomig call alert
		4->. Keyad tonnes
		5->.composer
		6->.Warning and games tonnes
		7->.vibrating alert
		8->.Screen Saver
		9->.Message Alerts tone
		""")
		TONNES = int(input("Enter options to pick Ringing Tonnes"))
		match (TONNES) :
			case 1 : print("1->.Ringing tone")
			case 2 : print("2->.Ringing Volume")
			case 3 : print("3->.Incoming call alert")
			case 4 : print("4->.Keypad tonnes")
			case 5 : print("5->.Composer")
			case 6 : print("6->.Warning and Game tonnes")
			case 7 : print("7->.Vibrating Alert")
			case 8 : print("8->.Screen Saver")
			case 9 : print("9->Mesage Alerts tone")
			case _ : print("Invalid Input")
	case 6 :
		print("""
		1->.Call Settings
		2->. Phone Settings
		3->. Security Settings
		4->. Restore Factory Settings
		""")
		CALL_SETINGS = int(input("Enter options to pick CALL SETINGS"))
		match (CALL_SETINGS) :
			case 1 : print("1->.Call Settings")
			case 2 : print("2->.Phone Settings")
			case 3 : print("3->. Security Settings")
			case 4 : print("4->.Restore Settings")
			case _ : print("Invalid Input")
	case 7 :
		print("Call Divert")
	case 8 :
		print("Game")
	case 9 :
		print("Calculator")
	case 10 : 
		print("Remainder")
	case 11 :
		print("""Clocks
		1->.Alarm Clocks
		2->.Clocks Settings
		3->.Date Settings
		4->.Stopwatch
		5->Countdown Timer
		6-> Auto Update Time and date

		""")
		CLOCKS = int(input("Enter options to pick Clocks"))
		match (CLOCKS) :
			case 1 : print("1->.Alarm Clocks")
			case 2 : print("2->.Clocks Settings")
			case 3 : print("3->.Date Settings")
			case 4 : print("4->.Stopwatch")
			case 5 : print("5->Countdown Timer")
			case 6 : print("6-> Auto Update Time and date")
			case _ : print("Invalid Input")
	case 12 :
		print("Profiles")
	case 13 :
		print("Sim Services")
	case _ :
		print("Invalid Option")	
		
