from django.urls import path

from store_account.views import (
    Profile,
    EditProfile,
    ChangePassword,
    UserResetPassword,
    UserChangeResetPassword,
    FavoriteProductList
)

app_name = 'store_account'
urlpatterns = [
    path('profile', Profile.as_view(), name='profile'),
    path('edit-profile', EditProfile.as_view(), name='edit_profile'),
    path('change-password', ChangePassword.as_view(), name='change_password'),
    path('reset-password', UserResetPassword.as_view(), name='reset_password'),
    path('reset-password-change/<uidb64>/<token>', UserChangeResetPassword.as_view(), name='reset_password_change'),
    path('favorite-list', FavoriteProductList.as_view(), name='favorite_list'),
]
