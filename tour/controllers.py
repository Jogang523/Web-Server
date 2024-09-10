from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from dependencies import get_db, get_password_hash, verify_password 
from schemas import UserCreate, UserLogin,BoardCreate,BoardUpdate # 만들어놓은 함수 임포트
from models import User,Board,Coment # 만들어놓은 함수 임포트

templates = Jinja2Templates(directory="templates")
router = APIRouter()


# 회원 가입
@router.post("/signup")
async def signup(signup_data: UserCreate, db: Session = Depends(get_db)):
    # 먼저 username이 이미 존재하는지 확인
    existing_user = db.query(User).filter(User.username == signup_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 동일 사용자 이름이 가입되어 있습니다.")
    hashed_password = get_password_hash(signup_data.password)
    new_user = User(username=signup_data.username, country=signup_data.country, email=signup_data.email, hashed_password=hashed_password)
    db.add(new_user)
    
    try:
        db.commit()
    except Exception as e:
        print (e)
        raise HTTPException(status_code=500, detail="회원가입이 실패했습니다. 기입한 내용을 확인해보세요.")
    
    db.refresh(new_user)
    return {"message": "회원가입이 성공했습니다."}

# 로그인
@router.post("/login")
async def login(request: Request, signin_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == signin_data.username).first()
    if user and verify_password(signin_data.password, user.hashed_password):
        request.session["username"] = user.username
        return {"message":"로그인이 성공했습니다."}
    else:
        raise HTTPException(status_code=401, detail="로그인이 실패했습니다.")

# 로그아웃
@router.post("/logout")
async def logout(request: Request):
    request.session.pop("username", None)
    return {"message": "로그아웃이 성공했습니다."}

# 회원 탈퇴
@router.delete("/delete_account")
async def delete_account(request: Request, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # 해당 사용자가 작성한 모든 게시글 삭제
    db.query(Board).filter(Board.user_id == user.id).delete()

    db.delete(user)
    db.commit()

    #탈퇴 후 로그아웃
    request.session.pop("username", None)

    return {"message": "회원 탈퇴가 성공적으로 완료되었습니다."}

###################################################################################################################################################

# 게시판 작성
@router.post("/board")
async def create_board(request: Request, board: BoardCreate, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_board = Board(user_id=user.id, subject=board.subject, content=board.content)
    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    return new_board

#게시판 목록
@router.get("/board")
async def list_board(db: Session = Depends(get_db)):
    boards = db.query(Board).all()
    return [{"id": board.id, "title": board.subject, "content": board.content} for board in boards]

#게시글 수정
@router.put("/board/{board_id}")
async def update_board(request: Request, board_id: int, board: BoardUpdate, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")     
    db_board = db.query(Board).filter(Board.user_id == user.id, Board.id == board_id).first()
    if db_board is None:
        return ({"error": "ㅋㅋ 니 글 없음"})

    if board.subject is not None:
        db_board.subject = board.subject
    if board.content is not None:
        db_board.content = board.content
        
    db.commit()
    db.refresh(db_board)
    return db_board

#게시글 삭제
@router.delete("/board/{board_id}")
async def update_board(request: Request, board_id: int, board: BoardUpdate, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")     
    db_board = db.query(Board).filter(Board.user_id == user.id, Board.id == board_id).first()
    if db_board is None:
        return ({"error": "ㅋㅋ 니 글 없음"})

        
    db.delete(db_board)
    db.commit()
    return ({"message": "Memo deleted"})


