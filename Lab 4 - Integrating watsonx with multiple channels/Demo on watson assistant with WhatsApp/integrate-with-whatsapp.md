# Integrating watsonx with whats app
Watson Assistant can be embedded with WhatsApp without any need for code. If you have a use case for using WhatsApp as a chatbot, you might want to consider this integration.


## Create Twilio Account.
Create twilio account [here](https://www.twilio.com/login)

<img width="1292" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/ef390a9d-bf38-4353-be36-69b8547bfa1a">

Twilio will ask for the phone number connected to WhatsApp. You can fill in your phone number here.

<img width="1512" alt="wa phone number indonesia" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/6850f9b8-8a76-41fb-9a8a-1c7ed2698b24">

Twilio will ask you to fill out surveys; you can choose to skip or answer the survey.

<img width="1512" alt="wa survey" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/01b9adec-6d9d-44a3-a61b-6e8a1e4b8d38">

Copy and save your **Account SID and Auth Token**

<img width="1512" alt="wa account sid and auth token" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/59eec09d-23e0-4be2-a20b-88b51196d14d">

Open Watson Assistant. We will still using our watson assistant from previously flow. Open integration. Scroll down untill you find Whats App with Twilio. Click Add

<img width="1297" alt="wa twilio" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/9379f2f4-5134-48c3-9c66-1a79041b6e02">

Enter your Account SID from Twilio into Watson Assistant, then click 'Next.' Proceed to fill in your Auth from Twilio into Watson Assistant. Click Next

<img width="1297" alt="wa account sid in wa" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/7ed6af7b-ea02-4696-a667-acfbcdbcbcb5">

The Watson Assistant will provide you with webhook link. **Copy the link of webhook**. Click Finish.

<img width="1297" alt="wa webhook" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/a25908e0-328d-4187-82c4-6faeb027f330">

Open Twilio. Click Messaging. Choose Send a Whats App Message 

<img width="1474" alt="wa send message" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/f3c62ce9-cb03-4184-9bce-3fc8b3f6a8d2">

Paste the webhook link that you already copy into sandbox settings like below example. Click Save

<img width="1512" alt="wa inetgrate link " src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/68561222-a4f0-45de-9238-b0ca307ad6b7">

Go to sanbox, you will find your barcode and also the phone number that will look like as your What App bot chat. Scan the QR code with your Whats App. 

<img width="1512" alt="wa to whats app" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/eed1e573-840c-42ec-99e0-a54a12b660a5">

<img width="1324" alt="wa open" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/0bfd0df2-fd90-41c9-97e5-4d453fb6b3f4">

To connect with your Watson Assistant flow, you need to send "join sandbox name". For example below the sanbox join name is join enjoy-village. You can find your sanbox name in the QR code on Twilio.

<img width="939" alt="wa send message join enjoy village" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/426b14b2-342a-406f-9736-b1bd6083422e">

Go to Twilio. Try to send any message. The Message will be send to the Whats App account. Try to reply the message in Whats App.

<img width="1512" alt="wa hallo send template message first time" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/2bab4c65-b0f6-4805-9018-0dc4c597b676">

<img width="967" alt="wa halo di wa" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/b3ec22d0-4d14-4527-8708-4b255ae35f59">

After you reply the message, you will now see all of the requirment in Twilio already check done 

<img width="1512" alt="wa finish the sandbox" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/5b261890-da01-4cda-81e2-434789c0dfbe">

You can start to asking anything in this [document](https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/blob/main/data/Peraturan_Perusahaan.pdf)

<img width="969" alt="wa finished " src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/bfcebe99-4f70-48ff-acd7-ab3e0db25e9d">

You can start asking question for example
- saya mau tanya mengenai kapan gaji dibayarkan
- berapa umur pensiun
- saya mau tanya mengenai kapan gaji dibayarkan
- jelaskan kepada saya mengenai THR dan bagaimana mendapatkannya




















