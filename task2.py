nums1 = [4, 1, 7, 7, 3]   # вывод: 4
nums2 = [10, 3]           # вывод: 3
nums3 = [5, 5, 5]         # вывод: Второго по величине элемента нет
data1 = []
max1 = -100000000
max2 = -10000000
for n1 in nums1:
	if n1 > max1:
		max1 = n1
for n2 in nums1:
	if n2 > max2 and n2 < max1:
		max2 = n2
		data1.append(max2)
if data1 == []:
	print('Второго по величине элемента не существует')
else:
	print(max2)
max1 = -1000000000
max2 = -1000000000
data2 = []
for n1 in nums2:
	if n1 > max1:
		max1 = n1
for n2 in nums2:
	if n2 > max2 and n2 < max1:
		max2 = n2
		data2.append(max2)
if data2 == []:
	print('Второго по величине элемента не существует')
else:
	print(max2)
max1 = -1000000000
max2 = -100000000
data3 = []
for n1 in nums3:
	if n1 > max1:
		max1 = n1
for n2 in nums3:
	if n2 > max2 and n2 < max1:
		max2 = n2
		data3.append(n2)
if data3 == []:
	print('Второго по величине элемента не существует')
else:
	print(max2)



