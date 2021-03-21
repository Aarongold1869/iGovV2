from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q

# API_KEY = settings.GOOGLE_API_KEY 
User = settings.AUTH_USER_MODEL
PostUser = get_user_model()

writing_weight = .25
bipartisan_weight = .25
popularity_weight = .25
transparency_weight = .25

class Country(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

class State(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    abbrev = models.CharField(max_length=50, null=False, blank=False)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE)

class Locality(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    postal_code = models.CharField(max_length=50, null=False, blank=False)
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE)

class Address(models.Model):
    raw = models.CharField(max_length=200, null=False, blank=False)
    street_number = models.CharField(max_length=50, null=False, blank=False)
    route = models.CharField(max_length=50, null=False, blank=False)
    locality = models.ForeignKey(Locality, blank=True, null=True, on_delete=models.CASCADE)

class RepresentativeTitle(models.Model):
    title_name = models.CharField(max_length=50, null=False, blank=False)
    title_description = models.TextField(blank=True, null=True, max_length=2000)

class Party(models.Model):
    party_name = models.CharField(max_length=50, null=False, blank=False)
    party_description = models.TextField(blank=True, null=True, max_length=2000)

# # This Author Entity represents a member of congress who wrote or co wrote a given bill
# # Author Entity can also represent a User on the Platform. 
class BillAuthor(models.Model): 
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    title = models.ForeignKey(RepresentativeTitle, blank=True, null=True, on_delete=models.PROTECT)
    party_affiliation = models.ForeignKey(Party, blank=True, null=True, on_delete=models.PROTECT)
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.PROTECT)
    contact = models.CharField(max_length=50, null=False, blank=False)
    writing_score = models.IntegerField()
    bipartisan_score = models.IntegerField()
    popularity_score = models.IntegerField()
    transparency_score = models.IntegerField()
    
    @property 
    def overall_score(self):
        overall = (
            (self.writing_score * writing_weight) + 
            (self.bipartisan_score * bipartisan_weight) + 
            (self.popularity_score * popularity_weight) +
            (self.transparency_score * transparency_weight)
            )
        return overall

class UserBillAuthor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # party_affiliation = models.ForeignKey(Party, blank=True, null=True, on_delete=models.PROTECT)
    # address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.PROTECT)
    # bio = models.TextField(null=True, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    # picture = models.ImageField(upload_to='profile_pictures', blank=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # followers = models.ManyToManyField(User, related_name="following", blank=True)
    writing_score = models.IntegerField()
    bipartisan_score = models.IntegerField()
    popularity_score = models.IntegerField()
    transparency_score = models.IntegerField()
    
    @property 
    def overall_score(self):
        overall = (
            (self.writing_score * writing_weight) + 
            (self.bipartisan_score * bipartisan_weight) + 
            (self.popularity_score * popularity_weight) +
            (self.transparency_score * transparency_weight)
            )
        return overall

class SubsectionLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subsection = models.ForeignKey("Subsection", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class SubsectionDisike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subsection = models.ForeignKey("Subsection", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class SubsectionCommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey("SubsectionComment", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class SubsectionCommentDisike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey("SubsectionComment", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class SubsectionComment(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subsection = models.ForeignKey("Subsection", on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    comment_likes = models.ManyToManyField(User, related_name='subsection_comment_like_user', blank=True, through=SubsectionCommentLike)
    comment_dislikes = models.ManyToManyField(User, related_name='subsection_comment_dislike_user', blank=True, through=SubsectionCommentDisike)
    timestamp = models.DateTimeField(auto_now_add=True)

class Subsection(models.Model):
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE)
    section_number = models.CharField(max_length=220, null=True, default=None)
    section_title = models.CharField(max_length=220, null=True, default=None)
    section_content = models.TextField(blank=True, null=True)
    subsection_likes = models.ManyToManyField(User, related_name='subsection_like_user', blank=True, through=SubsectionLike)
    subsection_dislikes = models.ManyToManyField(User, related_name='subsection_dislike_user', blank=True, through=SubsectionDisike)
    subsection_comments = models.ManyToManyField(User, related_name='subsection_comment_user', blank=True, through=SubsectionComment)
    writing_score = models.IntegerField()
    bipartisan_score = models.IntegerField()
    popularity_score = models.IntegerField()
    transparency_score = models.IntegerField()
    
    @property 
    def overall_score(self):
        overall = (
            (self.writing_score * writing_weight) + 
            (self.bipartisan_score * bipartisan_weight) + 
            (self.popularity_score * popularity_weight) +
            (self.transparency_score * transparency_weight)
            )
        return overall

class BillLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class BillDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class BillCommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey("BillComment", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class BillCommentDisLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey("BillComment", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class BillComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    comment_likes = models.ManyToManyField(User, related_name='bill_comment_like_user', blank=True, through=BillCommentLike)
    comment_dislikes = models.ManyToManyField(User, related_name='bill_comment_dislike_user', blank=True, through=BillCommentDisLike)
    timestamp = models.DateTimeField(auto_now_add=True)

class BillType(models.Model):
    bill_type = models.CharField(max_length=220, null=False, default=None)  

class Bill(models.Model):
    bill_title = models.CharField(max_length=220, null=False, default=None) 
    bill_number = models.CharField(max_length=220, null=False, default=None) 
    bill_type = models.ForeignKey("BillType", on_delete=models.PROTECT)
    bill_authors = models.ManyToManyField(BillAuthor, related_name='bill_author', blank=True)
    user_bill_author = models.ForeignKey(UserBillAuthor, on_delete=models.CASCADE, blank=True)
    # bill_supporters = models.ManyToManyField(BillAuthor, related_name='bill_supporter', blank=True)
    bill_heading = models.TextField(blank=False, null=False)
    bill_summary = models.TextField(blank=False, null=False)
    publish_date = models.DateTimeField(blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    bill_subsections = models.ManyToManyField(Subsection, related_name='bill_subsections', blank=True)
    bill_likes = models.ManyToManyField(User, related_name='bill_like_user', blank=True, through=BillLike)
    bill_dislikes = models.ManyToManyField(User, related_name='bill_dislike_user', blank=True, through=BillDislike)
    bill_comments = models.ManyToManyField(User, related_name='bill_comment_user', blank=True, through=BillComment)
    passed = models.BooleanField()
    passed_date = models.DateTimeField(blank=True, null=True)
    # house_vote 
    # senate_vote
    
    


    
