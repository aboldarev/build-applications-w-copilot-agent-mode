from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel, is_superhero=True)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel, is_superhero=True)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc, is_superhero=True)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc, is_superhero=True)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        run = Workout.objects.create(name='Run', description='Running workout', difficulty='Medium')
        swim = Workout.objects.create(name='Swim', description='Swimming workout', difficulty='Hard')
        lift = Workout.objects.create(name='Lift', description='Weight lifting', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=tony, workout=run, duration_minutes=30, calories_burned=300)
        Activity.objects.create(user=steve, workout=swim, duration_minutes=45, calories_burned=400)
        Activity.objects.create(user=bruce, workout=lift, duration_minutes=60, calories_burned=500)
        Activity.objects.create(user=clark, workout=run, duration_minutes=25, calories_burned=250)

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, total_points=700, rank=1)
        Leaderboard.objects.create(team=dc, total_points=750, rank=0)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
