# __all__
from travel import *
go_trip = china.ChinaPackage()
go_trip.detail() 

# 패키지 __init__ 에서 japan은 범위 설정을 하지 않았기 때문에 못씀
# go_trip = japan.JapanPackage()
# go_trip.JapanPackage()
