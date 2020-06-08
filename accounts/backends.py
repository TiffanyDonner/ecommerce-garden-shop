from django.contrib.auth.models import User


class EmailAuth:
    """Verify the user with username and Passord"""
    def authenticate(self, username=None, password=None):
        """ Get the user  """
        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user

            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Retrieve an instance of the user or return none """
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user

            return None
        except User.DoesNotExist:
            return None
