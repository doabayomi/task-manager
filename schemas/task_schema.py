from marshmallow import Schema, fields, validate
from constants import (
    VALID_PRIORITIES, VALID_STATUSES,
    DEFAULT_PRIORITY, DEFAULT_STATUS
)


class TaskSchema(Schema):
    """Schema for tasks model"""
    id = fields.Int()
    name = fields.Str(required=True,
                      validate=validate.Length(min=1, max=255))
    description = fields.Str()

    status = fields.Str(validate=validate.OneOf(VALID_STATUSES),
                        load_default=DEFAULT_STATUS)
    priority = fields.Str(validate=validate.OneOf(VALID_PRIORITIES),
                          load_default=DEFAULT_PRIORITY)

    deadline = fields.DateTime()
    date_added = fields.DateTime()
    user_id = fields.Int(required=True)
