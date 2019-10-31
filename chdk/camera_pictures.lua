--[[ @title camera_pcitures
@param f Far Zoom
@default f 10
@param m Mid Zoom
@default m 30
@param c Close Zoom
@default c 100
@param j number iterations
@default j 1
--]]


while 1 do
    k = get_usb_power(0)
    if (k>0) then
        print(k)
        takePictures()
    end
end


function takePictures(...)
    print("Shooting pictures" .. k)
    for i = 1,j do
        set_zoom(f)
        shoot()
        set_zoom(m)
        shoot()
        set_zoom(c)
        shoot()
    end
    repeat
        k = get_usb_power(0)
    until k = 0
end


