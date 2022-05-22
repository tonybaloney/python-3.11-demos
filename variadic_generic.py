from typing import Generic, Tuple, TypeVar, TypeVarTuple

TPacket = TypeVar('TPacket')
TFields = TypeVarTuple('TFields')

class Packet(Generic[TPacket, *TFields]):
    def __init__(self, *fields: *TFields):
        ...

    @property
    def fields(self) -> Tuple[*TFields]:
        ...

    @property
    def data(self) -> TPacket:
        ...

packet: Packet[bytes, int, str] = Packet(56, "example")
size, name = packet.fields  # Tuple[int, str]
data = packet.data # bytes