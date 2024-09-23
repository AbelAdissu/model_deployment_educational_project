from sklearn.preprocessing import LabelEncoder, OneHotEncoder, label_binarize
import category_encoders as ce
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x=np.array(['abel','yared','motherfers'])
data = {'Fruit': ['Apple', 'Banana', 'Orange', 'Banana', 'Apple'],
        'Price':[220,300,400,300,220]}
df = pd.DataFrame(data)
df.Fruit.value_counts().plot(kind='bar')
plt.xlabel("fruit")
plt.ylabel("count")
plt.show()
LabelEncoder=LabelEncoder()
df=LabelEncoder.fit_transform(df)
correlation=df.corr()
sns.heatmap(correlation,cbar=True)
plt.show()
LabelEncoder=LabelEncoder()
#OneHotEncoder=OneHotEncoder()
binary_encoder=ce.BinaryEncoder()

x_transformed=LabelEncoder.fit_transform(x)
#x_transformed0=OneHotEncoder.fit_transform(x).toarray()
df_bianry=binary_encoder.fit_transform(df)

print(x)
print(x_transformed)
#print(x_transformed0)
print(df.head())
print(df_bianry.head())

x_reversed=LabelEncoder.inverse_transform(x_transformed)
#x_reversed0=OneHotEncoder.inverse_transform(x_transformed0)

print(x_reversed)
#print(x_reversed0.reshape(1,-1))


import pandas as pd
import category_encoders as ce

# Sample data
data = {'Education': ['Primary', 'Secondary', 'Tertiary', 'Secondary', 'Primary']}
df = pd.DataFrame(data)

# Define the ordinal order
education_order = {'Primary': 1, 'Secondary': 2, 'Tertiary': 3}

# Initialize OrdinalEncoder with the defined order
ordinal_encoder = ce.OrdinalEncoder(mapping=[{'col': 'Education', 'mapping': education_order}])

# Fit and transform the data
ordinal_encoded_df = ordinal_encoder.fit_transform(df)

# Display the result
print(ordinal_encoded_df)


from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

# Sample data
data = {'Education': ['Primary', 'Secondary', 'Tertiary', 'Secondary', 'Primary']}
df = pd.DataFrame(data)

# Initialize OrdinalEncoder
ordinal_encoder = OrdinalEncoder(categories=[['Primary', 'Secondary', 'Tertiary']])

# Fit and transform the data
ordinal_encoded = ordinal_encoder.fit_transform(df[['Education']])

# Display the result
print(ordinal_encoded)
