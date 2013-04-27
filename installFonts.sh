#!/bin/bash

# Run as root
unzip -q figletfonts40.zip -d /usr/share/figlet/
mv /usr/share/figlet/fonts/* /usr/share/figlet/.
rm figletfonts40.zip