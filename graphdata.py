import matplotlib.pyplot as plt

altitude = []
speed = []
with open('test.txt') as file:
        for line in file:
                newAltitude, newSpeed = line.split()
                altitude.append(newAltitude)
                speed.append(newSpeed)

                print('Altitude: ' + newAltitude)
                print('Speed: ' + newSpeed + '\n')

plt.figure(1)
plt.plot(altitude)
plt.ylabel('Altitude')
plt.xlabel('Time')

plt.figure(2)
plt.plot(speed)
plt.ylabel('Speed')
plt.xlabel('Time')
plt.show()
