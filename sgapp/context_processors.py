from .models import Review, Application

def moderator_bildirimler(request):
    if request.user.is_authenticated and request.user.role == 'moderator':
        bekleyen_yorum = Review.objects.filter(status='pending').count()
        bekleyen_basvuru = Application.objects.filter(status='pending').count()
        return {
            'bekleyen_yorum_sayisi': bekleyen_yorum,
            'bekleyen_basvuru_sayisi': bekleyen_basvuru,
        }
    return {}
