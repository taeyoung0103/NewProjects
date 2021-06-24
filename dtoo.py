class EODTO:
    def __init__(self, newproductid, newproductname, newstandardcost, newlistprice, newcategoryid):
        self.PRODUCT_ID = newproductid
        self.PRODUCT_NAME = newproductname
        self.STANDARD_COST = newstandardcost
        self.LIST_PRICE = newlistprice
        self.CATEGORY_ID = newcategoryid

    def getproduct_id(self):
        return self.PRODUCT_ID
    
    def setproduct_id(self, newproductid):
        self.PRODUCT_ID = newproductid

    def getproduct_name(self):
        return self.PRODUCT_NAME
    
    def setproduct_name(self, newproductname):
        self.PRODUCT_NAME = newproductname

    def getstandard_cost(self):
        return self.STANDARD_COST
    
    def setstandard_cost(self, newstandardcost):
        self.STANDARD_COST = newstandardcost
    
    def getlist_price(self):
        return self.LIST_PRICE
    
    def setlist_price(self, newlistprice):
        self.LIST_PRICE = newlistprice

    def getcategory_id(self):
        return self.CATEGORY_ID
    
    def setcategory_id(self, newcategoryid):
        self.CATEGORY_ID = newcategoryid

    def __str__(self):
        return f'상품번호 : {self.PRODUCT_ID},  상품이름 : {self.PRODUCT_NAME} ,  표준가격 : {self.STANDARD_COST}, 가격 :  {self.LIST_PRICE}'
