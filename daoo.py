import cx_Oracle
from dtoo import EODTO
import json
import collections   # 데이터를 어떤 구조로 관리할 것인가를 의미하는 자료구조를 지원하는 library.


class EODAO:

    def insertproduct(self, dtoo):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("insert into products values (:product_id, :product_name, :standard_cost, :list_price, :category_id)",
                        product_id=dtoo.getproduct_id(), product_name=dtoo.getproduct_name(), standard_cost=dtoo.getstandard_cost(), list_price=dtoo.getlist_price(), category_id=dtoo.getcategory_id())
            conn.commit()

            # cur.execute("insert into emp01 values (:empno, :ename, :sal)", \
            #     empno=dto.getEmpno(), ename=dto.getEname(), sal=dto.getSal())
            # print("------------")
            # conn.commit()

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

    def updateProduct(self, dtoo):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        cur.execute("update products set product_name=:product_name, list_price=:list_price where product_id=:product_id",
                    product_id=dtoo.getproduct_id(), product_name=dtoo.getproduct_name(), list_price=dtoo.getlist_price())
        conn.commit()

        cur.close()
        conn.close()


    def deleteproduct(self, dtoo):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        cur.execute("delete from products where product_id =: product_id", product_id=dtoo.getproduct_id())
        conn.commit()

        cur.close()
        conn.close()


# if __name__ == "__main__":
#     dao = EODAO()
#     dto = EODTO(995, 'test', 2000.48, 3450.56, 3)
#     dao.insertproduct(dto)
