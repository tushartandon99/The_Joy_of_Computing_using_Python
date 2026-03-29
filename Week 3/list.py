t1="Amit"
t2="Simran"
t3="Vidhya"
i="sudarshan"
#list
shopping=["Bread","coffee","sugar"]
print(shopping)
for i in range(3):
    print (i)
for item in shopping:
    print (item)
#append
shopping.append("curd")
print(shopping)

#insert
shopping.insert(0,"shampoo")
print(shopping)

#count
ages=[12,23,34,42,15,87,12,16,12,25,23,24,23,20]
print(ages.count(12))
print(ages.count(23))
print(ages.count(70))

#len
print(len(ages))
print(len(shopping))

#sort
ages.sort()
print(ages)

#reverse
ages.reverse()
print (ages)

students=["Arun","Rajesh","Harish","Akansha","Luxmi","Varsha"]
students.sort()
print(students)

#slicing

#list_name[start:end+1]
print(students[1:4])
print(students[-4:-1])