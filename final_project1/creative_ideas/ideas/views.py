from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Business_idaea, Comment, Offers
from .serializers import business_idaeaSerializer, commentSerializer, offersSerializer


# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_profile(request : Request):

    if not request.user.is_authenticated or not request.user.has_perm('ideas.add_business_idaea'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)
    new_Business_idaea = business_idaeaSerializer(data=request.data)
    if new_Business_idaea.is_valid():
        new_Business_idaea.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Business_idaea" : new_Business_idaea.data
        }
        return Response(dataResponse)
    else:
        print(new_Business_idaea.errors)
        dataResponse = {"msg" : "couldn't create a Business_idaea"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_profile(request : Request):
    business_idaea = Business_idaea.objects.all()

    dataResponse = {
        "msg" : "List of All profile",
        "profiles" : business_idaeaSerializer(instance=business_idaea, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_profile(request : Request, business_id):
    if not request.user.is_authenticated or not request.user.has_perm('ideas.add_business_idaea'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    business_idaea = Business_idaea.objects.get(id=business_id)

    updated_business_idaea = business_idaeaSerializer(instance=business_idaea, data=request.data)
    if updated_business_idaea.is_valid():
        updated_business_idaea.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_business_idaea.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request: Request, business_id):
    if not request.user.is_authenticated or not request.user.has_perm('ideas.delete_business_idaea'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    profile = Business_idaea.objects.get(id= business_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})




@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request : Request):

    if not request.user.is_authenticated or not request.user.has_perm('ideas.add_comment'):
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    new_comment = commentSerializer(data=request.data)
    if new_comment.is_valid():
        new_comment.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "note" : new_comment.data
        }
        return Response(dataResponse)
    else:
        print(new_comment.errors)
        dataResponse = {"msg" : "couldn't create a comments"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_comment(request : Request):
    comments = Comment.objects.all()

    dataResponse = {
        "msg" : "List of All investor",
        "investor" : commentSerializer(instance=comments, many=True).data
    }

    return Response(dataResponse)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_comment(request: Request, comment_id):
    if not request.user.is_authenticated or not request.user.has_perm('ideas.delete_comment'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return Response({"msg" : "Deleted Successfully"})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_offers(request : Request):

    if not request.user.is_authenticated or not request.user.has_perm('ideas.add_offers'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)
    new_offers= offersSerializer(data=request.data)
    if new_offers.is_valid():
        new_offers.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Business_idaea" : new_offers.data
        }
        return Response(dataResponse)
    else:
        print(new_offers.errors)
        dataResponse = {"msg" : "couldn't create a offers"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_offers(request : Request):
    offers = Offers.objects.all()

    dataResponse = {
        "msg" : "List of All profile",
        "profiles" : offersSerializer(instance=offers, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_ofers(request : Request, offers_id):
    if not request.user.is_authenticated or not request.user.has_perm('ideas.update_offers'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    offers = Offers.objects.get(id=offers_id)

    updated_offers= offersSerializer(instance=offers, data=request.data)
    if updated_offers.is_valid():
        updated_offers.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_offers.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@authentication_classes([JWTAuthentication])
def delete_offers(request: Request, offers_id):
    if not request.user.is_authenticated or not request.user.has_perm('ideas.delete_offers'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    offers= Offers.objects.get(id= offers_id)
    offers.delete()
    return Response({"msg" : "Deleted Successfully"})






