from django.shortcuts import render, redirect

from django.views.generic import View

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from violations.forms import RoadViolationForm,SignUpForm,SignInForm

from violations.models import RoadViolation

class SignUpView(View):

    template_name="register.html"

    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            # form_instance.save()

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            return redirect("signin")
        
        return render(request,self.template_name,{"form":form_instance})

class SignInView(View):

    template_name="signin.html"

    form_class=SignInForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect('violation-list')
            
        return render(request,self.template_name,{"form":form_instance})


class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")
    

class ViolationCreateView(View):
    template_name = "post_violation.html"
    form_class = RoadViolationForm

    def get(self, request, *args, **kwargs):
        form_instance = self.form_class()
        return render(request, self.template_name, {"form": form_instance})

    def post(self, request, *args, **kwargs):
        form_data = request.POST
        form_instance = self.form_class(form_data, files=request.FILES)

        if form_instance.is_valid():
            violation = form_instance.save(commit=False)  
            violation.user = request.user  
            violation.save()  
            return redirect("violation-list")

        return render(request, self.template_name, {"form": form_instance})

class ViolationListView(View):

    template_name="violation_list.html"

    def get(self,request,*args,**kwargs):

        qs=RoadViolation.objects.all()

        return render(request,self.template_name,{"data":qs})

class ViolationDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        RoadViolation.objects.get(id=id).delete()
        return redirect("violation-list")

    
