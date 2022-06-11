from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Profile ,Comment
from .serializers import profileSerializer ,commentSerializer

# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_profile(request : Request):

    if not request.user.is_authenticated or not request.user.has_perm('creative_ideas.add_Profile'):
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
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
        dataResponse = {"msg" : "couldn't create a profile"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_profile(request : Request):
    notes = Profile.objects.all()

    dataResponse = {
        "msg" : "List of All profile",
        "profiles" : profileSerializer(instance=notes, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
#@permission_classes([IsAuthenticated])
def update_profile(request : Request, profile_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    #request.data.update(user=request.user.id)
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
#@authentication_classes([JWTAuthentication])
def delete_profile(request: Request, profile_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    #request.data.update(user=request.user.id)
    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})




@api_view(['POST'])
@authentication_classes([JWTAuthentication])
#@authentication_classes([JWTAuthentication])
def add_comment(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    #request.data.update(user=request.user.id)
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

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@authentication_classes([JWTAuthentication])
def update_comment(request : Request, comment_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    comments = Comment.objects.get(id=comment_id)

    updated_comment = commentSerializer(instance=comments, data=request.data)
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
@authentication_classes([JWTAuthentication])
def delete_comment(request: Request, comment_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return Response({"msg" : "Deleted Successfully"})



