from DailyPracticals.Day4.Car import Car

c1= Car("kia","fd",10000)
c2= Car("Suzuki","ffgd",10000)
c9= Car("Suzuki","ffgd",-10000)

print(c1.caclulate_premium(3))
c2.caclulate_premium(5)

Car.showCount()

c1._price = 200
c1.price =34


print(c1)
print(str(c1))
c3 = Car.from_string("kasfgfgfgd,df,5434")
print(c3)
c4 =eval(repr(c2))
