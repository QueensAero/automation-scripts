@title 3DR Shooter
rem author Brandon Basso, 3D Robotics
rem author Dave Mitchell - dave@zenoshrdlu.com
rem This script is based on the basic Gentled CHDK2 script
rem It takes pictures and sets zooms to a few different levels

@param o Zoom-extended
@default o 100
@param i Zoom-stowed
@default i 30
@param s Zoom-shoot
@default s 10
@param j iterations
@default j 10

while 1
   do
      k = get_usb_power
   until k>0
   if k < 5 then gosub "ch1up" 
   if k > 4 and k < 8 then gosub "ch1mid" 
   if k > 7 and k < 11 then gosub "ch1down" 
   if k > 10 and k < 14 then gosub "ch2up" 
   if k > 13 and k < 17 then gosub "ch2mid" 
   if k > 16 and k < 20 then gosub "ch2down" 
   if k > 19 then print "error"
wend
end

:ch1up
   print "Shooting Pictures"; k
   for c = 1 to j
        set_zoom s
        shoot
        set_zoom i
        shoot
        set_zoom o
        shoot
		sleep 500
    next c
	do
		k = get_usb_power
	until k = 0
   return

:ch1mid
   print "Ch1Mid-Stowed"; k
   set_zoom i
   sleep 1000
   return

:ch1down
   print "Ch1Down-Extended"; k
   set_zoom o
   sleep 1000
   return

:ch2up
   return

:ch2mid
   return
	
:ch2down
   return