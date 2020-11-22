'''
#TODO:
fix create_people() to include every person, right now it is skipping some people for some reason

'''


import csv

class Person:
    '''
    data class for a singular person on venmo

    class constructor takes in an ammount paid and an ammount recieved and a name


    '''
    __slots__ = ['__paid', '__recieved', '__transactions', '__name']
    def __init__(self, name, paid=0, recieved=0):
        self.__name = name
        self.__paid = float(paid)
        self.__recieved = float(recieved)
        self.__transactions = []

    def __str__(self):
        string = ""

        string += "Name: " + self.__name
        string += "\nPaid: " + str(self.__paid)
        string += "\nRecieved: " + str(self.__recieved)

        return string

    def __repr__(self):
        string = ""

        string += "Name: " + self.__name
        string += "\nPaid: " + str(self.__paid)
        string += "\nRecieved: " + str(self.__recieved)

        string += "\nTransactions: "
        for item in self.__transactions:
            string += "\n" + str(item)

        return string

    def add_transaction(self, transaction):
        self.__transactions.append(transaction)
    def add_to_paid(self, ammount):
        self.__paid += float(ammount)
    def add_to_recieved(self, ammount):
        self.__recieved += float(ammount)

    def get_name(self):
        return self.__name
    def get_paid(self):
        return self.__paid
    def get_recieved(self):
        return self.__recieved


class Payment:
    '''
    The payment class is a data class meant to store the information from one transaction on venmo

    the constructor takes in (about) all the data from one line of a venmo statement csv file
    '''
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

    def __repr__(self):
        final = ""

        final += "Datetime: " + self.__datetime
        final += "\nType: " + self.__type
        final += "\nFrom: " + self.__from
        final += "\nTo: " + self.__to
        final += "\nAmmount: " + str(self.__ammount)
        final += "\nFee: " + str(self.__fee)
        final += "\nFunding Source: " + self.__funding_source
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
    '''
    function will take a list of payment objects then parse through them to 
    take data on each person who has send or recieved a venmo

    function will return a list of people objects which each contain
    the information for one person interacting with venmo
    '''
    people_list = []
    flag = False
    for payment in payments_list:
        if payment.get_type() == "Payment":
            for person in people_list:
                if payment.get_from() == person.get_name():
                    person.add_transaction(payment)
                    person.add_to_paid(payment.get_ammount())
                    flag = True
                else:
                    pass
            if not flag:
                new_person = Person(payment.get_from(), payment.get_ammount())
                people_list.append(new_person)

    return people_list
            

def merge_people(person1, person2):
    '''
    function takes in 2 person objects and if they share the same name then it 
    will merge the 2 into another person which it returns
    '''
    if person1.get_name == person2.get_name:#if its the same person then we can merge it
        temp_person = Person(person1.get_name(), person1.get_paid() + person2.get_paid(), person1.get_recieved() + person2.get_recieved())

    return temp_person


def sum_list(li):
    #helper function to return the sum of all items in a list(as long as they are ints)
    sum = 0
    for item in li:
        sum += int(item)

    return sum


def main():
    test1 = create_payments('Venmo Statements/oct_statement_2020.csv')
    test2 = create_payments('Venmo Statements/sept_statement_2020.csv')
    people_list = create_people(test2)

    for item in people_list:
        print('----------')
        print(item)


if __name__ == "__main__":
    main()