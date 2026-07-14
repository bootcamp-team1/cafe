"""카페 키오스크 프로그램 실행 파일."""

from menu import get_menu, show_menu
from order import create_order
from payment import calculate_total, process_payment
from receipt import print_receipt


def main() -> None:
    """키오스크 프로그램을 실행한다."""
    print("카페 키오스크에 오신 것을 환영합니다.")

    menu = get_menu()
    show_menu(menu)

    order = create_order(menu)
    total = calculate_total(order)
    payment_result = process_payment(total)

    print_receipt(order, payment_result)


if __name__ == "__main__":
    main()
