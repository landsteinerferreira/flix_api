from django.db import models

NATIONALITY_CHOICES = (
    ('BRAZIL', 'Brasil'),
    ('ARGENTINA', 'Argentina'),
    ('CHILE', 'Chile'),
    ('URUGUAY', 'Uruguai'),
    ('PARAGUAY', 'Paraguai'),
    ('UNITED_STATES', 'Estados Unidos'),
    ('CANADA', 'Canadá'),
    ('MEXICO', 'México'),
    ('PORTUGAL', 'Portugal'),
    ('SPAIN', 'Espanha'),
    ('FRANCE', 'França'),
    ('GERMANY', 'Alemanha'),
    ('ITALY', 'Itália'),
    ('UNITED_KINGDOM', 'Reino Unido'),
    ('JAPAN', 'Japão'),
    ('CHINA', 'China'),
    ('INDIA', 'Índia'),
    ('AUSTRALIA', 'Austrália'),
    ('SOUTH_AFRICA', 'África do Sul'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name
    
    