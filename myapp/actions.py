from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.ui import ModelEditWindow
from .ui import UserAddWindow
from .controller import observer

class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    add_to_menu = True
    edit_window = add_window = UserAddWindow

class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_to_menu = True
    edit_window = add_window = ModelEditWindow.fabricate(model=Group)

class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_to_menu = True
    edit_window = add_window = ModelEditWindow.fabricate(model, model_register=observer)

class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    add_to_menu = True
    edit_window = add_window = ModelEditWindow.fabricate(model=ContentType)