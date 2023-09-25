from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from apps.hotels.models import Hotel
from apps.reviews.forms import ReviewForm, ModerationForm
from apps.reviews.models import Review

@login_required()
def hotel_comments(request: Request, pk, parent):
    hotel = get_object_or_404(Hotel, pk=pk)
    comments = Review.objects.filter(hotel=hotel, user=request.user)
    if parent != 0:
        parent_comment = f"Reply to comment: {get_object_or_404(Review, id=parent)}"
    else:
        parent_comment = f"Hotel commentary: {hotel.name}"

    print(request.method)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.hotel_id = pk
            comment.user_id = request.user.id
            print(comment)
            try:
                parent_id = int(parent)
            except:
                parent_id = None
            if parent_id:
                parent_obj = Review.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = form.save(commit=False)
                    replay_comment.parent = parent_obj
            comment.save()
        return redirect("review_create", pk=pk, parent=parent)
    else:
        form = ReviewForm()
    context = {
        "form": form,
        "comments": comments,
        "hotel": hotel,
        "parent_comment": parent_comment
    }
    return render(request, "reviews/review_form.html", context)

@login_required()
def review_delete(request, hotel, parent, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()

    return redirect("review_create", pk=hotel, parent=parent)

@login_required()
def hotel_reviews(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    comments = Review.objects.filter(hotel=hotel, moderation=True)

    context = {
        "comments": comments,
        "hotel": hotel,
    }

    return render(request, "reviews/hotel_reviews.html", context)

@login_required()
def review_moderation(request):
    comments = Review.objects.filter(moderation=False)

    context = {
        "comments": comments,
    }

    return render(request, "reviews/review_moderation.html", context)

@login_required()
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ModerationForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("review_moderation")
    else:
        form = ModerationForm(instance=review)

    context = {
        "form": form,
        "title": "Модерация",
        "review": review,
    }

    return render(request, "reviews/review_update.html", context)

@login_required()
def unmoderation(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()

    return redirect("review_moderation")
