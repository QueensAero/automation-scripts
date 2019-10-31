@title Take Pictures
rem continually takes pictures at two different zooms

@param o Zoom-extended
@default o 100
@param i Zoom-stowed
@default i 30
@param s Zoom-shoot
@default s 10
@param j iterations
@default j 10

while 1
   gosub "shoot"
wend
end

:shoot
    set_zoom s
    shoot
    set_zoom i
    shoot
	sleep 100
 return