## Building QnA with watxonx.ai, watsonx assistant, and DB2
This demo showcases how knowledge from databases (specifically DB2) can be utilized. The Q&A functionality works by translating text into SQL commands in DB2 and then presenting the output as text.

Overview:
watsonx.ai unleash the power of AI to convert human natural language into SQL statement without having technical knowledge about database. Helping management and other business users to get the data in more efficient way.

In this activity you will create 4 stages:
1. Create prompt template to convert human natural language into SQL query
2. Executing SQL query directly into DB2 database
3. Create prompt template to provide answer in more engaging way
4. Create watsonx assistant to orchestrate end-to-end process

### Prompt Template: Convert Human Natural Language into SQL Query

1. Create a new prompt template
2. Create a new prompt variable called user_question
3. Open file prompt-convert-query-to-SQL.txt, copy and paste into your new prompt template
4. Ensure you have put user_question variable in right place, or on 2nd line before end
5. Save your prompt template as your preferred name
6. Promote it into your deployment space
7. Go to your deployment space and deploy your prompt template
8. Wait until the process has done. You will get unique endpoint like https://us-south.ml.cloud.ibm.com/ml/v1/deployments/xxx-xxx-xxx-xxx-xxx/text/generation?version=2021-05-01 when the process is successful

### Function: Execute SQL Query

1. In your project, create a new jupyter notebook asset and use notebook deployment-execute-SQL-query.ipynb as base code
2. Set APIKEY and space_id with yours
3. You will get DB2 credentials from your mentor later during incubation
4. Try to experiment with the function to see how the data looks like
5. When you have run all cells, you will get new deployment space

### Prompt Template: Provide Engaging Answer

1. Create a new prompt template
2. Create 2 prompt variables called user_query and answer
3. Open file prompt-provide-engaging-answer.txt, copy and paste into your new prompt template
4. Ensure you have put user_query variable and answer variable in right place (you can check where the right place by checking in the file)
5. Save your prompt template as your preferred name
6. Promote it into your deployment space
7. Go to your deployment space and deploy your prompt template
8. Wait until the process has done. You will get unique endpoint like https://us-south.ml.cloud.ibm.com/ml/v1/deployments/xxx-xxx-xxx-xxx-xxx/text/generation?version=2021-05-01 when the process is successful

### watsonx Assistant: Orchestrate Gen AI Functions

1. Download file Q&A-to-Database-action.json and QA Database-custom-extension.json
2. Go to Actions from left pane
3. Click Global Settings icon
4. Go to Upload/Download tab
5. Select file Q&A-to-Database-action.json and click Upload button
6. Go to Integrations page from left pane
7. On Extensions section, click Build custom extension button
8. On Get started page, click Next button
9. Give the name "query-to-database-extension" on Extension name field. Then click Next button
10. On Import OpenAPI page, upload file QA Database-custom-extension.json
11. Click Finish button
12. Make sure you are still on Integrations page that you have followed on step 6
13. On Extension section, click Add button on "query-to-database-extension" that you have created on step 7-11
14. When there is popup window, click Add button
15. On Get started page, click Next button
16. On Authentication page, select "OAuth 2.0" on Authentication type field
17. Fill Apikey field with your unique API Key
18. Select "Send as Body" on Client authentication field
19. Click Finish button
20. Go to Actions page from left pane
21. Click Q&A Dokumen
22. Go to step named "Stage 1: Convert human prompt to SQL query". Follow instruction from your mentor to call funtion "convert human natural language into SQL query"
23. Go to step named "Stage 2: Execute SQL query to database". Follow instruction from your mentor to call funtion "execute SQL query"
24. Go to step named "Stage 3: Provide engaging answer". Follow instruction from your mentor to call funtion "provide engaging answer"
