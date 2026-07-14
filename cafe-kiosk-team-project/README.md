# ☕ Cafe Kiosk Team Project

GitHub Organization 기반 협업 실습을 위한 Python 콘솔 카페 키오스크 프로젝트입니다.

## 1. 프로젝트 목표

사용자가 콘솔에서 메뉴를 확인하고, 음료와 수량을 선택한 뒤 결제 금액과 영수증을 확인할 수 있는 간단한 키오스크를 구현합니다.

이 프로젝트에서는 다음 GitHub 협업 과정을 연습합니다.

- Organization 및 Repository 생성
- 역할 분담
- 기능별 Branch 생성
- Commit 및 Push
- Pull Request 생성
- 코드 리뷰
- main Branch에 Merge

---

## 2. 주요 기능

1. 메뉴 목록 출력
2. 음료 및 수량 선택
3. 장바구니 관리
4. 총금액 계산
5. 카드 및 현금 결제
6. 영수증 출력

---

## 3. 프로젝트 구조

```text
cafe-kiosk-team-project/
├── .github/
│   └── pull_request_template.md
├── .gitignore
├── CONTRIBUTING.md
├── README.md
├── main.py
├── menu.py
├── order.py
├── payment.py
└── receipt.py
```

---

## 4. 역할 분담 예시

| 담당자 | 역할 | 작업 파일 | Branch |
|---|---|---|---|
| 팀원 1 | 메뉴 관리 | `menu.py` | `feature/menu` |
| 팀원 2 | 주문 및 장바구니 | `order.py` | `feature/order` |
| 팀원 3 | 금액 계산 및 결제 | `payment.py` | `feature/payment` |
| 팀원 4 | 영수증 및 전체 통합 | `receipt.py`, `main.py` | `feature/receipt` |

> `main.py`는 충돌을 줄이기 위해 통합 담당자 한 명만 수정하는 것을 권장합니다.

---

## 5. 기능별 함수 규칙

팀원들이 각자 작업한 코드를 쉽게 합칠 수 있도록 함수 이름과 반환값을 미리 약속합니다.

### `menu.py`

```python
def get_menu() -> dict:
    """메뉴 정보를 딕셔너리로 반환한다."""

def show_menu(menu: dict) -> None:
    """메뉴를 화면에 출력한다."""
```

### `order.py`

```python
def create_order(menu: dict) -> list:
    """사용자의 주문을 받아 장바구니 리스트를 반환한다."""
```

### `payment.py`

```python
def calculate_total(order: list) -> int:
    """주문 목록의 총금액을 계산한다."""

def process_payment(total: int) -> dict:
    """결제를 처리하고 결제 결과를 반환한다."""
```

### `receipt.py`

```python
def print_receipt(order: list, payment_result: dict) -> None:
    """주문 정보와 결제 결과를 영수증 형태로 출력한다."""
```

---

## 6. 실행 방법

Python 3.10 이상을 권장합니다.

```bash
python main.py
```

Windows에서는 다음 명령어도 사용할 수 있습니다.

```powershell
py main.py
```

---

## 7. Branch 생성 및 작업 방법

저장소를 Clone합니다.

```bash
git clone https://github.com/조직이름/저장소이름.git
cd 저장소이름
```

자신의 기능 Branch를 생성합니다.

```bash
git switch -c feature/menu
```

작업한 파일을 Commit합니다.

```bash
git add menu.py
git commit -m "feat: 메뉴 출력 기능 구현"
```

원격 저장소에 Push합니다.

```bash
git push -u origin feature/menu
```

GitHub에서 다음 기준으로 Pull Request를 생성합니다.

```text
base: main
compare: feature/menu
```

---

## 8. Commit 메시지 규칙

| 구분 | 설명 | 예시 |
|---|---|---|
| `feat` | 새로운 기능 | `feat: 장바구니 기능 구현` |
| `fix` | 오류 수정 | `fix: 잘못된 메뉴 번호 입력 오류 수정` |
| `docs` | 문서 수정 | `docs: README 역할 분담 추가` |
| `refactor` | 코드 구조 개선 | `refactor: 결제 함수 분리` |
| `test` | 테스트 코드 | `test: 총금액 계산 테스트 추가` |

---

## 9. Merge 권장 순서

함수 의존성을 고려해 다음 순서로 Merge하는 것을 권장합니다.

```text
feature/menu
→ feature/order
→ feature/payment
→ feature/receipt
→ main 최종 실행 확인
```

각 Pull Request를 Merge하기 전에 팀원 한 명 이상이 코드를 확인합니다.

---

## 10. 추가 개발 아이디어

- 메뉴 카테고리 분류
- 주문 수량 변경 및 삭제
- 품절 메뉴 표시
- 쿠폰 할인
- 카드 및 현금 결제 선택
- 주문번호 생성
- 영수증에 주문 시간 출력
- 일일 매출 저장
- Tkinter를 활용한 GUI 버전 제작
