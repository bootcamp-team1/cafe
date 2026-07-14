"""영수증 출력 모듈."""

from datetime import datetime
from typing import TypeAlias

OrderItem: TypeAlias = dict[str, int | str]
PaymentResult: TypeAlias = dict[str, int | str]


def print_receipt(
    order: list[OrderItem],
    payment_result: PaymentResult,
) -> None:
    """주문 정보와 결제 결과를 영수증 형태로 출력한다."""
    print("\n" + "=" * 34)
    print("           CAFE RECEIPT")
    print("=" * 34)

    for item in order:
        name = str(item["name"])
        price = int(item["price"])
        quantity = int(item["quantity"])
        subtotal = price * quantity
        print(f"{name:<10} {quantity:>2}개 {subtotal:>8,}원")

    print("-" * 34)
    print(f"결제 방법: {payment_result['method']}")
    print(f"총금액: {int(payment_result['total']):,}원")
    print(f"받은 금액: {int(payment_result['paid']):,}원")
    print(f"거스름돈: {int(payment_result['change']):,}원")
    print(f"주문 시간: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("=" * 34)
    print("       이용해주셔서 감사합니다.")
    print("=" * 34)
