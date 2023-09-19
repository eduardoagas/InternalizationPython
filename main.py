import gettext
for lang in ['pt-br', 'en']:
    # set current language
    lang_translations = gettext.translation('base', localedir='locales', languages=[lang])
    lang_translations.install()
    # define _ shortcut for translations
    _ = lang_translations.gettext
    # mark a string translatable
    hw = _("Hello World")
    print(hw)
 