from datetime import date
def GetCurrentDate():
    today = date.today()
    print('It is:', today)
def main():
    GetCurrentDate()
main()
