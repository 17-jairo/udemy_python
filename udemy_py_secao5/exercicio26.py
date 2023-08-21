km = int(input("Insert the km: "))
gas = int(input("Insert how much gas have you spent (in liters): "))
kml = km / gas

if kml < 8:
    print("Sale this car!")

if 8< kml < 14:
    print("Economic!")

if kml > 12:
    print("Very economic!")
