from person import Person






if __name__ == '__main__':
    Dillon = Person('555-55-5555', 'Dillon', 'Potato')

    print(Dillon)
    Dillon.setAge(13)
    print(Dillon)
    Dillon.multiplyTwo()
    print(Dillon)

    Leanne = Person('876-53-0909', 'Leanne', 1)


    print("\n")
    print(Leanne)
    Leanne.setAge('Potato')
    Leanne.setAge(14)
    print(Leanne)
    Leanne.multiplyTwo()
    print(Leanne)



