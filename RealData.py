import os
import wave
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "output.wav"

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # 관리자 권한이 없으면 관리자 모드로 실행
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1
    )
    sys.exit()


# 경로 수정
DRIVE_FOLDER = r"C:\Users\ottokae ottokae\Google Drive\MyDrive\First\Speech"

# 폴더 생성
try:
    os.makedirs(DRIVE_FOLDER, exist_ok=True)
    print(f"폴더 생성 성공: {DRIVE_FOLDER}")
except PermissionError as e:
    print(f"권한 오류: {e}")
    exit(1)

def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* 녹음 시작 (중지하려면 Ctrl+C)")

    try:
        while True:
            print(f"* {RECORD_SECONDS}초간 녹음 중...")
            frames = []

            for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            # 파일 저장 경로
            filepath = os.path.join(DRIVE_FOLDER, WAVE_OUTPUT_FILENAME)

            # 녹음 파일 저장
            with wave.open(filepath, 'wb') as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))

            print(f"* 파일 저장 완료: {filepath}")
    except KeyboardInterrupt:
        print("\n* 녹음 중지")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

record_audio()
