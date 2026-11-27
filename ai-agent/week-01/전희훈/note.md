# Week 01 · 전희훈

## 💡 인사이트

### Prompt Engineering
- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- 기준과 예시가 정확를 가름

- Specific, Not Abstract
    - 구체적인 스펙, 계획 작성
    - 검증까지 나아가야함

- AI는 순수 함수가 아니기 때문에 eval(이벨, 평가) 필요
- 검증 과정
    - 기대값 설정

- Only Destination, Not Every Stop
    - 원하는 결과의 상태 값만 작성

- Use Few-Shot
    - 작은 개수의 예시

- Why, Not Just What
    - 이유 설명이 더 효과적

- Research First
    - 행동 보다 살펴보고 진행

### Context Engineering
- context window를 다음 단계에 필요한 정보로 채우는 기술

- clear, compact
    - opus 5.5는 96.7% 정도에 compact 동작
    - 25% ~ 45% 에서 compact 하는게 좋음

- message 줄이기
    - 산출물이 큰 업무는 스크립트를 활용하도록 함
    - 훅으로 읽는 양을 줄임
    - subagent 활용

- CLAUDE.md
    - 입력 토큰이 출력의 324배
    - import는 context 비용을 줄여주지 않음
        - Lazy loading이 되도록 최적화 필요
    - CLAUDE.md는 200줄 아래로
    - 같은 실수를 두 번 했을 때 적어라

- 기존 작성된 코드를 참조하는 경우가 매우 많음
    - 안 좋은 패턴을 가져가는 경우가 마이그레이션 도중 멈출 경우 더더욱 심해짐
    - 최대한 모든 코드를 정리 해야함

- Second Brain
    - 두뇌, 제 2의 저장소
    - LLM Wiki

- 필요한 것만 넣는 lazy loading 셋업
    - 토큰이 80% 가까이 줄어듬

- LLM Wiki
    - raw
        - 원본
        - 불변
    - wiki
        - concepts
        - entities
        - sources
        - syntheses

- wiki에는 어떤 자료를 채워야 하는가
    - 슬랙 스레드, 회의 전사본 등 모든 비즈니스 맥락

- Second Brain은 갱신 잘 해야함

- SSOT, DRY 원칙

- qmd 라이브러리 -> md 검색 라이브러리



## ❓ 질문
<!-- 질문은 Discussions Q&A에 올리고 링크만 남겨 주세요 -->
- 

## 🛠 실습
- 링크: https://github.com/citytexi/llm-wiki
- 한 줄 요약: 예전에 해봤던 거여서 막 새롭다는 없는듯
- 막혔던 점 / 배운 점:

### 좋았던 점
1. auto-compact 이거 괜찮은듯 superpowers spec 하네스 이용하니까 야무진듯
2. best practice랑 claude md 최적화 나이스

### 생각 해볼 점
1. 갱신이 꾸준해야한다는데 ingest가 주기마다 돌 경우 이 토큰 감당 가능할까?
2. 이미 진행되고 있는 프로젝트의 경우 nothing에서 시작하는게 아니라 이미 작업된 상태에서 실행해야 하는데 구축 비용을 감당 가능한건가?
3. 서로 다른 프로젝트의 아키텍쳐가 다른 경우 Second Brain을 공유할 경우 매우 큰 문제가 생기지 않을까?


