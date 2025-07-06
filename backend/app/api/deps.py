from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.security import SECRET_KEY, ALGORITHM
from app.schemas.user import TokenData, RoleEnum

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return TokenData(email=email, role=RoleEnum(role))
    except JWTError:
        raise HTTPException(status_code=401, detail="Token decode error")

def require_role(required_role: RoleEnum):
    def role_checker(current_user: TokenData = Depends(get_current_user)):
        if current_user.role not in [required_role, RoleEnum.ADMIN]:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return current_user
    return role_checker
