from sqlalchemy.orm import Session
from chat.models.entity import Projects

def getProjectCode(db: Session, projectCode: str):
    project = db.query(Projects).filter_by(projectCode = projectCode).first()
    return project