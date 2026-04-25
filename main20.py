from flask import Flask #Flask 웹서버 라이브러리 가져오기
from gpiozero import LED #GPIO LED 제어용 라이브러리 가져오기
# Flask 앱 생성
app = Flask(__name__)

red_led = LED(21) #GPIO 21번 핀에 연결된 LED 객체 생성

@app.route('/') #주소 접속 시 실행
def flask():
    return "hello Flask"   #브라우저에 문자 출력

#/ledon 주소 접속 시 실행
@app.route('/ledon')
def ledOn():
    red_led.on()   #LED 켜기
    return "<h1> LED ON </h1>" #화면에서 LED 상태를 나타내는 문구


# /ledoff 주소 접속 시 실행
@app.route('/ledoff')
def LedOff():
    red_led.off()   #LED 끄기
  return "<h1> LED OFF </h1>" # 화면에서 LED 상태를 나타내는 문구


#현재 파일을 직접 실행했을 때만 서버 실행
if __name__ == "__main__":
    
    #모든 IP 접속 허용 80번 포트 사용
    app.run(host="0.0.0.0", port="80")
