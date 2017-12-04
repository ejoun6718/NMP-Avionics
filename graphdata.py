import matplotlib.pyplot as plt
import serial

filename = "data.txt"

ser = serial.Serial('dev/cu.usbmodemFA131 (Arduino/Genuino Uno)', 9600);
f = open(filename, "w")

while True:
        x = ser.readline()
        f.write(x)
f.close()


altitude = []
speed = []
intervals = []
i = 0
with open('test.txt') as file:
        for line in file:
                newAltitude, newSpeed = line.split()
                altitude.append(newAltitude)
                speed.append(newSpeed)
                intervals.append(i)
                i = i + 0.5

                print('Altitude: ' + newAltitude)
                print('Speed: ' + newSpeed + '\n')

plt.figure(1)
plt.plot(intervals, altitude)
plt.ylabel('Altitude(feet)')
plt.xlabel('Time(seconds)')

plt.figure(2)
plt.plot(intervals, speed)
plt.ylabel('Speed(knots)')
plt.xlabel('Time(seconds)')
plt.show()
