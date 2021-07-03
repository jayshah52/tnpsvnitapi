from rest_framework import serializers

from .models import Job, Shortlist



class JobSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    class Meta:
        model = Job
        fields = "__all__"

    def get_count(self, job):
        shortlist, created = Shortlist.objects.get_or_create(job=job, number=4)
        users = shortlist.users.all()
        return users.count()

class ShortlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortlist
        fields = "__all__"


