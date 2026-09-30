nums = [1, 2, 3, 4, 5, 6, 4]
target = 7
otvet = list()
for n1 in nums:
	for n2 in nums:
		if [n2,n1] not in otvet:
			if nums.index(n1) != nums.index(n2):
				if [n1,n2] not in otvet:
					if (n1 + n2) == target:
						otvet.append([n1,n2])
print(otvet)