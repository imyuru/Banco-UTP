from datetime import datetime

centro = '*'
opcion = 0
op1 = 0
op2 = 0


class Account:
    def __init__(self, numberAccount, nameClient, balance):
        self.numberAccount = numberAccount
        self.nameClient = nameClient
        self.balance = balance

    def Deposit(self, value):
        self.balance += value

    def Consult(self):
        print(self.balance)

    def Withdrawals(self, value):
        self.balance -= value


class SavingsAccount(Account):
    def __init__(self, numberAccount, nameClient, balance, dateInitial, dateFinal):
        super().__init__(numberAccount, nameClient, balance)
        self.dateInitial = dateInitial
        self.dateFinal = dateFinal

    def final(self):
        return self.dateFinal

    def initial(self):
        return self.dateInitial

    def mostrar_informacion(self):
        print(self.dateInitial)
        print(self.dateFinal)
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
            dateInitial = input("Ingrese la fecha actual (en formato dd/mm/aaaa): ")
            try:
                dateInitial = datetime.strptime(dateInitial, "%d/%m/%Y")
                print("Fecha ingresada:", dateInitial)
            except ValueError:
                print("Fecha inválida. Asegúrese de seguir el formato dd/mm/aaaa.")

            DueDate = input("Ingrese una fecha de retiro (en formato dd/mm/aaaa): ")
            try:
                DueDate = datetime.strptime(DueDate, "%d/%m/%Y")
                print("Fecha ingresada:", DueDate)
            except ValueError:
                print("Fecha inválida. Asegúrese de seguir el formato dd/mm/aaaa.")
            newaccount = SavingsAccount(bank.accountNumber(), nClient, 0, dateInitial, DueDate)
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
                if nSus <= bank.accountNumber():
                    obj = bank.accounts[nSus]
                    deposit = float(input("Cuanto dinero desea ingresar: "))
                    obj.Deposit(deposit)
                    print("Dinero Depositado")
                    bank.accounts[nSus] = obj
                else:
                    print("Cuenta no existente")

            if op2 == 2:
                nSus = int(input("Ingrese su numero de suscriptor: "))
                if nSus <= bank.accountNumber():
                    obj = bank.accounts[nSus]
                    today = input("Ingrese la fecha actual (en formato dd/mm/aaaa): ")
                    try:
                        today = datetime.strptime(today, "%d/%m/%Y")
                        print("Fecha ingresada:", today)
                    except ValueError:
                        print("Fecha inválida. Asegúrese de seguir el formato dd/mm/aaaa.")
                    if obj.final() == today:
                        print(f"Su saldo actual bruto es: {obj.balance}")
                        diferenciaMeses = (obj.final().year - obj.initial().year) * 12 + (
                                obj.final().month - obj.initial().month)
                        if obj.initial().day > obj.final().day:
                            diferenciaMeses -= 1
                        print("Han pasado", diferenciaMeses, "meses entre las fechas.")
                        impuesto = diferenciaMeses * 5.00
                        if impuesto > obj.balance:
                            print("No puede retirar el dinero hasta que tenga mínimo, que es el pago del impuesto")
                            print(impuesto)
                        else:
                            print(f"Debe pagar {impuesto} de impuesto")
                            print(f"se retirara de la cuenta {obj.balance - impuesto}$")
                            obj.Withdrawals(obj.balance - impuesto)
                            print(f"Se ha retirado el dinero y eliminado la cuenta")
                    else:
                        print("Fecha final no coincide con la fecha actual, no puede retirar")
                else:
                    print("Cuenta no existente")
            if op2 == 3:
                nSus = int(input("Ingrese su numero de suscriptor: "))
                if nSus <= bank.accountNumber():
                    obj = bank.accounts[nSus]
                    print(f"Su dinero actual sin impuestos ni mantenimiento de cuenta es  {obj.balance}")
                else:
                    print("Cuenta no existente")
        if op1 == 2:
            print("1. Deposito")
            print("2. Uso de chequera")
            print("3. Consultar dinero")
            op2 = int(input("Ingrese una opción: "))
            if op2 == 1:
                nSus = int(input("Ingrese su numero de suscriptor: "))
                if nSus <= bank.accountNumber():
                    obj = bank.accounts[nSus]
                    deposit = float(input("Cuanto dinero desea ingresar: "))
                    obj.Deposit(deposit)
                    print("Dinero Depositado")
                    bank.accounts[nSus] = obj
                else:
                    print("Cuenta no existente")
            if op2 == 2:
                nSus = int(input("Ingrese su numero de suscriptor: "))
                if nSus <= bank.accountNumber():
                    obj = bank.accounts[nSus]
                    pago = float(input("Cuanto dinero desea en cheques: "))

                    if obj.balance >= 0.0:
                        print(
                            "Su saldo es menor de 0, por cada dolar que saque se le cobrara un impuesto de 0.50 "
                            "hasta que su dinero no esté en números negativos")
                        impuesto=(pago * 0.50)
                        pago = impuesto + pago
                        obj.Withdrawals(pago)

                    else:
                        obj.Withdrawals(pago)
                    print(f"Dinero retirado, nuevo saldo {obj.balance}")
                    bank.accounts[nSus] = obj
                else:
                    print("Cuenta no existente")

            if op2 == 3:
                nSus = int(input("Ingrese su numero de suscriptor: "))
                if nSus <= bank.accountNumber():
                    obj = bank.accounts[nSus]
                    print(f"SU SALDO ES DE {obj.balance}$")

                else:
                    print("Cuenta no existente")

    else:
        print("Opción inválida")

    continuar = input("¿Desea regresar al menú principal? (s/n): ")
    if continuar.lower() != 's':
        break



"""Nota para el eduardo del futuro, ojo debes ver lo de la fecha inicial y fecha final en las cuentas """