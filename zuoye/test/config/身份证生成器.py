import random
import time

#调用id_no 传参为6位数，身份证开头
class IdNo:
    def start_no(self,nub):
        '''随机生成出生日期 ；3位数字'''
        a1 = (1970, 7, 3, 18, 0, 0, 0, 0, 0)
        # 设置结束时间元组
        a2 = (2019, 9, 3, 10, 0, 0, 0, 0, 0)
        # 生成开始时间戳
        start = time.mktime(a1)
        # 生成结束时间戳
        end = time.mktime(a2)
        # 在开始时间戳和结束时间戳中随机选取一个
        t = random.randint(start, end)
        # 将时间戳转换成时间格式
        date_touple = time.localtime(t)
        date = str(time.strftime('%Y%m%d', date_touple))
        # print(date)
        end_no = str(random.randint(100, 999))
        # print(end_no)
        start = nub + date + end_no
        # print(start)
        return start

    def jiaoyanma(self,shenfenzheng17):
        '''进行身份证信息的校验;输入前17位数，自动计算第18位数'''
        def haoma_validate(shenfenzheng17):
            if type(shenfenzheng17) in [str, list, tuple]:
                if len(shenfenzheng17) == 17:
                    return True
            raise Exception('Wrong argument')
        if haoma_validate(shenfenzheng17):
            if type(shenfenzheng17) == str:
                seq = map(int, shenfenzheng17)
            elif type(shenfenzheng17) in [list, tuple]:
                seq = shenfenzheng17
            t = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            s = sum(map(lambda x: x[0] * x[1], zip(t, map(int, seq))))
            b = s % 11
            bd = {
                0: '1',
                1: '0',
                2: 'X',
                3: '9',
                4: '8',
                5: '7',
                6: '6',
                7: '5',
                8: '4',
                9: '3',
                10: '2'
            }
            return bd[b]

    def id_no(self,nub):
        start = self.start_no(nub)
        end = self.jiaoyanma(start)
        ID = start + end
        print(ID)
        return ID


if __name__ == '__main__':
    IdNo().id_no('320323')  #传的是身份证前6位 暂时未参数化
