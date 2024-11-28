import time
from pydub import AudioSegment
from pydub.playback import play

# 음성 파일 경로
recorded_audio_path = "/home/pi/audio_files/recorded_audio.wav"
patrolling_audio_path = "/home/pi/audio_files/patrolling.wav"

# 음성 파일 로드
recorded_audio = AudioSegment.from_file(recorded_audio_path)
patrolling_audio = AudioSegment.from_file(patrolling_audio_path)

def play_audio(audio):
    """음성 파일 재생 함수"""
    play(audio)

try:
    while True:
        print("녹음된 음성 파일 재생 중...")
        play_audio(recorded_audio)  # 녹음된 음성 파일 재생

        print("3초 대기 후 '순찰중입니다' 음성 파일 재생 중...")
        time.sleep(3)  # 3초 대기
        play_audio(patrolling_audio)  # "순찰중입니다" 음성 파일 재생

        print("10초 대기 중...")
        time.sleep(10)  # 10초 대기
except KeyboardInterrupt:
    print("프로그램 종료")

