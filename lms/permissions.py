from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().owner


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()
