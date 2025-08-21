import os
import subprocess
import openpyxl
import re

def clean_for_excel(text):
    """엑셀 기록을 위해 제어 문자를 제거하는 함수"""
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)

def read_file_with_fallback_encodings(file_path):
    """다양한 인코딩을 시도하여 파일을 읽는 함수"""
    encodings_to_try = ['utf-8-sig', 'utf-8', 'cp949', 'utf-16']
    for enc in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return f.read()
        except (UnicodeDecodeError, UnicodeError):
            continue
    # 모든 인코딩 실패 시, 바이트로 읽고 강제로 디코딩 (최후의 수단)
    with open(file_path, 'rb') as f:
        return f.read().decode('utf-8', errors='ignore')

def grade_problem(folder_path, program_path, excel_path="result.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "채점결과"
    ws.append(["테스트케이스", "정답", "내 출력", "결과"])

    for i in range(1, 13):
        in_file = os.path.join(folder_path, f"{i:02}.1.in")
        out_file = os.path.join(folder_path, f"{i:02}.out")

        if not os.path.exists(in_file) or not os.path.exists(out_file):
            print(f"[{i:02}] 케이스 파일 없음")
            continue

        # --- 핵심 수정 부분 1: 견고한 파일 읽기 ---
        input_data = read_file_with_fallback_encodings(in_file)
        expected_output = read_file_with_fallback_encodings(out_file)
        # ----------------------------------------

        my_output = "" # my_output 초기화
        try:
            # --- 핵심 수정 부분 2: universal_newlines 사용 ---
            # universal_newlines=True는 인코딩 오류를 더 잘 처리하고,
            # 다양한 줄바꿈 문자를 파이썬의 '\n'으로 통일해줍니다.
            result = subprocess.run(
                ["python", program_path],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=5,
                errors='ignore' # 디코딩 에러를 무시하고 진행
            )
            my_output = result.stdout.strip()
            if result.stderr:
                my_output += f"\n[에러 발생]: {result.stderr.strip()}"
        except subprocess.TimeoutExpired:
            my_output = "시간 초과"
        except Exception as e:
            my_output = f"실행 에러 발생: {e}"

        # 비교를 위해 양쪽의 공백, 줄바꿈, 널문자 등을 모두 정리
        processed_expected = re.sub(r'\s+', ' ', expected_output.replace('\x00', '')).strip()
        processed_my = re.sub(r'\s+', ' ', my_output).strip()

        verdict = "맞음" if processed_my == processed_expected else "틀림"
        
        ws.append([
            f"{i:02}",
            clean_for_excel(expected_output),
            clean_for_excel(my_output),
            verdict
        ])
        
        # 콘솔 출력은 원본으로 하여 디버깅에 용이하게 함
        print(f"[{i:02}] 정답: {expected_output!r}, 내출력: {my_output!r}, 결과: {verdict}")

    wb.save(excel_path)
    print(f"채점 완료! 결과는 {excel_path} 에 저장됨")

# --- 사용자 환경에 맞게 경로 수정 ---
folder = "C:\\Users\\DB실\\Downloads\\제14회 전국대회 비즈니스프로그래밍 문제 및 정답\\답안(1년후배포)\\답안(1년후배포)\\문제8"
program_file = "제14회 전국대회 비즈니스프로그래밍 문제\\8.py"

grade_problem(folder, program_file)