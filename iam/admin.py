from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _


class CustomBackendLoginView(LoginView):
    extra_context = {'site_type': _('Identity Access Management'),
                     'helper_text': _('Please provide your credentials to proceed further'),
                     }

    # Add any additional customizations here

    pass
