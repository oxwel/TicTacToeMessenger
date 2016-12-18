#!/usr/bin/env bash

curl -X POST -H "Content-Type: application/json" -d "{
  \"setting_type\" : \"call_to_actions\",
  \"thread_state\" : \"existing_thread\",
  \"call_to_actions\":[
    {
      \"type\":\"postback\",
      \"title\":\"Start new game\",
      \"payload\":\"PAYLOAD_START_NEW_GAME\"
    },
    {
      \"type\":\"postback\",
      \"title\":\"Start a New Order\",
      \"payload\":\"DEVELOPER_DEFINED_PAYLOAD_FOR_START_ORDER\"
    },
    {
      \"type\":\"web_url\",
      \"title\":\"Checkout\",
      \"url\":\"http://petersapparel.parseapp.com/checkout\",
      \"webview_height_ratio\": \"full\",
      \"messenger_extensions\": true
    },
    {
      \"type\":\"web_url\",
      \"title\":\"View Website\",
      \"url\":\"http://petersapparel.parseapp.com/\"
    }
  ]
}" "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"