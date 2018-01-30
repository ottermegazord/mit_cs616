import pycs616
import datetime

cs616 = pycs616.get_freq()
dt = datetime.datetime.now()
file = open('spot.csv', 'a')
output = "%s, %s\n" % (dt, cs616)
file.write(output)
print(output)

