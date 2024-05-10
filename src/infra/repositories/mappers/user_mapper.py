from domain.entities.user import User
from domain.values.user_email import UserEmail
from domain.values.user_name import Username
from infra.models.user import DBUser


# TODO user friend
def db_user_to_user_entity(user: DBUser) -> User:
    entity_user = User(
        Username(user.username),
        user.hashed_password,
        UserEmail(user.email),
        id=user.id,
        created_at=user.created_at,
    )
    return entity_user


# TODO user friend
def entity_user_to_db_user(user: User) -> DBUser:
    db_user = DBUser(
        id=user.id,
        username=user.username.as_generic_type(),
        hashed_password=user.hashed_password,
        email=user.email.as_generic_type(),
    )
    return db_user
