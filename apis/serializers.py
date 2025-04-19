from rest_framework import serializers
from TFFBullets.models import Tff5BulletEmails, TffBullets

class TFFBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = TffBullets
        fields = ['bullet_id', 'bullet_heading', 'bullet_content', 'searchable_bullet_content']
        extra_kwargs = {
            'bullet_id' : {'source': 'id'}, 
        }

class TFFEmailSerializer(serializers.ModelSerializer):
    bullets = TFFBulletSerializer(source = 'tffbullets_set', many = True)
    email_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Tff5BulletEmails
        fields = ['email_id', 'email_date', 'email_title', 'bullets']
        extra_kwargs = {
            'email_id' : {'source': 'id'},
        }