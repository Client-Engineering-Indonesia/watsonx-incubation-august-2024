## Classification and Entity Extraction Financial use cases
In this demonstration, your objective is to effectively get **Classification and Entity Extraction Financial** based on the information from the passage text based on your specific requirements. Feel free to use zero-shot, one-shot, or few-shot learning, and adjust your model parameter and instruction of the prompt.

***

### Description:
Your task is to classify and extract the information based on the Financial Metrics Earnings Reports

**Instruction:** 


Berdasarkan laporan pendapatan tahunan atau quarterly perusahaan yang diperdagangkan secara publik, identifikasi dan ekstrak metrik keuangan berikut, beserta periode yang sesuai dan angka pembanding (jika tersedia):
1. Revenue
2. Net Income
3. Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA)
4. Cash Flow
Pastikan untuk menyertakan periode pelaporan (misalnya, Q1 2023 atau FY 2022) dan angka pembanding apa pun dari periode sebelumnya yang disebutkan di samping metrik. Juga, berikan sumber atau nomor halaman dari laporan tempat setiap metrik ditemukan.


**Example:** 


Input:
Acme Corp melaporkan pendapatan bersih sebesar $45,2 juta untuk kuartal keempat tahun 2022, naik dari $40,1 juta pada kuartal yang sama tahun sebelumnya. Laba bersih mencapai $5,3 juta, meningkat dari $4,8 juta pada Q4 2021.

Output:
- Revenue: $45.2 juta (Q4 2022), $40.1 juta (Q4 2021)
- Net Income: $5.3 juta (Q4 2022), $4.8 juta (Q4 2021)

Input:
Untuk tahun fiskal 2022, Beta Inc. memiliki laba bersih sebesar $150 juta, dan EBITDA sebesar $200 juta. Cash flow dari operasi dilaporkan sebesar $180 juta.


Output:
```
- Net Income: $150 juta (FY 2022)
- EBITDA: $200 juta (FY 2022)
- Cash Flow: $180 juta (FY 2022)
```

**Exercise:** 


Input: Gamma Industries mengumumkan pendapatan sebesar $75 juta untuk kuartal pertama tahun 2023, dengan laba bersih sebesar $10 juta. EBITDA untuk periode tersebut dilaporkan sebesar $15 juta, sedangkan arus kas dari operasi sebesar $20 juta.


Output: ???


Input: PT. XYZ mengumumkan pendapatan sebesar Rp500 miliar untuk kuartal pertama tahun 2023, dengan laba bersih sebesar Rp50 miliar. EBITDA untuk periode tersebut dilaporkan sebesar Rp75 miliar, sedangkan arus kas dari operasi sebesar Rp100 miliar.


Output: ???
