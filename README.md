# bebexl
read(xls, xlsx) - write(xls) in the shape of a dictionary like:<br/>
{Col1: [cell1, cell1 ..], Col2:[cell1, cell2...etc]} (which looks like pandas df.to_dict("list")) 
<br/>
Use case:
<br/>
```
import bebexl as xl
```

Get from xls and xlsx file a dictionary like: {Col1: [cell1, cell1 ..], Col2:[cell1, cell2...etc]}
```
table_dict = xl.read_excel(path_to_workbook, sheetName=None, sheetIndex=0)
```
<br/>
Do the work you need to do, but make sure you keep the same row length for each list in the dict.
<br/>
<br/>
Write the dictionary which looks like pandas df.to_dict('list') to a xls file.

```
xl.write_excel(table_dict, excelName, sheetName="Sheet1")
```

<br/>
Uses xlrd, xlwt modules to do that. 
<br/>
In development..
