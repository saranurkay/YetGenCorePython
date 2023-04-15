#!/usr/bin/env python
# coding: utf-8

# # Problem 1
# Vehicle sınıfından miras alan bir Bus sınıfı oluşturun. Bus.seating_capacity()'nin kapasite bağımsız değişkenine varsayılan olarak 50 değerini verin.
# 
# ```
# Output:
# > The seating capacity of a bus is 50 passengers
# ```
# 

# In[ ]:

class Vehicle:
    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed

class Bus(Vehicle):
    def __init__(self, color, max_speed, seating_capacity=50):
        super().__init__(color, max_speed)
        self.seating_capacity = seating_capacity

    def seating_capacity(self):
        return self.seating_capacity



# # Problem 2
# 
# 
# School_bus'ın aynı zamanda Vehicle sınıfının bir örneği olup olmadığını belirleyiniz.

# In[ ]:

    
School_bus = Bus("pink", 22)

print(isinstance(School_bus, Vehicle))

