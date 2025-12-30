import sys
import pandas as pd
from modules.processing import DataProcessor
from modules.statistics import Statistics


def print_menu():
    print("\n" + "="*40)
    print("CHƯƠNG TRÌNH PHÂN TÍCH NETFLIX (NHÓM 12)")
    print("="*40)
    print("1. Xem tổng quan số lượng phim (Movie vs TV Show)")
    print("2. Xem Top 10 Quốc gia sản xuất phim")
    print("3. Xem Đạo diễn ra mắt nhiều phim nhất")
    print("4. Gợi ý phim ngẫu nhiên (Bonus)")
    print("0. Thoát chương trình")
    print("="*40)

def main():
    # --- KHỞI TẠO VÀ NẠP DỮ LIỆU ---
    print("⏳ Đang nạp và xử lý dữ liệu, vui lòng chờ...")
    
 
    file_path = 'data/netflix_titles.csv'
    
    try:
        # Gọi Class xử lý dữ liệu
        processor = DataProcessor(file_path)
        df = processor.process() # Nhận về DataFrame sạch
        print(f"Đã nạp thành công {len(df)} dòng dữ liệu!")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại '{file_path}'")
        return
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return

    # --- KHỞI TẠO BỘ MÁY THỐNG KÊ ---
    # Truyền dữ liệu sạch (df) vào cho Class Statistics
    stats = Statistics(df)

    # --- CHẠY MENU ĐIỀU KHIỂN ---
    while True:
        print_menu()
        try:
            choice = input("Nhập lựa chọn của bạn (0-4): ")

            if choice == '1':
                print("\nTHỐNG KÊ SỐ LƯỢNG PHIM:")
                result = stats.count_total_types()
                print(result)
            
            elif choice == '2':
                print("\nTOP 10 QUỐC GIA SẢN XUẤT:")
                result = stats.get_top_countries()
                print(result)

            elif choice == '3':
                name, count = stats.get_top_director()
                print(f"\n``ĐẠO DIỄN TIÊU BIỂU NHẤT:")
                print(f"- Tên: {name}")
                print(f"- Số lượng tác phẩm: {count}")

            elif choice == '4':
                # Tính năng Bonus: Lấy ngẫu nhiên 5 phim để xem
                print("\nGỢI Ý 5 PHIM NGẪU NHIÊN CHO BẠN:")
                sample = df[['title', 'type', 'release_year']].sample(5)
                print(sample.to_string(index=False))

            elif choice == '0':
                print("\nTạm biệt! Hẹn gặp lại.")
                sys.exit()
            
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

        except Exception as e:
            print(f"Có lỗi xảy ra khi chạy chức năng: {e}")
            input("Nhấn Enter để quay lại menu...")

# Điểm khởi chạy chương trình
if __name__ == "__main__":
    main()