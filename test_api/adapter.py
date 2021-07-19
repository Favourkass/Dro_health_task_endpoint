from allauth.account.adapter import DefaultAccountAdapter

class RegisterUserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.email = data.get('email')
        user.last_period_date = data.get('last_period_date')
        user.cycle_average = data.get('cycle_average')
        user.period_average = data.get('period_average')
        user.start_date = data.get('start_date')
        user.end_date = data.get('end_date')
        
        user.save()
        return user