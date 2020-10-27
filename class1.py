#!/usr/bin/env python
# coding: utf-8

# In[2]:


# class 만들기
class cHuman :
    def greeting(self) :
        print("안녕하세요")
        


# In[3]:


dongil = cHuman()


# In[4]:


dongil.greeting()


# In[5]:


class cHuman :     
    def greeting(self) :
        print("안녕하세요")
        
    def sing_a_song(self) :
        self.greeting()
        print("랄라라라라")


# In[6]:


dongil = cHuman()
dongil.sing_a_song()


# In[9]:


# class data 초기화, 설계도에 잘못 입력...
class cHuman :     
    def __init__(self) :
        self.name = "동일"
        self.age = 20
        self.city = 'Daejeon'
        
    def greeting(self) :
        print("안녕하세요")
        
    def sing_a_song(self) :
        self.greeting()
        print("랄라라라라")


# In[10]:


dd = cHuman()

dd.name


# In[11]:


dd1 = cHuman()
dd1.name


# In[12]:


# class data 초기화

class cHuman :     
    def __init__(self, name, age, city) :
        self.name = name
        self.age = age
        self.city = city
        
    def greeting(self) :
        print("안녕하세요")
        
    def sing_a_song(self) :
        self.greeting()
        print("랄라라라라")


# In[13]:


# dd = cHuman()

dd = cHuman("dongil", 20, "Daejeon")


# In[14]:


dd.sing_a_song()


# In[15]:


dd.name


# In[16]:


dd.city


# In[17]:


dd2 = cHuman('mina', 22, 'seoul')
dd3 = cHuman('kim', 33, 'busan')


# In[18]:


dd2.name


# In[19]:


dd3.city


# In[ ]:





# In[21]:


# class 내부 data
class cHuman :   
    gender = ''
    items = []
    
    def __init__(self, name, age, city) :
        self.name = name
        self.age = age
        self.city = city
        
    def addItem(self, item) :
        self.items.append(item)
        print(item, "추가...")
        
    def getItem(self) :
        print(self.items)
        
    def greeting(self) :
        print("안녕하세요")
        
    def sing_a_song(self) :
        self.greeting()
        print("랄라라라라")


# In[22]:


# 인스턴스 생성

kim = cHuman('kim', 33, 'busan')


# In[23]:


# item 직접 넣기
kim.items.append("스마트폰")


# In[24]:


kim.items


# In[25]:


kim.addItem("컴퓨터")


# In[26]:


kim.items


# In[27]:


# 데이터를 클래스 내부 메소드를 통해서만 접근 가능하도록
# 디버깅... 재사용성 등..

class cHuman :   
    gender = ''
    __items = []
    
    def __init__(self, name, age, city) :
        self.name = name
        self.age = age
        self.city = city
        
    def addItem(self, item) :
        self.__items.append(item)
        print(item, "추가...")
        
    def getItem(self) :
        print(self.__items)


# In[28]:


mina = cHuman('mina', 22, 'seoul')


# In[29]:


# mina.__items.append("책 한권")
mina.addItem("책 한권")


# In[30]:


# private, public
class cHuman :   
    gender = ''
    __items = []
    
    def __init__(self, name, age, city) :
        self.name = name
        self.__age = age
        self.city = city
        
    def addItem(self, item) :
        self.__items.append(item)
        print(item, "추가...")
        
    def getItem(self) :
        print(self.__items)


# In[31]:


mina2 = cHuman('mina2', '27', 'seoul')


# In[33]:


# mina2.age
mina2.__age


# In[37]:


# private, public ==> 내부 처리값, 외부 리턴값...
class cHuman :   
    gender = ''
    __items = []
    
    def __init__(self, name, age, city) :
        self.name = name
        self.__age = age
        self.city = city
        
    def getAge(self) :
        print(self.__age - 5)
        
    def addItem(self, item) :
        self.__items.append(item)
        print(item, "추가...")
        
    def getItem(self) :
        print(self.__items)


# In[38]:


mina3 = cHuman('mina3', 28, 'daejeon')


# In[39]:


mina3.getAge()


# In[40]:


# 정적 메소드 (static method)
# 인스턴스가 따로 필요 없는 경우..

class Calcul :
    @staticmethod
    
#     def add(self, a, b) :
    def add(a, b) :
        return a+b


# In[41]:


Calcul.add(10, 11)


# In[ ]:





# In[42]:


# 클래스의 상속
class cHuman2 :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        
    def greeting(self) :
        print('안녕하세요. 저는 %s 입니다.'%self.name)


# In[43]:


kim2 = cHuman2('kim2', 33)


# In[44]:


kim2.greeting()


# In[45]:


class Student(cHuman2) :
    pass


# In[46]:


min = Student('minho', 20)


# In[47]:


min.greeting()


# In[49]:


# class method 추가
class Student(cHuman2) :
    def study(self) :
        print("열공중입니다~")


# In[50]:


min2 = Student('민학생', 21)
min = cHuman2('minho', 22)


# In[51]:


min2.study()


# In[52]:


min.study()


# In[54]:


# 자식 class 별도 init
class Student(cHuman2) :
    
    def __init__(self, name, age, sid) :
        self.name = name
        self.age = age
        self.sid = sid
    
    def study(self) :
        print("열공중입니다~")


# In[55]:


mm = Student('김학생', 22)


# In[56]:


mm = Student('김학생', 22, 12345)


# In[57]:


mm.greeting()


# In[58]:


mm.study()


# In[62]:


# 자식 class에서 부모클래스 method와 이름 같게

class Student(cHuman2) :
    
    def __init__(self, name, age, sid) :
        self.name = name
        self.age = age
        self.sid = sid
        
    def greeting(self) :
        print("안녕하세요. student 입니다.")
    
    def study(self) :
        print("열공중입니다~")


# In[63]:


mm = Student('김학생', 22, 12345)


# In[65]:


# 자식 본인의 class method가 먼저 호출
mm.greeting()


# In[66]:


# 부모 super class method 호출하기
class Student(cHuman2) :
    
    def __init__(self, name, age, sid) :
        self.name = name
        self.age = age
        self.sid = sid
        
    def greeting(self) :
        super().greeting()
        print("안녕하세요. student 입니다.")
    
    def study(self) :
        print("열공중입니다~")


# In[67]:


s1 = Student('김학생', 22, 12345)


# In[68]:


s1.greeting()


# In[69]:


class colleage(Student) :
    moim = ''
    


# In[70]:


c1 = colleage('김대학생', 22, 12345)


# In[71]:


c1.greeting()


# In[72]:


c1.moim = '방송부'


# In[73]:


c1.moim


# In[75]:


# getInfo 추가
class Student(cHuman2) :   
    def __init__(self, name, age, sid) :
        self.name = name
        self.age = age
        self.sid = sid
        
    def getInfo(self) :
        print('name :', self.name)
        print('age :', self.age)
        print('sid :', self.sid)
        
    def greeting(self) :
        super().greeting()
        print("안녕하세요. student 입니다.")
    
    def study(self) :
        print("열공중입니다~")

class colleage(Student) :
    moim = ''
    
    def getInfo(self) :
        super().getInfo()
        print('moim :', self.moim)     


# In[76]:


c2 = colleage('나대학생', 22, 112233)


# In[77]:


c2.moim = '연극부'


# In[78]:


c2.getInfo()


# In[79]:


# 다중 상속
class university :
    uni_name = ''
    uni_address = ''


# In[80]:


class colleage(Student, university) :
    pass


# In[81]:


c3 = colleage('남대학생', 23, 1234)
c3.uni_name = '해운대'
c3.uni_address = '부산시 해운대구'
c3.moim = '출판부'


# In[82]:


c3.greeting()


# In[83]:


c3.getInfo()


# In[84]:


# 다중상속 문제.... 속성끼리 꼬이는 거... 혼란... 예상치 못한 결과..
# 따라서, 다중상속을 최소화... java c# 에서는 금지, c++ 가능
# 추상 클래스....

