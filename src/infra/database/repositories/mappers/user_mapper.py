from domain.entities.user import User
from infra.database.persistence.models.user import DBUser

# TODO user friend
# def db_user_to_user_entity(user: DBUser) -> User:
#     entity_user = User(
#         Username(user.username),
#         user.hashed_password,
#         UserEmail(user.email),
#         id=user.id,
#         created_at=user.created_at,
#     )
#     return entity_user


def user_entity_to_db_user(user: User) -> DBUser:
    db_user = DBUser(
        id=user.id,
        username=user.username.as_generic_type(),
        hashed_password=user.hashed_password.as_generic_type(),
        email=user.email.as_generic_type(),
        created_at=user.created_at,
        friends=user.friends,
    )
    return db_user
