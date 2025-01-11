from marshmallow import (
    Schema, fields, validate, validates_schema,
    ValidationError
)


class UserSchema(Schema):
    """Schema for user input validation"""
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        validate=validate.Regexp(
            r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$',
            error="Password must be at least 6 characters long, "
            "include at least one digit, and one uppercase letter."
        )
    )

    new_password = fields.Str(
        validate=validate.Regexp(
            r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$',
            error="Password must be at least 6 characters long, "
            "include at least one digit, and one uppercase letter."
        )
    )

    @validates_schema
    def confirm_new_password(self, data, **kwargs):
        """Ensure new_password is different from password"""
        password = data.get('password')
        new_password = data.get('new_password')
        if new_password and new_password == password:
            raise ValidationError(
                'New password must be different from the old password.',
                field_name='new_password'
            )
