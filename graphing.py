import matplotlib.pyplot as plt
import numpy as np

year, comp130, comp190, comp290 = np.loadtxt("attendance.csv",
                  usecols=(0, 1, 2, 3),
                  dtype=int,
                  delimiter=",",
                  skiprows=1,
                  unpack=True)
print(year)
print(comp130)

plt.plot(year, comp130, "m-.", label="COMP130")
plt.plot(year, comp190, "r-", label="COMP190")
plt.plot(year, comp290, "y:", label="COMP290")

plt.title("Attendance through the years")
plt.xlabel("Years")
plt.ylabel("Students")
plt.legend(loc="lower right")
plt.xticks([2022, 2023, 2024])
plt.grid(True)
plt.show()
