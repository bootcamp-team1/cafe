"""카페 메뉴 관리 모듈."""

from typing import TypeAlias

Menu: TypeAlias = dict[int, dict[str, int | str]]


def get_menu() -> Menu:
    """카페 메뉴 정보를 반환한다."""
    return {
        1: {"name": "아메리카노", "price": 3000},
        2: {"name": "카페라테", "price": 4000},
        3: {"name": "바닐라라테", "price": 4500},
        4: {"name": "초코라테", "price": 4500},
        5: {"name": "레몬에이드", "price": 5000},
    }


def show_menu(menu: Menu) -> None:
    """메뉴 목록을 화면에 출력한다."""
    print("\n========== 메뉴 ==========")

    for number, item in menu.items():
        name = str(item["name"])
        price = int(item["price"])
        print(f"{number}. {name:<10} {price:>5,}원")

    print("0. 주문 완료")
    print("==========================")
