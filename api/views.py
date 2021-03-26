from django.shortcuts import render
from .serializers import Companyserializers
from .models import CompanyModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
 


@api_view(['GET','POST'])
def product_list(request):
    if request.method =='GET':
        pizza = request.GET.get('pizza_type',"")
        pizza1 = request.GET.get('pizza_size',"")
        if pizza=='Regular' or pizza=='Square':
            if pizza1=='small' or pizza1=='large' or pizza1=='medium':
                     pizza_list=[]
                     iteam = list(CompanyModel.objects.filter(pizza_type=pizza,pizza_size=pizza1))
                     for i in iteam:
                         data = {
                             'pizza_type':i.pizza_type,
                             'pizza_size':i.pizza_size,
                             'topping_type':i.topping_type
                         }
                         pizza_list.append(data)
                     return Response(status=status.HTTP_200_OK,
                                     data={'data':pizza_list,'success': True})
            else:
                 return Response(status=status.HTTP_404_NOT_FOUND, data={"message":"Only small,medium and large Availabe ", "success": False})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message":"Only Square and Regular are Availabe ", "success": False})
        

    elif(request.method =='POST'):
        serializers=Companyserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def delete_order(request):
    try:
        CompanyModel.objects.filter(id=request.data['order_id']).delete()
        return Response(status=status.HTTP_200_OK,
                        data={'message':'Successfully Deleted','success': True})
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": str(e), "success": False})


@api_view(["GET"])
def get_all_data(request):
    pizza_list = CompanyModel.objects.values()
    final_list = []
    for i in pizza_list:
        data = {
                   'id'  : i['id'],
                   'pizza_type':i['pizza_type'],
                   'pizza_size':i['pizza_size'],
                   'topping_type':i['topping_type']
               }
        final_list.append(data)
    return Response(status=status.HTTP_200_OK,
                                     data={'data':final_list,'success': True})

@api_view(["POST"])
def edit_order(request):
    try:
         
        pizza_obj = CompanyModel.objects.get(id=request.data['order_id'])
        if 'pizza_type' in request.data:
            pizza_obj.pizza_type= request.data['pizza_type']
        if 'pizza_size' in request.data:
            pizza_obj.pizza_size= request.data['pizza_size']
        if 'topping_type' in request.data:
            pizza_obj.topping_type = request.data['topping_type']
      
        pizza_obj.save()
        return Response(status=status.HTTP_200_OK,
                        data={'message':'Successfully Updated','success': True})
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": str(e), "success": False})