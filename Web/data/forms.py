from wtforms import Form, StringField, IntegerField, validators


class myform(Form):
    search_key = StringField('Your Sentence',
                             validators=[validators.InputRequired()])
    # tweet_count = IntegerField('if_offensive',
    #                            validators=[validators.InputRequired()])