import scrapy
import numpy as np
from air_quality.items import AirQualityItem

class collect_air_data(scrapy.Spider): #Khởi tạo class dùng để thu thập
    name = 'air_datas' #Tên spider
    
    data = AirQualityItem() #spider Field để chuyển đổi sang json
    
    #Bắt đầu request
    def start_requests(self):
        start = 'https://www.iqair.com/vi/world-most-polluted-cities?sort=-rank&page=1&perPage=50' #Url bắt đầu

        urls = [] #Danh sách url cần lấy dữ liệu
        
        for i in range(1, 131): #Có tổng cộng 130 url, lặp qua để thêm vào danh sách urls
            url = start.replace('1', str(i))
            urls.append(url)
            
        for url in urls: #Thực hiện request với từng url
            yield scrapy.Request(url = url, callback = self.parse)
    
    #Lấy dữ liệu cần thiết
    def parse(self, response):
        #Tìm thẻ tbody chứa bảng 50 thành phố
        res = response.css('tbody[role = "rowgroup"]') 
        
        #Thêm từng thành phố vào list_rank, mỗi thành phố được định nghĩa trong thẻ tr
        list_rank = np.array(res.css('tr')) 
        
        #Với mỗi thành phố trích xuất dữ liệu cần thiết, những dữ liệu này đều nằm trong thẻ td
        for i in list_rank:
            city = i.css('td')
            
            self.data['Rank'] = city[0].css('td::text').get() #Hạng
            self.data['City'] = city[1].css('div::text').get() #Tên thành phố
            
            self.data['Year_2021'] = city[2].css('span::text').get() #Chỉ số năm 2021
            
            self.data['Jan'] = city[3].css('span::text').get() #Chỉ số tháng 1
            self.data['Feb'] = city[4].css('span::text').get() #Chỉ số tháng 2
            self.data['Mar'] = city[5].css('span::text').get() #Chỉ số tháng 3
            self.data['Apr'] = city[6].css('span::text').get() #Chỉ số tháng 4
            self.data['May'] = city[7].css('span::text').get() #Chỉ số tháng 5
            self.data['Jun'] = city[8].css('span::text').get() #Chỉ số tháng 6
            self.data['Jul'] = city[9].css('span::text').get() #Chỉ số tháng 7
            self.data['Aug'] = city[10].css('span::text').get() #Chỉ số tháng 8
            self.data['Sep'] = city[11].css('span::text').get() #Chỉ số tháng 9
            self.data['Oct'] = city[12].css('span::text').get() #Chỉ số tháng 10
            self.data['Nov'] = city[13].css('span::text').get() #Chỉ số tháng 11
            self.data['Dec'] = city[14].css('span::text').get() #Chỉ số tháng 12
            
            self.data['Year_2020'] = city[15].css('span::text').get() #Chỉ số năm 2020
            self.data['Year_2019'] = city[16].css('span::text').get() #Chỉ số năm 2019
            self.data['Year_2018'] = city[17].css('span::text').get() #Chỉ số năm 2018
            self.data['Year_2017'] = city[18].css('span::text').get() #Chỉ số năm 2017
                
            yield self.data #Trả về spider Field data
