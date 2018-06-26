import random
from datetime import datetime
from datetime import timedelta
nday = []
w = []
t = []
h = []
p = []
for j in range(10):
    t.append(random.randint(75, 85))
    w.append(random.randint(9, 11))
    h.append(random.randint(55, 62))
    p.append(random.randint(90, 120))
StartDate = datetime.now()
StartDate=StartDate.strftime("%d/%m/%y")
day = 10
Date = datetime.strptime(StartDate, "%d/%m/%y")
for d in range(day):
    EndDate = Date.today()+timedelta(days=d)
    
    nday.append(EndDate.strftime("%d/%m/%y"))
    
        
