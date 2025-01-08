from companies.views.base import Base
from companies.utils.permissions import EmployeesPermission, GroupsPermission
from companies.models import Employee, Enterprise
from companies.serializers import EmployeeSerializer, EmployeesSerializer

from accounts.auth import Authentication
from accounts.models import User, UserGroups

from rest_framework.views import Response, status
from rest_framework.exceptions import APIException



