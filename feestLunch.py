croissaints = 17
bread = 2
coupons = 3

croissaintsPrice = 0.39
breadPrice = 2.78
discount = 0.50

outCome = croissaintsPrice * 17 + breadPrice * 2 - discount * 3

text = "De feestlunch kost je bij de bakker " + str(outCome) + " euro voor de " + str(croissaints) + " croissantjes en de " + str(bread) + " stokbroden als de " + str(coupons) + " kortingsbonnen nog geldig zijn!"

print(text)
