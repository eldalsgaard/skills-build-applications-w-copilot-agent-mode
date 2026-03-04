from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, date='2023-01-01'),
            Activity(user=users[1], type='Cycling', duration=45, date='2023-01-02'),
            Activity(user=users[2], type='Swimming', duration=60, date='2023-01-03'),
            Activity(user=users[3], type='Yoga', duration=50, date='2023-01-04'),
        ]
        for activity in activities:
            activity.save()

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body workout', suggested_for='Marvel'),
            Workout(name='Squats', description='Lower body workout', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
