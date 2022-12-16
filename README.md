# NHẬP MÔN KHOA HỌC DỮ LIỆU
## I. THÔNG TIN NHÓM
|**STT**|**MSSV**|**Họ và tên**|**Email**|
|---|--------|------|-------|
|1|20120307|Phạm Gia Khiêm|20120307@student.hcmus.edu.vn|
|2|20120210|Trần Thị Kim Tiến|20120210@student.hcmus.edu.vn|
|3|20120334|Lý Thành Nam|20120334@student.hcmus.edu.vn|
|4|20120258|Lâm Quốc Chung|20120258@student.hcmus.edu.vn|
- Link Google Meet: https://meet.google.com/cbd-nbiy-nvq
- Link Trello: https://trello.com/b/3IwUJh7Z/nh%C3%B3m-06
- Link Google Drive: https://drive.google.com/drive/u/0/folders/1C-pl17tjqsUDnD0-LzaP8nF-FGcX9GqT
## II. QUY TRÌNH KHOA HỌC DỮ LIỆU
### A. Thu thập dữ liệu: 
#### 1) Yêu cầu dữ liệu:
- Không được phép sử dụng tập dữ liệu đã được công khai hoặc có sẵn trên Kaggle trong đồ án này.
- Dữ liệu phải được cấu trúc hóa thành một bảng gồm ít nhất 5 thuộc tính (trường dữ liệu) và 1000 dòng (records).
#### 2) Nguồn dữ liệu:
- Tên đề tài dữ liệu: Ô NHIỄM MÔI TRƯỜNG
- Từ trang web ô về vấn đề ô nhiễm môi trường https://www.iqair.com
- URL crawl dữ liệu: https://www.iqair.com/vi/world-most-polluted-cities?sort=-rank&page=1&perPage=50
### B. Khám phá dữ liệu:
#### 1) Hiểu dữ liệu:
- Dữ liệu sẽ gồm tên các thành phố, quốc gia, các chỉ số qua từng năm hoặc tháng đã ghi nhận lại. 
- Các thông tin cần biết:
  - Chỉ số PM2.5: Các hạt bụi có kích thước đường kính nhỏ hơn hoặc bằng 2.5 µm
  - Nồng độ PM2.5 trong không khí: Các hạt bụi đạt chỉ số PM2.5 trong không khí với đơn vị đo là μg/m³
  - Chia ra thành các mức độ đánh giá như sau: (Theo WHO)
![image](https://user-images.githubusercontent.com/94270107/201021134-805bd9ff-b8de-4d30-b999-5c051296004e.png)
#### 2) Thông tin dữ liệu:
- Sau khi crawl dữ liệu về thì sẽ có tên: iqair_country_2017-2021.csv (hoặc json)
- Mỗi dòng có ý nghĩa là một thành phố trên thế giới.
- Mỗi cột có ý nghĩa:
  - Cột Thành phố: Tên các thành phố và quốc gia tương ứng
  - Cột 2017 - 2021: Nồng độ PM2.5 được đo tại mỗi thành phố trên thế giới trong từng năm (Từ 2017 - 2021)
  - Cột Tháng 1 - 12: Nồng độ PM2.5 được do tại mỗi thành phố trên thế giới trong từng tháng (Từ tháng 1 - 12) của năm 2022 - (Có dự đoán)
- Hầu như các cột đều có dữ liệu là float, khoảng dữ liệu biểu diễn [0, +oo]. Tuy nhiên cột thành phố có kiểu dữ liệu là string và có thể tiền xử lý là phân tách thành 2 cột khác nhau, 1 cột là Thành phố, 1 cột là Quốc gia.
- Với mỗi cột dữ liệu phân bố tương đối đều, tuy nhiên có một số cột sẽ không có đủ dữ liệu do có thể là thời gian đó không có người ghi nhận tình hình nên không thể thống kê số liệu cụ thể.
### C. Đặt câu hỏi có ý nghĩa để trả lời:
- **Câu hỏi 1**: Đâu la top 5 thanh phô, quôc gia có mật độ ô nhiễm cao nhất, thấp nhất trong 5 năm 2017 - 2021? Với mỗi thanh phô, quôc gia cao nhất, thấp nhất trong năm 2022 mật độ ô nhiễm biến đổi như thế nao theo
các tháng? Thử giải thich.
- **Câu hỏi 2**: Việt Nam nằm trong top bao nhiêu, với mật độ ô nhiễm là bao nhiêu qua từng năm (2017 - 2021). Có sự thay đổi như nao ở Việt Nam trong giai đoạn nay và sự thay đổi nay là tốt hay xấu ? Thử giải thich.
- **Cẩu hỏi 3**: Tháng nao trong năm 2022 sẽ có mức độ ô nhiễm cao nhất cũng như thành phố nào ô nhiễm nhất trong 12 tháng qua, và sự thay đổi của không khi Việt Nam từ 2017 đến 2022.
- **Câu hỏi 4**: Thành phố thuộc quốc gia nào có sự thay đổi nhiều nhất (tăng ô nhiễm nhiều nhất, giảm ô nhiễm nhiều nhất) ? Giai đoạn nào là nhiều nhất? Tại sao?
- **Câu hỏi 5**: Địa điểm, quôc gia nào có nhiều biến động về khi hậu lớn nhất trong 12 tháng của năm 2022, có thể chỉ ra tháng nào hay không ?
## III. CÔNG CỤ. THƯ VIỆN ĐỂ THỰC HIỆN PROJECT:
- Scrapy: https://docs.scrapy.org/en/latest/
- Pandas: https://pandas.pydata.org/docs/reference/
- Matplotlib: https://matplotlib.org/stable/plot_types/index
- Seaborn: https://seaborn.pydata.org/tutorial
- Scikit-learn: https://scikit-learn.org/stable/user_guide.html
