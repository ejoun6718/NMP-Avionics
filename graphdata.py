import matplotlib.pyplot as plt

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
plt.ylabel('Altitude')
plt.xlabel('Time(Seconds)')

plt.figure(2)
plt.plot(intervals, speed)
plt.ylabel('Speed')
plt.xlabel('Time(Seconds)')
plt.show()
