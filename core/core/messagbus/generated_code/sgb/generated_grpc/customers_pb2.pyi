from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CustomerRetrieveRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CustomerUserRetrieveRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class CustomerCreateRequest(_message.Message):
    __slots__ = ["user_id", "name", "email"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    name: str
    email: str
    def __init__(self, user_id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class CustomerData(_message.Message):
    __slots__ = ["user_id", "name", "id", "email"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    name: str
    id: int
    email: str
    def __init__(self, user_id: _Optional[int] = ..., name: _Optional[str] = ..., id: _Optional[int] = ..., email: _Optional[str] = ...) -> None: ...
