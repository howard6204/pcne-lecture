// PCNE 講義領取 — Email 記錄腳本
// 試算表：https://docs.google.com/spreadsheets/d/1tlXm73C23HkS5sheYldhd8ZlQp56Z1UN9CWGu1dI1T8/edit
// 部署為 Web App：Execute as Me，Anyone can access

const SHEET_NAME = 'PCNE講義領取';

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(SHEET_NAME);

    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(['時間', 'Email', '課程']);
      sheet.getRange(1, 1, 1, 3).setFontWeight('bold');
    }

    sheet.appendRow([
      new Date(data.time || new Date()),
      data.email || '',
      data.course || '',
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: 'PCNE logger active' }))
    .setMimeType(ContentService.MimeType.JSON);
}
