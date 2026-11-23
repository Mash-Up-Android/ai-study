# ai-study

인프런 강의 2개를 함께 듣고, 매주 질문·인사이트·실습을 공유하는 스터디입니다.

| 강의 | 분량 | 폴더 |
| --- | --- | --- |
| [LangChain, LangGraph, LangSmith 기초부터 총정리](https://www.inflearn.com/course/a-complete-overview) | 22강 · 8시간 46분 | [`langchain/`](langchain) |
| [글로벌 상위 1% 빅테크 기업 엔지니어들의 AI Agent 활용법](https://www.inflearn.com/course/how-engineers-at-the) | 38강 · 2시간 43분 (섹션 6~ 12월 공개) | [`ai-agent/`](ai-agent) |

## 진행 방식

1. 그 주 범위의 강의를 듣는다. (범위는 각 강의 폴더의 README 참고)
2. `<강의>/week-NN/<이름>/note.md`에 **인사이트**를 적는다. (주차 추가 시 자동 생성)
3. 질문은 [Discussions Q&A](https://github.com/Mash-Up-Android/ai-study/discussions/categories/q-a)에 올리고, 노트에는 링크만 남긴다.
4. 실습 코드는 `<강의>/practice/<이름>/`에 올린다.
5. **모임 당일까지 PR**을 올려 `main`에 머지한다.
6. 모임에서 머지된 각자의 학습자료와 Discussions 질문을 같이 보며 이야기하고, 진행자가 `<강의>/week-NN/README.md`에 결론을 정리한다.

## 질문 (Discussions)

- [Q&A 카테고리](https://github.com/Mash-Up-Android/ai-study/discussions/categories/q-a)에서 **New discussion**을 누르면 강의·주차·질문을 입력하는 폼이 나온다.
- 제목은 `[AI Agent W01] 질문 요약` 형식으로 쓴다.
- 답을 찾으면 도움이 된 댓글을 **Mark as answer**로 채택한다. 모임에서 결론이 나면 진행자가 채택한다.
- 채택되지 않은 질문은 다음 모임에서 다시 본다.

## 실습

실습 환경(언어, 패키지 관리, LLM API)은 각자 자유롭게 정한다.

## 폴더 구조

```
ai-study/
├── templates/
│   ├── note.md              # 개인 노트 템플릿
│   └── week.md              # 주차 README 템플릿 (주차 추가 시 사용)
├── langchain/
│   ├── README.md            # 강의 정보 + 주차별 범위
│   ├── week-01/
│   │   ├── README.md        # 이번 주 범위 + 모임 후 정리
│   │   └── <이름>/note.md   # 개인 노트
│   └── practice/<이름>/     # 실습 코드 (주차를 넘어 이어서 작업)
└── ai-agent/                # langchain/과 같은 구조
```

## 일정

| 날짜 | 강의 | 주차 | 범위 |
| --- | --- | --- | --- |
| 2026/11/29 (일) | AI Agent | 1 | 섹션 1 ~ 4 (오리엔테이션 ~ Second Brain) |

## 주차 추가

GitHub **Actions → 주차 추가 → Run workflow**에서 강의, 주차, 범위, 모임 날짜를 입력하면 아래가 자동으로 `main`에 커밋됩니다.

- `<강의>/week-NN/README.md` 생성 (이미 있으면 제목·범위만 수정)
- 아래 멤버 표의 이름마다 `<강의>/week-NN/<이름>/note.md` 생성 (이미 있으면 그대로 둠, 모임 날짜가 지난 주차는 생성하지 않음)
- `<강의>/README.md`의 주차별 범위 표와 위 일정 표에 해당 주차 추가

## 멤버 추가

아래 멤버 표에 한 줄 추가해 `main`에 머지하면, **모임 날짜가 오늘 이후인 주차**에만 새 멤버의 `note.md`가 생성됩니다. 지난 주차에는 생기지 않습니다.

## 규칙

- 브랜치: `week-NN/<이름>` → `main`으로 PR
- 각자 자기 파일·폴더만 수정해서 충돌을 피한다.
- **API 키는 `.env`에만 두고 절대 커밋하지 않는다.** (`.gitignore`에 포함됨)

## 멤버

| 이름  | GitHub                                         |
| --- | ---------------------------------------------- |
| 이재성 | [@JaesungLeee](https://github.com/JaesungLeee) |
| 전희훈 | [@citytexi](https://github.com/citytexi)       |
