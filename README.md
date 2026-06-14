# Đồ án Khai phá dữ liệu - Nhóm 4

## Đề tài
Ứng dụng kỹ thuật gom nhóm trong khai thác dữ liệu khách hàng để phân khúc thị trường

## Giới thiệu

Đây là đồ án học phần **Khai phá dữ liệu (Data Mining)** của **Nhóm 4**.

Mục tiêu của đề tài là sử dụng các kỹ thuật khai phá dữ liệu để phân tích hành vi khách hàng và thực hiện phân khúc khách hàng dựa trên mô hình **RFM (Recency - Frequency - Monetary)**.

Từ dữ liệu giao dịch bán lẻ trực tuyến, nhóm tiến hành:

- Thu thập và tiền xử lý dữ liệu
- Xây dựng mô hình RFM
- Phân tích dữ liệu khám phá (EDA)
- Áp dụng thuật toán K-Means Clustering
- So sánh với Hierarchical Clustering
- Đánh giá mô hình bằng Elbow Method và Silhouette Score
- Phân khúc khách hàng thành các nhóm có đặc điểm tương đồng
- Đề xuất chiến lược marketing phù hợp cho từng nhóm khách hàng

---

## Thành viên nhóm

- Nguyễn Phạm Đình Bảo
- Lương Viễn Đông
- Trần Anh Khoa
- Trần Anh Tú
- Nguyễn Đình Chương

---

## Bộ dữ liệu sử dụng

**Online Retail Dataset**

Nguồn dữ liệu:

https://archive.ics.uci.edu/ml/datasets/online+retail

Thông tin dữ liệu:

- 541.909 giao dịch bán lẻ trực tuyến
- 8 thuộc tính
- Dữ liệu từ 01/12/2010 đến 09/12/2011
- Hơn 4.000 khách hàng

Các thuộc tính chính:

| Thuộc tính | Mô tả |
|------------|--------|
| InvoiceNo | Mã hóa đơn |
| StockCode | Mã sản phẩm |
| Description | Tên sản phẩm |
| Quantity | Số lượng mua |
| InvoiceDate | Ngày giao dịch |
| UnitPrice | Đơn giá |
| CustomerID | Mã khách hàng |
| Country | Quốc gia |

---

## Công nghệ sử dụng

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Plotly
- OpenPyXL

---

## Cài đặt thư viện

Cài đặt tất cả thư viện cần thiết:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit plotly openpyxl
```

Hoặc sử dụng file requirements:

```bash
pip install -r requirements.txt
```

---

## Cấu trúc thư mục

```text
kpdl_nhom4/
│
├── data/
│   ├── rfm_customers.csv
│   ├── rfm_clustered_result.csv
│   └── data_quality_report.txt
│
├── 1_Phan_Tich_EDA.py
├── 2_Mo_Hinh_KMeans.py
├── app.py
├── eda_plot.png
├── kmeans_plot.png
├── requirements.txt
└── README.md
```

---

## Hướng dẫn chạy chương trình

### Bước 1: Chạy phân tích dữ liệu (EDA)

```bash
python 1_Phan_Tich_EDA.py
```

Chức năng:

- Phân tích dữ liệu RFM
- Vẽ biểu đồ phân bố khách hàng
- Vẽ Heatmap tương quan
- Phân tích Monetary, Frequency

Kết quả:

```text
eda_plot.png
```

---

### Bước 2: Chạy mô hình phân cụm

```bash
python 2_Mo_Hinh_KMeans.py
```

Chức năng:

- Chuẩn hóa dữ liệu bằng StandardScaler
- Chạy Elbow Method
- Tính Silhouette Score
- Huấn luyện K-Means
- Huấn luyện Hierarchical Clustering
- So sánh kết quả hai mô hình
- Gán nhãn cụm khách hàng

Kết quả:

```text
rfm_clustered_result.csv
kmeans_plot.png
```

---

### Bước 3: Chạy Dashboard

```bash
streamlit run app.py
```

Sau khi chạy, mở trình duyệt theo đường dẫn hiển thị trên Terminal.

Dashboard hỗ trợ:

- Xem phân bố khách hàng
- Xem thông tin từng cụm
- Trực quan hóa dữ liệu
- Hỗ trợ ra quyết định marketing

---

## Quy trình thực hiện

### 1. Thu thập dữ liệu

- Sử dụng bộ dữ liệu Online Retail
- 541.909 giao dịch

### 2. Tiền xử lý dữ liệu

- Loại bỏ CustomerID bị thiếu
- Loại bỏ dữ liệu trùng lặp
- Loại bỏ hóa đơn bị hủy
- Loại bỏ Quantity <= 0
- Loại bỏ UnitPrice <= 0

Kết quả:

```text
541.909 dòng ban đầu
↓
392.692 giao dịch hợp lệ
```

### 3. Xây dựng RFM

Tạo các thuộc tính:

- Recency
- Frequency
- Monetary

Kết quả:

```text
4.338 khách hàng
```

### 4. Tăng cường dữ liệu

Feature Engineering:

- Recency_Log
- Frequency_Log
- Monetary_Log
- Customer_Value_Level

### 5. Phân tích dữ liệu

- Histogram
- Scatter Plot
- Heatmap
- Pie Chart

### 6. Phân cụm khách hàng

Áp dụng:

- K-Means Clustering
- Hierarchical Clustering

### 7. Đánh giá mô hình

Sử dụng:

- Elbow Method
- Silhouette Score

### 8. Phân tích kết quả

Chia khách hàng thành các nhóm có hành vi tương đồng.

---

## Kết quả chính

### Sau tiền xử lý

| Chỉ tiêu | Giá trị |
|-----------|----------|
| Dữ liệu ban đầu | 541.909 |
| Dữ liệu sau làm sạch | 392.692 |
| Khách hàng RFM | 4.338 |

---

### Kết quả phân cụm

Số cụm được lựa chọn:

```text
K = 3
```

Các nhóm khách hàng:

| Cụm | Tên nhóm | Đặc điểm |
|------|-----------|-----------|
| Cluster 0 | VIP / Kim cương | Mua gần đây, mua nhiều, chi tiêu cao |
| Cluster 1 | Ngủ đông | Lâu không mua, ít mua, chi tiêu thấp |
| Cluster 2 | Tiềm năng | Mua ổn định, có khả năng phát triển |

---

## Chiến lược marketing đề xuất

### VIP / Kim cương

- Chương trình khách hàng thân thiết
- Tích điểm
- Ưu đãi độc quyền
- Chăm sóc cá nhân hóa

### Tiềm năng

- Upsell
- Cross-sell
- Combo sản phẩm
- Voucher khuyến mãi

### Ngủ đông

- Email marketing
- Voucher quay lại
- Chiến dịch kích hoạt lại khách hàng

---

## Kết luận

Đề tài đã xây dựng thành công hệ thống phân khúc khách hàng dựa trên mô hình RFM kết hợp thuật toán K-Means Clustering.

Kết quả cho phép doanh nghiệp nhận diện các nhóm khách hàng có giá trị khác nhau, từ đó xây dựng chiến lược marketing phù hợp, góp phần nâng cao hiệu quả kinh doanh và tối ưu chi phí chăm sóc khách hàng.

---

## Ghi chú

Đây là đồ án phục vụ cho học phần **Khai phá dữ liệu (Data Mining)** của **Nhóm 4**.

Mọi dữ liệu và kết quả trong repository được sử dụng cho mục đích học tập và nghiên cứu.