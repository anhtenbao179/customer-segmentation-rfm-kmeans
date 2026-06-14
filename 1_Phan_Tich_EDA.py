# -*- coding: utf-8 -*-
"""
File 1: Phân tích Khám phá Dữ liệu (EDA)
"""
#%% 1. IMPORT THƯ VIỆN VÀ ĐỌC DỮ LIỆU
import pandas as pd
import matplotlib.pyplot as plt
import sys
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

import seaborn as sns

# Thiết lập phong cách biểu đồ cho đẹp mắt
sns.set_theme(style="whitegrid")

# Đọc dữ liệu từ file CSV (đảm bảo file rfm_customers.csv để cùng thư mục với file code này)
# Thay dòng df = pd.read_csv('rfm_customers.csv') thành:
df = pd.read_csv(r'C:\Users\TRAN ANH TU\Downloads\kpdl_nhom4\data\rfm_customers.csv')

print("Đã đọc dữ liệu thành công. Kích thước dữ liệu:", df.shape)

#%% 2. VẼ TẤT CẢ BIỂU ĐỒ VÀO CÙNG MỘT KHUNG (FIGURE)
# Khởi tạo một khung chứa các biểu đồ
fig = plt.figure(figsize=(18, 12))

# --- Biểu đồ 1: Tỷ lệ các nhóm khách hàng ban đầu (Pie Chart) ---
plt.subplot(2, 2, 1)
label_counts = df['Customer_Value_Level'].value_counts()
colors = ['#ff9999','#66b3ff','#99ff99']
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', 
        startangle=90, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.title('Phân bố nhãn Customer_Value_Level', fontsize=14, fontweight='bold')

# --- Biểu đồ 2: Phân phối Monetary sau khi lấy Logarit (Histogram) ---
plt.subplot(2, 2, 2)
sns.histplot(df['Monetary_Log'], kde=True, color='purple', bins=40)
plt.title('Phân phối của Monetary (sau khi Transform Log)', fontsize=14, fontweight='bold')
plt.xlabel('Monetary_Log')
plt.ylabel('Số lượng khách hàng')

# --- Biểu đồ 3: Ma trận tương quan các đặc trưng Log (Correlation Heatmap) ---
plt.subplot(2, 2, 3)
correlation_matrix = df[['Recency_Log', 'Frequency_Log', 'Monetary_Log']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Ma trận tương quan giữa các đặc trưng (R-F-M Log)', fontsize=14, fontweight='bold')

# --- Biểu đồ 4: Scatter Plot thể hiện mối quan hệ F và M ---
plt.subplot(2, 2, 4)
sns.scatterplot(data=df, x='Frequency_Log', y='Monetary_Log', 
                hue='Customer_Value_Level', palette='Set1', alpha=0.7)
plt.title('Mối quan hệ giữa Frequency và Monetary theo nhóm', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('eda_plot.png')
plt.show() # Biểu đồ sẽ hiển thị ở tab "Plots" trong Spyder