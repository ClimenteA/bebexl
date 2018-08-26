# bebexl
read(xls, xlsx) - write(xls) in the shape of a dictionary like pandas df.to_dict("list")
<br/>
<br/>
Use case:
<br/>
```
from bebexl import read_excel, write_excel
```

Get from xls and xlsx file a dictionary 

```
table_dict = read_excel(path_to_workbook, sheetName=None, sheetIndex=0, showInfo=False)

#table_dict looks like: {Col1: [cell1, cell1 ..], Col2:[cell1, cell2...etc]}

```

<br/>

```
#Do the work you need to do, but make sure you keep the same row length for each list in the dict.
```
<br/>
Write the dictionary which looks like pandas df.to_dict('list') to a xls file.

```
write_excel(table_dict, excelName, sheetName="Sheet1")
```

<br/>
Uses xlrd, xlwt modules to do that. 
<br/>

