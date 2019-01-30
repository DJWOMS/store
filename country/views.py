# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions
#
# from .models import Country, State, City
# from .serializers import CountrySerializer, StateSerializer, CitySerializer
#
#
# class Countries(APIView):
#     """Вывод стран, штатов, городов"""
#     permission_classes = [permissions.IsAuthenticated]
#
#     def all_countries(self):
#         countries = Country.objects.all()
#         return countries
#
#     def get_states(self, pk):
#         states = State.objects.filter(country_id=pk)
#         return states
#
#     def get_cities(self, pk):
#         cities = City.objects.filter(state_id=pk)
#         return cities
#
#     def get(self, request):
#         country_pk = request.GET.get("country_pk", None)
#         state_pk = request.GET.get("state_pk", None)
#         if country_pk is None and state_pk is None:
#             countries = self.all_countries()
#             country_ser = CountrySerializer(countries, many=True)
#             return Response({"countries": country_ser.data})
#         if country_pk is not None and state_pk is not None:
#             states = self.get_states(country_pk)
#             states_ser = StateSerializer(states, many=True)
#             cities = self.get_cities(state_pk)
#             cities_ser = CitySerializer(cities, many=True)
#             return Response({"states": states_ser.data,
#                              "cities": cities_ser.data})
#         if country_pk is not None:
#             states = self.get_states(country_pk)
#             states_ser = StateSerializer(states, many=True)
#             return Response({"states": states_ser.data})
#         if state_pk is not None:
#             cities = self.get_cities(state_pk)
#             cities_ser = CitySerializer(cities, many=True)
#             return Response({"cities": cities_ser.data})
