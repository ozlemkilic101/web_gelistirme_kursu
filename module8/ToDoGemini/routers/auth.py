from fastapi import APIRouter,Depends,HTTPException,status
from pydantic import BaseModel
from models import User
from passlib.context import CryptContext
from typing import Annotated
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError
from datetime import timedelta,datetime,timezone


router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
bcrypt_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_bearer=OAuth2PasswordBearer(tokenUrl="auth/token")

SECRET_KEY = "sfdb342lknlr224km44nr442345dsfgd8v5b42kf8vb653n"#ŞİMDİLİK RANDOM OLARAK BELİRLENDİ
ALGORITHM= "HS256"


def get_db():
    db=SessionLocal()
    try:
        yield db  # yield return gibidir. teknik farkı yield kullanılan fonksiyonlar generatordur. Birden fazla şey döndürür.
    finally:
        db.close()

db_dependency=Annotated[Session , Depends(get_db)]

class CreateUserRequest(BaseModel):
    username:str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str
    phone_number:str

class Token(BaseModel):
    access_token:str
    token_type:str


@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,create_user_request:CreateUserRequest):
    user=User(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        is_active=True,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        phone_number=create_user_request.phone_number

    )
    db.add(user)
    db.commit()

def create_access_token(username:str ,user_id:int,role:str,expires_delta:timedelta):
    payload={'sub':username , 'id':user_id,'role':role}
    expires=datetime.now(timezone.utc)+expires_delta
    payload.update({'exp':expires})
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    
async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get('sub')
        user_id=payload.get('id')
        user_role=payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Username or ID is invalid")
        return{'username':username,'id':user_id,'user_role':user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token is invalid")



def authenticate_user(username:str,password:str,db):
    user=db.query(User).filter(User.username==username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user


@router.post("/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dependency):
    user=authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect Username or password")
    token=create_access_token(user.username,user.id,user.role,timedelta(minutes=60))
    return {"access_token":token,"token_type":"bearer"}



@router.get("/get_user")
async def get_user():
    return "Hello World!"