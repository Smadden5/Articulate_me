from rest_framework import serializers
from article import models

        
# class NestedAOCSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.AOC
#         fields = ('subject',)

# class NestedAuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Article
#         fields = ('author',)
        
class ArticleSerializer(serializers.ModelSerializer):
    # aoc_detail = NestedAOCSerializer(read_only=True, many=True, source='aoc')    
    class Meta:
        model = models.Article
        fields = ('author', 'title', 'content', 'created_date', 'slug', 'id')
              
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Comment
        fields = ('article', 'comment_author', 'comment_content', 'created_date', 'id')

# class AOCSerializer(serializers.ModelSerializer):
#     # article = NestedAuthorSerializer(read_only=True, many=True)
#     class Meta:
#         model = models.AOC
#         fields = ('aoc', 'subject', 'id')
        

        
# class AuthorSerializer(serializers.ModelSerializer):
#     aoc_detail = NestedAOCSerializer(many=True, read_only=True, source='posts')
#     class Meta: 
#         model = models.Article
#         fields = ('id', 'username', 'articles', 'aoc_detail')