"""주차 추가: <강의>/week-NN/README.md와 멤버별 note.md를 만들고, 강의 README와 루트 README 일정 표에 주차를 넣는다."""
import datetime
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSES = {"langchain": "LangChain", "ai-agent": "AI Agent"}
WEEKDAYS = "월화수목금토일"


def format_date(value):
    if not value:
        return ""
    d = datetime.date.fromisoformat(value)
    return f"{d.year}/{d.month}/{d.day} ({WEEKDAYS[d.weekday()]})"


def split_row(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def join_row(cells):
    return "| " + " | ".join(cells) + " |"


def week_number(value):
    return int(value) if value.isdigit() else float("inf")


def upsert_row(path, heading, header, key, fill):
    """heading 아래 표에서 key({열: 값})가 모두 같은 줄을 찾아 fill로 채운다. 없으면 붙이고, 표가 없으면 만든다.
    줄은 강의가 처음 나온 순서, 그다음 주차 순으로 정렬한다."""
    lines = path.read_text().split("\n")
    start = lines.index(heading)
    end = next((k for k in range(start + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
    table = [k for k in range(start + 1, end) if lines[k].startswith("|")]
    if table:
        i, j = table[0], table[-1] + 1
    else:
        lines[start + 1:end] = ["", join_row(header), join_row(["---"] * len(header)), ""]
        i, j = start + 2, start + 4

    header = split_row(lines[i])
    rows = [split_row(line) for line in lines[i + 2:j]]
    cols = {name: header.index(name) for name in key}
    row = next((r for r in rows if all(r[c] == key[name] for name, c in cols.items())), None)
    if row is None:
        row = [key.get(name, "") for name in header]
        rows.append(row)
    fill(header, row)

    w = header.index("주차")
    if "강의" in header:
        c = header.index("강의")
        first = {}
        for r in rows:
            first.setdefault(r[c], len(first))
        rows.sort(key=lambda r: (first[r[c]], week_number(r[w])))
    else:
        rows.sort(key=lambda r: week_number(r[w]))
    lines[i + 2:j] = [join_row(r) for r in rows]
    path.write_text("\n".join(lines))


def write_week_readme(course, week, scope, date):
    path = ROOT / course / f"week-{week:02d}" / "README.md"
    date_suffix = f" · {date}" if date else ""
    if path.exists():
        # 모임 후 정리 내용은 두고 제목과 범위만 바꾼다
        text = path.read_text()
        if date:
            text = re.sub(r"^# Week .*$", f"# Week {week:02d}{date_suffix}", text, count=1, flags=re.M)
        text = re.sub(r"^\*\*범위\*\*: .*$", lambda _: f"**범위**: {scope}", text, count=1, flags=re.M)
    else:
        text = (ROOT / "templates" / "week.md").read_text()
        text = text.replace("{{week}}", f"{week:02d}").replace("{{date}}", date_suffix).replace("{{scope}}", scope)
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def members():
    """루트 README 멤버 표의 이름 열"""
    lines = (ROOT / "README.md").read_text().split("\n")
    start = lines.index("## 멤버")
    rows = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        if line.startswith("|"):
            rows.append(split_row(line)[0])
    return [name for name in rows[2:] if name]


def write_notes(course, week, names):
    template = (ROOT / "templates" / "note.md").read_text()
    for name in names:
        path = ROOT / course / f"week-{week:02d}" / name / "note.md"
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(template.replace("{{week}}", f"{week:02d}").replace("{{name}}", name))


def main():
    course = os.environ["COURSE"]
    week = int(os.environ["WEEK"])
    scope = os.environ["SCOPE"].strip()
    date = format_date(os.environ.get("DATE", "").strip())
    if course not in COURSES:
        raise SystemExit(f"알 수 없는 강의: {course}")

    write_week_readme(course, week, scope, date)
    # 지난 주차를 다시 실행할 때는 노트를 만들지 않는다 (나중에 합류한 멤버 노트 방지)
    raw_date = os.environ.get("DATE", "").strip()
    if not raw_date or datetime.date.fromisoformat(raw_date) >= datetime.date.today():
        write_notes(course, week, members())

    def fill(header, row):
        if date:
            row[header.index("날짜")] = date
        row[header.index("범위")] = scope

    upsert_row(ROOT / course / "README.md", "## 주차별 범위", ["주차", "날짜", "범위"], {"주차": str(week)}, fill)
    # 강의를 차례로 듣고 주차 번호도 강의별로 따로 매기므로 일정 표는 강의 + 주차로 줄을 찾는다
    upsert_row(ROOT / "README.md", "## 일정", ["날짜", "강의", "주차", "범위"],
               {"강의": COURSES[course], "주차": str(week)}, fill)


if __name__ == "__main__":
    main()
