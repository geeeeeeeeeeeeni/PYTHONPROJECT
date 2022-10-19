#step1 pymysql 모듈 불러오기

import pymysql


#step2 Mysql Connection 연결

con = pymysql.connect(
    host='172.16.12.101',
    user='scott',
    password='tiger',
    db='hr',
    charset='UTF8'
)

# step3 Connection으로 부터 Cursor 생성
cur = con.cursor();

# step4 Sql문 실행
sql = 'SELECT empno, ename, job FROM emp'
cur.execute(sql)

#데이타 fetch
rows = cur.fetchall();
print(rows)

#step5
con.close()
