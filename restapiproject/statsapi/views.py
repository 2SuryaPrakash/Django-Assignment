from django.db.models import Avg, Max, Min, F
from django.http import JsonResponse
from .models import Student, Placement, PlacementApplication
import statistics  # Python's built-in statistics module

def placement_statistics(request):
    branches = Student.objects.values_list('branch', flat=True).distinct() #getting unique branches
    stats = {
        "highest_ctc": {},
        "median_ctc": {},
        "lowest_ctc": {},
        "average_ctc": {},
        "percentage_placed": {},
        "students": []
    }

    for branch in branches:
        students_in_branch = Student.objects.filter(branch=branch)
        total_students = students_in_branch.count() or None

        placed_students = (
            PlacementApplication.objects.filter(student__branch=branch, selected=True)
            .values("student")  #groupby students
            .distinct()  #get unique students
            .count()
        ) or None

        placements_in_branch = PlacementApplication.objects.filter(student__branch=branch, selected=True)

        ctc_values = [app.placement.ctc for app in placements_in_branch if app.placement and app.placement.ctc is not None]

        stats["highest_ctc"][branch] = max(ctc_values, default=None)
        stats["lowest_ctc"][branch] = min(ctc_values, default=None)
        # Average of all CTCs in each branch- given. So we are not taking the average of max of each student.
        stats["average_ctc"][branch] = sum(ctc_values) / len(ctc_values) if ctc_values else None 

        stats["median_ctc"][branch] = statistics.median(ctc_values) if ctc_values else 0

        stats["percentage_placed"][branch] = (placed_students / total_students * 100) if total_students and placed_students else None

    students = Student.objects.all()
    for student in students:
        applications = PlacementApplication.objects.filter(student=student, selected=True)
        stats["students"].append({
            "rollno": student.rollno,
            "branch": student.branch,
            "batch": student.batch,
            "companies_selected": [app.placement.name for app in applications],
            "ctc": max((app.placement.ctc for app in applications if app.placement and app.placement.ctc is not None), default=None)    
        })
    stats = {key: (value if value else None) for key, value in stats.items()} # checking if any field  is empty. if so it is None
    return JsonResponse(stats)
