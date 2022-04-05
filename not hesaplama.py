vize1=int(input("vize-1:"))
vize2=int(input("vize-2:"))
final=int(input("final:"))

avarage_note=vize1*(30/100)+vize2*(30/100)+final*(40/100)

if avarage_note>=90:
    print("AA")
elif avarage_note>=85:
    print("BA")
elif avarage_note>=80:
    print("BB")
elif avarage_note>=75:
    print("CB")
elif avarage_note>=70:
    print("CC")
elif avarage_note>=65:
    print("DC")
elif avarage_note>=60:
    print("DD")
elif avarage_note>=55:
    print("FD")
else:
    print("FF")
