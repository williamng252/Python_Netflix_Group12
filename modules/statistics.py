import pandas as pd

class Statistics:
    def __init__(self, df):
      
        self.df = df

    def count_total_types(self):
        """1. Đếm tổng số Movie và TV Show"""
        type_counts = self.df['type'].value_counts()
        return type_counts

    def get_top_countries(self):
        """2. Tìm Top 10 quốc gia"""
        return (
            self.df['country']
            .str.split(', ')
            .explode()
            .value_counts()
            .head(10)
        )

    def get_top_director(self):
        """3. Tìm đạo diễn nhiều phim nhất"""
        # Lọc bỏ Unknown
        valid_directors = self.df[self.df['director'] != 'Unknown']
        
        directors_count = (
            valid_directors['director']
            .str.split(', ')
            .explode()
            .value_counts()
        )
        
        # Trả về tên và số lượng
        return directors_count.idxmax(), directors_count.max()