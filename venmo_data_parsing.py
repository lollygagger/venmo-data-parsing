import csv

class Person:
    '''
    data class for a singular person on venmo

    class constructor takes in an ammount paid and an ammount recieved


    '''
    __slots__ = ['__paid', '__recieved', '__transactions', '__name']
    def __init__(self, name, paid=0, recieved=0):
        self.__name = name
        self.__paid = paid
        self.__recieved = recieved
        self.__transactions = []

    def add_transaction(self, transaction):
        self.__transactions.append(transaction)
    def add_to_paid(self, ammount):
        self.__paid += ammount
    def add_to_recieved(self, ammount):
        self.__recieved += ammount

    def get_name(self):
        return self.__name
    def get_paid(self):
        return self.__paid
    def get_recieved(self):
        return self.__recieved


class Payment:
    __slots__ = ['__datetime', '__type', '__from', '__to', '__ammount', '__fee', '__funding_source', '__note']
    def __init__(self, datetime, ty, note, fro, to, ammount, fee, funding_source):
        if fee == '':
            fee = 0.0
        if ammount == '':
            ammount = 0.0
        
        
        self.__datetime = datetime
        self.__type = ty
        self.__from = fro
        self.__to = to
        self.__ammount = ammount
        self.__funding_source = funding_source
        self.__note = note
        self.__fee = fee


    def __str__(self):
        final = ""

        final += "Type: " + self.__type
        final += "\nFrom: " + self.__from
        final += "\nTo: " + self.__to
        final += "\nAmmount: " + str(self.__ammount)
        final += "\nNote: " + self.__note

        return final
    
    def get_datetime(self):
        return self.__datetime
    def get_type(self):
        return self.__type
    def get_from(self):
        return self.__from
    def get_to(self):
        return self.__to
    def get_ammount(self):
        return self.__ammount
    def get_fee(self):
        return self.__fee
    def get_funding_source(self):
        return self.__funding_source

def create_payments(filename):
    '''
    function parses an entire file for all transactions and creates a list of each payment

    format:
    Username,ID,Datetime,Type,Status,Note,From,To,Amount (total),Amount (fee),Funding Source,Destination,Beginning Balance,Ending Balance,Statement Period Venmo Fees,Terminal Location,Year to Date Venmo Fees,Disclaimer
    '''
    payments_list = []

    with open(filename, encoding='utf-8') as csv_file:
        csv_read = csv.reader(csv_file)
        next(csv_read)
        next(csv_read)


        for record in csv_read:
            temp_payment = Payment(record[2], record[3], record[5], record[6], record[7], record[8][3:], record[9][3:], record[11])
            payments_list.append(temp_payment)

    return payments_list

def create_people(payments_list):
    people_list = []
    for payment in payments_list:
        if payment.get_type() == "Payment":
            pass

def merge_people(person1, person2):
    if person1.get_name == person2.get_name:#if its the same person then we can merge it
        temp_person = Person(person1.get_name(), person1.get_paid() + person2.get_paid(), person1.get_recieved() + person2.get_recieved())

    return temp_person

'''

THIS NEEDS TO BE REPLACED BY merge_people()

LEGACY SHIZZ
def concat_lists(li1, li2, li3=None, li4=None, li5=None, li6=None):
    
    function will concatonate up to 6 lists at once, requires at least 2 as input
    
    final = []

    final.append(li1)
    final.append(li2)

    if li3 != None:
        final.append(li3)
    if li4 != None:
        final.append(li4)
    if li5 != None:
        final.append(li5)
    if li6 != None:
        final.append(li6)

    return final

'''

def sum_list(li):
    sum = 0
    for item in li:
        sum += int(item)

    return sum


def main():
    test = create_payments('Venmo Statements/oct_statement_2020.csv')

    for item in test:
        print('----------')
        print(item)


if __name__ == "__main__":
    main()