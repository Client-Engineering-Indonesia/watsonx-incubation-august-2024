# Integrating watsonx with Map
Watson Assistant can be integrated with map. If you have usecase in finding the nearest area, you can use Watson Assistant to embed the map, and let the AI to choose the nearest place from your database. In this lab, we will only learn how easy it is to integrate map with watson assistant and using AI to convert string to longitude and latitude (geocode), no code at all 🚀.


## Create New Assistant
Create new assistant

<img width="1512" alt="maps create new" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/53940b59-6d55-4984-add3-7094bf562e98">


Below is the new appearance of the assistant that has been created. 
Go to the settings to upload the flow (action.json). Download the action.json [here](https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/blob/main/Lab%206%3A%20watsonx%20use%20case/Integrate%20watsonx%20assistant%20with%20maps%20location/Assistant-action.json)

<img width="1512" alt="maps upload" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/d9a512e9-9f14-4c3a-9b7c-26ea69bc1464">
 
Once you open the setting, you will have this display, click the following button to upload action.json that you already download in the previously step.

<img width="1512" alt="maps to upload" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/57c2d693-be23-45f6-bf5a-609bcee96a86">

Upload the action.json and save it. 
<img width="1512" alt="maps upload section" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/a5392ce7-c9f1-413f-b0d2-66f5d1d08732">

<img width="1512" alt="maps already upload" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/c4165c05-f81a-4cd1-8ccc-3ec02651986a">

After uploading, you will see the following display. The red status indicates that there are integrations that have not been done yet, so integration needs to be done first. Click the integration, to integrate it with Watsonx and Watson Discovery

<img width="1512" alt="maps status red" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/82b66508-709c-4e5a-af4e-fd32e07e9ed7">

## Integrate with Watsonx and Watson Discovery
We are going to integrate Watsonx and Watson Discovery.

Scroll down until you find "build custom extension".

<img width="1512" alt="maps build extension" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/a49d4038-93c3-42e8-88f1-d82638fd95a5">

Naming the extension as shown below (watsonx). Click Next. Download watsonx oepn api [here](https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/blob/main/Lab%206%3A%20watsonx%20use%20case/Integrate%20watsonx%20assistant%20with%20maps%20location/watsonx-openapi.json). Upload the watsonx open api that already been download.

<img width="1512" alt="maps integration watsonx" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/3e157692-edde-4204-84ea-3416503fd408">

Click next. Review it. Then click finish
<img width="1512" alt="maps finish extension" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/6ba6e3e1-8411-4bdf-ae7c-0b7cc2ca856d">

You will find something like this, now time to embed the APIkey of watsonx there. Click add

<img width="1512" alt="maps add watsonx" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/e7c2b917-448d-496e-b98b-ff6afbe13bd8">

Select OAuth 2.0 as the authentication type, and fill in the API Key field with your own API key. Click Next then Finish.

<img width="1512" alt="maps watsonx" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/60f9df4b-1262-4b1d-bc17-3f060fc41508">

Voila, the watsonx already integrated with watson assistant 🎈. Now do the same part to integrate Watson Discovery.

Naming the extension as shown below (watson discovery). Download watson discovery open api [here](https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/blob/main/Lab%206%3A%20watsonx%20use%20case/Integrate%20watsonx%20assistant%20with%20maps%20location/watson-discovery-query-openapi.json). Upload the watson discovery open api that already been download.

<img width="1512" alt="maps discovery" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/2c3c8912-a307-4e87-8c19-edb403618cd5">

You will find something like this, now time to embed the APIkey of watson discovery there. Click add
<img width="1512" alt="maps discovery add" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/3f570c64-56ae-4194-a071-5cda6c4e162d">

Fill the apikey field with 'api key' and for the password and discovery_url field  we will email it to you. Click Next, click Finish

Congratulations, you already integrate Watsonx and Watson Discovery to Watson Assistant with no code at all 😃. Your Assistant now should be look like this

<img width="1512" alt="maps configured" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/20d36518-fea6-4087-9259-d0163902c6b1">

## Generate Map
Click Preview, and call the function with something similiar like "saya mau cek lokasi" or "cek lokasi". Then the Watson Assistant will asking you about your destination and currect condition, and will provide you with map. For example here i use destination: 'grand indonesia' and current location 'fatmawati'

<img width="1297" alt="maps to grand indonesia" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/d7aa117c-b679-4288-a81f-044f982634ac">

Above shown that, AI can convert your current position (string) into geocode (long lat). We use this prompt to make that happen. If you want to create it more precise, you can also adding more prompt to make it detail.
<img width="1297" alt="maps prompt" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/58867427-d4a9-4b2e-b0b7-fc505f892c70">

The long lat then will be as input in the map such as this.
<img width="1297" alt="map long lat" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/68722344/63862bfd-4fd5-49c8-92da-37c205b4ec9e">

What do you think? is it cool to embed map with no code at all? can you imagine how fast to integrate it? 

Many our client ask this feature for searching the nearest location that integrate with their own databases, AI will convert the destination to geocode, then will search and provide you with the nearest location.































