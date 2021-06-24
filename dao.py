import cx_Oracle
from dto import EDTO

class EDAO:
    def empone(self, order_id):  
        
        data = ''
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from orders where order_id=:v", v=order_id) 
                row = cur.fetchone() 

                data = '{"customer_id":"' + str(row[1]) +'", "status":"' + row[2] + '","order_date":"' + str(row[4]) + '"}'

            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data

if __name__ == '__main__':

    print(EDAO().empone(5))