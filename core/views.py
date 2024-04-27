# from django.shortcuts import render
# from django.views import View

# # Create your views here.
# class Home(View):
#     def get(self, request):
#         error_message = request.GET.get('error_message', None)
#         context = {'error_message': error_message}
#         return render(request, 'core/home.html', context)

# from rest_framework import generics
# from .models import Person
# from .serializers import PersonSerializer
# from django.http import JsonResponse
# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib import messages 
# from django.shortcuts import get_object_or_404, render, redirect


# class Signup(generics.CreateAPIView):
#     def post(self, request):

#         serializer = PersonSerializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#             username = request.data.get("username")

#             # Check if the username already exists
#             if Person.objects.filter(username=username).exists():
#                 return JsonResponse({"error": "Username already exists"}, status=400)

#             user = serializer.save()
#             user.password = make_password(request.data.get("password"))
#             user.save()
#             messages.success(request, 'Registration successful!') 
#             return redirect("/")
#             # return JsonResponse({"message": "User created successfully"}, status=201)
#         except Exception as e:
#             return JsonResponse(
#                 {"error": "Invalid data", "details": serializer.errors}, status=400
#             )
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import status

# class Login(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         try:
#             user = Person.objects.get(username=username)
#         except Person.DoesNotExist:
#             return JsonResponse(
#                 {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
#             )

#         if not check_password(password, user.password):
#             return JsonResponse(
#                 {"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED
#             )

#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)
#         refresh_token = str(refresh)
#         return render(request, 'gameapp/welcome_page.html', {'access_token': access_token, 'refresh_token': refresh_token})






# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from .utils import generate_otp, send_otp_email
# # from .models import CustomUser

# # class LoginWithOTP(APIView):
# #     def post(self, request):
# #         email = request.data.get('email', '')
# #         try:
# #             user = CustomUser.objects.get(email=email)
# #         except CustomUser.DoesNotExist:
# #             return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

# #         otp = generate_otp()
# #         user.otp = otp
# #         user.save()

# #         send_otp_email(email, otp)
# #         # send_otp_phone(phone_number, otp)

# #         return Response({'message': 'OTP has been sent to your email.'}, status=status.HTTP_200_OK)

# # from django.contrib.auth import authenticate
# # from rest_framework.authtoken.models import Token

# # class ValidateOTP(APIView):
# #     def post(self, request):
# #         email = request.data.get('email', '')
# #         otp = request.data.get('otp', '')

# #         try:
# #             user = CustomUser.objects.get(email=email)
# #         except CustomUser.DoesNotExist:
# #             return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

# #         if user.otp == otp:
# #             user.otp = None  # Reset the OTP field after successful validation
# #             user.save()

# #             # Authenticate the user and create or get an authentication token
# #             token, _ = Token.objects.get_or_create(user=user)

# #             return Response({'token': token.key}, status=status.HTTP_200_OK)
# #         else:
# #             return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)

# # class UserCreate(generics.CreateAPIView):
# #     serializer_class = UserSerializer

# #     def create(self, request, *args, **kwargs):
# #         serializer = self.get_serializer(data=request.data)
# #         if serializer.is_valid():
# #             try:
# #                 self.perform_create(serializer)
# #                 messages.success(request, 'Registration successful!') 
# #                 return redirect("/")

# #             except Exception as e:
# #                 return Response(
# #                     {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
# #                 )

# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

