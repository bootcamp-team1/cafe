"""금액 계산 및 결제 모듈."""

from typing import TypeAlias

OrderItem: TypeAlias = dict[str, int | str]
PaymentResult: TypeAlias = dict[str, int | str]

_CARD = "1"
_CASH = "2"


def calculate_total(order: list[OrderItem]) -> int:
    """주문 목록의 상품 가격과 수량을 이용해 총금액을 계산한다."""
    total = 0

    for item in order:
        price = int(item["price"])
        quantity = int(item["quantity"])

        total += price * quantity

    return total


def _read_payment_method() -> str:
    """올바른 결제 방법이 입력될 때까지 반복해서 입력받는다."""
    while True:
        method = input(
            "결제 방법을 선택하세요 (1: 카드, 2: 현금): "
        ).strip()

        if method in {_CARD, _CASH}:
            return method

        print("1 또는 2를 입력해주세요.")


def _read_cash_amount() -> int:
    """0원 이상의 현금 금액이 입력될 때까지 반복해서 입력받는다."""
    while True:
        paid_text = (
            input("받은 현금 금액을 입력하세요: ")
            .strip()
            .replace(",", "")
        )

        try:
            paid = int(paid_text)
        except ValueError:
            print("금액은 숫자로 입력해주세요.")
            continue

        if paid < 0:
            print("금액은 0원 이상이어야 합니다.")
            continue

        return paid


def _create_payment_result(
    method: str,
    total: int,
    paid: int,
) -> PaymentResult:
    """영수증 모듈에서 사용하는 형식으로 결제 결과를 생성한다."""
    return {
        "method": method,
        "total": total,
        "paid": paid,
        "change": paid - total,
    }


def process_payment(total: int) -> PaymentResult:
    """카드 또는 현금 결제를 처리하고 결제 결과를 반환한다."""
    if total < 0:
        raise ValueError("총금액은 0원 이상이어야 합니다.")

    print(f"\n결제 금액: {total:,}원")

    method = _read_payment_method()

    if method == _CARD:
        print("카드 결제가 완료되었습니다.")

        return _create_payment_result(
            method="카드",
            total=total,
            paid=total,
        )

    while True:
        paid = _read_cash_amount()

        if paid < total:
            shortage = total - paid
            print(f"결제 금액이 {shortage:,}원 부족합니다.")
            continue

        payment_result = _create_payment_result(
            method="현금",
            total=total,
            paid=paid,
        )

        print(
            "현금 결제가 완료되었습니다. "
            f"거스름돈: {payment_result['change']:,}원"
        )

        return payment_result