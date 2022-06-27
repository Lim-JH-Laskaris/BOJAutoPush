### Python - TypeError - Object of type ‘int64’ is not JSON serializable
* 참고자료 : https://frhyme.github.io/python-libs/int64_is_not_json_serializable/
* 해결방법 : move_elements 함수 내부의 for 문에서 마지막에 moving_elements리스트에 원소를 추가해줄때(코드14번째 줄) int함수추가
