a=int(input("Masukkan bilangan 1 :"))
b=int(input("Masukkan bilangan 2 :"))
c=int(input("Masukkan bilangan 3 :"))
if a<b:
    a,b=b,a
    if a<c:
        a,c=c,a
        if b<c:
            b,c=c,b
            print("Urutan bilangan dari yang terbesar adalah :", a, b, c)
        else:
            print("Urutan bilangan dari yang terbesar adalah :", a, b, c)
    else:
        if b<c:
            b,c=c,b
            print("Urutan bilangan dari yang terbesar adalah :", a, b, c)
        else:
            print("Urutan bilangan dari yang terbesar adalah :", a, b, c)
else:
    if a<c:
        a,c=c,a
        if b<c:
            b,c=c,b
            print("Urutan bilangan dari yang terbesar adalah :", a, b, c)
        else:
            print("Urutan bilangan dari yang terbesar adalah :", a, b, c)
    else:
        if b<c:
            b,c=c,b
            print("Urutan bilangan dari yang terbesar adalah :", a, b, c)
        else:
            print("Urutan bilangan dari yang terbesar adalah :", a, b, c)