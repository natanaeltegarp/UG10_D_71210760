a=float(input("Nilai a: "))
b=float(input("Nilai b: "))
c=float(input("Nilai c: "))
D=(b**2)-(4*a*c)

if D<0:
    print("Fungsi tersebut tidak memiliki akar riil")
elif D==0:
    x=((-b)+D**0.5)/2*a
    print("Fungsi tersebut memiliki akar kembar yaitu ", x)
else:
    x1=((-b)-D**0.5)/2*a
    x2=((-b)+D**0.5)/2*a
    print("Akar-akar dari persamaan tersebut adalah ", x1, " dan ", x2)