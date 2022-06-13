from django.shortcuts import render
from django.contrib.auth.models import User
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
def add_Business_idaea(request : Request):
    '''
     idea owner add new idea , cost but must be register and login
    '''

    if not request.user.is_authenticated or not request.user.has_perm('ideas.add_business_idaea'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(idea_owner=request.user.id)
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
def list_Business_idaea(request : Request):
    '''
    to view ideas to evrey one
    '''
    business_idaea = Business_idaea.objects.all()

    dataResponse = {
        "msg" : "List of All business ideas",
        "profiles" : business_idaeaSerializer(instance=business_idaea, many=True).data
    }

    return Response(dataResponse)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_Business_idaea(request : Request, business_id):
    '''
    idea owner update new idea , cost but must be register , login and have permission
    '''
    if not request.user.is_authenticated or not request.user.has_perm('ideas.add_business_idaea'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(idea_owner=request.user.id)
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
def delete_Business_idaea(request: Request, business_id):
    '''
    idea owner delete new idea , cost but must be register , login and have permission
    '''
    if not request.user.is_authenticated or not request.user.has_perm('ideas.delete_business_idaea'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(idea_owner=request.user.id)
    profile = Business_idaea.objects.get(id= business_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})




@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request : Request):
    '''
    investor add new comment in idea  but must be register , login and have permission
    '''

    if not request.user.is_authenticated or not request.user.has_perm('ideas.add_comment'):
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(investor=request.user.id)
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_comment(request : Request):
    '''
        investor view comment in idea
    '''
    if not request.user.is_authenticated or not request.user.has_perm('ideas.view_comment'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(investor=request.user.id)
    comments = Comment.objects.all()

    dataResponse = {
        "msg" : "List of All comments",
        "investor" : commentSerializer(instance=comments, many=True).data
    }

    return Response(dataResponse)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_comment(request: Request, comment_id):
    '''
        investor delete comment in idea  but must be register , login and have permission
    '''
    if not request.user.is_authenticated or not request.user.has_perm('ideas.delete_comment'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(investor=request.user.id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return Response({"msg" : "Deleted Successfully"})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_offers(request : Request):
    '''
        idea owner accept or reject the offers  but must be register , login and have permission
    '''

    if not request.user.is_authenticated or not request.user.has_perm('ideas.add_offers'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(idea_owner=request.user.id)
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
    '''
            idea owner accept or view offers
    '''

    offers = Offers.objects.all()

    dataResponse = {
        "msg" : "List of All offers",
        "profiles" : offersSerializer(instance=offers, many=True).data
    }

    return Response(dataResponse)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_offers(request : Request, offers_id):
    '''
            idea owner update the offers  but must be register , login and have permission
    '''

    if not request.user.is_authenticated or not request.user.has_perm('ideas.change_offers'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(idea_owner=request.user.id)
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
    '''
            idea owner delete the offers  but must be register , login and have permission
    '''

    if not request.user.is_authenticated or not request.user.has_perm('ideas.delete_offers'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(idea_owner=request.user.id)
    offers= Offers.objects.get(id= offers_id)
    offers.delete()
    return Response({"msg" : "Deleted Successfully"})




@api_view(['GET'])
def search_ideas(request : Request ,idea):
    '''
    to search about idea
    '''
    ideas = Business_idaea.objects.filter(ideas=idea)

    dataResponse = {
        "msg" : "the idea:",
        "students" : business_idaeaSerializer(instance=ideas, many=True).data
    }

    return Response(dataResponse)






