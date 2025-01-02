from marshmallow import Schema, fields, validate


class TaskSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True,
                      validate=validate.Length(min=1, max=255))
    description = fields.Str()
    deadline = fields.DateTime()
    date_added = fields.DateTime()
