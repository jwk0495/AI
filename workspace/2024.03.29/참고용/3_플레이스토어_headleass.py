{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 모듈 임포트\n",
    "import time\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver import Keys\n",
    "# 2-1. 드라이버 옵션 설정 및 브라우저 띄우기\n",
    "chrom_options = webdriver.ChromeOptions()\n",
    "chrom_options.add_experimental_option('detach', True)\n",
    "driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), \n",
    "                          options=chrom_options)\n",
    "# 3. 주소 이동\n",
    "url = \"https://play.google.com/store/games?hl=ko-KR\"\n",
    "driver.get(url)\n",
    "time.sleep(2)\n",
    "# 4. 실제 앱 주소로 이동\n",
    "app_package = \"com.devsisters.CookieRunForKakao\"\n",
    "app_url = f\"https://play.google.com/store/apps/details?id={app_package}&hl=ko-KR\"\n",
    "driver.get(app_url)\n",
    "# 5-1. 댓글 수집\n",
    "comments = driver.find_elements(By.CSS_SELECTOR, \".h3YV2d\")\n",
    "len(comments) # 화면에 보이는 것만 추출이 됩니다. 리뷰 더보기 클릭 필요\n",
    "# 5-2. 리뷰 더보기 클릭\n",
    "buttons = driver.find_elements(By.CSS_SELECTOR, \".VfPpkd-Bz112c-LgbsSe\")\n",
    "print(len(buttons)) # 여러개 버튼 확인\n",
    "# 5-3. 리뷰 더보기 버튼 선택후 클릭\n",
    "for btn in buttons:\n",
    "    if btn.get_attribute(\"aria-label\") == \"평가 및 리뷰 자세히 알아보기\":\n",
    "        review_btn = btn\n",
    "        break\n",
    "review_btn.click()\n",
    "# 6-1. 리뷰 확인\n",
    "reviews = driver.find_elements(By.CSS_SELECTOR, \"div.h3YV2d\")\n",
    "print(len(reviews)) # 총 23개 밖에 안됨. 스크롤 다운이 필요\n",
    "# 6-2. 스크롤 다운 후 리뷰 확인\n",
    "page = driver.find_element(By.CLASS_NAME, 'fysCi')\n",
    "page.click() # 팝업창 클릭\n",
    "driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)\n",
    "reviews = driver.find_elements(By.CSS_SELECTOR, \"div.h3YV2d\")\n",
    "print(len(reviews)) # 리뷰 증가 - 20개씩 증가\n",
    "time.sleep(2)\n",
    "# 6-3. while 문으로 스크롤 다운 작성\n",
    "target_review = 200\n",
    "while True:\n",
    "    reviews = driver.find_elements(By.CSS_SELECTOR, \"div.h3YV2d\")\n",
    "    if len(reviews) < target_review: # 목표 리뷰 숫자보다 작을 경우\n",
    "        #스크롤다운\n",
    "        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)\n",
    "        time.sleep(1)\n",
    "    else:\n",
    "        break\n",
    "result_list = []\n",
    "for review in reviews:\n",
    "    result_list.append(review.text)\n",
    "result_list"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "sesac2024",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
