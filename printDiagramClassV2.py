#
# manageDiagram class provides methods to capture and print the diagram
#

class manageDiagram:

        def stubDiagram():
                diagramValues = [['01','10','19','28','37','46','55','64','73'],['02','11','20','29','38','47','56','65','74'],['03','12','21','30','39','48','57','66','75'],['04','13','22','31','40','49','58','67','76'],['05','14','23','32','41','50','59','68','77'],['06','15','24','33','42','51','60','69','78'],['07','16','25','34','43','52','61','70','79'],['08','17','26','35','44','53','62','71','80'],['09','18','27','36','45','54','63','72','81']]
                return diagramValues
        
        def captureDiagram():
                diagram='XYZ'
                for row in range(9):
                        for col in range(9):
                                #cellValue  = ((row)*9)+col+1 #-- default/stub value
                                print('debug1')
                                while True:
                                        print('(r'+str(row+1)+', c'+str(col+1)+') integer = ',end='')
                                        cellValue=input()
                                        print('debug2~'+cellValue)
                                        print(type(cellValue))
                                        if type(cellValue)=='int':
                                                print('debug3~'+cellValue)
                                                int(cellValue)
                                                print('debug4~'+cellValue)
                                                print(type(cellValue))
                                                cellValue+=100
                                                print('debug6~'+cellValue)
                                                break
                                if col == 0:
                                        diagramRow = [cellValue]
                                else:
                                        diagramRow.append(cellValue)
                                print('')
                        print(diagramRow)
                        if row == 0:
                                diagram = [diagramRow]
                        else:
                                diagram.append(diagramRow)
                print('')
                print('')
                return diagram
        
        def printDiagram(diagram):
                tab = '          '
                print('')
                print('')
                print(tab+'----------------------------------------------')
                for row in range(9):
                        print(tab+'|',end='')
                        for col in range(9):
                                print((str(diagram[col][row]).rjust(3)+' '),end='')
                                if col == 2 or col == 5 or col == 8:
                                        print('|',end='')
                                else:
                                        print(':',end='')
                        print('')
                        if row == 2 or row == 5 or row == 8:
                                print(tab+'----------------------------------------------')
                        else:
                                print(tab+'|....:....:....|....:....:....|....:....:....|')
                print('')
                print('')

diagramMatrix = manageDiagram.captureDiagram()
#diagramMatrix = manageDiagram.stubDiagram()
print(diagramMatrix)
manageDiagram.printDiagram(diagramMatrix)
# that's it folks!







