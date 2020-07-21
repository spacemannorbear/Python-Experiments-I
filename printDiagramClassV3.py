#
# manageDiagram class provides methods to capture and print the diagram
#

class manageDiagram:
        
        #
        # can assign a defult value to the sudoku diagram if capture diagram not used
        #
        def stubDiagram():
                diagramValues = [['01','10','19','28','37','46','55','64','73'],['02','11','20','29','38','47','56','65','74'],['03','12','21','30','39','48','57','66','75'],['04','13','22','31','40','49','58','67','76'],['05','14','23','32','41','50','59','68','77'],['06','15','24','33','42','51','60','69','78'],['07','16','25','34','43','52','61','70','79'],['08','17','26','35','44','53','62','71','80'],['09','18','27','36','45','54','63','72','81']]
                return diagramValues
        
        #
        # captures 81 values from user and stores in 2d array (actually list)
        #
        def captureDiagram():
                diagram=''
                #
                # loop through digram matrix one cell at a time
                #
                for row in range(9):
                        for col in range(9):
                                #
                                # get non-zero integer value 1-9 or null
                                #
                                while True:
                                        print('(r'+str(row+1)+', c'+str(col+1)+') integer = ',end='')
                                        cellValue=input()
                                        try:
                                                cellValue=int(cellValue)
                                        except ValueError:
                                                if cellValue!='':
                                                        continue
                                                else:
                                                        break
                                        if cellValue !=0:
                                                break
                                #
                                # format cell value to fixed length 2 with leading zero or else 2 spaces
                                #
                                cellValue=str(cellValue)
                                cellValue=cellValue.rjust(2,'0')
                                #
                                # build single row of the diagram
                                #
                                if cellValue=='00':
                                        cellValue='  '
                                if col == 0:
                                        diagramRow = [cellValue]
                                else:
                                        diagramRow.append(cellValue)
                                print('')
                        print(diagramRow)
                        #
                        # insert row into the diagram
                        if row == 0:
                                diagram = [diagramRow]
                        else:
                                diagram.append(diagramRow)
                print('')
                print('')
                return diagram # 81-cell diagram returned with all cells populated
        
        #
        # prints out populated sudoku diagram using ASCII characters
        #
        def printDiagram(diagram):
                tab = '          '
                print('')
                print('')
                #
                # print top line
                #
                print(tab+'----------------------------------------------')
                #
                # print one row at a time starting with left pipe
                #
                for row in range(9):
                        print(tab+'|',end='')
                        #
                        # print one column at a time
                        #
                        for col in range(9):
                                print((str(diagram[col][row]).rjust(3)+' '),end='')
                                #
                                # colons between columns but pipes every 3 columns
                                #
                                if col == 2 or col == 5 or col == 8:
                                        print('|',end='')
                                else:
                                        print(':',end='')
                        print('')
                        #
                        # line of dots under the row but line of dashes every 3 rows
                        #
                        if row == 2 or row == 5 or row == 8:
                                print(tab+'----------------------------------------------')
                        else:
                                print(tab+'|....:....:....|....:....:....|....:....:....|')
                print('')
                print('')

        #
        # updates row control array
        # each row contains

#
# capture then print calling sequence
#
diagramMatrix = manageDiagram.captureDiagram()
print(diagramMatrix)
manageDiagram.printDiagram(diagramMatrix)
# that's it folks!

