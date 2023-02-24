from rest_framework import serializers
from user_app.models import MemberShip


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = MemberShip
        fields = ['username', 'password',
                  'email', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):

        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'Error': 'password does not match'})

        if MemberShip.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'email': 'email already exist'})

        account = MemberShip(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            aproval=MemberShip.Register.NOTVERIFIED
        )
        account.password = password
        account.save()

        return account


class UserAprovalSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberShip
        fields = ['id', 'username', 'email', 'aproval']
