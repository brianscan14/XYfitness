from django.contrib.auth.models import User


class EmailAuth:
    """Authenticates user by matching email and password"""

    def authenticate(self, username=None, password=None):
        """Get user from email and verify their password."""

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user

            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Django auth system retrieves user instance"""
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user

            return None
        except User.DoesNotExist:
            return None
