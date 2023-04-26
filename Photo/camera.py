import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768) # 카메라 해상도 설정
    camera.sharpness() # 선명도 설정
    camera.start_preview() # 미리보기 화면 시작
    # 2초간 대기하여 카메라가 미리보기를 시작하도록 함
    time.sleep(10)
    camera.capture('image.jpg') # 사진 촬영 후 파일로 저장