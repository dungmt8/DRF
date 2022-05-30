from rest_framework import permissions

from .premissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission
    ]
