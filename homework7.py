import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer

# 1. 读取数据
df = pd.read_csv('fraudulent.csv')

# 2. 检查缺失值并剔除缺失值过多的列
threshold = 0.3  # 缺失值比例阈值
total_rows = df.shape[0]
columns_to_drop = []
for column in df.columns:
    missing_values = df[column].isnull().sum()
    if missing_values / total_rows > threshold:
        columns_to_drop.append(column)
df.drop(columns=columns_to_drop, inplace=True)

# 3. 填充剩余的缺失值
imputer = SimpleImputer(strategy='mean')  # 可以选择'median', 'most_frequent'等
df[:] = imputer.fit_transform(df)

# 4. 分割数据集
X = df.drop('y', axis=1)
y = df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 5. 训练模型
# 这里以k-近邻为例，你可以添加更多的模型
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# 6. 模型评估
y_pred = knn.predict(X_test)
f1 = f1_score(y_test, y_pred)
print(f'KNN F1 Score: {f1}')

# 训练其他模型并评估
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
f1_dt = f1_score(y_test, y_pred_dt)
print(f'Decision Tree F1 Score: {f1_dt}')

lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
f1_lr = f1_score(y_test, y_pred_lr)
print(f'Logistic Regression F1 Score: {f1_lr}')

svc = SVC()
svc.fit(X_train, y_train)
y_pred_svc = svc.predict(X_test)
f1_svc = f1_score(y_test, y_pred_svc)
print(f'SVM F1 Score: {f1_svc}')

# 7. 比较模型
best_model = max((knn, f1), (dt, f1_dt), (lr, f1_lr), (svc, f1_svc), key=lambda x: x[1])
print(f'Best Model: {best_model[0].__class__.__name__} with F1 Score: {best_model[1]}')