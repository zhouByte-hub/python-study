## 面向对象

class Player(object): ## object是Python中的一个基类
    number = 0 ## 类属性，属于类，所有类实例都共享这个属性，也就是 Java 中的 static 属性
    address = "中国"
    lever = ['青铜', '白银', '黄金', '钻石', '大师']

    ## 实例方法
    ## 构造方法，当实例化一个类的时候被调用
    def __init__(self, name, age):
        ## 实例属性，只属于类实例，每个类实例都有自己的属性
        self.name = name
        self.age = age
        print("Player __init__")
    
    ## 实例方法
    def show(self):
        print("我是 %s，我今年 %d 岁" % (self.name, self.age))
        print("我是 %s 级" % self.lever[0])

    ## 类方法， 使用 @classmethod 装饰器；第一个参数应该是 cls，代表类本身，后面可以接其他参数
    @classmethod
    def change_lever(cls, obj):
        obj.lever[0] = "王者"
        print("我是 %s 级" % cls.lever[0])

tom = Player("张三", 18) ## 创建一个类实例
print(isinstance(tom, Player)) ## 判断tom是否是Player类的实例 True
print(isinstance(tom, object)) ## 判断tom是否是object类的实例 True
print(tom.__dict__) ## 使用__dict__属性可以查看类实例的属性字典 {}，不会输出类属性

Player.number += 100
print(Player.number) ## 100

tom.show()
Player.change_lever(tom)    ## 调用类方法



## 继承
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Animal __init__")

    def show(self):
        print("我是 %s，我今年 %d 岁" % (self.name, self.age))

class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age) ## 子类调用父类的构造方法
        print("Dog __init__")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age) ## 子类调用父类的构造方法
        print("Cat __init__")

dog = Dog("旺财", 3)
dog.show()

cat = Cat("小白", 2)
cat.show()


## 多态
def show_animal(animal: Animal):
    animal.show()

show_animal(dog)
show_animal(cat)


## 封装
class User(object):
    def __init__(self, name, age):
        self._name = name       ## 受保护的属性，protected，只能在类内部和子类中访问
        self.__age = age        ## 私有属性，private，只能在类内部访问
    
    def show(self):
        print("我是 %s，我今年 %d 岁" % (self._name, self.__age))

    def _get_age(self):     ## 受保护的方法，protected，只能在类内部和子类中访问
        self.__set_age(18)
        return self.__age
    
    def __set_age(self, age):     ## 私有方法，private，只能在类内部访问
        self.__age = age

    @property   ## 装饰器，将方法转换为属性，调用时直接通过属性名访问，不需要加括号
    def name(self):
        return self._name
    
    @name.setter   ## 装饰器，将方法转换为属性，调用时直接通过属性名赋值，不需要加括号
    def name(self, name):
        self._name = name

user = User("张三", 18)
print(user._name) ## 张三
# print(user.__age) ## 报错，不能在类外部访问私有属性

## @property和@name.setter标注的方法名一定要相同，否则会报错
print(user.name)
user.name = "李四"
print(user.name)
