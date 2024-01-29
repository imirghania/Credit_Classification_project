from pydantic import BaseModel, Field


class InferencePayload(BaseModel):
        Age: int
        Credit_Mix: str
        Payment_of_Min_Amount: bool
        Payment_Behaviour: str
        Annual_Income: float
        Monthly_Inhand_Salary: float
        Num_Bank_Accounts: int
        Num_Credit_Card: int
        Interest_Rate: float
        Num_of_Loan: int
        Delay_from_due_date: int
        Num_of_Delayed_Payment: int
        Changed_Credit_Limit: float
        Num_Credit_Inquiries: int
        Outstanding_Debt: float
        Credit_History_Age: int
        Amount_invested_monthly: float
        Monthly_Balance: float
        Mortgage_Loan: int
        Personal_Loan: int
        Credit_Builder_Loan: int = Field(alias='Credit-Builder_Loan')
        Debt_Consolidation_Loan: int
        Payday_Loan: int
        Auto_Loan: int
        Not_Specified_Loan: int
        Home_Equity_Loan: int
        Student_Loan: int