from django.conf import settings


def matomo(request):
    ret = {
        'matomo_host': settings.MATOMO_HOST or None,
        'matomo_site_id': settings.MATOMO_SITE_ID or None,
    }
    print(ret)
    return ret
