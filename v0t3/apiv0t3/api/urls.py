from django.urls import path
from apiv0t3.api.views import ( ElectorDetailCreateAPIView,
								ElectorListCreateAPIView,
								VoteDetailCreateAPIView,
								VoteListCreateAPIView )


urlpatterns = [
	path("electors/", 
		ElectorListCreateAPIView.as_view(), 
		name="electors-list"),
	path("electors/<int:pk>/", 
		ElectorDetailCreateAPIView.as_view(), 
		name="elector-detail"),
	path("votes/", 
		VoteListCreateAPIView.as_view(), 
		name="votes-list"),
	path("votes/<int:pk>/", 
		VoteDetailCreateAPIView.as_view(), 
		name="vote-detail")

]