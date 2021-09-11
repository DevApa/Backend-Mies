from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from emprendedor.models import Entrepreneur
from tipo_actividad_economica.models import TypeActivityEconomic
from estudiante.models import Student


class UsuarioProfileManager(BaseUserManager):
    def create_user(self, email, names, password=None):
        if not email:
            raise ValueError('Usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            names=names,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, names, password):
        user = self.create_user(email, names, password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class Permission(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_permiso')
    title = models.CharField(max_length=45, db_column='titulo')
    description = models.CharField(max_length=45, db_column='descripcion')
    status = models.CharField(max_length=45, db_column='status')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tbl_permiso'


class Role(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_rol')
    name = models.CharField(max_length=45, db_column='nombre_rol')
    description = models.CharField(max_length=45, db_column='descripcion')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_rol'


class RolePermission(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    id_rol = models.ForeignKey(Role, blank=False, null=False, db_column='role_id', on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permission, blank=False, null=False, db_column='permission_id',
                                      on_delete=models.CASCADE)


    class Meta:
        db_table = 'tbl_rol_permiso'


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True, db_column='id_usuario')
    email = models.CharField(unique=True, max_length=45, blank=True, null=True, db_column='email')
    names = models.CharField(max_length=45, blank=True, null=True, db_column='full_name')
    identify = models.CharField(max_length=45, unique=True, db_column='no_identificacion')
    password = models.CharField(max_length=128, blank=True, null=True, db_column='password')
    status = models.CharField(default='A', max_length=1, blank=True, null=True, db_column='status')
    rol = models.ForeignKey(Role, on_delete=models.DO_NOTHING, db_column='id_rol')
    create_time = models.DateTimeField(blank=True, null=True, db_column='create_time')
    last_login = models.DateTimeField(blank=True, null=True, db_column='last_login')
    is_admin = models.BooleanField(default=False, null=True, blank=True)

    objects = UsuarioProfileManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['names']

    def get_short_name(self):
        return self.names

    def __str__(self):
        txt = '{0} con Email: {1}'
        return txt.format(self.names, self.email)

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'tbl_usuario'


class ActivityEconomic(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_actividad_economica')
    name = models.CharField(max_length=45, blank=True, null=True, unique=True, db_column='nombre')
    description = models.CharField(max_length=45, blank=True, null=True, db_column='descripcion')
    typeActEcon = models.ForeignKey(TypeActivityEconomic, on_delete=models.CASCADE, db_column='id_tipo_act_economica')
    status = models.CharField(max_length=2, blank=True, null=True, db_column='status')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_actividad_economica'


class Entrepreneurship(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_emprendimiento')
    latitude = models.CharField(max_length=45, blank=True, null=True, db_column='latitud')
    length = models.CharField(max_length=45, blank=True, null=True, db_column='longitud')
    code = models.CharField(max_length=45, blank=True, null=True, db_column='codigo')
    address = models.CharField(max_length=45, blank=True, null=True, db_column='direccion')
    status = models.CharField(max_length=2, blank=True, null=True, db_column='status')
    description = models.CharField(max_length=100, blank=True, null=True, db_column='descripcion')
    activity_eco = models.ForeignKey(ActivityEconomic, db_column='id_actividad_economica', on_delete=models.DO_NOTHING)
    entrepreneur = models.ForeignKey(Entrepreneur, db_column='id_emprendedor', on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, db_column='id_estudiante', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'tbl_emprendimiento'


class LogGeneral(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_log_general')
    event = models.DateTimeField(db_column='event_time')
    host = models.TextField(db_column='HOST', )
    mac = models.TextField(db_column='MAC', )
    end_time = models.DateTimeField(blank=True, null=True, db_column='end_time')
    user_data_base = models.CharField(max_length=45, blank=True, null=True, db_column='user_data_base')
    request = models.JSONField(blank=True, null=True, db_column='request')
    sql_text = models.TextField(blank=True, null=True, db_column='sql_text')
    response = models.JSONField(blank=True, null=True, db_column='response')
    user = models.ForeignKey(Usuario, blank=True, null=True, db_column='user', on_delete=models.DO_NOTHING)
    latitude = models.CharField(max_length=45, blank=True, null=True, db_column='latitud')
    length = models.CharField(max_length=45, blank=True, null=True, db_column='longitud')

    class Meta:
        db_table = 'tbl_log_general'


class Bond(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_bono')
    date_reception = models.DateField(blank=True, null=True, db_column='fecha_recepcion')
    value = models.FloatField(blank=True, null=True, db_column='valor')
    description = models.CharField(max_length=45, blank=True, null=True, db_column='descripcion')
    entrepreneur = models.ForeignKey(Entrepreneur, db_column='id_emprendedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_bono'


class MiesStorageValidated(models.Model):
    field_base_mies = models.IntegerField(db_column='#-Base-MIES', blank=True, null=True)
    identify = models.TextField(db_column='CEDULA', blank=True, null=True)
    names = models.TextField(db_column='APELLIDOS Y NOMBRES', blank=True, null=True)
    phone = models.TextField(db_column='TELEFONO', blank=True, null=True)
    email = models.TextField(db_column='Correos electronicos', blank=True, null=True)
    sector = models.TextField(db_column='SECTOR', blank=True, null=True)
    neighborhood = models.TextField(db_column='Barrio', blank=True, null=True)
    address = models.TextField(db_column='Domicilio', blank=True, null=True)
    type_act_econ = models.TextField(db_column='TipoActEcon', blank=True, null=True)
    economic_activity = models.TextField(db_column='ACTIVIDAD ECONOMICA', blank=True, null=True)
    is_active = models.TextField(db_column='Act-Activa', blank=True, null=True)
    bond_reception_date = models.TextField(db_column='FECHA de RECEPCION DE BONO', blank=True, null=True)
    observations_mies = models.TextField(db_column='OBSERVACIONES MIES', blank=True, null=True)
    observations_sociology = models.TextField(db_column='OBSERVACIONES SOCIOLOGIA', blank=True, null=True)
    student_sociology = models.TextField(db_column='Estudiante  Sociologia', blank=True, null=True)

    class Meta:
        db_table = 'stage_mies_validada'


class Observations(models.Model):
    id = models.AutoField(primary_key=True, db_column='idt_obs_mies')
    detail = models.CharField(max_length=45, blank=True, null=True, db_column='detalle')
    entrepreneurship = models.ForeignKey(Entrepreneurship, db_column='id_emprendimiento',
                                         on_delete=models.DO_NOTHING)
    type_observation = models.CharField(max_length=45, blank=True, null=True, db_column='tipo_observacion')

    def __str__(self):
        return self.detail

    class Meta:
        db_table = 'tbl_observaciones'


