
## 테스트는 왜 하는 것일까요?

- 테스트를 하면 다음과 같은 장점이 있습니다. 
    - 코드를 변경했을 때, 기존 코드가 잘 동작하는지 확인할 수 있습니다.
    - 코드를 변경했을 때, 기존 코드가 잘 동작하지 않는다면, 어떤 부분이 문제인지 확인할 수 있습니다.
    - 코드를 변경했을 때, 기존 코드가 잘 동작하지 않는다면, 어떻게 수정해야 하는지 확인할 수 있습니다.
- 하지만 테스트가 필요 없다고 하는 사람도 있습니다. 
- 이 페이지는 저의 경험에 대해 적은 내용이므로, 테스트가 필요하지 않다고 생각하시는 분은 이 페이지를 읽지 않으셔도 됩니다.


##  AssertEquls 

- 가장 많이 쓰는 AssertEquals 에 대해 알아봅니다. 
- AssertEquals 는 두 값이 같은지 확인하는 함수입니다.
- AssertEquals 는 다음과 같이 사용합니다. 

```python
self.assertEqual(1, 1)
``` 

- 위 코드는 1과 1이 같은지 확인하는 코드입니다.

## assert 함수 종류

- assert 함수는 다음과 같이 많이 있습니다. 
    - assertEqual
    - assertNotEqual
    - assertTrue
    - assertFalse
    - assertIs
    - assertIsNot
    - assertIsNone
    - assertIsNotNone
    - assertIn
    - assertNotIn
    - assertIsInstance
    - assertNotIsInstance
- 관련 사용에 대해서는 아래 링크를 참고하세요. 
    - https://docs.python.org/3/library/unittest.html#assert-methods

