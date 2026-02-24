from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, username, email, password):
        if not phone:
            raise ValueError("Phone entry error")
        if not username:
            raise ValueError("Username entry error")
        if not email:
            raise ValueError("Email entry error")
        
        user = self.model(
            phone = phone,
            username = username,
        )
        if email:
            user.email = self.normalize_email(email),
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_adminuser(self, phone, username, email, password):
        user = self.create_user(phone, username, email, password)
        user.is_admin = True
        user.save(using = self._db)
        return user
    
    def create_superuser(self, phone, username, email, password):
        user = self.create_user(phone, username, email, password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using = self._db)
        return user
