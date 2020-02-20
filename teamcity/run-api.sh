#!/bin/bash

buildId=$1
isNotify=$2

cd ..

pip3 install -r requirements.txt

pytest -v -s tests/api/ --alluredir=allure-results

if [[ $? -eq 0 ]]; then
  title="API 測試通過"
  title_link="http://ec2-54-199-172-196.ap-northeast-1.compute.amazonaws.com:8111/repository/download/EndToEndTesting_RunApiTests/$buildId:id/allure-report/index.html"
  text="點擊連結至測試報表"
  image_url=https://slack-files.com/T7NUD3U1W-FTTP4VDQU-f7894e7423
  if [[ $isNotify -eq 1 ]]; then
    curl -d '{"text":"佛系 DevOps，時間到了就會好","attachments":[{"color": "#f4b042","title": "'"$title"'","title_link": "'"$title_link"'","text": "'"$text"'","image_url": "'"$image_url"'"}]}' -H "Content-Type: application/json" -X POST https://hooks.slack.com/services/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
  fi
  exit 0
else
  title="API 測試失敗"
  title_link="http://ec2-54-199-172-196.ap-northeast-1.compute.amazonaws.com:8111/repository/download/EndToEndTesting_RunApiTests/$buildId:id/allure-report/index.html"
  text="點擊連結至測試報表"
  image_url=https://slack-files.com/T7NUD3U1W-FTTP4VDQU-f7894e7423
  if [[ $isNotify -eq 1 ]]; then
    curl -d '{"text":"佛系 DevOps，時間到了還沒好","attachments":[{"color": "#f4b042","title": "'"$title"'","title_link": "'"$title_link"'","text": "'"$text"'","image_url": "'"$image_url"'"}]}' -H "Content-Type: application/json" -X POST https://hooks.slack.com/services/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
  fi
  exit 1
fi
