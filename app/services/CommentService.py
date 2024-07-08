from app.models.models import Comment as CommentModel

class CommentService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_comments(self, company_id):
        result = self.db.query(CommentModel).all()
        return result