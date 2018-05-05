from djchoices import DjangoChoices, ChoiceItem


class BlogTemplates(DjangoChoices):
    TEMPLATE_NOT_SET = ChoiceItem(0)
    JEKYLL_NOW = ChoiceItem(1)
    STARTBOOTSTRAP = ChoiceItem(2)
