from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Team1")
        user = User.objects.create(name="Test User", email="test@example.com", team=team)
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.team.name, "Team1")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team2")
        self.assertEqual(team.name, "Team2")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", difficulty="Easy")
        self.assertEqual(workout.name, "Pushups")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Team3")
        user = User.objects.create(name="User2", email="user2@example.com", team=team)
        workout = Workout.objects.create(name="Squats", difficulty="Medium")
        activity = Activity.objects.create(user=user, workout=workout, duration_minutes=30, calories_burned=200)
        self.assertEqual(activity.user.name, "User2")
        self.assertEqual(activity.workout.name, "Squats")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team4")
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, rank=1)
        self.assertEqual(leaderboard.team.name, "Team4")
        self.assertEqual(leaderboard.total_points, 100)
