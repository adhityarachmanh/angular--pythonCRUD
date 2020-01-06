            for sheet_num in range(sh.shtxlo, sh.shtxhi):
                sheet = book.sheet_by_index(sheet_num)
                row_lim = min(sh.rowxhi, sheet.nrows)
                col_lim = min(sh.colxhi, sheet.ncols)

                # Iterate over each column
                for row_num in range(sh.rowxlo, row_lim):
        
                # Iterate over each row
                    for col_num in range(sh.colxlo, col_lim):
                        col_type = sheet.cell_type(row_num, col_num)
            
                        if not col_type == xlrd.XL_CELL_EMPTY:
                            cval = sheet.cell_value(row_num, col_num)
                            data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
