from flask import Flask, render_template, request # Flask 웹서버 라이브러리
from gpiozero import LED # GPIO LED 제어 라이브러리
app = Flask(__name__) #Flask 앱 생성
red_led = LED(21) #GPIO 21번 핀 LED 연결

#화면 접속 시 index.html 보여주기
@app.route('/')
def home():
    return render_template("index.html")
  
# 버튼 눌렀을 때 실행되는 주소
# POST 방식으로 데이터 받음
@app.route('/data', methods=['POST'])
def data():

    #HTML 폼에서 led 값 가져오기
    data = request.form['led']

    #ON 버튼 눌렀다면
    if(data == 'on'):
        red_led.on()

    #OFF 버튼 눌렀다면
    elif(data == 'off'):
        red_led.off()
      
    #다시 메인 페이지로 이동
    return home()

# 서버 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
