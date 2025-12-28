import pandas as pd

# Giả định df đã được nạp và làm sạch (điền "Unknown" cho director và country)
# df = pd.read_csv('netflix_titles.csv')

# --- 1. Đếm tổng số Movie và TV Show ---
type_counts = df['type'].value_counts()
total_movies = type_counts.get('Movie', 0)
total_tv_shows = type_counts.get('TV Show', 0)

# --- 2. Tìm Top 10 quốc gia sản xuất nhiều phim nhất ---
# Tách chuỗi quốc gia và đếm từng nước riêng biệt
top_10_countries = (
    df['country']
    .str.split(', ')
    .explode()
    .value_counts()
    .head(10)
)

# --- 3. Tìm đạo diễn ra mắt nhiều phim nhất ---
# Lọc bỏ "Unknown", tách tên và tìm người có số lượng lớn nhất
directors_count = (
    df[df['director'] != 'Unknown']['director']
    .str.split(', ')
    .explode()
    .value_counts()
)

top_director_name = directors_count.idxmax()
top_director_count = directors_count.max()

# --- XUẤT KẾT QUẢ ---
print(f"Tổng số Movie: {total_movies}")
print(f"Tổng số TV Show: {total_tv_shows}")
print("\nTop 10 quốc gia sản xuất nhiều nhất:")
print(top_10_countries)
print(f"\nĐạo diễn có nhiều phim nhất: {top_director_name} ({top_director_count} tác phẩm)")
