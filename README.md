# 📝 Algorithm & Coding Test Study in Python

![GitHub repo size](https://img.shields.io/github/repo-size/MartinusChoi/Algorithm-PlayGround)
![GitHub stars](https://img.shields.io/github/stars/MartinusChoi/Algorithm-PlayGround?style=social)
![GitHub forks](https://img.shields.io/github/forks/MartinusChoi/Algorithm-PlayGround?style=social)

## 📌 소개
이 리포지토리는 **알고리즘 및 코딩 테스트 준비**를 위한 Python 코드 및 학습 자료를 포함하고 있습니다.  
다양한 문제를 해결하고, 최적화된 코드를 작성하며, CS 개념을 복습하는 데 도움을 줄 수 있습니다.

## 📂 폴더 구조
```
📂 Algorithm
 ┣ 📂 Graph               # 그래프 알고리즘 (최단 경로, 최소 신장 트리 등)
 ┣ 📂 BackTracking        # 백트래킹 알고리즘
 ┣ 📂 Sorting             # 정렬 알고리즘
 ┣ 📂 Simulation          # 시뮬레이션 문제 풀이이
 ┣ 📂 Dynamic_Programming # 동적 프로그래밍 (DP)
 ┣ 📂 Greedy              # 그리디 알고리즘
 ┗ 📂 Data_Structure      # 자료구조 (스택, 큐, 힙 등)

📂 Coding_Test
 ┣ 📂 BOJ                 # 백준 온라인 저지 문제 풀이
 ┣ 📂 Programmers         # 프로그래머스 문제 풀이
 ┗ 📂 LeetCode            # 리트코드 문제 풀이
```

## 📜 학습 목표
✅ **알고리즘 및 자료구조 학습**  
✅ **다양한 유형의 문제 풀이 및 최적화 연습**  
✅ **코딩 테스트 준비 및 문제 해결 능력 향상**  
✅ **Python을 활용한 효율적인 문제 해결 기법 익히기**  

## 🔥 학습 자료
- **Online-Judgement**
    - **백준 온라인 저지 (BOJ)**: [https://www.acmicpc.net/](https://www.acmicpc.net/)
    - **프로그래머스 (Programmers)**: [https://programmers.co.kr/](https://programmers.co.kr/)
    - **LeetCode**: [https://leetcode.com/](https://leetcode.com/)
- **학습 자료**
    - **코딩테스트 합격자 되기 (파이썬 편)**

## 🛠 환경 설정
- Python 3.11 이상
- 필수 라이브러리 설치 (필요시)
```bash
pip install -r requirements.txt
```

## 📢 문제 풀이 방식
문제 풀이 코드의 기본 템플릿은 다음과 같습니다.

```python
# 문제 출처 : (예: BOJ 1000번 - A+B)
# 문제 링크 : https://www.acmicpc.net/problem/1000

def solution():
    a, b = map(int, input().split())
    print(a + b)

if __name__ == "__main__":
    solution()
```