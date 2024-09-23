class missing_value():
    def __init__(self,df):
        self.df=df
    def total_missing_value(self):
        for column in df.columns:
            total_missing_value=total_missing_value.append([self.df[column].isna().sum()])
    