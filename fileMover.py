import os
import shutil

# get user input | 유저 입력 (GUI)
def get_user_input():
    print("처리할 폴더의 주소를 입력:")
    origin_path = input()

    print("목적지 폴더의 주소를 입력:")
    target_path = input()

    print("첫번째 문자를 입력:")
    start_keyword = input()

    print("마지막 문자를 입력:")
    end_keyword = input()

    return origin_path, target_path, start_keyword, end_keyword


# set class FileOrganizer --> will be soon refactor 2 step
# FileOrganizer 클래스 설정 --> 코드 리팩터링 예정
class FileOrganizer:
    # init class
    def __init__(self, origin_path, target_path, start_keyword, end_keyword):
        self.origin_path = origin_path
        self.target_path = target_path
        self.start_keyword = start_keyword
        self.end_keyword = end_keyword
        self.dst_map = self._mapping_dst_path()

    # mapped target path (private) | 목표 주소 맵핑
    def _mapping_dst_path(self):
        dir_in_target = os.listdir(self.target_path)
        return {folder.upper(): folder for folder in dir_in_target}

    # extract target name (private) | 목표 이름 추출
    def _extract_target_name(self, file_name):
        first_index = file_name.find(self.start_keyword)
        first_index +=1
        end_index = file_name.find(self.end_keyword)
        return file_name[first_index:end_index].upper()

    # run automation code | 자동 코드 실행
    def run(self):
        files_to_move = os.listdir(self.origin_path)
        for file_name in files_to_move:
            target_name = self._extract_target_name(file_name)
            if target_name in self.dst_map:
                dst_dir = self.dst_map[target_name]
                print(target_name + "폴더 발견")
                src_path = os.path.join(self.origin_path, file_name)
                dst_path = os.path.join(self.target_path, dst_dir, file_name)
                print("소스 파일 " + src_path + " 도착 폴더 " + dst_path)

                try:
                    shutil.move(src_path, dst_path)
                    print(f'{src_path}에서 {dst_path}로 이동하였습니다.')
                except shutil.Error as error:
                    print(f"파일이 중복되었어요. : {error}")
                    continue

# main code | 메인 코드
if __name__ == "__main__":
    origin_path, target_path, start_keyword, end_keyword = get_user_input()
    organizer = FileOrganizer(origin_path, target_path, start_keyword, end_keyword)
    organizer.run()
