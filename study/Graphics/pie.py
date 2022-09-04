import matplotlib.pyplot as plt

labels = ['Others', 'Samsung', 'Apple', 'Xiaomi', 'Vivo', 'OPPO']
values = [30, 20, 17, 13, 10, 10]
colors = ['deeppink', 'green', 'red', 'blue', 'yellow', 'orange']
explode = [0.1, 0, 0, 0, 0, 0]
plt.title('A Pie Chart')
plt.pie(values, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.show()
