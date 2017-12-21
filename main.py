import aiml
import os
# Create the kernel and learn AIML files
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
	 kernel.bootstrap(brainFile = "bot_brain.brn")
else:
	kernel.bootstrap(learnFiles = "aiml/std-startup.xml", commands = "load aiml b")
	kernel.saveBrain("bot_brain.brn")
# Press CTRL-C to break this loop
while True:
	message=raw_input("Enter your message >> ")
	if message == "exit":
	        exit()
	elif message == "save":
	        kernel.saveBrain("bot_brain.brn")
	else:
   		print (kernel.respond(message))
