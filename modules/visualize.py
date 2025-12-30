import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, df):
        self.df = df

    def draw_type_distribution(self):
        """Vẽ biểu đồ tròn (Pie Chart)"""
        # Tạo khung hình
        fig = plt.figure(figsize=(8, 6))
        
        type_counts = self.df['type'].value_counts()
        plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', 
                startangle=140, colors=['#ff9999','#66b3ff'])
        plt.title('Tỉ lệ giữa Phim lẻ và TV Show')
        
        # Trả về cái hình để Web nó vẽ
        return fig

    def draw_top_countries(self):
        """Vẽ biểu đồ cột (Bar Chart)"""
        fig = plt.figure(figsize=(10, 6))
        
        top_countries = (
            self.df['country']
            .str.split(', ')
            .explode()
            .value_counts()
            .head(10)
        )
        
        sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
        plt.title('Top 10 Quốc gia sản xuất nhiều phim nhất')
        plt.xlabel('Số lượng phim')
        
        return fig