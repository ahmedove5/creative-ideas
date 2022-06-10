from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Profile ,Comment
from .serializers import profileSerializer ,commentSerializer

# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_profile(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_profile = profileSerializer(data=request.data)
    if new_profile.is_valid():
        new_profile.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "note" : new_profile.data
        }
        return Response(dataResponse)
    else:
        print(new_profile.errors)
        dataResponse = {"msg" : "couldn't create a note"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_profile(request : Request):
    notes = Profile.objects.all()

    dataResponse = {
        "msg" : "List of All cities",
        "cities" : profileSerializer(instance=notes, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_profile(request : Request, profile_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = Profile.objects.get(id=profile_id)

    updated_profile = profileSerializer(instance=profile, data=request.data)
    if updated_profile.is_valid():
        updated_profile.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_profile.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_profile(request: Request, profile_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})




@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_comment(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

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
        dataResponse = {"msg" : "couldn't create a note"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_comment(request : Request):
    comments = Comment.objects.all()

    dataResponse = {
        "msg" : "List of All cities",
        "cities" : profileSerializer(instance=comments, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_comment(request : Request, comment_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    comments = Comment.objects.get(id=comment_id)

    updated_comment = profileSerializer(instance=comments, data=request.data)
    if updated_comment.is_valid():
        updated_comment.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_comment.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_comment(request: Request, profile_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    comment = Comment.objects.get(id=profile_id)
    Comment.delete()
    return Response({"msg" : "Deleted Successfully"})



