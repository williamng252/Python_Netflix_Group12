import pandas as pd


class DataProcessor:
    """
    Class xử lý:
    - Nạp dữ liệu
    - Làm sạch dữ liệu (Data Loading & Cleaning)
    """

    def __init__(self, file_path):
        """
        __init__:
        - Nhận đường dẫn file CSV
        """
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Đọc file netflix_titles.csv
        """
        self.df = pd.read_csv(self.file_path)
        return self.df

    def handle_missing_values(self):
        """
        Xử lý các ô trống:
        - Điền 'Unknown' cho các giá trị bị thiếu
        """
        self.df = self.df.fillna("Unknown")
        return self.df

    def convert_date_format(self):
        """
        Chuyển cột date_added từ:
        'September 25, 2021'
        sang:
        '2021-09-25'
        """
        self.df["date_added"] = pd.to_datetime(
            self.df["date_added"],
            errors="coerce"
        ).dt.strftime("%Y-%m-%d")

        # Nếu còn giá trị NaN sau khi convert
        self.df["date_added"] = self.df["date_added"].fillna("Unknown")
        return self.df

    def process(self):
        """
        Pipeline tổng:
        - Load data
        - Clean missing values
        - Convert date format
        """
        self.load_data()
        self.handle_missing_values()
        self.convert_date_format()
        return self.df
