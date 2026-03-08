# 조울증 기분추적기 v1.0 - 44세 1인 2역 활동지원사+개발자
# Phthon 3.14.3 | 정보처리기능사 인증

moods = {"분노":3, "초조":5, "과대자아":7, "충동":2}
total = sum(moods.values() )
gaf = max(100 - total * 2, 31)

print(f" 7pm GAF 점수: {gaf}점")
print("4알 복용 → 천사 모드 활성화")
print("GitHub 포트폴리오: mood-tracker-v1")