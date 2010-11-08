from django.conf import settings

FAMFAM_ROOT = getattr(settings, 'FAMFAM_ROOT', 'http://www.famfamfam.com/lab/icons/')

FAMFAM_SILK_ROOT = getattr(settings, 'FAMFAM_SILK_ROOT', '%ssilk/icons/' % FAMFAM_ROOT)

FAMFAM_MINI_ROOT = getattr(settings, 'FAMFAM_MINI_ROOT', '%smini/icons/' % FAMFAM_ROOT)

FAMFAM_FLAGS_ROOT = getattr(settings, 'FAMFAM_FLAGS_ROOT', '%sflags/icons/png/' % FAMFAM_ROOT)

FAMFAM_MINT_ROOT = getattr(settings, 'FAMFAM_MINT_ROOT', '%smint/icons/' % FAMFAM_ROOT)
