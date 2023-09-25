from pydantic import BaseModel, field_validator, model_validator


class CreateUser(BaseModel):
    '''Checking custom validation with pydantic validation'''
    
    email: str
    password: str
    confirm_password: str

    @field_validator('email')
    def validate_email(cls, value):
        if 'admin' in value:
            raise ValueError('Email not valid')
        return value

    @model_validator(mode='after')
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self

CreateUser(email="xx@yy.com", password="123456", confirm_password="123456")