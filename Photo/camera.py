import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768) # 카메라 해상도 설정
    camera.sharpness=100 # 선명도 설정


    camera.start_preview() # 미리보기 화면 시작

    while True:
        user_input = input("엔터 키를 누르면 프로그램이 종료됩니다.")
        if user_input == "":
            break


    time.sleep(10) # 2초간 대기하여 카메라가 미리보기를 시작하도록 함
    camera.capture('image.jpg') # 사진 촬영 후 파일로 저장


