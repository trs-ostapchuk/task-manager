from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from tasks.models import Task, TaskType, Position
import random

fake = Faker()
User = get_user_model()


class Command(BaseCommand):
    help = "Seed database with fake positions, workers, task types, and tasks"

    def handle(self, *args, **kwargs):
        # --- Create positions ---
        positions = [
            "Frontend Developer", "Backend Developer",
            "Project Manager", "QA Engineer", "Designer"
        ]
        position_objs = []
        for pos in positions:
            position, created = Position.objects.get_or_create(name=pos)
            position_objs.append(position)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(position_objs)} positions."))

        # --- Create task types ---
        task_types = ["Feature", "Bugfix", "Code Review", "Testing", "Deployment"]
        task_type_objs = []
        for t in task_types:
            tt, created = TaskType.objects.get_or_create(name=t)
            task_type_objs.append(tt)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(task_type_objs)} task types."))

        # --- Create workers ---
        workers = []
        for _ in range(10):
            username = fake.user_name()
            worker, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": fake.email(),
                    "position": random.choice(position_objs),
                    "password": "pbkdf2_sha256$..."  # не потрібно для розробки
                }
            )
            workers.append(worker)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(workers)} workers."))

        # --- Create tasks ---
        for _ in range(20):
            task = Task.objects.create(
                name=fake.sentence(nb_words=4),
                description=fake.text(max_nb_chars=100),
                deadline=fake.future_datetime(end_date="+10d"),
                is_completed=random.choice([True, False]),
                priority=random.choice([p[0] for p in Task.Priority.choices]),
                task_type=random.choice(task_type_objs),
            )

            # Assign random workers (1–3 per task)
            assigned = random.sample(workers, random.randint(1, 3))
            task.assignees.set(assigned)

        self.stdout.write(self.style.SUCCESS("🎉 Successfully populated database with fake data!"))
