# File: WRS_Readersapi/views/reviews.py

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from ..models import Review
from ..serializers.review_serializer import ReviewSerializer

class ReviewViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        """
        Retrieves a list of all reviews.

        Returns:
        - HTTP 200 OK with serialized review data on success.
        """
        # Retrieve all reviews from the database
        reviews = Review.objects.all()

        # Serialize the reviews and include request context
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})

        # Return serialized data with HTTP 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        Creates a new review.

        Returns:
        - HTTP 201 Created with serialized review data on success.
        - HTTP 400 Bad Request if serializer validation fails.
        """
        # Serialize the incoming data and validate it
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        # Save the validated review
        serializer.save()

        # Return serialized data with HTTP 201 Created status
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """
        Retrieves a specific review by its primary key (pk).

        Args:
        - pk: Primary key of the review to retrieve.

        Returns:
        - HTTP 200 OK with serialized review data on success.
        - HTTP 404 Not Found if the review does not exist.
        """
        try:
            # Retrieve the requested review from the database
            review = Review.objects.get(pk=pk)

            # Serialize the review and include request context
            serializer = ReviewSerializer(review, context={'request': request})

            # Return serialized data with HTTP 200 OK status
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Review.DoesNotExist:
            # Return HTTP 404 Not Found if the review does not exist
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        Deletes a specific review by its primary key (pk).

        Args:
        - pk: Primary key of the review to delete.

        Returns:
        - HTTP 204 No Content on successful deletion.
        - HTTP 403 Forbidden if the authenticated user is not the review's author.
        - HTTP 404 Not Found if the review does not exist.
        """
        try:
            # Retrieve the requested review from the database
            review = Review.objects.get(pk=pk)

            # Check if the authenticated user is the author of the review
            if review.user.id != request.user.id:
                # Return HTTP 403 Forbidden if not authorized to delete
                return Response(status=status.HTTP_403_FORBIDDEN)

            # Delete the review from the database
            review.delete()

            # Return HTTP 204 No Content on successful deletion
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Review.DoesNotExist:
            # Return HTTP 404 Not Found if the review does not exist
            return Response(status=status.HTTP_404_NOT_FOUND)
