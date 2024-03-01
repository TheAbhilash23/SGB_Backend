from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserRetrieveRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class TokenVerificationRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class TokenVerificationResponse(_message.Message):
    __slots__ = ["is_valid_token"]
    IS_VALID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    is_valid_token: bool
    def __init__(self, is_valid_token: bool = ...) -> None: ...

class UserData(_message.Message):
    __slots__ = ["id", "username", "email"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    email: str
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
