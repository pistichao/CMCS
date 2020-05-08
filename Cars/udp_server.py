import os
import socket

UDP_IP = '0.0.0.0'
UDP_PORT = 9999

def listen():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(("",UDP_PORT))
	print "Server started at %s : %s " % (UDP_IP,UDP_PORT)
	status = False
	while True:
		data,ip = s.recvfrom(1024)
		print data.decode()
		while data.decode() != "STOP":
			#os.system('roslaunch drive_module telepo.launch')
			if not status:
				os.system('roslaunch ydlidar_ros_driver lidar.launch')
				status = True
		os.system('killall -9 rosmaster')
		exit()
if __name__ == "__main__":
	listen()