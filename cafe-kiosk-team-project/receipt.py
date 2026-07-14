"""웃긴 영수증 출력 모듈."""

from datetime import datetime
from typing import TypeAlias

OrderItem: TypeAlias = dict[str, int | str]
PaymentResult: TypeAlias = dict[str, int | str]


def print_receipt(
    order: list[OrderItem],
    payment_result: PaymentResult,
) -> None:
    """주문 정보와 결제 결과를 재미있는 영수증 형태로 출력한다."""

    print("\n" + "=" * 40)
    print("        ☕ CAFE HAPPINESS RECEIPT ☕")
    print("=" * 40)

    for item in order:
        name = str(item["name"])
        price = int(item["price"])
        quantity = int(item["quantity"])
        subtotal = price * quantity

        print(f"{name:<12} x {quantity:<2} = {subtotal:>8,}원")

    print("-" * 40)

    total = int(payment_result["total"])

    print(f"💳 결제 방법 : {payment_result['method']}")
    print(f"💰 총 금액   : {total:,}원")
    print(f"💵 받은 금액 : {int(payment_result['paid']):,}원")
    print(f"🪙 거스름돈  : {int(payment_result['change']):,}원")

    print("-" * 40)

    messages = [
        "오늘도 커피로 버티는 당신... 멋집니다 ☕",
        "카페인 충전 완료! 이제 일하세요(?) 😎",
        "커피값은 비싸지만 행복도 같이 결제되었습니다 😆",
        "당신의 피로도가 10% 감소했습니다 ✨",
    ]

    print(f"📝 오늘의 한마디 : {messages[total % len(messages)]}")

    print(f"🕒 주문 시간 : {datetime.now():%Y-%m-%d %H:%M:%S}")

    print("=" * 40)
    print("     감사합니다! 다음에는 디저트도 사주세요 🍰")
    print("=" * 40)