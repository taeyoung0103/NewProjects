class EDTO:
    def __init__(self, neworderid, newcustomerid, newstatus, newsalesmanid, neworderdate):
        self.ORDER_ID = neworderid
        self.CUSTOMER_ID = newcustomerid
        self.STATUS = newstatus
        self.SALESMAN_ID = newsalesmanid
        self.ORDER_DATE = neworderdate

    def getorder_id(self):
        return self.ORDER_ID
    
    def setorder_id(self, neworderid):
        self.ORDER_ID = neworderid

    def getcustomer_id(self):
        return self.CUSTOMER_ID
    
    def setcustomer_id(self, newcustomerid):
        self.CUSTOMER_ID = newcustomerid

    def getstatus(self):
        return self.STATUS
    
    def setstatus(self, newstatus):
        self.STATUS = newstatus
    
    def getsalesman_id(self):
        return self.SALESMAN_ID
    
    def setsalesman_id(self, newsalesmanid):
        self.SALESMAN_ID = newsalesmanid

    def getorder_date(self):
        return self.ORDER_DATE
    
    def setorder_date(self, neworderdate):
        self.ORDER_DATE = neworderdate

    def __str__(self):
        return '주문번호 : ' + self.ORDER_ID + '- 고객번호 : ' + self.CUSTOMER_ID + '- 배송상태 : ' + self.STATUS + '- 주문날짜 : ' + self.ORDER_DATE

