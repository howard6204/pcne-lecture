# PCNE-DRP 概論 — 課程網站

## 目錄結構

```
pcne-web/
├── index.html          # 課程首頁（Email 領取講義）
├── slides.html         # Reveal.js 互動簡報
├── pcne-slides.md      # 投影片內容（Reveal.js Markdown 格式）
├── handout.pdf         # 講義 PDF（自動生成，不要手動編輯）
├── assets/
│   └── avatar.jpg      # 大頭照
└── .github/workflows/
    └── deploy.yml      # 自動部署到 Cloudflare Pages
```

## 更新投影片內容

1. 修改 `PCNE-DRP概論簡報.md`（上層目錄）
2. 執行轉換：
   ```
   uv run python convert_marp.py
   ```
3. git push → 自動部署

## 上線前設定清單

- [ ] 在 `index.html` 第 135 行替換 `WEBHOOK_URL` 為 Make.com webhook 網址
- [ ] 在 GitHub repo → Settings → Secrets 新增：
  - `CLOUDFLARE_API_TOKEN`（Cloudflare API Token，需要 Pages Edit 權限）
  - `CLOUDFLARE_ACCOUNT_ID`（`9c174c7ba80c1fc80d4c22c9f829c9d7`）
- [ ] 在 Cloudflare Pages 建立專案名稱 `pcne-lecture`

## 畫圖快捷鍵（演講時）

| 按鍵 | 功能 |
|---|---|
| `C` | 在投影片上畫筆 |
| `B` | 切換黑板模式 |
| `Del` | 清除筆跡 |
| `S` | 演講者備忘稿視窗 |
| `→` / `←` | 換頁 |
| `F` | 全螢幕 |
