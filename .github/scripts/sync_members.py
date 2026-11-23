"""멤버 표가 바뀌면 모임 날짜가 오늘 이후인 주차에만 빠진 멤버의 note.md를 만든다."""
import datetime
import re

from add_week import COURSES, ROOT, members, write_notes


def meeting_date(week_dir):
    """주차 README 제목의 YYYY/M/D를 읽는다."""
    title = (week_dir / "README.md").read_text().split("\n", 1)[0]
    match = re.search(r"· (\d{4})/(\d+)/(\d+)", title)
    if not match:
        return None
    return datetime.date(*map(int, match.groups()))


def main():
    today = datetime.date.today()
    names = members()
    for course in COURSES:
        for week_dir in sorted((ROOT / course).glob("week-*")):
            date = meeting_date(week_dir)
            if date and date >= today:
                write_notes(course, int(week_dir.name.split("-")[1]), names)


if __name__ == "__main__":
    main()
