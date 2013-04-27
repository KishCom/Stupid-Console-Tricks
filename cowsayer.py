import os
import subprocess #this is what we need to use to save stdout to a variable -- not os.system (depcrated in 2.7, unavailable in 3.0)
fonts = os.listdir("/usr/share/cowsay/cows")
terminalWidth = str(os.system("tput cols"));
if terminalWidth == "0" : terminalWidth = "200"
for font in fonts:
    print "Cow: " + font + ": "
    cmd = subprocess.Popen("cowsay -f " + font + " 'Some String'", shell=True)
    figletOutput = cmd.communicate()
    if figletOutput != 0:
        print figletOutput
        print ""
        print "---------"
        print ""

print "Your terminal is " + terminalWidth + " wide.";
