from app.schemas import SolicitudIn, ClasificacionOut

PALABRAS_URGENTES = ("caído", "caido", "no puedo", "urgente")


def clasificar_solicitud(solicitud: SolicitudIn) -> ClasificacionOut:
    mensaje = solicitud.mensaje.casefold()
    es_urgente = any(palabra in mensaje for palabra in PALABRAS_URGENTES)

    return ClasificacionOut(
        cliente=solicitud.cliente,
        categoria="incidente" if es_urgente else "consulta",
        prioridad="alta" if es_urgente else "normal",
        requiere_atencion=es_urgente,
        metodo="regla_determinista",
    )