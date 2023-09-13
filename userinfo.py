

class User:

    def __init__(self,uid,fnm,lnm,gender,age,email,contact,adr,usernm,passwrd):
        self.user_id = uid
        self.first_name = fnm
        self.last_name = lnm
        self.gender = gender
        self.age = age
        self.email = email
        self.mobile =contact
        self.address = adr
        self.username = usernm
        self.password = passwrd

    def __str__(self):      # which is used for object presention -->
         return f"Fullname : {self.first_name} {self.last_name} Email : {self.email} Username : {self.username} Address : {self.address}"

    def __repr__(self):     # list --> repr + str           --> single/indi --> only str
         return str(self)    # one by one -->object --> str la --> present an object

#ur = User(uid=101,fnm="XXXX",lnm="YYYY",gender="M",age=23,email="avc@gmail.com",contact=8828367334,adr="Pune",usernm="python",passwrd="python123")
#print(ur)
# #print(ur.__dict__)  # entire attributes along with values
# print(ur)       # directly -- memory address --> instead properties/data... --> whatever code that you have written in str -->
#
#userlist = [ur,ur,ur]   # 3 times..
#print(userlist)

#string formatting

# result = "UserName :{}  Password:{}   FirstName:{}  Lastname:{}".format(ur.username,ur.password,ur.first_name,ur.last_name) # position
# result = "UserName :{x}  Password:{y}   FirstName:{a} Lastname:{b},".format(a=ur.first_name,b=ur.last_name,x=ur.username,y=ur.password)#name
# result = "UserName :{1}  Password:{0}   FirstName:{2} Lastname : {3}".format(ur.password,ur.username,ur.first_name,ur.last_name)
# result = f"UserName :{ur.username}  Password:{ur.password}   FirstName:{ur.first_name} Lastname:{ur.last_name}"
#
# print(result)


def take_input_from_user():
    userid = input('Enter User Id : ')
    username = input('Enter User Name : ')
    password = input('Enter Password : ')
    firstname = input('Enter FirstName : ')
    lastname = input('Enter LastName : ')
    age = int(input('Enter Age : '))
    email = input('Enter Email :')
    address = input('Enter Address : ')
    contact = int(input('Enter Mobile Number : '))
    gendertype = input('Choose Gender Type : 1. Male  2. Female')
    gender = "-"
    if gendertype == "1":
        gender = 'Male'
    elif gendertype == "2":
        gender = 'Female'
    return User(uid=userid,fnm=firstname,lnm=lastname,gender=gender,age=age,
                email=email,contact=contact,adr=address,usernm=username,passwrd=password)

