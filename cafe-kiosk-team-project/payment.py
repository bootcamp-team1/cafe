"""금액 계산 및 결제 모듈."""

from typing import TypeAlias

OrderItem: TypeAlias = dict[str, int | str]
PaymentResult: TypeAlias = dict[str, int | str]


def calculate_total(order: list[OrderItem]) -> int:
    """주문 목록의 총금액을 계산한다."""
    return sum(
        int(item["price"]) * int(item["quantity"])
        for item in order
    )


def process_payment(total: int) -> PaymentResult:
    """결제 방법과 받은 금액을 입력받아 결제 결과를 반환한다."""
    print(f"\n결제 금액: {total:,}원")

    while True:
        method = input("결제 방법을 선택하세요 (1: 카드, 2: 현금): ").strip()

        if method == "1":
            print("카드 결제가 완료되었습니다.")
            return {
                "method": "카드",
                "total": total,
                "paid": total,
                "change": 0,
            }

        if method == "2":
            while True:
                paid_text = input("받은 현금 금액을 입력하세요: ").strip()

                try:
                    paid = int(paid_text)
                except ValueError:
                    print("숫자로 입력해주세요.")
                    continue

                if paid < total:
                    print(f"{total - paid:,}원이 부족합니다.")
                    continue

                change = paid - total
                print(f"현금 결제가 완료되었습니다. 거스름돈: {change:,}원")

                return {
                    "method": "현금",
                    "total": total,
                    "paid": paid,
                    "change": change,
                }

        print("1 또는 2를 입력해주세요.")
