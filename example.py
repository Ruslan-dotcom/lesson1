def get_vat(payment, percent = 18):
	try:
		payment = float(payment)
		percent = int(percent)
		vat = payment/100*percent
		vat = round(vat, 2)
		return "Сумма НДС: {}".format(vat)
	except (TypeError, ValueError):
		print("Не могу посчитать")	

result = get_vat(400, "ololo")
print(result)
