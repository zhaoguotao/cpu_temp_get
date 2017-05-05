#coding=utf-8
import time

#get cpu tep
def get_cpu_temp():
    cpu_temp_file = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = cpu_temp_file.read()
    cpu_temp_file.close()
    return float(cpu_temp)/1000

def main():
    while 1:
        strftime=time.strftime("%Y-%m-%d %H:%M:%S")
        print "time:",strftime
        print "cpu_temp:",get_cpu_temp()
        #sleep 6s
        time.sleep(6)

if __name__ == '__main__': 
    main()


