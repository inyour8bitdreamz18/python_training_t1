#class ContactInfo contained contact info

class PrimaryInfo:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, mobile_number,
                        home_number, work, fax, email, bday, bmonth, byear, aday, amonth, ayear):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.mobile_number = mobile_number
        self.home_number = home_number
        self.work = work
        self.fax = fax
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear


class SecondaryInfo:
    def __init__(self, address2, notes, phone2):
        self.address2 = address2
        self.notes = notes
        self.phone2 = phone2