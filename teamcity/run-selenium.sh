#!/bin/bash

buildId=$1

cd ..

pip3 install -r requirements.txt

pytest -v -s tests/selenium/ --alluredir=allure-results

#if [ $? -eq 0 ]; then
#  exit 0
#else
#  title="Selenium 測試有點問題"
#  title_link="http://tc.xteamstudio.club/repository/download/HealthChecker_Build/$buildId:id/allure-report/index.html"
#  text="點擊標題連結至測試報表"
#  image_url=https://cdn2.ettoday.net/images/2132/2132200.jpg
#  curl -d '{"text":"佛系 DevOps","attachments":[{"color": "#f4b042","title": "'"$title"'","title_link": "'"$title_link"'","text": "'"$text"'","image_url": "'"$image_url"'"}]}' -H "Content-Type: application/json" -X POST https://hooks.slack.com/services/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
#  exit 1
#fi
