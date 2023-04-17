import visa
import time
from datetime import datetime

now = datetime.now()
print(now)


fT = open('/Users/TSD/Google Drive/share-TSD/Tem_Perm/Heating-Temperature.txt', 'w+')
d = input('please input distance between lamp and KTN(/mm)')
Interval = input('please input Interval for measurement: ')
Time = int(input('please input the total Time for the measurement: '))
fT.write(str(now))
fT.write("\n")
fT.write(str(d))
fT.write(' mm')
fT.write("\n")
N = int(Time/Interval)
fT.write('Interval: ')
fT.write(str(Interval))
fT.write("\n")
fT.write('Total time: ')
fT.write(str(Time))
fT.write("\n")
fT.close()

rm = visa.ResourceManager()
print(rm.list_resources())
dev1 = rm.open_resource('GPIB0::9::INSTR')  #dev1=34970a
print(dev1.query('*IDN?'))

dev1.write("*RST")
dev1.write("SYST:DATE 2011,07,24")  # set the time
dev1.write("SYST:TIME 00,00,00")
dev1.write("CONF:TEMP TC,K,(@103)")
dev1.write("ROUT:SCAN (@103)")
dev1.write("ROUT:MON:STAT ON")
dev1.write("FORM:READ:UNIT OFF")
dev1.write("FORM:READ:TIME:TYPE ABS")
dev1.write("FORM:READ:TIME ON")

fT = open('/Users/TSD/Google Drive/share-TSD/Tem_Perm/Heating-Temperature.txt', 'a')
xixi = input('please input any number to start measurement: ')

for i in range(N):
    I = dev1.query('READ?')
    print(I)
    fT.write(str(I))
    time.sleep(Interval-0.115)

fT.close()