from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, ListView
from store_account.forms import EditProfileForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView

from store_favorite.models import FavoriteRelation


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'store_account/user_account/profile.html'
    extra_context = {
        'title': 'پروفایل من',
    }


class EditProfile(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('store_account:edit_profile')
    form_class = EditProfileForm
    template_name = 'store_account/user_account/edit_profile.html'
    extra_context = {
        'title': 'ویرایش پروفایل',
    }

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "پروفایل شما با موفقیت ویرایش شد", 'success')
        return super().form_valid(form)


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'store_account/user_account/change_password.html'
    success_url = reverse_lazy('store_main:home')

    extra_context = {
        'title': 'تغییر رمز عبور',
    }

    def form_valid(self, form):
        logout(self.request)
        messages.success(self.request, 'رمز عبور شما با موفقیت تغییر کرد', 'success')
        return super(ChangePassword, self).form_valid(form)


class UserResetPassword(PasswordResetView):
    template_name = 'store_account/reset_password/password_reset_form.html'
    success_url = reverse_lazy('store_main:home')
    email_template_name = 'store_account/reset_password/email_send_user.html'

    def form_valid(self, form):
        messages.success(self.request, 'ایمیل بازیابی برای شما ارسال  شد', 'success')
        return super(UserResetPassword, self).form_valid(form)


class UserChangeResetPassword(PasswordResetConfirmView):
    template_name = 'store_account/reset_password/password_reset_change.html'
    success_url = reverse_lazy('store_main:home')

    def form_valid(self, form):
        messages.success(self.request, 'رمز عبور شما با موفقیت تغییر کرد', 'success')
        return super(UserChangeResetPassword, self).form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'رمز عبور شما یکی از شرایط چهار گانه را ندارد', 'error')
        return super(UserChangeResetPassword, self).form_invalid(form)


class FavoriteProductList(ListView):
    template_name = 'store_account/user_account/favorite_product.html'
    paginate_by = 6

    def get_queryset(self):
        return FavoriteRelation.objects.filter(user=self.request.user)

    extra_context = {
        'title': 'محصولات مورد علاقه'
    }
