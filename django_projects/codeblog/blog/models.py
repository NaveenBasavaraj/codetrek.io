from django.db import models
from blog.lookup_models import Difficulty
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField()
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
    total_pages = models.IntegerField(default=0, editable=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return self.title
    
    def get_completed_pages_count(self, user):
        """Get number of completed pages for a specific user"""
        if not user.is_authenticated:
            return 0
        return UserProgress.objects.filter(
            user=user,
            page__section__course=self,
            completed=True
        ).count()
    
    def get_progress_percentage(self, user):
        """Calculate completion percentage for a user"""
        if self.total_pages == 0:
            return 0
        completed = self.get_completed_pages_count(user)
        return int((completed / self.total_pages) * 100)
    
    def update_total_pages(self):
        """Update the total pages count"""
        self.total_pages = Page.objects.filter(section__course=self).count()
        self.save()
    
class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='sections')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    order = models.IntegerField(default=0, help_text="Order in which section appears")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        unique_together = ('course', 'slug')
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
    def get_pages_count(self):
        """Get total number of pages in this section"""
        return self.pages.count()

class Page(models.Model):
    section = models.ForeignKey(
        Section, 
        on_delete=models.CASCADE, 
        related_name='pages'
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField(help_text="Page content in Markdown format")
    order = models.IntegerField(default=0, help_text="Order in which page appears")
    estimated_minutes = models.IntegerField(default=5, help_text="Estimated reading time")
    is_free = models.BooleanField(default=True, help_text="Free or Pro content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        unique_together = ('section', 'slug')
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    
    def __str__(self):
        return self.title
    
    def is_completed_by(self, user):
        """Check if this page is completed by a specific user"""
        if not user.is_authenticated:
            return False
        return UserProgress.objects.filter(
            user=user,
            page=self,
            completed=True
        ).exists()
    
    def get_next_page(self):
        """Get the next page in order"""
        # Try to get next page in same section
        next_in_section = Page.objects.filter(
            section=self.section,
            order__gt=self.order
        ).first()
        
        if next_in_section:
            return next_in_section
        
        # If no next page in section, get first page of next section
        next_section = Section.objects.filter(
            course=self.section.course,
            order__gt=self.section.order
        ).first()
        
        if next_section:
            return next_section.pages.first()
        
        return None
    
    def get_previous_page(self):
        """Get the previous page in order"""
        # Try to get previous page in same section
        prev_in_section = Page.objects.filter(
            section=self.section,
            order__lt=self.order
        ).order_by('-order').first()
        
        if prev_in_section:
            return prev_in_section
        
        # If no previous page in section, get last page of previous section
        prev_section = Section.objects.filter(
            course=self.section.course,
            order__lt=self.section.order
        ).order_by('-order').first()
        
        if prev_section:
            return prev_section.pages.last()
        
        return None


class UserProgress(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='course_progress'
    )
    page = models.ForeignKey(
        Page, 
        on_delete=models.CASCADE, 
        related_name='user_progress'
    )
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    first_viewed_at = models.DateTimeField(auto_now_add=True)
    last_viewed_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'page')
        verbose_name = 'User Progress'
        verbose_name_plural = 'User Progress'
        ordering = ['-last_viewed_at']
    
    def __str__(self):
        status = '✓' if self.completed else '○'
        return f"{self.user.username} - {self.page.title} {status}"
    
    def mark_complete(self):
        """Mark this page as completed"""
        if not self.completed:
            self.completed = True
            self.completed_at = timezone.now()
            self.save()
            self.page.section.course.update_total_pages()
    
    def mark_incomplete(self):
        """Mark this page as incomplete"""
        if self.completed:
            self.completed = False
            self.completed_at = None
            self.save()