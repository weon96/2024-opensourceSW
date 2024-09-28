# 샘플 Python 스크립트입니다.

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.


def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    print_hi('PyCharm')

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
fruits = {
    '사과': 1000,
    '바나나': 2000,
    '자두': 500,
    '복숭아': 4000,
}
while true:
    fruit_name = input("어서옵쇼~ 어떤 과일을 찾으세요?: ")

if fruit_name.lower() == 'exit':
    print("프로그램을 종료합니다.")
    break

# 가격 출력
if fruit_name in fruits:
    print( f"아! {fruit_name}는 {fruits[fruit_name]}원입죠~ ")
    else:
    print(f"아이고~ {fruit_name} 는 매장에 없네요.")