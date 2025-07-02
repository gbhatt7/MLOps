class chatbook:
    
    __user_id=1
    
    def __init__(self):
        self.id=chatbook.__user_id
        chatbook.__user_id+=1
        self.__name='default'
        self.username=''
        self.password=''
        self.loggedin=False
        
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id=value
    
    def menu(self):
        user_input=input(" Welcome to chatbook! how would you like to proceed?\n1. press 1 to singup\n2. press 2 to signin\n3. press 3 to write a post\n4. press 4 to message a friend\n5.press any other key to exit")
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=='3':
            self.mypost()
        elif user_input=="4":
            self.sendmessage()
        else:
            exit()
            
    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name=value
            
    def signup(self):
        email=input("Email : ")
        pwd=input("Password : ")
        self.username=email
        self.password=pwd
        print("successfully signed up")
        print('\n')
        self.menu()
        
    def signin(self):
        if self.username=='' and self.password=='':
            print('signup first')
        else:
            uname=input("email/username : ")
            pwd=input("passsword : ")
            if self.username==uname and self.password==pwd:
                print('signed in successful')
                self.loggedin=True
            else:
                print("input correct credentials ... ")
        print('\n')
        self.menu()
    
    def mypost(self):
        if self.loggedin==True:
            txt=input("Enter the post : ")
            print(f"your post is : {txt}")
        else:
            print("signin first to post something")
        print('\n')
        self.menu()
        
    def sendmessage(self):
        if self.loggedin==True:
            txt=input("enter the message : ")
            friend=input("enter the friend name : ")
            print(f'your message {txt} is sent to {friend}')
        else:
            print("signin first to post something")
        print('\n')
        self.menu()