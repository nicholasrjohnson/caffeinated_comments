# This is the first iteration of the caffeinated comments idea
#
#This template injector will put the comments system in the server side template with the { caffeinated_comments } tag
#

#use safestring
from django import template

register = template.Library()

# what do we take in to make sure it is the comments for he correct post? We will definitely need to use the context
from caffeinated_comments.models import Comment

@register.inclusion_tag('caffeinated_comments/caffeinated_comments.html')
def caffeinated_comments(postID):
    #Get the previous comments and the authors for that Post
    comments = Comment.objects.filter(postid=postID)
    
    return {
       'comments': comments,
       'postId': postID
    }

@register.simple_tag
def getAuthorName(comment):
    if(comment.created_by is None):
        name = 'Anonymous'
    else:
        author = comment.created_by
        name = author.name
    return name
