# 협업 규칙

## 1. 작업 전

항상 `main` Branch를 최신 상태로 갱신합니다.

```bash
git switch main
git pull origin main
```

그다음 자신의 기능 Branch를 생성합니다.

```bash
git switch -c feature/기능이름
```

## 2. 작업 파일

본인이 담당한 파일을 중심으로 수정합니다.

다른 팀원의 파일을 수정해야 한다면 먼저 팀원과 상의합니다.

## 3. Commit

한 Commit에는 하나의 목적만 담습니다.

```bash
git add 작업파일.py
git commit -m "feat: 구현한 기능 설명"
```

## 4. Push 및 Pull Request

```bash
git push -u origin feature/기능이름
```

Pull Request에는 다음 내용을 작성합니다.

- 구현한 기능
- 수정한 파일
- 실행 및 테스트 결과
- 리뷰어가 확인할 부분

## 5. Merge 후

Merge가 끝나면 로컬 `main`을 갱신합니다.

```bash
git switch main
git pull origin main
```
