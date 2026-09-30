lecture = ["Аня", "Борис", "Вика", "Гоша", "Аня"]
seminar = ["Вика", "Дима", "Борис", "Ева"]

people_at_lecture = {}
people_at_seminar = {}
for human in lecture:
	people_at_lecture[human] = people_at_lecture.get(human,0) + 1
for individ in seminar:
	people_at_seminar[individ] = people_at_seminar.get(individ,0) + 1
people_na_2_parax = []
people_only_na_lecture = []
people_hotya_bi_na_1_pare = []
for human in people_at_lecture:
	if human in people_at_seminar:
		people_na_2_parax.append(human)
	else:
		people_only_na_lecture.append(human)
for human1 in people_at_lecture:
	for human2 in people_at_seminar:
		if human1 != human2:
			people_hotya_bi_na_1_pare.append(human1)
			people_hotya_bi_na_1_pare.append(human2)
print('Всего уникальных студентов:',len(set(people_hotya_bi_na_1_pare)))
print('На обеих парах:',people_na_2_parax)
print('Только на лекции:',people_only_na_lecture)
print('Хотя бы на одной:',sorted(set(people_hotya_bi_na_1_pare)))


























