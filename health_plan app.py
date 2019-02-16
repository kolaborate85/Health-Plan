class healthplan:
  def __init__(self, plan, coverage):
    self.plan = plan 
    self.coverage = coverage
  #coverage is prepaid money for health service
  def deduct(self, deduct_coverage):
    self.coverage -= deduct_coverage
#deductible is cost deduct from coverage
myplan = healthplan("studentplan", 1500) # object created

print(myplan.plan)
print(myplan.coverage)

myplan.deduct(300) # this gives you the deductable cost
print(myplan.coverage)