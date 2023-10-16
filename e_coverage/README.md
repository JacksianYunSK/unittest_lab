# Coverage 

- 테스트를 진행하면서 어느정도의 코드가 테스트 되었는지를 나타내는 지표입니다. 
- 각 파일별로 어느라인이 진행되었고 진행되지 않았는지 확인이 가능합니다. 
- 이 세션에서는 lcov 파일을 생성하고 적용하는 것을 실습해봅니다.

- coverage 커맨드를 통해 lcov를 만들어보겠습니다. 
```
$ coverage run -m unittest discover -s tests
$ coverage report -m
$ coverage xml
```

위 과정을 거치면 coverage.xml 파일이 생성됩니다.
이를 Coverage Gutters 플러그인을 통해 적용해보겠습니다.

