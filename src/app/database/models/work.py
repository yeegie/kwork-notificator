from tortoise import Model, fields


class Work(Model):
    id = fields.IntField(pk=True)

    category = fields.IntField()

    status = fields.BooleanField()

    name = fields.TextField()
    description = fields.TextField()

    price = fields.IntField()
    possible_price = fields.IntField()

    kwork_count = fields.IntField()
    projects = fields.IntField()
    hired_precent = fields.IntField()

    max_days = fields.IntField()
    date_create = fields.DateField()
    date_expire = fields.DateField()

    language = fields.CharField(max_length=2)

    link = fields.TextField()  # https://kwork.ru/projects/ + ID + /view
