# staff/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from .models import Staff
from .serializers import StaffSerializer


# 🔹 REGISTER STAFF
class RegisterStaffView(APIView):

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Staff registered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🔹 LOGIN STAFF
class LoginStaffView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            staff = Staff.objects.get(email=email)
        except Staff.DoesNotExist:
            return Response(
                {"error": "Invalid email"},
                status=status.HTTP_404_NOT_FOUND
            )

        if check_password(password, staff.password):
            return Response({
                "message": "Login successful",
                "staff_id": staff.id,
                "name": staff.name
            }, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid password"},
            status=status.HTTP_400_BAD_REQUEST
        )


# 🔹 STAFF DETAIL (GET, PUT, DELETE)
class StaffDetailView(APIView):

    def get_object(self, staff_id):
        try:
            return Staff.objects.get(id=staff_id)
        except Staff.DoesNotExist:
            return None


    # 🔸 GET Staff Details
    def get(self, request, staff_id):
        staff = self.get_object(staff_id)
        if not staff:
            return Response({"error": "Staff not found"}, status=404)

        serializer = StaffSerializer(staff)
        return Response(serializer.data)


    # 🔸 UPDATE Staff
    def put(self, request, staff_id):
        staff = self.get_object(staff_id)
        if not staff:
            return Response({"error": "Staff not found"}, status=404)

        staff.name = request.data.get('name', staff.name)
        staff.email = request.data.get('email', staff.email)

        if request.data.get('password'):
            staff.password = make_password(request.data.get('password'))

        staff.save()

        return Response({"message": "Staff updated successfully"})


    # 🔸 DELETE Staff
    def delete(self, request, staff_id):
        staff = self.get_object(staff_id)
        if not staff:
            return Response({"error": "Staff not found"}, status=404)

        staff.delete()
        return Response({"message": "Staff deleted successfully"})
