from datetime import date,timedelta
d_int = [
        [21,19,"aquarius"],
        [20,20,"pisces"],
        [21,20,"aries"],
        [21,21,"taurus"],
        [22,21,"gemini"],
        [22,22,"cancer"],
        [23,21,"leo"],
        [22,23,"virgo"],
        [24,23,"libra"],
        [24,22,"scorpio"],
        [23,22,"sagittarius"],
        [23,20,"capricorn"]]


def get_zodiacsign(d_obj):
    for e in range(12):
        if (d_int[e][0] <= d_obj.day and (e+1) == d_obj.month) or \
                (d_int[e][1] >= d_obj.day and (e+2 if e+2 < 13 else 1) == d_obj.month):
            return d_int[e][2]
w40 = timedelta(weeks=40)
t = int(input())
caso = 0
while t:
    t-=1
    caso += 1
    l = input()
    m,d,y = int(l[:2],10),int(l[2:4],10),int(l[4:],10)
    d_obj = date(y,m,d)+w40
    zs = get_zodiacsign(d_obj)
    print("{} {} {}".format(caso,d_obj.strftime("%m/%d/%Y"),zs))

