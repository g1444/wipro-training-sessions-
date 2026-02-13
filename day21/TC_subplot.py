import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])
plt.title("plot 1")

plt.subplot(1,2,2)
plt.plot(["A","B","C"],[3,5,2])
plt.title("plot2")
plt.show()