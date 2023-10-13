# 시작하기 

시작하기 앞서 서버에서 실행하시는 분들은 conda로 실습환경을 만들어주세요.  
로컬 사용자는 아래 코드를 꼭 쓰실 필요는 없습니다.
```
(base) > conda create -name {사번}_unittest python=3.9
(base) > conda deactivate 
> conda activate {사번}_unittest
({사번}_unittest) > _ 
```


- VSCODE 하단부에서 Terminal을 열어 필요패키지를 설치해주세요 
```
> pip install -r requirement.txt 
```

- vscode 실행 뒤 왼쪽에 있는 플라스크 모양을 클릭하여 'Configure Python Tests' 를 클릭해 unittest를 선택해주세요. 
- test 범위 설정은 tests폴더로 정해주시고 identify test files에서는 test_*.py 타입을 선택해주세요 

![Alt text](resource/image.png)  
- RUN TEST를 클릭하여 잘 동작하는지 확인해 보시기 바랍니다.
    - 중간에 테스트가 실패하는 경우가 있을 수 있으나 지금은 무시합니다.


