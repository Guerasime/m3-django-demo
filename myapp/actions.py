from m3_ext.ui.fields import ExtStringField, ExtCheckBox
from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.ui import ModelEditWindow, BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field_username = ExtStringField(
            label=u'Имя пользователя',
            name='username',
            allow_blank=False,
            anchor='100%'
        )

        self.field_password = ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=True,
            anchor='100%',
            input_type='password'
        )

        self.field_first_name = ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=True,
            anchor='100%'
        )

        self.field_last_name = ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=True,
            anchor='100%'
        )

        self.field_email = ExtStringField(
            label=u'Email',
            name='email',
            allow_blank=True,
            anchor='100%'
        )

        self.field_is_staff = ExtCheckBox(
            label=u'Пользователь',
            name='is_staff',
            anchor='100%'
        )

        self.field_is_superuser = ExtCheckBox(
            label=u'Суперпользователь',
            name='is_superuser',
            anchor='100%'
        )

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field_username,
            self.field_password,
            self.field_first_name,
            self.field_last_name,
            self.field_email,
            self.field_is_staff,
            self.field_is_superuser
        ))

        for field in self.form.items:
            if getattr(field, 'name', None) == 'password':
                field.input_type = 'password'
                field.allow_blank = True

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.title = u'Редактирование пользователя'

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

class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label='Name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = make_combo_box(
            label='Content Type',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=[(ct.id, ct.model) for ct in ContentType.objects.all()])

        self.field__codename = ext.ExtStringField(
            label='Codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'

class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_to_menu = True
    edit_window = add_window = PermissionAddWindow

class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    add_to_menu = True