import streamlit as st
import pandas as pd
from modules.processing import DataProcessor
from modules.statistics import Statistics
from modules.visualize import Visualizer

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="Netflix Dashboard", page_icon="🎬", layout="wide")

# Tiêu đề đẹp
st.title("🎬 PHÂN TÍCH DỮ LIỆU NETFLIX (NHÓM 12)")
st.write("Chào mừng bạn đến với Dashboard phân tích phim!")

# --- PHẦN NẠP DỮ LIỆU ---
@st.cache_data # Dòng này giúp nạp 1 lần cho nhanh, ko nạp lại khi bấm nút
def load_data():
    processor = DataProcessor('data/netflix_titles.csv')
    return processor.process()

# Gọi hàm nạp
try:
    df = load_data()
    st.success(f"✅ Đã nạp thành công {len(df)} dòng dữ liệu!")
except Exception as e:
    st.error(f"❌ Lỗi nạp dữ liệu: {e}")
    st.stop() # Dừng web nếu lỗi

# Khởi tạo các bộ máy
stats = Statistics(df)
viz = Visualizer(df)

# --- THANH MENU BÊN TRÁI ---
st.sidebar.header("🔧 Chức năng")
menu = st.sidebar.radio(
    "Chọn chức năng:",
    ("🏠 Tổng quan", "📊 Thống kê chi tiết", "📈 Biểu đồ trực quan", "🎲 Gợi ý phim")
)

# --- NỘI DUNG CHÍNH (Thay đổi theo nút bấm) ---

if menu == "🏠 Tổng quan":
    st.subheader("Dữ liệu thô (5 dòng đầu)")
    st.dataframe(df.head()) # Hiện bảng đẹp như Excel
    
    # Hiện mấy cái số to to cho đẹp
    col1, col2 = st.columns(2)
    type_counts = stats.count_total_types()
    col1.metric("Tổng số Phim Lẻ", type_counts.get('Movie', 0))
    col2.metric("Tổng số TV Show", type_counts.get('TV Show', 0))

elif menu == "📊 Thống kê chi tiết":
    st.subheader("🏆 Top 10 Quốc gia sản xuất")
    top_country = stats.get_top_countries()
    st.table(top_country) # Hiện bảng tĩnh

    st.subheader("🎬 Đạo diễn xuất sắc nhất")
    name, count = stats.get_top_director()
    st.info(f"Đạo diễn **{name}** với tổng cộng **{count}** tác phẩm!")

elif menu == "📈 Biểu đồ trực quan":
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Tỉ lệ Phim/Show")
        # Gọi hàm vẽ và đưa hình lên web
        fig1 = viz.draw_type_distribution()
        st.pyplot(fig1)
        
    with col2:
        st.write("### Top Quốc Gia")
        fig2 = viz.draw_top_countries()
        st.pyplot(fig2)

elif menu == "🎲 Gợi ý phim":
    if st.button("🎲 Bấm để chọn ngẫu nhiên 5 phim"):
        sample = df[['title', 'type', 'release_year', 'description']].sample(5)
        for i, row in sample.iterrows():
            with st.expander(f"Phim: {row['title']} ({row['release_year']})"):
                st.write(f"**Thể loại:** {row['type']}")
                st.write(f"**Nội dung:** {row['description']}")

# Footer
st.markdown("---")
st.caption("Code bởi Nhóm 12 - Môn Python")