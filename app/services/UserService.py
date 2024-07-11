from app.models.UserModel import User

class UserService():
    def __init__(self, db) -> None:
        self.db = db
    
        
    """
    This function retrieves a user from the database based on the provided user_id, which can be the
    user's email, username, or mobile number.
    
    :param user_id: The `get_user` function you provided takes a `user_id` as input and queries the
    database to find a user based on the provided `user_id`. The function searches for a user with a
    matching `user_email`, `user_name`, or `mobile_no` in the database
    :return: The `get_user` function is returning the user object that matches the provided
    `user_id`. The function queries the database for a user where the user_email, user_name, or
    mobile_no matches the `user_id`, and then returns the first result found.
    """
    
    
    # Query to select specific columns from the User table
    # result = self.db.query(User.id, User.user_email, User.user_name, User.mobile_no).filter(

    # Inner join query between User and Address tables
    # (User, Address).join(Address, User.id == Address.user_id)

    # Left outer join query between User and Address tables
    # (User, Address).outerjoin(Address, User.id == Address.user_id)

    # Right outer join query between User and Address tables
    # (User, Address).outerjoin(User, User.id == Address.user_id, isouter=True)

    # Query to select all columns from the User table
    # this db table all column select
    
    def get_user(self, user_id):
        result = self.db.query(User).filter(
            (User.user_email == user_id) |
            (User.user_name == user_id) |
            (User.mobile_no == user_id)
        ).first()
        return result