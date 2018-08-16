try:
	import os
	help = """
Commands:
set [OPTION]: Set The Value Of a chosen option (E.G.: set PAYLOAD example)

help: Show This Help Screen

quit: quit

options: Shows The Variables That You can change.

run: Start The Web Server"""

	def menu():
		print("""
Welcome To WebTRAP!
A Tool made by NSK B3, and NSK M4O
The purpose of this tool to be used in pentesting.
If you perform ANY Illegal activities using this tool
It's all on you.
We Do NOT Take responsibility for YOUR Actions.
------------------------------------------------------
""")
		PAYLOAD = None
		while True:
			r = None
			r = str(input("webtrap@menu:~# "))
			if "help" in r.lower():
				print(help)
			elif "quit" in r.lower():
				print("Thank you for using WebTRAP.")
				quit()
			elif "set" in r.lower():
				PAYLOAD = r.lower()[12:]
				print("Payload =>",r.lower()[12:])
			elif "options" in r.lower():
				print("""

Variable | Current Value
_________________________

PAYLOAD   """,PAYLOAD)
			else:
				print("Unknown Command:",r)
				r = "Unknown"
except Exception as e:
	print("An Error Occured:",e)

menu()
