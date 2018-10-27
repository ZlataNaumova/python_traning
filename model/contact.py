from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, homephone = None, mobilephone=None,
                 workphone = None, secondaryphone=None, id=None, all_phones_from_contact_page = None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_contact_page = all_phones_from_contact_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and \
               (self.id is None or other.id is None or self.id == other.id)

    def id_or_max( self ):
        if self.id:
            return int(self.id)
        else:
            return maxsize
