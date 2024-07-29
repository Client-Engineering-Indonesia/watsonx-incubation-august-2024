# watson Discovery Set-Up Process

## Introduction
_Watson Discovery is an award-winning AI-powered intelligent search and text-analytics platform that eliminates data silos and retrieves information buried inside enterprise data. It uses innovative, market-leading natural language processing (NLP) to uncover meaningful business insights from documents, webpages, and big data. Watson Discovery makes it possible to rapidly build cognitive, cloud-based exploration applications that unlock actionable insights hidden in unstructured data including your own proprietary data, as well as public and third-party data._

## Uploading Document Process
### 1. Launch Watson Discovery
Click _"Launch Watson Discovery"_ to start creating the project

<img width="521" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/8d2865ec-a29e-444f-a105-7de3e45d2257">

_Notes:_

API key and URL information: _Credentials_ are used to connect Watson Discovery to other services or applications.

_Plan of Watson Discovery:_ There are _Plus, Enterprise, Premium Plan_ packages. Further information can be found at [Pricing Watson Discovery](https://www.ibm.com/products/watson-discovery/pricing)

### 2. Build your First Project
There are Projects and Collections in Watson Discovery that can be used to manage the utilization of the documents we have. To start the process you can click "New Project"

<img width="570" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/32fa4387-3bb6-4a02-818a-66e0f47f5e49">

_Notes:_

_Sample Project_: This project has been automatically created by the system and can be used to explore Watson Discovery capabilities

### 3. Creating a new project
After clicking New Project, you will be asked to enter your project name and project type when using Watson Discovery

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/9fd0da8b-9be8-4a65-9064-331203c79e82">


### 4. Create a new collectionto Upload Document
A. To start the data upload process, you will be asked to create a new _collection_.

B. Provide a _collection name_ and select the language to use

C. Upload the files to be used as simply as _drag and drop files_

D. Click Finish

<img width="172" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/943966d4-a5bf-44b3-aa02-23d179a8da8b">

E. Apart from _uploading files via local_ there are several options for _uploading files_. Click _here_ on _Need to connect to data source_. Apart from that, there are several other _data preprocessing_ options such as OCR and Stemming

<img width="184" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/0bb7d185-8091-4e98-af0a-0a85d94c0e5e">

<img width="275" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/e4307f7e-ae11-4367-99e6-8e72b3f605b5">

### 5. Click on Improve and customize
If you select the _conversation search_ option as the _project type_, Watson Discovery will provide an internal chatbot to conduct questions and answers from documents.

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/5b393765-8e71-4570-ac45-3e90219e7af5">

_Notes:_

_Improvement tools_: These tools can be used to improve the results of Watson Discovery. Open the link[berikut](https://cloud.ibm.com/docs/discovery-data?topic=discovery-data-improvements) to learn more.

### 6. Manage collections

If you move to the navigation menu. You can select manage collection_ to see a list of _collections_ that have previously been created.

<img width="123" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/908fa328-cd33-4f08-b065-91a32bb05332">
<img width="401" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/f446b996-3267-42bf-aa3e-ba1f5245fdef">

Click _preview data_ then you can see the uploaded document

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/c2f9ff71-732c-4e17-8a36-faef8d12b278">

### 7. Add More Collection

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/b209a233-16c7-4f0c-93d0-74b1d4441786">

You can use the following document to upload, follow the same process as before.

## Additional Feature of watson Discovery
### OCR 

Apart from being able to retrieve information from PDF or Docx files, Watson Discovery also has the capability to upload text files in the form of images and can be OCRed directly.
#### 1. Buat Collection Baru dan Upload Document Anda

Make sure to turn on the OCR feature when you upload your document

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/1901d1ea-46a3-4259-bd4d-bdebabb0a1e4">

#### 2. Klik Finisih lalu pergi ke Manage and Collection

Wait until Document Processing is complete.

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/0168ade6-4be0-47f9-8be3-0b8e55077a89">

Click Preview data according to the name of the project that has been created, and you can see the results. You will see that the result has become text that you can preprocess further.
<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/ca8aa53b-0e93-40e7-b65f-f4d8b63237ef">

### Webcrawling

One of the other features that Watson Discovery has is crawling data from certain websites.
#### 1. Buat Collection baru

Fill in your collection name, then click "Need to connect to a data source? Click here."

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/74fc041b-8568-4fa9-8006-5df848a08e1a">

#### 2. Pilih Web Crawl

There are several options provided by Watson Discovery, for now we will use the webcrawl option.

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/1b8237e3-3bab-4f91-978d-a319cac34a5a">

#### 3. Fill in the information needed

You need to specify the crawling intensity and the website that you will use as the crawling source

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/1b462097-1f59-4771-bc13-81bac0fdf354">

Apart from that, you can crawl more than one website

<img width="467" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/e246ce0e-59c2-4272-bacd-82659dea0986">

Finally, click Finish and wait for the process to complete.

### Smart Document Understanding

In the process of understanding a document, sometimes on each page there will be several fields, such as header, sub header, text, and page. But when we try to read the document directly from the PDF, we cannot extract the information. By using SDU we can define fields on several pages which will then automatically be reflected on all existing pages.


<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/954408ec-417a-4c4c-91fc-c0efea0bf3bb">

Pilih use your trained model

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/bcd02238-a861-4878-81c8-bcdd9516ae76">

<img width="1728" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2/assets/105551267/e6179a80-3d54-438f-88dd-775ed563fe49">

Then you can see the following display, select the labels field which is on the rightmost toggle. Select a specific field then mark the field in your document, click submit page. Repeat this process on several file sheets. Then at the end you will see that all pages have been identified.




























