import os
import xlrd
import xlwt

#path_to_workbook = "xlsx_test.xlsx"


def get_book(path_to_workbook):
    """Get a xlrd book object"""
    endChars = path_to_workbook.split(".")[-1] 
    if os.path.isfile(path_to_workbook):
        if endChars in ["xlsx", "xls"]:
            wbook = xlrd.open_workbook(path_to_workbook, encoding_override="UTF-8")
            return wbook
        else:
            raise Exception("Expected a xls or xlsx file!")


def get_sheet(book, sheetName=None, sheetIndex=0):
    """Get xlrd sheet object"""
    if sheetName is not None:
        sheet = book.sheet_by_name(sheetName)
        return sheet
    else:
        sheet = book.sheet_by_index(sheetIndex)
        return sheet


def dictTable(sheet):
    """Get from the sheet a dict from the table found 
       that looks like df.to_dict('list') in pandas
    """
    
    rows = sheet.get_rows()
    shape = (sheet.nrows-1, sheet.ncols)

    #Prepare dict
    table_dict_raw = {}
    for irow, row in enumerate(rows):
        temp_dict = {}
        for icol in range(shape[1]):
            row_value = str(row[icol].value).strip()
            temp_dict[icol] = row_value

        table_dict_raw[irow] = temp_dict
    
    columns_dict = table_dict_raw[0]

    #Finalize dict to look like {columnName: [cell1, cell1 etc..]}
    tableDict = {}
    for i, colName in columns_dict.items():
        rowli = []
        for irow, valDict in table_dict_raw.items():
            if irow == 0: 
                continue #because row 0 is the header columns
            rowli.append(valDict[i])
        
        tableDict[colName] = rowli
    
    return tableDict, shape, list(columns_dict.values())


def read_excel(path_to_workbook, sheetName=None, sheetIndex=0):
    """Return from the excel a df.to_dict("list") dict like in pandas
       {"co1": [cell1, cell2, etc], "col2":[cell1, cell2, etc]}
    """
    
    book = get_book(path_to_workbook)
    sheet = get_sheet(book)
    
    table_dict, shape, columnNames = dictTable(sheet)
    
    table_dict["shape"] = shape
    table_dict["columns"] = columnNames
     
    return table_dict


#tb = read_excel(path_to_workbook, sheetName=None, sheetIndex=2)


def checkBeforeWrite(table_dict):
    """Check key:list dict if the list are of type list and of the same lentgh"""
    if not isinstance(table_dict, dict):
        raise Exception("Data must be of type dict!")
    
    lenli = []
    for kcol, vli in table_dict.items():
        if kcol.strip() in ["shape", "columns"]:
            continue
        if isinstance(vli, list):
            lenli.append(len(vli))
        else:
            raise Exception("Key value not of type list!")

    sample = lenli[0]
    for val_len in lenli:
        if val_len != sample:
            raise Exception("Lists in the 'key:list' table must be the same lentgh!")



def write_excel(table_dict, excelName, sheetName="Sheet1"):
    """Write to a xls file a dict with shape like (key:list):
    {Col11: [cell1, cell2..], Col2:[coll1, coll2..etc] 
    """
    
    checkBeforeWrite(table_dict)
    
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheetName)

    columns = list(tb_dict.keys())
    columns = [c for c in columns if c.strip() not in ["shape", "columns"]]

    for icol, col in enumerate(columns):
        writeColName = True
        for icell, cell in enumerate(tb_dict[col]):
            if writeColName:
                sheet.write(icell, icol, col)
                writeColName = False
            else:
                sheet.write(icell, icol, cell)

    book.save("{}.xls".format(excelName))


#write_excel(tb_dict, 'excelName', sheetName="Sheet1")
