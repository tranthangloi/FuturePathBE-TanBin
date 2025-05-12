from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

def validate_password(value):
    if len(value) < 8:
        raise serializers.ValidationError("Mật khẩu phải có ít nhất 8 ký tự.")
    
    if not any(char.isupper() for char in value):
        raise serializers.ValidationError("Mật khẩu phải có ít nhất một chữ in hoa.")
    
    if not any(char.isdigit() for char in value):
        raise serializers.ValidationError("Mật khẩu phải có ít nhất một số.")
    
    if not any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?' for char in value):
        raise serializers.ValidationError("Mật khẩu phải có ít nhất một ký tự đặc biệt.")
    
    if ' ' in value:
        raise serializers.ValidationError("Mật khẩu không được có khoảng trắng.")
    
    return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        return make_password(value)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = ['id', 'name']


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRole
        fields = ['user', 'role']


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ['quiz_id', 'quiz_type', 'content', 'option1', 'option2', 'category']


class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizResult
        fields = ['id', 'quiz_type','user', 'quiz', 'E_score', 'I_score', 'S_score', 'N_score', 'T_score', 'F_score', 'J_score', 'P_score', 'R_score', 'I_score_h', 'A_score_h', 'S_score_h', 'E_score_h', 'C_score_h', 'result']


class ChatbotHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChatbotHistory
        fields = ['id', 'user', 'message', 'response', 'timestamp', 'conversation']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = ['id', 'user', 'message', 'created_at', 'status']


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForumPost
        fields = ['id', 'user', 'title', 'content', 'created_at', 'status',]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['id', 'post', 'user', 'reason', 'reported_at', 'status']


class BannedUserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BannedUserHistory
        fields = ['id', 'user', 'banned_at', 'reason', 'reject_count']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ['id', 'user', 'expert', 'amount', 'transaction_date', 'transaction_status']


class RevenueManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RevenueManagement
        fields = ['id', 'total_revenue', 'report_date']


class ExpertInformationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = models.ExpertInformation
        fields = ['id','name', 'user', 'expertise', 'experience_years', 'date_of_birth', 'gender','major','workplace','description','certifications', 'account_balance']


class ConsultantScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConsultantSchedule
        fields = ['id', 'expert', 'available_date', 'available_time']


class ExpertWithdrawInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpertWithdrawInformation
        fields = ['id', 'expert', 'bank_account', 'withdraw_amount']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = ['id', 'user', 'message', 'created_at']


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInformation
        fields = '__all__'
        
class ForumContentManagementSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    expert = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.ForumContentManagement
        fields = ['id', 'user', 'action', 'timestamp']

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consultation
        fields = ['expert', 'schedule', 'reason']
        read_only_fields = ['is_confirmed', 'created_at']
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChatMessage
        fields = '__all__'

