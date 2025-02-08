fetch("https://www.sportybet.com/api/ng/pocket/v1/bankTrades/bankTrade/250208082001trd56091306/additional", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en",
    "clientid": "web",
    "content-type": "application/json;charset=UTF-8",
    "operid": "2",
    "platform": "web",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin"
  },
  "referrer": "https://www.sportybet.com/ng/my_accounts/deposit",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"tradeId\":\"250208082001trd56091306\",\"type\":11}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
})
  .then(e=>   console.log(e))
  .then((result) => {
    console.log(result);
    
  }).catch((err) => {
    console.log(err);
    
  })