# encoding=utf-8
# @Author : wangjie
# @Time : 2021/1/13 下午4:07
import datetime


class TimeUitl():
    today = datetime.datetime.now()

#获取当天之后或之前n天的日期
    def day_gen(self,n):
        oneday = datetime.timedelta(days=n)
        day = self.today + oneday
        date_from = datetime.date(day.year, day.month, day.day)
        return str(date_from)


if __name__ == '__main__':
    date = TimeUitl().day_gen(-1)
    print(date)