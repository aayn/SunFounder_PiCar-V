import requests
import time

HOST = '192.168.43.174'
PORT = '8000'
BASE_URL = 'http://' + HOST + ':'+ PORT



def __request__(url, times=10):
	for x in range(times):
		try:
			requests.get(url)
			return 0
		except :
			print("Connection error, try again")
	print("Abort")
	return -1


def mytest():
    global BASE_URL
    print(BASE_URL)
    connection_test = BASE_URL + '/connection_test/'
    print(connection_test)
    __request__(connection_test)
    fw_ready = BASE_URL + '/run/?action=fwready'
    __request__(fw_ready)
    bw_ready = BASE_URL + '/run/?action=bwready'
    __request__(bw_ready)
    speed = BASE_URL + '/run/?speed=40'
    __request__(speed)
    fw = BASE_URL + '/run/?action=forward'
    __request__(fw)
    time.sleep(5)
    stop = BASE_URL + '/run/?action=stop'
    __request__(stop)
    fwturn = BASE_URL + '/run/?action=fwturn:45'
    # __request__(fwturn)
    # __request__(stop)
    # fwturn = BASE_URL + '/run/?action=bwturn:45'
    # __request__(fwturn)


    __request__(stop)



mytest()