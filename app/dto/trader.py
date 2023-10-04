from pydantic import BaseModel, Field, field_validator, validator, NonNegativeFloat, NonNegativeInt
import re


class Person(BaseModel):
    name: str

    @field_validator('name', mode='before')
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not bool(re.match("^[A-Za-z/s]*$", value)):
            raise ValueError('name must contain spaces and letters only')
        return value


class Trader(Person):
    transaction_type: str
    asset_type: str
    asset_value: NonNegativeFloat
    quantity: NonNegativeInt

    @field_validator('transaction_type', mode='before')
    @classmethod
    def validate_transaction_type(cls, value: str) -> str:
        if value not in ['buy', 'sell']:
            raise ValueError('transaction_type should be buy or sell')
        return value
