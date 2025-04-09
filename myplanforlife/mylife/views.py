from django.shortcuts import render

# Create your views here.
class HomeView(TemplateView):
    template_name = 'mylife/home.html'
    extra_context = {'title': 'Home'}
class AboutView(TemplateView):
    template_name = 'mylife/about.html'
    extra_context = {'title': 'About'}


class MyPlanListView(ListView):
    model = MyPlan
    template_name = 'mylife/myplan_list.html'
    context_object_name = 'myplans'

class MyPlanDetailView(DetailView):
    model = MyPlan
    template_name = 'mylife/myplan_detail.html'

class MyPlanCreateView(LoginRequiredMixin, CreateView):
    model = MyPlan
    form_class = MyPlanForm
    template_name = 'mylife/myplan_form.html'
    success_url = reverse_lazy('profile_list')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Consider adding a success message before redirecting
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
        else:
            # Handling form errors
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class MealListView(ListView):
    model = Meal
    template_name = 'mylife/meal_list.html'
    context_object_name = 'meals'

class MealCreateView(CreateView):
    model = Meal
    meals = ['name']
    template_name = 'mylife/meal_form.html'
    success_url = reverse_lazy('meal_list')

class MealUpdateView(UpdateView):
    model = Meal
    meals = ['name']
    template_name = 'mylife/meal_form.html'
    success_url = reverse_lazy('meal_list')

class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'mylife/meal_confirm_delete.html'
    success_url = reverse_lazy('meal_list')