import schedule
import time
import os
import shutil
import main_run as mr
import insertDB as db


#### 특정 디렉토리 조회해서 파일 있는지 없는지 확인

# 특정 디렉토리 조회하기
# 파일이 나오면 파일 이름 찍어주기
# 파일 이름 찍어주면 따로 빼기 위해 무브


def file_move(path):
    # path = "C:/project folder/receive video"
    file_names = os.listdir(path)

    if len(file_names) > 0:
        shutil.move(path + '/' + file_names[0], 'C:/project folder/run video/')
        return file_names[0]


def job_minute():
    print("I'm working...every minute")
    b = file_move("C:/project folder/receive video")
    if b != None:
        mr.main(b)
        for f_name in os.listdir('C:/project folder/resultvideo'):
            # 파일이 존재할 경우만 처리
            print('b:', b)
            print('f_name:', f_name)
            if f_name.startswith(str(b.split('.')[0])) != None:
                for file in os.scandir('C:/project folder/frame'):
                    os.remove(file.path)
                for file in os.scandir('C:/project folder/run video'):
                    os.remove(file.path)
                for file in os.scandir('C:/project folder/invoked frame'):
                    os.remove(file.path)

                db.insert(str(b.split('.')[0]))
        b == None



# 무한 루프를 돌리다음에 waiting을 1분 걸어주면 일정 주기별 스케졸
# 1분에 한번씩 실행
schedule.every(1).minutes.do(job_minute)

while True:
    schedule.run_pending()
    time.sleep(1)





########## 10/07
########## 모델실행은 한번만 해도 가능하지 않을까?
########## main_run를 나눌 수 있지 않을까?

