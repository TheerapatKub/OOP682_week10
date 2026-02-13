from pathlib import Path

from .log_source_factory import create_log_source


def run_ui() -> None:
    print("=== Log Viewer (OCP Challenge) ===")

    default_text = Path(__file__).with_name("sample.log")
    default_csv = Path(__file__).with_name("sample.csv")

    print("ตัวอย่างไฟล์ที่มีให้:")
    print(f"  1) Text log : {default_text}")
    print(f"  2) CSV log  : {default_csv}")
    print()

    path_str = input("กรอก path ของไฟล์ log ที่ต้องการอ่าน (Enter เพื่อใช้ sample.csv): ").strip()
    if not path_str:
        path_str = str(default_csv)

    source = create_log_source(path_str)
    logs = source.read_logs()

    print("\n--- Logs ---")
    for line in logs:
        print(line)


if __name__ == "__main__":
    run_ui()

