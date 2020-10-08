import python.Vehicle as vehicle
import matplotlib.pyplot as plt

print(vehicle.steer_angles)
plt.plot(vehicle.a)
plt.ylabel('steering angles')
plt.xlabel('time')
plt.show()