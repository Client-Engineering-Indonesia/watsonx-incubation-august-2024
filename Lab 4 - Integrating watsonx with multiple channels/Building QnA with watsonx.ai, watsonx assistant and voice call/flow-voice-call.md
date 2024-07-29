# watsonx flow with Phone Voice Calls

To ensure a seamless flow, it's essential to ensure that the flow meets our expectations. We'll create several intents, such as greetings, introductions, knowledge retrieval, and connecting with a live agent.

<img width="1200" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2024/assets/20800128/fd327c7a-5087-4d50-9c62-5be9a953b394">


## Conversation Flow:


[Question Introduction]
- Hello

[Question Discovery]
- I want to take paternity leave!
- How much leave is available per year?
- what is the process of cancellation of leave

[Question End Conversation]
- Okay, thank you

[Question Live Agent]
- I want to talk to a live agent


## Integration Setup:
1. **Upload OAS Files:**
First, you need to upload OAS for call watsonx and watsonx discovery API in the integration tab
[Upload OAS file name watsonx-openapii.json](https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/blob/main/Lab%206%3A%20watsonx%20use%20case/Building%20QnA%20with%20watsonx.ai%2C%20watsonx%20assistant%20and%20voice%20call/watsonx-openapii.json) and [Upload OAS file name watson-discovery-query-openapi.json](https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/blob/main/Lab%206%3A%20watsonx%20use%20case/Building%20QnA%20with%20watsonx.ai%2C%20watsonx%20assistant%20and%20voice%20call/watson-discovery-query-openapi.json)

<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/dfc426cc-9562-41b3-b40b-0cd33faad581">


2. **Upload Phone Action File:**
Second, you need to upload phone-action.json in the global setting. Once you upload, the flow will be automatically created
[Upload action file name Phone-action.json](https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/blob/main/Lab%206%3A%20watsonx%20use%20case/Building%20QnA%20with%20watsonx.ai%2C%20watsonx%20assistant%20and%20voice%20call/Phone-action.json)

<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/cb3a75da-ff4a-497d-83c6-536eca45a166">


## Flow Overview:
### Greet Customer:
Ensure the bot welcomes users by setting the condition "Channel Name" to "Phone" as the first interaction.
  
<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/5da3cce4-9501-464d-bf25-dbe9ea46820e">


You can adjust variations response to make a variation response
<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/64b05e5c-0b22-4a6b-af93-dfbe0acdfabf">

<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/692bc89a-d55b-4684-bd53-9196eae515ce">


Then, whenever the user says something we will direct it to either one of these 4 actions; introduction, policy, end_conversation, and agent


<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/e1070c0d-5e13-4504-965d-3327005ef511">


### Introduction:
The assistant responds to casual greetings with "Is there any help?"

<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/cd755a7e-40a3-459e-bd9f-e1a7764f412b">


### Policy:
Handles queries regarding company policy or leave policies using watsonx ai and watson discovery.
  
First, we need to put the intention, if the user asks about the policy or leaves the company. The assistant will proceed in this flow.


<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/518b3211-8d59-4d54-9d63-5ab0a76f20e9">


Every time we say over the phone, there is a session history that can keep the conversation. We set the variable for the first_invokation for the question that we need on watson discovery and watsonx ai part


<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/25a2fd27-5531-4298-9a38-6eb15ae8335b">


We use an extension for watson discovery for step 2


<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/94654956-d4de-44f6-8f2b-f386e1fe808f">


In step 3, we save the output of watson discovery where this output contain a retrieval of the document that we searched

<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/ced7269e-9b9f-4771-bbdd-a99adc0fbe2b">


In step 4, use the watsonx ai extension to generate the passage from the document retrieval based on the question

<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/89614743-bdde-4dee-b217-6c3b1a3a9efa">


You can easily put an instruction and adjust the prompt for the ai


<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/b22b9d0b-ffe1-4479-9438-46e1248a5073">


In the last step, this is where the output of watsonx ai is generated


<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/18039bfb-e807-436f-bd03-7134ad425f8c">


### Live Agent:
Transfers to a live agent for direct assistance.


<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/822e86f1-639e-42fa-978e-bda815d19756">

<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/a7e14914-0d35-4f14-8404-c3b93b2c0c72">


### End Conversation:
Concludes the call if the user indicates they have received enough assistance.

<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/a0631fea-9cd4-4cc3-86a7-d3258865ce35">


<img width="1722" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/20800128/93fcc58f-b09d-489f-af4c-41159103b23b">
















