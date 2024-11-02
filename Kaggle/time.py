from datetime import datetime

# 현재 시간 얻기
now = datetime.now()

# 기본 포맷으로 출력 (예시: 2024-08-07 05:40:28)
basic_format = now.strftime('%Y-%m-%d %H:%M:%S')
print(f"기본 포맷: {basic_format}")

# 한글 포맷으로 출력 (예시: 2024년 08월 07일 05시 40분 28초)
korean_format = now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
print(f"한글 포맷: {korean_format}")

# 날짜만 출력 (예시: 2024/08/07)
date_only_format = now.strftime('%Y/%m/%d')
print(f"날짜만: {date_only_format}")

# 12시간제 시간만 출력 (예시: 05:40 AM)
time_12h_format = now.strftime('%I:%M %p')
print(f"12시간제 시간만: {time_12h_format}")

# 요일과 월 이름 포함 포맷 (예시: Wednesday, 07 August 2024)
weekday_month_format = now.strftime('%A, %d %B %Y')
print(f"요일과 월 이름 포함 포맷: {weekday_month_format}")

# ISO 8601 표준 포맷 (예시: 2024-08-07T05:40:28)
iso_format_basic = now.strftime('%Y-%m-%dT%H:%M:%S')
print(f"ISO 8601 표준 포맷 (기본): {iso_format_basic}")

# ISO 8601 표준 포맷 (예시: 2024-08-07T05:40:28+0900)
# 시간대 포함
iso_format_with_timezone = now.strftime('%Y-%m-%dT%H:%M:%S%z')
print(f"ISO 8601 표준 포맷 (시간대 포함): {iso_format_with_timezone}")