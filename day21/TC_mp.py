import matplotlib.pyplot as plt


# plt.plot([1,2,3],[4,5,6])
# plt.show()

x=[1,2,3,4]
y=[10,20,30,40]

plt.plot(x,y,marker='o',linestyle='--')


plt.xlabel("Y axis")
plt.ylabel("Y axis")
plt.title("Line chart")
plt.grid(True)
plt.show()

names=["A","B","C"]
scores=[80,90,100]

plt.bar(names,scores)
plt.title("student scores")
plt.show()

plt.barh(names,scores) #horizontal bar graph
plt.show()

plt.scatter(x,y)
plt.show()
marks=[50,60,70,77,86]
plt.hist(marks,bins=5)
plt.title("Marks")
plt.show()

lables=["chrome","firefox","edge"]
sizes=[60,25,15]
plt.pie(sizes,labels=lables,autopct="%1.1f%%")
plt.title("browser usage")
plt.show()