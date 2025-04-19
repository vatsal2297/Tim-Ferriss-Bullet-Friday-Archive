from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from TFFBullets.models import Tff5BulletEmails
from .serializers import TFFEmailSerializer


# Create your views here.

# class TFFEmailViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Tff5BulletEmails.objects.prefetch_related('tffbullets_set')
#     serializer_class = TFFEmailSerializer

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset() # Fetch the queryset
#         serializer = self.get_serializer(queryset, many = True) # Serialize the queryset
#         return Response({'emails': serializer.data}) # Wrap the serialized data in a dictionary

class TFFEmailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tff5BulletEmails.objects.prefetch_related('tffbullets_set')
    serializer_class = TFFEmailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        #Extract 'year' from kwargs
        year = self.kwargs.get('year', None)
        #print(self.kwargs)
        #print(f"Filtering by year: {year}")
        if year is not None:
            #Filter emails by the year extracted from 'email_date'
            queryset = queryset.filter(email_date__year=year)
            if not queryset.exists():
               raise NotFound(f"No emails found for the year {year}.")
        #print(queryset.query)
        return queryset #super().get_queryset()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset() # Fetch the queryset
        serializer = self.get_serializer(queryset, many = True) # Serialize the queryset
        return Response({'emails': serializer.data}) # Wrap the serialized data in a dictionary

