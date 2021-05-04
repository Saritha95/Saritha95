class Booking:
    def __init__(self, tickets):
        self.tickets = tickets

    def ___init__(self,passenger_name,source,destination):
        self.passenger = passenger_name
        self.source = source
        self.destination = destination

    def source_and_destination(self):
        if (self.__source=="Delhi" and (self.__destination=="Pune" or self.__destination=="Mumbai" or self.__destination=="Chennai" or self.__destination=="Kolkata")):
            return True
        else:
            return False

    def booking(self, bkticket):
        self.bkticket = bkticket
        availtk = self.tickets


        if self.tickets < self.bkticket:
            print("Availale ticket is", availtk)
            print("No tickets available")
        else:
            print("booking confirmed")
            availtk = self.tickets - self.bkticket
            print("Remaining tickets are", availtk)


bkticket = int(input("Enter how many ticket you want to enter"))

def place(self,places):
        self.places = places
        bukedplace = self.places

bukedplace = input("Enter the city")


obj = Booking(2)
obj.booking(bkticket)
