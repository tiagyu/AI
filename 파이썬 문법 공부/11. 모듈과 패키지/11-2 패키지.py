# 패키지 이용
"""
class 또는 함수는 import를 할 수 없다
모듈과 패키지만 import를 할 수 있다
"""
import travel.china
trip_to = travel.china.ChinaPackage()
trip_to.detail()

from travel.china import ChinaPackage
go_trip = ChinaPackage()
go_trip.detail()

from travel import japan
go_trip = japan.JapanPackage()
go_trip.detail()