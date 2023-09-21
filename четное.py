заново = "r"
while заново == "r":
    x = float (input ("Введите число"))
    def chet (x):
        if x%2==0:
            print(x,True)
        else:
            print(x, False)
            
    chet (x)
else: 
    print ("Ошибка")