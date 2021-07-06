import crawling
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

page = 13322569

while page > 13320569 :
  page=str(page)
  url = f"http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={page}&target=after"

  with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(crawling.do_crawl, url)

    page = int(page)
    page -= 1
        
