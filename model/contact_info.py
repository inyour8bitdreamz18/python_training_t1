from sys import maxsize

class ContactInfo:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None, company=None, address=None, mobile_number=None,
                 home_number=None, work_number=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, group=None, address2=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.mobile_number = mobile_number
        self.home_number = home_number
        self.work_number = work_number
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.group = group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "\nfirstname:%s\n lastname:%s\n id:%s\n" % (self.firstname, self.lastname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize