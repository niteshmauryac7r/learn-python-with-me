#Hybrid Inheritance

class Baseclass:
    pass

class DerivedClass1(Baseclass):
    pass

class DerivedClass2(Baseclass):
    pass

class DerivedClass3(DerivedClass1,DerivedClass2):
    pass

#hierarchical inheritance

class Baseclass:
    pass

class Derivedclass1(Baseclass):
    pass

class Derivedclass2(Baseclass):
    pass

class Derivedclass3(Derivedclass1):
    pass