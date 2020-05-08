# CHDP
![Made by kiki](https://img.shields.io/badge/Made%20By%20KIKI-Good%20Job-brightgreen)

CHDP는 Cogs를 반대하고 쉬운 커맨드핸들러를 원하는 유저들을 위한 커맨드핸들러입니다.

클래스 싫고 일일이 cog를 추가하는게 귀찮다고요?

그렇다면 chdp를 사용해주세요

chdp는 자동으로 커맨드를 로드해주고 on_message 이벤트도 있어요

권한설정도 쉽다고요

버그가 있다고요? Issue에서 건의하세요

키키는 항상 고칠 준비가 되어있답니다.

## CHDP 사용 방법

아래 단계대로 하시면 완료입니다!

### 1. 레퍼스토리지 보고 구조 공부하기!

### 2. client.py 다운로드하기

### 3. client를 임포트하기 (import client)

### 4. client를 client.CHDPClient(prefix = '접두사', games = 봇 게임 리스트, command_dir = '커맨드파일 폴더')로 정의해주시고 on_message 함수 마지막에 client.use_cmd(message)를 작성해주세요

### 5. 커맨드파일 폴더에 파일 추가후(커맨드파일 폴더 안에 폴더 추가하고 파일 추가 가능(서버 디랙토리 설정으로 비활성화 가능)) 파일에 아래 코드를 작성해주세요

```python
name = '커맨드 이름'
aliases = '커맨드 부명령어'
user_per = '유저가 필요한 권한'
bot_per = '봇이 필요한 권한'

async def run(client, message, args):

```

### 6. run 함수에 코드를 입력해주면 끝이랍니다 ~(엄청 간단하죠 ^^)~

### client 클래스에는 prefix(접두사), cmds(명령어들, 도움말 만들때 편리) 등이 있습니다

