import openpyxl, json, os

p = r'c:\Users\陈龙\.trae-cn\attachments\6a7d63d9eeb166e957782c40\c4138f80-c904-4ae0-9ebc-29620842dab7_3e47c6bb-fd85-4611-8172-d7a36663f0ba_数据转换提取配置.xlsx'
wb = openpyxl.load_workbook(p, data_only=True)
ws = wb.active
rows = []
for r in ws.iter_rows(values_only=True):
    rows.append([str(c).replace('\n',' ') if c is not None else '' for c in r])

out = r'd:\00 云上江西\03 赣政通\需求设计\态势感知\excel_rows.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
print('ok', len(rows))
