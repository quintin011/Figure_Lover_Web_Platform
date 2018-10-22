{"filter":false,"title":"models.py","tooltip":"/Web/app/models.py","undoManager":{"mark":38,"position":38,"stack":[[{"start":{"row":12,"column":0},"end":{"row":57,"column":49},"action":"insert","lines":["mindate = datetime.date(datetime.MINYEAR, 1, 1)","","","class ContactGroup(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique = True, nullable=False)","","    def __repr__(self):","        return self.name","","","class Gender(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique = True, nullable=False)","","    def __repr__(self):","        return self.name","","","class UserExtended(Model, UserExtensionMixin):","    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)","    contact_group = relationship(\"ContactGroup\")","","","class Contact(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(150), unique = True, nullable=False)","    address = Column(String(564))","    birthday = Column(Date, nullable=True)","    personal_phone = Column(String(20))","    personal_celphone = Column(String(20))","    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=False)","    contact_group = relationship(\"ContactGroup\")","    gender_id = Column(Integer, ForeignKey('gender.id'), nullable=False)","    gender = relationship(\"Gender\")","","    def __repr__(self):","        return self.name","","    def month_year(self):","        date = self.birthday or mindate","        return datetime.datetime(date.year, date.month, 1) or mindate","","    def year(self):","        date = self.birthday or mindate","        return datetime.datetime(date.year, 1, 1)"],"id":2}],[{"start":{"row":3,"column":39},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":8,"column":61},"action":"insert","lines":["import datetime","from sqlalchemy import Column, Integer, String, ForeignKey, Date","from sqlalchemy.orm import relationship","from flask_appbuilder import Model","from flask_appbuilder.models.mixins import UserExtensionMixin"],"id":5}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":59},"action":"remove","lines":["from sqlalchemy import Column, Integer, String, ForeignKey "],"id":6},{"start":{"row":1,"column":78},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":15},"action":"remove","lines":["import datetime"],"id":7}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":15},"action":"insert","lines":["import datetime"],"id":9}],[{"start":{"row":3,"column":39},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":10}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":39},"action":"remove","lines":["from sqlalchemy.orm import relationship"],"id":11},{"start":{"row":4,"column":64},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":34},"action":"remove","lines":["from flask_appbuilder import Model"],"id":12},{"start":{"row":4,"column":64},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":43},"end":{"row":5,"column":61},"action":"remove","lines":["UserExtensionMixin"],"id":13}],[{"start":{"row":2,"column":78},"end":{"row":2,"column":79},"action":"insert","lines":[","],"id":15}],[{"start":{"row":2,"column":79},"end":{"row":2,"column":80},"action":"insert","lines":[" "],"id":16}],[{"start":{"row":2,"column":80},"end":{"row":2,"column":98},"action":"insert","lines":["UserExtensionMixin"],"id":17}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":43},"action":"remove","lines":["from flask_appbuilder.models.mixins import "],"id":18},{"start":{"row":4,"column":64},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":0},"end":{"row":59,"column":0},"action":"remove","lines":["mindate = datetime.date(datetime.MINYEAR, 1, 1)","","","class ContactGroup(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique = True, nullable=False)","","    def __repr__(self):","        return self.name","","","class Gender(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique = True, nullable=False)","","    def __repr__(self):","        return self.name","","","class UserExtended(Model, UserExtensionMixin):","    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)","    contact_group = relationship(\"ContactGroup\")","","","class Contact(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(150), unique = True, nullable=False)","    address = Column(String(564))","    birthday = Column(Date, nullable=True)","    personal_phone = Column(String(20))","    personal_celphone = Column(String(20))","    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=False)","    contact_group = relationship(\"ContactGroup\")","    gender_id = Column(Integer, ForeignKey('gender.id'), nullable=False)","    gender = relationship(\"Gender\")","","    def __repr__(self):","        return self.name","","    def month_year(self):","        date = self.birthday or mindate","        return datetime.datetime(date.year, date.month, 1) or mindate","","    def year(self):","        date = self.birthday or mindate","        return datetime.datetime(date.year, 1, 1)        ",""],"id":19},{"start":{"row":13,"column":0},"end":{"row":100,"column":49},"action":"insert","lines":["class ContactGroup(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique=True, nullable=False)","","    def extra_col(self):","        return \"EXTRA {0}\".format(self.id)","","    def extra_col2(self):","        return Markup(\"<h2>\" + self.name + \"</h2>\")","","","    def __repr__(self):","        return self.name","","","class ProductManufacturer(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique = True, nullable=False)","","    def __repr__(self):","        return self.name","","","class ProductModel(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique = True, nullable=False)","    product_manufacturer_id = Column(Integer, ForeignKey('product_manufacturer.id'), nullable=False)","    product_manufacturer = relationship(\"ProductManufacturer\")","","    def __repr__(self):","        return self.name","","","class Product(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique = True, nullable=False)","    product_manufacturer_id = Column(Integer, ForeignKey('product_manufacturer.id'), nullable=False)","    product_manufacturer = relationship(\"ProductManufacturer\")","    product_model_id = Column(Integer, ForeignKey('product_model.id'), nullable=False)","    product_model = relationship(\"ProductModel\")","","    def __repr__(self):","        return self.name","","","class Gender(Model):","    id = Column(Integer, primary_key=True)","    name = Column(String(50), unique = True, nullable=False)","","    def __repr__(self):","        return self.name","","","def test():","        return math.pi - 1.0","","","class FloatModel(Model):","    id = Column(Integer, primary_key=True)","    value = Column(Float, nullable = False, default=test)","","","    def __repr__(self):","        return self.value","","","class Contact(Model):","    id = Column(Integer, primary_key=True)","    name =  Column(String(150), unique = True, nullable=False)","    address = Column(String(564))","    birthday = Column(Date, nullable=True)","    personal_phone = Column(String(20))","    personal_celphone = Column(String(20))","    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=False)","    contact_group = relationship(\"ContactGroup\")","    gender_id = Column(Integer, ForeignKey('gender.id'), nullable=False)","    gender = relationship(\"Gender\")","","    def __repr__(self):","        return \"%s : %s\\n\" % (self.name, self.contact_group)","","    def month_year(self):","        date = self.birthday or mindate","        return datetime.datetime(date.year, date.month, 1) or mindate","","    def year(self):","        date = self.birthday or mindate","        return datetime.datetime(date.year, 1, 1)"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":20}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":15},"action":"remove","lines":["import datetime"],"id":21},{"start":{"row":1,"column":0},"end":{"row":2,"column":11},"action":"insert","lines":["import datetime","import math"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":24},"action":"insert","lines":["from flask import Markup"],"id":22}],[{"start":{"row":4,"column":98},"end":{"row":4,"column":99},"action":"insert","lines":[","],"id":23}],[{"start":{"row":4,"column":99},"end":{"row":4,"column":100},"action":"insert","lines":[" "],"id":24}],[{"start":{"row":4,"column":100},"end":{"row":4,"column":109},"action":"insert","lines":["BaseMixin"],"id":25}],[{"start":{"row":6,"column":64},"end":{"row":6,"column":65},"action":"insert","lines":[","],"id":26}],[{"start":{"row":6,"column":65},"end":{"row":6,"column":66},"action":"insert","lines":[" "],"id":27}],[{"start":{"row":6,"column":66},"end":{"row":6,"column":71},"action":"insert","lines":["Float"],"id":28}],[{"start":{"row":14,"column":3},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":29}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":47},"action":"insert","lines":["mindate = datetime.date(datetime.MINYEAR, 1, 1)"],"id":30}],[{"start":{"row":15,"column":47},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":31}],[{"start":{"row":82,"column":0},"end":{"row":82,"column":2},"action":"insert","lines":["\"\""],"id":32}],[{"start":{"row":82,"column":2},"end":{"row":82,"column":3},"action":"insert","lines":["\""],"id":33}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"insert","lines":["\"\""],"id":34}],[{"start":{"row":94,"column":2},"end":{"row":94,"column":3},"action":"insert","lines":["\""],"id":35}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":3},"action":"remove","lines":["\"\"\""],"id":36}],[{"start":{"row":104,"column":49},"end":{"row":105,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":105,"column":0},"end":{"row":105,"column":8},"action":"insert","lines":["        "]},{"start":{"row":105,"column":8},"end":{"row":105,"column":9},"action":"insert","lines":["\""]},{"start":{"row":105,"column":9},"end":{"row":105,"column":10},"action":"insert","lines":["\""]},{"start":{"row":105,"column":10},"end":{"row":105,"column":11},"action":"insert","lines":["\""]}],[{"start":{"row":105,"column":4},"end":{"row":105,"column":8},"action":"remove","lines":["    "],"id":38},{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":82,"column":0},"end":{"row":82,"column":3},"action":"remove","lines":["\"\"\""],"id":39}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":3},"action":"insert","lines":["\"\"\""],"id":40}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":3},"action":"remove","lines":["\"\"\""],"id":41}],[{"start":{"row":105,"column":2},"end":{"row":105,"column":3},"action":"remove","lines":["\""],"id":42},{"start":{"row":105,"column":1},"end":{"row":105,"column":2},"action":"remove","lines":["\""]},{"start":{"row":105,"column":0},"end":{"row":105,"column":1},"action":"remove","lines":["\""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":105,"column":0},"end":{"row":105,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1540244135069,"hash":"47b46f35892fceedf4018e61af48ce3ae12a71d0"}