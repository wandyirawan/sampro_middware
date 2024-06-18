from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Broadcast(Base):
    __tablename__ = 'Broadcast'
    BroadcastID = Column(Integer, primary_key=True)
    MobileNo = Column(String(50))
    MessageType = Column(String(50))
    Message = Column(String(1000))
    CategoryID = Column(Integer)
    SendNow = Column(String(1))
    TxReference = Column(String(50))
    ReceiverName = Column(String(200))
    VA_No = Column(String(20))
    MarketingName = Column(String(200))
    OS_Premium = Column(Numeric)
    ConfirmDate = Column(DateTime)
    DueDate = Column(DateTime)
    BroadcastDate = Column(DateTime)
    AsOfDate = Column(DateTime)
    DateOfBirthday = Column(DateTime)
    InsuredNameQQ = Column(String(255))  # Specify length here
    InsuredName = Column(String(255))    # Specify length here if needed
    LineOfBusiness = Column(String(30))
    ObjectOfInsured = Column(String(200))
    ExpiryDate = Column(DateTime)
    PolicyNo = Column(String(50))
    PackageName = Column(String(255))    # Specify length here
    ProductTypePlan = Column(String(255)) # Specify length here
    Destination = Column(String(255))     # Specify length here
    GrossPremium = Column(Numeric)
    EffectiveDate = Column(DateTime)
    PeriodPolicy = Column(String(50))
    Coverage = Column(String(200))
    AdditionalCoverage = Column(String(200))
    AdditionalCoverage2 = Column(String(200))
    AdditionalCoverage3 = Column(String(200))
    AdditionalCoverage4 = Column(String(200))
    AdditionalCoverage5 = Column(String(200))
    TemplateName = Column(String(100))
    NameSpace = Column(String(100))
    T = Column(DateTime)

