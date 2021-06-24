class EDTO:
    def __init__(self, neworderid, newcustomerid, newstatus, newsalesmanid, neworderdate):
        self.ORDER_ID = neworderid
        self.CUSTOMER_ID = newcustomerid
        self.STATUS = newstatus
        self.SALESMAN_ID = newsalesmanid
        self.ORDER_DATE = neworderdate

    def getEmpno(self):
        return self.ORDER_ID
    
    def setEmpno(self, neworderid):
        self.ORDER_ID = neworderid

    def getEname(self):
        return self.CUSTOMER_ID
    
    def setEname(self, newcustomerid):
        self.CUSTOMER_ID = newcustomerid

    def getSal(self):
        return self.STATUS
    
    def setSal(self, newstatus):
        self.STATUS = newstatus
    
    def getEname(self):
        return self.SALESMAN_ID
    
    def setEname(self, newsalesmanid):
        self.SALESMAN_ID = newsalesmanid

    def getSal(self):
        return self.ORDER_DATE
    
    def setSal(self, neworderdate):
        self.ORDER_DATE = neworderdate

    def __str__(self):
        return '주문번호 : ' + self.ORDER_ID + '- 고객번호 : ' + self.CUSTOMER_ID + '- 배송상태 : ' + self.STATUS + '- 주문날짜 : ' + self.ORDER_DATE

        