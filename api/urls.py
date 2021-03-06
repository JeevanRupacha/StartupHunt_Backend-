from rest_framework.routers import DefaultRouter,SimpleRouter
from django.urls import path, include


from .views import(
    ProductViewSet,
    ProductCommentViewSet,
    ProductImageViewSet,
    ProductIconViewSet,
    CategoryViewSet,
    ProductUpvoteViewSet,
    UpcommingProductViewSet,
    HomePageView
)

## Using default router 
## It provides all the CRUD route by default 
router = DefaultRouter()

# route for all the product list 
router.register(f'products', ProductViewSet, 'Product')
router.register(f'product_upvote', ProductUpvoteViewSet, 'Product Upvote ')
#upcomming product only 
router.register(f'upcomming_products', UpcommingProductViewSet, 'Upcomming Product ')
# route for product feature images 
router.register(f'product_images', ProductImageViewSet, 'Product Images')
# route for all the comment od products
router.register(f'comments', ProductCommentViewSet, 'Comment')
# api route for profile images table
router.register(f'product_icon', ProductIconViewSet, 'Product Icon Image')
# api route for Category of product table 
router.register(f'categories', CategoryViewSet, 'product Category ')

# Assigning the api urls which is used in main urls setting 
urlpatterns = [
    path('', HomePageView.as_view()),
    path('', include(router.urls)),
]