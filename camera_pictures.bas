@title camera_pictures
rem runs on a chdk camer, takes pictures when voltage high level (high pwm) is recieved through chdk cable

@param o Zoom-extended
@default o 100
@param i Zoom-stowed
@default i 30
@param s Zoom-shoot
@default s 10
@param j iterations
@default j 1

while 1
   do
      k = get_usb_power
   until k>0
   gosub "takePictures" 
wend
end

:takePictures
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
