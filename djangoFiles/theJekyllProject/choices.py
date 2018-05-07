from djchoices import DjangoChoices, ChoiceItem


class BlogTemplates(DjangoChoices):
    TEMPLATE_NOT_SET = ChoiceItem('NS')
    JEKYLL_NOW = ChoiceItem('JN')
    STARTBOOTSTRAP = ChoiceItem('SB')
