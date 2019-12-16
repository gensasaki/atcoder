import datetime
S = input()

formatted_s = datetime.datetime.strptime(S, "%Y/%m/%d")
heisei = datetime.datetime(2019, 4, 30)

if formatted_s <= heisei:
    print("Heisei")
else:
    print("TBD")