import csv

def parse_file_recieved(filename):
    '''
    function parses an entire file for all transactions recieved
    and returns a list of all recieved ammounts for a month

    format:
    Username,ID,Datetime,Type,Status,Note,From,To,Amount (total),Amount (fee),Funding Source,Destination,Beginning Balance,Ending Balance,Statement Period Venmo Fees,Terminal Location,Year to Date Venmo Fees,Disclaimer
    '''
    ammounts = []

    with open(filename) as file:
        csv_read = csv.reader(file)
        next(csv_read)

        for record in csv_read:
            print(record[8])
            if record[8][0] == "+": #if its adding money(we only want to count the money I recieved)
                ammounts.append(record[8].strip())




def concat_lists(li1, li2, li3=None, li4=None, li5=None, li6=None):
    '''
    function will concatonate up to 6 lists at once, requires at least 2 as input
    '''