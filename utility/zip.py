import os
import zipfile

def create_folder(path):
    """
    주어진 경로에 폴더를 생성합니다.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def check_zip_file(zip_file_path):
    """
    주어진 ZIP 파일의 유효성을 검사합니다.
    """
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.namelist()  # 유효성 검사를 위해 ZIP 파일 내용 리스트를 가져옵니다.
        return True
    except zipfile.BadZipFile:
        print(f"잘못된 ZIP 파일: {zip_file_path}")
        return False

def extract_and_move_files(zip_file_path, final_path):
    """
    주어진 ZIP 파일을 압축 해제하여 지정된 경로로 이동합니다.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(final_path)
    print(f"{zip_file_path} 압축 해제 완료 및 파일 이동 완료!")

def setup_folders_and_extract_files(folders, zip_files):
    """
    폴더를 생성하고 ZIP 파일을 압축 해제합니다.
    """
    # 폴더 생성 및 초기 내용 출력
    for folder in folders:
        create_folder(folder)

    # 파일 경로 및 존재 여부 확인 후 압축 해제
    for zip_file, final_path in zip(zip_files, folders):
        print(f"Checking file: {zip_file}")
        if os.path.exists(zip_file):
            if check_zip_file(zip_file):
                extract_and_move_files(zip_file, final_path)

    # 생성된 폴더의 내용 출력
    for folder in folders:
        print(f"폴더 '{folder}'의 최종 내용:")
        print(os.listdir(folder)[:20])

folders = ['./sign_train', './sign_test']
zip_files = ['./sign_train.zip', './sign_test.zip']

setup_folders_and_extract_files(folders, zip_files)