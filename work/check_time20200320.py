import pymysql
'''把你从excel表获取的每一条数据，写成元祖格式，比如（时间，需要更改的单号），再组成list
    假设有一条记录为：单号为123456，录入时间为 2016 '''
#data=[('2016','123434'),('更新的时间','需要改的单号')]

#再调用这个函数，循环去执行update语句
def update_time(datas):
    con = pymysql.connect(
            host="120.79.160.193",
            user="sxftech",
            password="sxftech@211",
            database="zsyk_dev",
            port=3306)
    # dataTable = "pymyaql")
    cur = con.cursor()
    for data in datas:
        #data【0】代表真实时间,data[1]代表需要更新的时间

        sql = "update check_report set check_time='{1}' where check_code='{0}'"
        sql = sql.format(data[0], data[1])
        try:
            cur.execute(sql)
            con.commit()
        except:
            print("没有找到数据")
    return  sql


list1 = ['201906110001','201906120002','201906120003','201906120011','201909060002','201909100002','201910100002','201911220001','201911220002','202001060001']
list2 = ['1900-01-28 10:02:04','1900-01-28 10:02:04','1954-01-28 10:02:04','2019-01-29 10:02:04','2019-01-29 10:02:04','2019-01-29 10:02:04','2019-01-29 10:02:04','2019-01-29 10:02:04','2019-01-29 10:02:04','2019-01-29 10:02:04']

datas = list(zip(list1,list2))

update_time(datas)
