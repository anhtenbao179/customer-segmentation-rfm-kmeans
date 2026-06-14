# -*- coding: utf-8 -*-
"""
File 2: Huấn luyện mô hình K-Means Clustering và Trích xuất Đặc trưng
"""
#%% 1. IMPORT THƯ VIỆN VÀ CHUẨN BỊ DỮ LIỆU
import pandas as pd
import numpy as np
import sys
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Đọc dữ liệu
# Thay dòng df = pd.read_csv('rfm_customers.csv') thành:
df = pd.read_csv(r'C:\Users\TRAN ANH TU\Downloads\kpdl_nhom4\data\rfm_customers.csv')

# Lấy ra các cột Features (đã biến đổi Log để phân phối chuẩn hơn)
X = df[['Recency_Log', 'Frequency_Log', 'Monetary_Log']]

# Chuẩn hóa dữ liệu (Standardization) - Bước bắt buộc của K-Means
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Đã chuẩn bị và chuẩn hóa dữ liệu xong.")

#%% 2. TÌM SỐ CỤM TỐI ƯU (ELBOW & SILHOUETTE METHOD)
wcss = []
silhouette_scores = []
K_range = range(2, 8)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Vẽ biểu đồ đánh giá
fig, ax1 = plt.subplots(figsize=(10, 5))

# Vẽ đường WCSS (Elbow) - Trục Y bên trái
color = 'tab:blue'
ax1.set_xlabel('Số lượng cụm (k)')
ax1.set_ylabel('WCSS (Inertia)', color=color)
ax1.plot(K_range, wcss, marker='o', color=color, label='WCSS')
ax1.tick_params(axis='y', labelcolor=color)

# Vẽ đường Silhouette - Trục Y bên phải
ax2 = ax1.twinx()  
color = 'tab:orange'
ax2.set_ylabel('Silhouette Score', color=color)  
ax2.plot(K_range, silhouette_scores, marker='s', color=color, label='Silhouette')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Phương pháp Elbow và Silhouette để chọn số cụm tối ưu', fontsize=14)
plt.grid(True)
plt.savefig('kmeans_plot.png')
plt.show()

#%% 3. ÁP DỤNG K-MEANS VỚI K=3 VÀ PHÂN TÍCH ĐẶC TRƯNG CỤM
# Dựa vào biểu đồ trên, ta chọn k=3
kmeans_final = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans_final.fit_predict(X_scaled)

# Tính giá trị trung bình trên các cột gốc (chưa Log) để dễ diễn giải
cluster_profile = df.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'CustomerID': 'count' # Đếm số lượng khách hàng trong mỗi cụm
}).round(2)

# Đổi tên cột cho dễ đọc
cluster_profile.rename(columns={'CustomerID': 'So_luong_KH'}, inplace=True)

print("\n==================================================")
print("ĐẶC TRƯNG CỦA CÁC CỤM KHÁCH HÀNG (K-MEANS VỚI K=3):")
print("==================================================")
print(cluster_profile)

# Lấy điểm Silhouette Score của K-Means để so sánh
kmeans_silhouette = silhouette_score(X_scaled, kmeans_final.labels_)
print(f"Silhouette Score của K-Means: {kmeans_silhouette:.4f}")

#%% 4. ÁP DỤNG THUẬT TOÁN THỨ 2 (HIERARCHICAL CLUSTERING) ĐỂ SO SÁNH
print("\n==================================================")
print("ĐÁNH GIÁ VÀ SO SÁNH VỚI HIERARCHICAL CLUSTERING")
print("==================================================")

# Khởi tạo mô hình Agglomerative Clustering với K=3
hc_model = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
hc_labels = hc_model.fit_predict(X_scaled)

# Tính toán Silhouette Score cho Hierarchical Clustering
hc_silhouette = silhouette_score(X_scaled, hc_labels)
print(f"Silhouette Score của Hierarchical Clustering: {hc_silhouette:.4f}")

# So sánh 2 mô hình
print("\nKẾT LUẬN SO SÁNH:")
if kmeans_silhouette > hc_silhouette:
    print("=> K-Means có Silhouette Score cao hơn, nên K-Means gom cụm tốt hơn trên bộ dữ liệu này.")
else:
    print("=> Hierarchical Clustering có Silhouette Score cao hơn, nên tốt hơn trên bộ dữ liệu này.")

# Lưu lại kết quả phân cụm ra file csv mới để chuyển giao
df.to_csv(r'C:\Users\TRAN ANH TU\Downloads\kpdl_nhom4\data\rfm_clustered_result.csv', index=False)
print("\nĐã lưu file dữ liệu kèm nhãn phân cụm thành rfm_clustered_result.csv vào thư mục data.")