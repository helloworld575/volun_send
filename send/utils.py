from django.utils import timezone
import datetime
def get_volun_time(a,b):
    if (a==b) or (a=='1' and b=='3') or (b=='1'and a=='3') or (a=='1' and b=='4') or (a=='4' and b=='1'):
        return 0.5
    if (a=='1' and b=='2') or (b=='1' and a=='2') or (a=='2' and b=='3') or (a=='3' and b=='2') or (a=='2' and b=='4') or (a=='4' and b=='2') or (a=='3' and b=='4') or (a=='4' and b=='3'):
        return 1

def get_time(a):
    now_date=timezone.datetime.today()
    then_time=datetime.time(a+12,00,00)
    return datetime.datetime(year=now_date.year,month=now_date.month,day=now_date.day,hour=then_time.hour,minute=then_time.minute,second=then_time.second)
