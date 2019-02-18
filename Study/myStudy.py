# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2019/2/17
from configparser import ConfigParser
import xlrd,logging,sys,xlsxwriter

logging.basicConfig(level=logging.ERROR,
                    filename="access.log",
                    format='%(asctime)s-%(levelname)s::%(message)s')


def getconfig():
    config = ConfigParser()
    config.read("config.ini",encoding='utf-8')
    key = config.get("key","key")
    title = config.get("title","title")
    fromfile = config.get("fromfile","file")
    fromsheet = config.get("fromsheet","sheet")
    tofile = config.get("tofile","file")
    tosheet = config.get("tosheet","sheet")
    return key,title,fromfile,fromsheet,tofile,tosheet




def getalldatas():
    fromfile,fromsheet = getconfig()[2:4]
    try:
        rd = xlrd.open_workbook(fromfile)
    except:
        logging.error("this file (%s) is no exits"%fromfile)
        sys.exit(0)
    try:
        st = rd.sheet_by_name(fromsheet)
    except:
        logging.error("this sheet (%s) is no exits"%fromsheet)
        sys.exit(0)
    rows = st.nrows
    titles = st.row_values(0)
    datas = []
    for row in range(1,rows):
        values = st.row_values(row)
        datas.append(values)
    return titles,datas


def screendatas():
    key = getconfig()[0].split(";")
    title = getconfig()[1].split(";")
    titles = getalldatas()[0]
    datas = getalldatas()[1]
    key_index = []
    title_index = []
    for k in title:
        if k in titles:
            title_index.append(titles.index(k))
    for k in key:
        if k in titles:
            key_index.append(titles.index(k))


    todatas = {}
    for data in datas:
        k = tuple([data[i] for i in key_index])
        v = [data[i] for i in title_index]
        todatas.setdefault(k,[]).append(v)
    return todatas


def writedatas():
    title = getconfig()[1].split(";")
    tofile,tosheet = getconfig()[4:6]
    todatas = screendatas()

    ks = list(screendatas().keys())
    wk = xlsxwriter.Workbook(tofile)
    wt = wk.add_worksheet(tosheet)
    wt.write_row(0, 0, title)
    wt.write(0,len(title),"count")
    n = 1
    for i in ks:
        count = len(todatas.get(i))
        wt.write_row(n,0,todatas.get(i)[0])
        wt.write(n,len(todatas.get(i)[0]),count)
        n +=1
    wk.close()

writedatas()