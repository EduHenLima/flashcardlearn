from pydantic import BaseModel


class CreateAssunto(BaseModel):
    idUsuario: int
    nomeCategoria: str
    descricao: str | None = None
    ativo: int
