from observer_practice.canal import CanalNoticias
from observer_practice.suscriptores import SuscriptorEmail, SuscriptorSMS


def main():
    canal = CanalNoticias("Noticias Unibague")
    suscriptor_email = SuscriptorEmail("Steven")
    suscriptor_sms = SuscriptorSMS("Betancur")

    canal.suscribir(suscriptor_email)
    canal.suscribir(suscriptor_sms)
    canal.publicar("Nueva clase sobre el patrón Observer")

    print(f"Canal: {canal.nombre}")
    print(f"Suscriptor 1: {suscriptor_email}")
    print(f"Mensajes recibidos por {suscriptor_email.nombre}: {suscriptor_email.mensajes}")
    print(f"Suscriptor 2: {suscriptor_sms}")
    print(f"Mensajes recibidos por {suscriptor_sms.nombre}: {suscriptor_sms.mensajes}")


if __name__ == "__main__":
    main()