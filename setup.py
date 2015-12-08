import usb.core
import usb.util

def setup() : 
	device = usb.core.find(idVendor=0x045e,idProduct=0x2ae)
	if device is None : 
		raise ValueError('no device found')
	else : 
		print('Kinect connected !')
	device.set_configuration()
	cfg = device.get_active_configuration()
	print(cfg)

setup()

# def crawl() :
# 	count = 10 
# 	for i in range(65536) : 
# 		for j in range(65536) :
# 			device = usb.core.find(idVendor=i,idProduct=j)
# 			if device is None : 
# 				pass
# 			else : 
# 				print('device found',i,j)
# 			print(i,j)

# 		# if(65536*i + j > (65536*65536)/count) :
# 		# 	print('#',end='')
# 		# 	count -= 1
# 		print(i,j)

# crawl()