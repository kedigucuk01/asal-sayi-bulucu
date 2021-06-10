while True:
	try:
		i = int(input("Sayı giriniz: ")) # 2
	except:
		print("Hata Kodu: 5786, \nAçıklama: Lütfen bir \"tam sayı\" giriniz.")

	else:
		for s in range(2, i, 1):
			if i%s == 0:
				print(f"{i} sayısı, asal değildir.")
				break
			else:
				if s == i - 1:
					print(f"{i} sayısı, asal bir sayıdır.")


		if i < 2:
			print(f"{i} sayısı, asal değildir.")

		elif i == 2:
			print(f"{i} sayısı, asal bir sayıdır.")