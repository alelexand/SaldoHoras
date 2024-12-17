import win32com.client as win32


class Mudar:
    def __init__(self):
        print("ALTERANDO FORMATO DA PLANILHA")
        self.fname = fr'CaminhoArquivoObsoleto'
        self.Excel = win32.gencache.EnsureDispatch('Excel.Application')
        self.wb = self.Excel.Workbooks.Open(self.fname)

    def save(self):
        self.wb.SaveAs(self.fname+"x", FileFormat=51)
        self.wb.Close()
        self.Excel.Application.Quit()
