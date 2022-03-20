#!/usr/bin/env python
# -*- coding: utf-8 -*-
from myimports import *
from connect import *
from all_download_rev import Execute_All
#from fr_download_rev import Execute_FR
#from de_download_rev import Execute_DE
#from es_download_rev import Execute_ES
#from it_download_rev import Execute_IT
#from in_download_rev import Execute_IND
#from com_download_rev import Execute_COM

#db connection
df = Connect()

id_req = df['ID']
asin = df['ASIN']
email = df['EMAIL']
date = df['DATE']
uk = df['UK']
de = df['DE']
it = df['IT']
ind = df['IND']
fr = df['FR']
es = df['ES']
com = df['COM']
format = df['FORMAT']

asinlist = asin.tolist()
id_req_list = id_req.tolist()


def SelectExecutable():
    for id in id_req_list:
        try:
            index_id = id_req_list.index(id)
            uk_id = uk[index_id]
            fr_id = fr[index_id]
            de_id = de[index_id]
            it_id = it[index_id]
            ind_id = ind[index_id]
            es_id = es[index_id]
            com_id = com[index_id]
            #print ([uk_id,fr_id,de_id,es_id,it_id,com_id])
            if [uk_id, fr_id, de_id, es_id, it_id, ind_id, com_id] != ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']:
                Update_main(id)
            #print ([uk_id,fr_id,de_id,es_id,it_id,com_id])

            if uk_id == 'Y':
                try:
                    Execute_All(id,'UK')
                except Exception as e:
                    print(str(id) + ' for the country UK was skipped due to an error')
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            if fr_id == 'Y':
                try:
                    Execute_All(id,'FR')
                except Exception as e:
                    print(str(id) + ' for the country FR was skipped due to an error')
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            if de_id == 'Y':
                try:
                    Execute_All(id,'DE')
                except Exception as e:
                    print(str(id) + ' for the country DE was skipped due to an error')
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            if es_id == 'Y':
                try:
                    Execute_All(id,'ES')
                except Exception as e:
                    print(str(id) + ' for the country ES was skipped due to an error')
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            if it_id == 'Y':
                try:
                    Execute_All(id,'IT')
                except Exception as e:
                    print(str(id) + ' for the country IT was skipped due to an error')
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            if ind_id == 'Y':
                try:
                    Execute_All(id,'IND')
                except Exception as e:
                    print(str(id) + ' for the country IND was skipped due to an error')
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            if com_id == 'Y':
                try:
                    Execute_All(id,'COM')
                except Exception as e:
                    print(str(id) + ' for the country COM was skipped due to an error')
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            sleep(5)


        except:
            print(str(id) + ' was skipped due to an error')
            raise

def Execute_main():
    SelectExecutable()

if __name__ == '__main__':
    Execute_main()
