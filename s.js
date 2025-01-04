fetch("https://worldexpresscarrier.com/fetch/", {
    "headers": {
      "accept": "*/*",
      "accept-language": "en-US,en;q=0.9,pt;q=0.8",
      "content-type": "application/json",
      "priority": "u=1, i",
      "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-csrftoken": "JU8EBMFW1237v8qrRVEJ5LKZY4dtQIBJvcuFX4wkbSfBulfqrzChfvHpR8T3pR4Q"
    },
    "referrer": "https://worldexpresscarrier.com/auth-central/1/",
    "referrerPolicy": "same-origin",
    "body": "{\"SName\":\"Muhammad Adib\",\"SAddress\":\"******\",\"SEmail\":\"******@gmail.com\",\"SPhone\":\"+66841657160\",\"message\":\"in Transit\",\"RName\":\"ELPIRA ROSITA HERAWATI\",\"RAddress\":\"Majalengka regency/WestJavaProvince   \",\"REmail\":\"*****@gmail.com\",\"RPhone\":\"+6283863550823\",\"Origin\":\"Bangkok Thailand\",\"Destination\":\"Neglasari block   Rt/Rw 001/002  Enggalwangi village   District Palasah \",\"Mode\":\"Express/home delivery\",\"Quantity\":\"1\",\"Weight\":\"15kg\",\"Amount\":\" 3million Rupiah\",\"PaymentMode\":\"Mobile/bank/payment\",\"Delivery\":\"1st January 2025\",\"DepartureDate\":\"31st December 2024\",\"PackageItems\":\" 1 sealed brown boxes\"}",
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
  })
  .then(e=>e.json())
  .then((result) => {
    console.log(result);
    
  }).catch((err) => {
    console.log(err);
    
  })