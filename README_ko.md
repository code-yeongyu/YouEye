# YouEye - 시각장애인을 위한 키오스크 기계 사용 도우미 솔루션

시각능력이 부족한 사람에게, 음성이 나오지 않는 키오스크를 사용하기란 대단히 어렵겠죠.

그래서, 터치하고자 하는곳에 손을 뻗고 카메라로 찍으면, YouEye가 당신이 터치 할 내용을 읽어줍니다.

현재는 파이썬용 데모와, web server 기반의 wrapper만 공개되어있습니다.  
본 프로젝트는 글자 좌표 측정을 위해 <https://github.com/code-yeongyu/east-detector-socket-wrapper> 를 사용하며, 소켓 기반의 ipc를 진행합니다.

## 현재 작업물

### 동영상

[![유튜브 시연 동영상](https://img.youtube.com/vi/GAdjqtUidms/0.jpg)](https://youtu.be/GAdjqtUidms)

### 사진

![불고기버거세트](https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_0.jpeg)

<https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_0.txt>

![양념감자1](https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_1.jpeg)

<https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_1.txt>

![빅 불고기 버거 세트](https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_2.jpeg)

<https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_2.txt>

![치즈 버거 세트](https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_3.jpeg)

<https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_3.txt>

![양념감자2](https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_4.jpeg)

<https://raw.githubusercontent.com/code-yeongyu/YouEye/master/python-demo/demo-images/result_4.txt>

모든 OCR된 결과들은 naver-ocr-api를 사용하여 생성되었고, 테서렉트와 naver-ocr-api 모두 사용 가능합니다.  
데이터셋의 빈약함 때문에, naver-ocr-api 사용을 권장합니다.

## 직접 시연해보기

이 프로젝트를 클론하시고, python-demo 디렉토리로 이동한 뒤, 다음의 명령어를 실행해주세요:

```bash
pip install -r requirements.txt
```

그리곤 다음의 명령어를 입력하면 됩니다.

```bash
python demonstration.py
```

웹 인터페이스 시연은 다음과 같이 하시면 되겠습니다.

```bash
python web-wrapper.py
```

### 웹 인터페이스

/i_am_iron_man 에 post request를 form-data 형식으로 원하는 이미지를 'image' 키에 포함시켜주세요.  
그러면 서버가 생각하던 값을 반환해줄겁니다.  
현재 웹 인터페이스는 naver-ocr-api를 사용하도록 설정되어있으니 naver-ocr-api의 사용권한을 받으시거나 tesseract를 사용하도록 설정 해야 합니다.
