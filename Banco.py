from datetime import datetime
centro = '*'
opcion=0
op1=0
op2=0
class Account:
    def __init__(self, numberAccount, nameClient, balance):
        self.numberAccount = numberAccount
        self.nameClient = nameClient
        self.balance = balance

    def Deposit(self, value ):
        self.balance += value

    def Consult(self):
        print(self.balance)

    def Withdrawals(self, value):
        self.balance -= value


class SavingsAccount(Account):
    def __init__(self, numberAccount, nameClient, balance, date):
        super().__init__(numberAccount, nameClient, balance)
        self.date = date

    def mostrar_informacion(self):
        print(self.date)
        print(self.numberAccount)
        print(self.nameClient)
        print(self.balance)


class CheckingAccount(Account):
    def __init__(self, numberAccount, nameClient, balance):
        super().__init__(numberAccount, nameClient, balance)

    def mostrar_informacion(self):
        print(self.numberAccount)
        print(self.nameClient)
        print(self.balance)


class Bank:
    def __init__(self):
        self.accounts = []

    def accountNumber(self):
        return len(self.accounts)

    def add(self, account):
        self.accounts.append(account)

    def see(self):
        for cuenta in self.accounts:
            cuenta.mostrar_informacion()


bank = Bank()

while True:
    print("Bienvenido al mini proyecto 1".center(70, '-'))
    print("Menú".center(70, '-'))
    print("1. Registro de una cuenta")
    print("2. Movimientos y Consultas")

    opcion = int(input("Ingrese una opción: "))
    print("\n")

    if opcion == 1:
        print("1. Registro Cuenta de Ahorros")
        print("2. Registro Cuenta de Cheques ")
        op1 = int(input("Ingrese una opción: "))

        if op1 == 1:
            nClient = ""
            print("Bienvenid@ al sistema de registro de Cuentas de Ahorros")
            print(f"Numero de suscriptor : {bank.accountNumber()}")
            nClient = str(input("Ingrese su nombre: "))
            DueDate = input("Ingrese una fecha de retiro (en formato dd/mm/aaaa): ")
            try:
                DueDate = datetime.strptime(DueDate, "%d/%m/%Y")
                print("Fecha ingresada:", DueDate)
            except ValueError:
                print("Fecha inválida. Asegúrese de seguir el formato dd/mm/aaaa.")
            newaccount = SavingsAccount(bank.accountNumber(), nClient, 0, DueDate)
            bank.add(newaccount)
            bank.see()

        elif op1 == 2:
            nClient = ""
            print("Bienvenid@ al sistema de registro de Cuentas de Cheques")
            print(f"Numero de suscriptor : {bank.accountNumber()}")
            nClient = str(input("Ingrese su nombre: "))
            newaccount = CheckingAccount(bank.accountNumber(), nClient, 0)
            bank.add(newaccount)
            bank.see()

    elif opcion == 2:
        print("Bienvenid@ al sistema de movimientos")
        print("1. Cuenta de Ahorros")
        print("2. Cuenta de Cheques ")
        op1 = int(input("Ingrese una opción: "))

        if op1 == 1:
            print("1. Deposito")
            print("2. Retiro")
            print("3. Consultar")
            op2 = int(input("Ingrese una opción: "))

            if op2 == 1:
                nSus = int(input("Ingrese su numero de suscriptor: "))
                if nSus<=bank.accountNumber():
                    obj = bank.accounts[nSus]
                    deposit = float(input("Cuanto dinero desea ingresar: "))
                    obj.Deposit(deposit)
                    print("Dinero Depositado")
                    bank.accounts[nSus] = obj
                else:
                    print("Cuenta no existente")
    else:
        print("Opción inválida")

    continuar = input("¿Desea regresar al menu principal? (s/n): ")
    if continuar.lower() != 's':
        break




"""Nota para el eduardo del futuro, ojo debes ver lo de la fecha inicial y fecha final en las cuentas """