"""주문 및 장바구니 관리 모듈."""

from typing import TypeAlias

Menu: TypeAlias = dict[int, dict[str, int | str]]
OrderItem: TypeAlias = dict[str, int | str]


def _read_integer(message: str) -> int:
    """정수가 입력될 때까지 다시 입력받는다."""
    while True:
        value = input(message).strip()

        try:
            return int(value)
        except ValueError:
            print("숫자로 입력해주세요.")


def create_order(menu: Menu) -> list[OrderItem]:
    """사용자의 주문을 받아 장바구니 목록을 반환한다."""
    order: list[OrderItem] = []

    while True:
        menu_number = _read_integer("\n메뉴 번호를 입력하세요: ")

        if menu_number == 0:
            if not order:
                print("한 개 이상의 메뉴를 주문해주세요.")
                continue

            return order

        if menu_number not in menu:
            print("존재하지 않는 메뉴 번호입니다.")
            continue

        quantity = _read_integer("수량을 입력하세요: ")

        if quantity <= 0:
            print("수량은 1개 이상이어야 합니다.")
            continue

        selected = menu[menu_number]
        item_name = str(selected["name"])
        item_price = int(selected["price"])

        existing_item = next(
            (item for item in order if item["name"] == item_name),
            None,
        )

        if existing_item:
            existing_item["quantity"] = int(existing_item["quantity"]) + quantity
        else:
            order.append(
                {
                    "name": item_name,
                    "price": item_price,
                    "quantity": quantity,
                }
            )

        print(f"{item_name} {quantity}개가 장바구니에 추가되었습니다.")
