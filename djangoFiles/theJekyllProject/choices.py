from djchoices import DjangoChoices, ChoiceItem


class BlogTemplates(DjangoChoices):
    JEKYLL_NOW = ChoiceItem(0)
    STARTBOOTSTRAP = ChoiceItem(1)
