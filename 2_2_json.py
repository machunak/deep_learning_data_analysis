import json

j = '{"ip": "8.8.8.8"}'
#load 문자열 -> 객체 수신
#dump 객체 -> 문자열 송신
d = json.loads(j)

print(d, type(d))

st = json.dumps(d)
print(st, type(st))

dt = '''{
   "time": "03:53:25 AM",
   "milliseconds_since_epoch": 1362196405309,
   "date": "03-02-2013"
}'''

dt_load = json.loads(dt)
print(dt_load['time'])
for key in dt_load.keys():
    print(dt_load[key])