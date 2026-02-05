def triple_and(name,age,rela):
    if(name=='vishva'):
        if(age==18):
            if(rela=='single'):
                print(True)

name=input("enter name").lower().strip()
age=int(input("enter age: "))
rela=input("enter single or comitted ").lower().strip()
triple_and(name,age,rela)
