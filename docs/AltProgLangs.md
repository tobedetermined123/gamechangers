## Official Lego EV3 programming environments
* [LEGO MINDSTORMS Retail EV3](https://www.lego.com/en-ca/themes/mindstorms/downloads) ([LabVIEW](https://www.ni.com/en-ca/shop/labview.html) dialect with simplified UI)

* [LEGO MINDSTORMS Education EV3](https://education.lego.com/en-us/downloads/mindstorms-ev3/software) ([LabVIEW](https://www.ni.com/en-ca/shop/labview.html) dialect with simplified UI)

* [MicroPython](https://education.lego.com/en-us/downloads/mindstorms-ev3/software#MicroPython)
Visual Studio Code version 1.31 or above with EV3 MicroPython extension installed
SD Card for EV3 Brick: Micro SDHC (min. 4GB, max. 32GB) with Application Performance Class A1
  * EV3 MicroPython runs on top of ev3dev with a new Pybricks MicroPython runtime and library. It also comes with a dedicated Visual Studio Code extension that includes project templates and documentation to get started. 
  * [Documentation](https://pybricks.github.io/ev3-micropython/index.html)

## Research on 3rd party EV3 programming environments/languages (not finished)
* [EV3dev](http://www.ev3dev.org/) - debian VM on EV3, bootable from SD card
    * [Demo - Programming Lego Mindstorms robots with Python](https://www.youtube.com/watch?v=kyfbYv6eZQQ) ([Jupyter Notebook on github](https://github.com/sshopov/pyconau2017)) - running Python directly on EV3 brick running Debian; creates Jupiter server on brick that is accessible from client browser on laptop)
  * [Python EV3DEV - version 2](https://sites.google.com/site/ev3devpython/) 
  uses Microsoft's Visual Studio Code (VS Code) with the EV3 extension (uses EV3DEV code on SD Card without having to reflash firmware)

  * ~~[EV3Python - version 1 - deprecated](https://sites.google.com/site/ev3python/)~~
  * [EV3 BASIC](https://sites.google.com/site/ev3basic/) - Windows only
  EV3 Basic is a textual programming language.
  * [Ev3devSim](https://www.aposteriori.com.sg/Ev3devSim/index.html) - Browser-based Simulator for EV3DEV - 2D only

* [LabVIEW for LEGO MINDSTORMS ](https://www.ni.com/en-ca/support/downloads/software-products/download.labview-for-lego-mindstorms.html)
LabVIEW for LEGO MINDSTORMS (LVLM) and LabVIEW for Education (LV4E) are visual programming environments. 
The EV3 Software was built in LabVIEW, LVLM is the base software and is much more powerful.

* [ROBOTC for LEGO MINDSTORMS 4.x](http://www.robotc.net) ($49USD/year/seat; $149USD/year/6seats)
  * Seems like a visual programming environment 
  * RobotC is a C-based programming language with a fully integrated software debugger that supports a range of different hardware platforms. 
  * Debugging and lots of documentation and online support. 
  * Can be used with [Robot Virtual Worlds (RVW)](http://www.robotvirtualworlds.com/) ($49USD/seat; $149USD/6seats - not clear if separate license required or if ROBOTC license includes RVW)

* [Java with leJOS](http://www.lejos.org/ev3.php)
LeJOS (pronounced like the Spanish word “lejos” for “far”) is a tiny Java Virtual Machine that supports Java. 

### browser-based block programming IDE
* [MakeCode](https://makecode.mindstorms.com) - Microsoft MakeCode is an online programming platform that can control the EV3 and others.  MakeCode uses blocks (like Scratch) or JavaScript (text) programming.
  * USB cable only; drag code to EV3
  * [Disadvantages](https://thecodingfun.com/2020/05/28/is-it-a-good-alternative-to-use-microsoft-makecode-to-program-lego-mindstorms-ev3-part-2/) (browser based languages make debugging more difficult)

* [OpenRoberta](https://lab.open-roberta.org/)
Open Roberta is a free, drag and drop, cloud-based platform for programming LEGO EV3 and NXT robots. 

* [CoderZ](https://gocoderz.com/) ($6.25USD/month/year)
CoderZ is a 3D simulated robot environment using virtual robots that are similar to the EV3 robot.
Programming can be done with either Blockly or Java programming languages. 
For CoderZ to work with LEGO® MINDSTORMS® EV3 You will need to install [leJOS](http://www.lejos.org/ev3.php) on your EV3 Brick.

* ~~[Scratch](https://scratch.mit.edu/)~~
  * ~~Bluetooth only - can't use in competition~~
  * ~~Visual programming environment. nned Scratch link to support the EV3. ~~
  
### 3rd Party Firmware for the EV3 Brick
* [leJOS](http://www.lejos.org/ev3.php)
LeJOS (pronounced like the Spanish word “lejos” for “far”) is a tiny Java Virtual Machine that supports Java. 
* [c4ev3](https://c4ev3.github.io/) is a software package for programming stock-firmware LEGO® Mindstorms® EV3 in C/C++. 

### 3rd Party Virtual Machine installable from SD card on EV3 brick (boot from SD Card Linux image)
* [EV3dev](http://www.ev3dev.org/) 
(like a dual boot from SD card that does not overwrite firmware on EV3)
EV3dev isn’t actually a programming language, but rather a Debian Linux-based operating system that can run almost all languages that any other linux distribution can run, including C++, Node.js, and Python. 
*  [ROBOTC for LEGO MINDSTORMS 4.x](http://www.robotc.net) uses an 1. updated EV3 Linux Kernel/firmware; and 2. ROBOTC Virtual Machine (VM) to enable you to program your EV3 with ROBOTC. 
* [QEV3Bot Simulator](https://sites.google.com/site/qev3bot/qev3bot-simulator) - This is a free, educational, real-time WindowsTM based graphical simulator that accurately models a QEV3Bot running any RobotC program 

# 4. Virtual Environments
### Free
* [Virtual Robotics Toolkit (VRT)](https://www.virtualroboticstoolkit.com/) - (uses Unity)
  * [First Robotics Canada VRT free license](https://www.firstroboticscanada.org/cancode/vrt/) - uses EV3 programming environment, but is finicky to set up
* [Ev3devSim](https://www.aposteriori.com.sg/Ev3devSim/index.html) - Browser-based Simulator for EV3DEV
* [OpenRoberta](https://lab.open-roberta.org/)
  
### Paid
* [CoderZ](https://gocoderz.com/) ($6.25USD/month)
* [Robot Virtual Worlds (RVW)](http://www.robotvirtualworlds.com/) - RobotC 
  * [Virtual Brick - EV3 simulator](http://www.robotvirtualworlds.com/virtualbrick/) ($49USD/seat; $149USD/6seats)
  
# Other software
* [Lego Digital Designer](https://www.lego.com/en-us/ldd)