#!/usr/bin/env bash
echo $1
curl -X POST -H "Content-Type: application/json" -d "{
  \"setting_type\":\"greeting\",
  \"greeting\":{
    \"text\": "Play Tic-tac-toe with GameClub bot. See the menu to start new game"
  }
}" "https://graph.facebook.com/v2.6/me/thread_settings?access_token=$PAGE_ACCESS_TOKEN"