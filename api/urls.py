from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('running/', views.running, name='running'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginView.as_view(), name='check login'),
    path('AddUser/', views.AddUserView.as_view(), name='add user'),
    path('DeleteUser/<int:user_id>/', views.DeleteUserView.as_view(), name='delete user'),
    path('UpdateUser/<int:user_id>/', views.UpdateUserView.as_view(), name='update user'),
    path('quiz-result/', views.TakeQuizView.as_view(), name='test quiz'),
    path('forum-post/', views.ForumPostView.as_view(), name='forum post'),
    path('comment/<int:post_id>/', views.CommentCreateView.as_view(), name='test comment'),
    path('user-info/create/', views.CreateUserInformationView.as_view(), name='create_user_info'),
    path('user-info/<int:pk>/update/', views.UpdateUserInformationView.as_view(), name='update_user_info'),
    path('user-info/<int:pk>/delete/', views.DeleteUserInformationView.as_view(), name='delete_user_info'),
    path('consultation/', views.CreateConsultationView.as_view(), name='create_consultation'),
    path('consultation/<int:pk>/update/', views.UpdateConsultationView.as_view(), name='update_consultation'),
    path('consultation/<int:pk>/delete/', views.DeleteConsultationView.as_view(), name='delete_consultation'),
    path('SendChat/', views.ChatMessageView.as_view(), name='Send Chat Message'),
    path('chathistory/<int:user_id>/<int:expert_id>/', views.ChatHistoryView.as_view(), name='chat-history'),
    path('getexpert/<int:expert_id>/', views.ExpertInformationDetailView.as_view(), name='get expert'),
    path('getfullexpert/', views.ExpertInformationListView.as_view(), name='get full expert'),
    path('createtransaction/', views.CreateTransactionView.as_view(),name='create transaction'),
    path('confirmtransaction/<int:transaction_id>/', views.ConfirmTransactionView.as_view(),name='confirm transaction'),
    path('notification/<int:notification_id>/', views.NotificationDetailView.as_view(), name='notification-detail'),
]