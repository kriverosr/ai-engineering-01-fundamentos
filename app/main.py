import logging
from fastapi import FastAPI

from app.schemas import ClasificacionOut, SolicitudIn
from app.service import clasificar_solicitud


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Clasificador de solicitudes de soporte",
    version="1.0.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/clasificar", response_model=ClasificacionOut)
def clasificar(solicitud: SolicitudIn) -> ClasificacionOut:
    logger.info("Solicitud recibida desde el canal %s", solicitud.canal)
    return clasificar_solicitud(solicitud)