from wtforms import Form, StringField, validators

class phoneForm(Form):
    phone1 = StringField('Telefonun Kodu', [validators.DataRequired(), validators.Length(min=1, max=3)])
    phone2 = StringField('Telefonun Kodu', [validators.DataRequired(), validators.Length(min=1, max=3)])