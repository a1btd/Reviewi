#!/usr/bin/env python
# -*- coding: utf-8 -*-
	
from myimports import *

from connect import *

#internationalization parameters
webdomain = 'de'
pre_author = ''
rating_rep = ' von 5 Sternen'
date_rep = 'am '
init_price_cut = 0
fin_price_cut = -2
currency = 'Euro'
retailer = 'Amazon'
country = 'DE'

tr=TorRequest(password='<your pwd>')

#time parameters
now = datetime.datetime.now()
today = now.strftime("%d-%m-%Y")

#other parameters
pgnum='1'
ua = UserAgent(verify_ssl=False, use_cache_server=False)

#set charset
#reload(sys)  # Reload does the trick!
#sys.setdefaultencoding('UTF8')

df = Connect()

id_req = df['ID']
asin = df['ASIN']
email = df['EMAIL']
date = df['DATE']
uk = df['UK']
format = df['FORMAT']

asinlist = asin.tolist()
id_req_list = id_req.tolist()



def ParseReviewsPages(id_req_exec):
	# Added Retrying 
	index_id = id_req_list.index(id_req_exec)
	asin_id = asin[index_id]
	asin_str = asin_id.strip()
	date_id = date[index_id]
	date_str = date_id.strip()
	email_id = email[index_id]
	email_str = email_id.strip()
	format_id = format[index_id]
	format_str = format_id.strip()	
	
	for i in range(10):
  		try:
  			amazon_url  = 'http://www.amazon.'+ webdomain +'/product-reviews/'+asin_str+'/ref=cm_cr_arp_d_paging_btm_2?pageNumber='+pgnum+'&sortBy=recent'
  			print(amazon_url)
 			# Find some chrome user agent strings  here https://udger.com/resources/ua-list/browser-detail?browser=Chrome
 			#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'}
  			headers = {'User-Agent': str(ua.random)}
  			#page = requests.get(amazon_url,headers = headers)
  			tr.reset_identity() #Reset Tor
  			page= tr.get(amazon_url,headers = headers)
  			page_response = page.text
			
  			parser = html.fromstring(page_response)
			
  			XPATH_REVIEWS_COUNT  = './/span[@data-hook="total-review-count"]//text()'							
			 
			
  			raw_reviews_count = parser.xpath(XPATH_REVIEWS_COUNT)
  			reviews_count = ''.join(raw_reviews_count).strip().replace(',','').replace('.','')		
  			reviews_count_int =  int(float(reviews_count))
			
			
  			if (reviews_count_int/10.0)>0.0:         			
  				tot_pages = math.floor(reviews_count_int/10.0)+1.0
  			else:					
  				tot_pages = math.floor(reviews_count_int/10.0)
				
  			data = [asin_str,tot_pages,reviews_count_int,country,date_str,email_str,format_str]							
					
  			return data

  		except ValueError:
  			print('Retrying to get the correct response')
   	
	data = [asin_str,'0','0','0','0','','']
	return data


def ParseReviews(asin,pgnum):
	# Added Retrying 
	for i in range(10):
		try:
          		       
			amazon_url  = 'http://www.amazon.'+ webdomain +'/product-reviews/'+asin+'/ref=cm_cr_arp_d_paging_btm_2?pageNumber='+str(pgnum)+'&sortBy=recent'
			amazon_url_short = 'http://www.amazon.'+ webdomain +'/product-reviews/'+asin+'/ref=cm_cr_arp_d_paging_btm_2?'
			# Find some chrome user agent strings  here https://udger.com/resources/ua-list/browser-detail?browser=Chrome
			#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
			headers = {'User-Agent': str(ua.random)}
			#page = requests.get(amazon_url,headers = headers)

			if i==5:
				tr.reset_identity() #Reset Tor

			page = tr.get(amazon_url,headers = headers)
			page_response = page.text
					
			parser = html.fromstring(page_response)
			XPATH_AGGREGATE = '//span[@id="acrCustomerReviewText"]'
			XPATH_REVIEW_SECTION_1 = '//div[contains(@id,"reviews-summary")]'
			XPATH_REVIEW_SECTION_2 = '//div[@data-hook="review"]'
            
			XPATH_AGGREGATE_RATING = '//table[@id="histogramTable"]//tr'
			XPATH_PRODUCT_NAME = '//h1//a[@data-hook="product-link"]//text()'
			XPATH_PRODUCT_PRICE  = '//span[@class="a-color-price arp-price"]/text()'
			XPATH_REVIEWS_COUNT  = './/span[@data-hook="total-review-count"]//text()'									
         			
			raw_product_price = parser.xpath(XPATH_PRODUCT_PRICE)
			product_price = u''.join(raw_product_price).replace(',','.')
					
			raw_reviews_count = parser.xpath(XPATH_REVIEWS_COUNT)
			reviews_count = ''.join(raw_reviews_count).strip()	
					
			raw_product_name = parser.xpath(XPATH_PRODUCT_NAME)
			product_name = ''.join(raw_product_name).strip()
			total_ratings  = parser.xpath(XPATH_AGGREGATE_RATING)
			reviews = parser.xpath(XPATH_REVIEW_SECTION_1)
			if not reviews:
				reviews = parser.xpath(XPATH_REVIEW_SECTION_2)
				ratings_dict = {}
				reviews_list = []
         			
				if not reviews:
					raise ValueError('unable to find reviews in page')
            
         			#grabing the rating  section in product page
				try:
					while i<=10:
						extracted_rating = parser.xpath('//table[@id="histogramTable"]//tr/td//a//text()')
						if extracted_rating:
							rating_key = extracted_rating[i] 
							raw_raing_value = extracted_rating[i+1]
							rating_value = raw_raing_value
						if rating_key:
							ratings_dict.update({rating_key:rating_value})
						i=i+2
				except:
					pass
         			#Parsing individual reviews
				for review in reviews:
					XPATH_RATING  = './/i[@data-hook="review-star-rating"]//text()'
					XPATH_REVIEW_HEADER = './/a[@data-hook="review-title"]//text()'
					XPATH_REVIEW_POSTED_DATE = './/span[@data-hook="review-date"]//text()'
					XPATH_REVIEW_TEXT_1 = './/span[@data-hook="review-body"]//text()'
					XPATH_REVIEW_TEXT_2 = './/div//span[@data-action="columnbalancing-showfullreview"]/@data-columnbalancing-showfullreview'
					XPATH_REVIEW_COMMENTS = './/span[@data-hook="review-comment"]//text()'
					XPATH_AUTHOR  = './/span[@class="a-profile-name"]//text()'
					XPATH_REVIEW_TEXT_3  = './/div[contains(@id,"dpReviews")]/div/text()'
					raw_review_author = review.xpath(XPATH_AUTHOR)
					raw_review_rating = review.xpath(XPATH_RATING)
					raw_review_header = review.xpath(XPATH_REVIEW_HEADER)
					raw_review_posted_date = review.xpath(XPATH_REVIEW_POSTED_DATE)						
					raw_review_text1 = review.xpath(XPATH_REVIEW_TEXT_1)
					raw_review_text2 = review.xpath(XPATH_REVIEW_TEXT_2)
					raw_review_text3 = review.xpath(XPATH_REVIEW_TEXT_3)
            
					author = ' '.join(raw_review_author)
            
            				#cleaning data
					review_rating = ''.join(raw_review_rating).replace(rating_rep,'').replace(',','.')
					review_header = ' '.join(' '.join(raw_review_header).split())
							
            				#For UK and US dates
					#review_posted_date = dateparser.parse(''.join(raw_review_posted_date)).strftime('%d %b %Y')							
							

            				#For IT,DE and FR dates							
					review_posted_date1 = ''.join(raw_review_posted_date).replace(date_rep,'')
					review_posted_date = dateparser.parse(review_posted_date1).strftime('%d %b %Y')
					review_text = ' '.join(' '.join(raw_review_text1).split())
            
            				#grabbing hidden comments if present

					full_review_text = review_text
					if 1==1:
						#full_review_text = ' '.join(' '.join(raw_review_text3).split())
            
						raw_review_comments = review.xpath(XPATH_REVIEW_COMMENTS)
						review_comments = ''.join(raw_review_comments)
						review_comments = re.sub('[A-Za-z]','',review_comments).strip()
						review_dict = {
           							#'review_comment_count':review_comments,
           							'review_text':full_review_text.replace('"'," ").replace("'"," "),
           							'review_posted_date':review_posted_date,
           							'review_header':review_header.replace('"'," ").replace("'"," "),
           							'review_rating':review_rating,
           							'review_author':author.replace('"'," ").replace("'"," "),
           							'review_url':amazon_url										
            						}
						reviews_list.append(review_dict)
            
				data = {
          						'ratings':ratings_dict,
          						'reviews':reviews_list,
          						'url':amazon_url_short,
          						'price':unidecode.unidecode(product_price[init_price_cut:]),
								'currency': currency,
          						'name':product_name.replace('"'," ").replace("'"," "),
								'asin': asin,
								'reviews-count': reviews_count,
								'retailer': retailer,
								'country': country									
           					}
				return data
					
		except ValueError:
			print ("Retrying to get the correct response")
           	
	return {
						'ratings':'N/A',
          				'reviews':'N/A',
          				'url':amazon_url_short,
          				'price':'N/A'	,
						'currency': 'N/A',
          				'name':'N/A',
						'asin': asin,
						'reviews-count': 'N/A',
						'retailer': retailer,		
						'country': country							
				}

def Execute_DE(id_req):
	extracted_data = []
	#for id_req in id_req_list:
	data = ParseReviewsPages(id_req)
	asin = data[0]
	pgnum = data[1]
	date = data[4]
	email = data[5]
	format_req = data[6] 
	rev_count = data[2]
	print(asin)
	print(int(pgnum))
	print(email)
	for pgnumi in range(1,int(pgnum)+1):
		reviews = ParseReviews(asin,pgnumi)
		extracted_data.append(reviews)
	if format_req == 'JSON':
		filename = str(id_req) + '_'+asin+ '_'+country + '_'+str(date)+'.json'
		f=open(filename,'w')
		json.dump(extracted_data,f,indent=4)
		p_filename = './'+filename
		print(str(p_filename))
		f.close()
		sendemail(email,str(p_filename),country,asin)
	if format_req == 'CSV':
		filename = str(id_req) + '_'+asin+ '_'+country + '_'+str(date)+'.csv'
		file =  open(filename, 'w')
		header_csv = ['asin','name','url','price','currency','reviews_count','retailer','country','rating_5','rating_4','rating_3','rating_2','rating_1','review_text','review_posted_date','review_header','review_rating','review_author','review_url']
		with file as f:
			writer = csv.DictWriter(f,fieldnames=header_csv)
			writer.writeheader()
			
			for data in extracted_data:
				data = str(data).replace("'",'"').replace("\\","")
				json_data = json.loads(data)
				asin = json_data['asin']
				name = json_data['name']
				url = json_data['url']
				price = json_data['price']
				currency = json_data['currency']
				reviews_count = json_data['reviews-count']
				retailer =	json_data['retailer']
				country_rev = json_data['country']
				try:
					rating_5 = json_data['ratings']['5 Sterne']
				except:
					rating_5 = '0%'
				try:
					rating_4 = json_data['ratings']['4 Sterne']
				except:
					rating_4 = '0%'
				try:
					rating_3 = json_data['ratings']['3 Sterne']
				except:
					rating_3 = '0%'
				try:
					rating_2 = json_data['ratings']['2 Sterne']
				except:
					rating_2 = '0%'
				try:
					rating_1 = json_data['ratings']['1 Stern']
				except:
					rating_1 = '0%'
				rev_list = json_data['reviews']
				for r in range(len(rev_list)):
					review_text = json_data['reviews'][r]['review_text']
					review_posted_date = json_data['reviews'][r]['review_posted_date']
					review_header = json_data['reviews'][r]['review_header']
					review_rating = json_data['reviews'][r]['review_rating']
					review_author = json_data['reviews'][r]['review_author']
					review_url = json_data['reviews'][r]['review_url']
					csv_line = {
									'asin' : asin,
									'name' : name,
									'url' : url,
									'price' : price,
									'currency' : currency,
									'reviews_count' : reviews_count,
									'retailer' : retailer,
									'country' : country_rev,
									'rating_5' : rating_5,
									'rating_4' : rating_4,
									'rating_3' : rating_3,
									'rating_2' : rating_2,
									'rating_1' : rating_1,
									'review_text' : review_text,
									'review_posted_date' : review_posted_date,
									'review_header' : review_header,
									'review_rating' : review_rating,
									'review_author' : review_author,
									'review_url' : review_url
								}
					writer.writerow(csv_line)

		p_filename = './'+filename
		print(str(p_filename))
		file.close()
		sendemail(email,str(p_filename),country,asin)

	if format_req == 'XLSX':
		filename = str(id_req) + '_'+asin+ '_'+country + '_'+str(date)+'.xlsx'
		workbook = xlsxwriter.Workbook(filename)
		worksheet = workbook.add_worksheet()
		file =  open(filename, 'w')
		header_xlsx = ['asin','name','url','price','currency','reviews_count','retailer','country','rating_5','rating_4','rating_3','rating_2','rating_1','review_text','review_posted_date','review_header','review_rating','review_author','review_url']
		for i in range(len(header_xlsx)):
			worksheet.write(0,i,header_xlsx[i])

		c = 0
		for data in extracted_data:
			data = str(data).replace("'",'"').replace("\\","")
			json_data = json.loads(data)
			asin = json_data['asin']
			name = json_data['name']
			url = json_data['url']
			price = json_data['price']
			currency = json_data['currency']
			reviews_count = json_data['reviews-count']
			retailer =	json_data['retailer']
			country_rev = json_data['country']
			try:
				rating_5 = json_data['ratings']['5 Sterne']
			except:
				rating_5 = '0%'
			try:
				rating_4 = json_data['ratings']['4 Sterne']
			except:
				rating_4 = '0%'
			try:
				rating_3 = json_data['ratings']['3 Sterne']
			except:
				rating_3 = '0%'
			try:
				rating_2 = json_data['ratings']['2 Sterne']
			except:
				rating_2 = '0%'
			try:
				rating_1 = json_data['ratings']['1 Stern']
			except:
				rating_1 = '0%'
			rev_list = json_data['reviews']
			
			for r in range(len(rev_list)):
				c=c+1
				review_text = json_data['reviews'][r]['review_text']
				review_posted_date = json_data['reviews'][r]['review_posted_date']
				review_header = json_data['reviews'][r]['review_header']
				review_rating = json_data['reviews'][r]['review_rating']
				review_author = json_data['reviews'][r]['review_author']
				review_url = json_data['reviews'][r]['review_url']
				xlsx_line = [
								asin,
								name,
								url,
								price,
								currency,
								reviews_count,
								retailer,
								country_rev,
								rating_5,
								rating_4,
								rating_3,
								rating_2,
								rating_1,
								review_text,
								review_posted_date,
								review_header,
								review_rating,
								review_author,
								review_url
							]
				for i in range(len(xlsx_line)):
						worksheet.write(c,i,xlsx_line[i])

		p_filename = './'+filename
		print(str(p_filename))
		workbook.close()
		sendemail(email,str(p_filename),country,asin)		
	
	Update(id_req,country)
	Insert(id_req,rev_count,country)

        
#if __name__ == '__main__':
#	Execute_DE(170)
#db.close()