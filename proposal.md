
# 1125025334 貢獻提案 

  

## 一、專案資訊（Project Information）

  

- **專案名稱**：**[ipinfo.tw](https://github.com/PeterDaveHello/ipinfo.tw)**

- **GitHub 網址**：https://github.com/PeterDaveHello/ipinfo.tw/tree/master

- **專案簡介**：
>A self-hosted, non-tracking, and ad-free solution to reveal client-side IP info like IP address, country, AS number/description, and additionally, user agent. 

  

## 二、貢獻類型（Type of Contribution）

  

- 其他(新增功能)

  

## 三、具體修改內容（Detailed Contribution Content）

  

- **新增檔案**：
新增一個檔案，此檔案類似api的功能，能夠輸入ip而return校名，裡面存了各個大學ip範圍以及對應的校名
  

- **具體修改內容說明**：
目前規劃是新增一個處理ip位址的檔案，與原本的呼叫並行，這個處理ip位址的檔案能夠把輸入查詢的字串，在內部進行比對後輸出該ip區段對應的網域。
假如傳入的ip是 `140.115.197.133`
回傳值
`{"ip":"140.115.197.133","country_code":"TW","country_name":"TAIWAN",university:National Central University}`

  

- **目前文件問題參考**：
 暫時沒有人提出，是我想出來的創意想法

  

## 四、規劃與進度安排（Planning & Schedule）

  

1. **前期準備**

- 將文件與程式讀得更熟
- 找到國內各大學的ip位置範圍
- 把docker學會

2. **撰寫程式**

- 會新增對應ip表與處理傳入ip的判斷程式

  

3. **測試功能是否正確**

- 測試 `140.115.197.133`為例，會顯示出中央大學，也輸入不同學校的ip位址，確定是回傳正確的學校


4. **發送 Pull Request**

- 提交Commit（暫定 `docs: add university searching tool`）

- 在 Pull Request 中說明本次貢獻的有趣功能。

  

## 五、風險評估與備援方案（Risk Assessment & Backup Plan）

  

- **可能遇到的問題**：

- 需要在原有檔案內加入一個新的檔案來面對新功能，可能整個架構會變動(一個是向原本的功能發出請求，另一個再向我新增的功能提出請求)

- 可能之後有些大學會倒閉，IP範圍會更動。

  

- **解決與備援方案**：

- 把文件讀熟，學會docker，並且謹慎地將兩個功能整合。

- 之後要定期更新學校與ip對應表。

  

## 六、動機與預期成效（Motivation & Expected Outcomes）

  

- **貢獻動機與原因**：

- 以前常常在網路上看到有人說自己考上112大學，後來才了解是用學校ip範圍來作為幽默的用途。想說如果之後看到別人的大學ip，可以放進這個工具來查詢，因此想要新增輸入ip問大學的功能(因為裡面也有輸入ip問國家的功能)

  

- **預期成效與收穫**：

  輸入了一間大學的ip，結果可收到回傳值為ip對應之學校。
-  **未來發展**：
在未來還可以新增更多不限大學的機構或單位