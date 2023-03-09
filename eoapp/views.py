from django.shortcuts import render

def home(request):
	if request.GET.get("num"):
		try:
			num=int(request.GET.get("num"))
			if num%2==0:
				msg="num "+str(num)+" is even"
			else:
				msg="num "+str(num)+" is odd"
			return render(request,"home.html",{"msg":msg})
		except ValueError:
			msg="u shud enter integers only"
			return render(request,"home.html",{"msg":msg})
	else:
		return render(request,"home.html")
