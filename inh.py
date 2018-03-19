class parent():
    def __init__(self,last_name,eye_color):
        print "parent costructor called"
        self.last_name = last_name
        self.eye_color = eye_color


class child(parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print "child constructor called"
        parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys



billy_cyrus = child("cyrus","blue",15)
print billy_cyrus.last_name




