from django.contrib.auth.models import User
from django.db.models import Q


class EmailAuth:
    """use email and password match to authenticate user"""

    def authenticate(self, username=None, password=None):
        """
        get user from email and verify password
        """

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user

            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Django auth system retrieves user instance
        """
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user

            return None
        except User.DoesNotExist:
            return None
