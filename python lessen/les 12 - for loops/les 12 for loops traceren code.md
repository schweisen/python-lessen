# vraag 4:
### optie 1:
```python
import garden

plant_nummer = 1

for i in range(plant_nummer, 16):
    garden.water(plant_nummer)
    garden.bemest(plant_nummer)
```
### optie 2:
```python
import garden

num_planten = 15

for plant_nummer in range(1, num_planten + 1):
    garden.water(plant_nummer)

garden.bemest(plant_nummer)
```
### optie 3:
```python
import garden

num_planten = 15

for plant_nummer in range(1, num_planten + 1):
    garden.water(plant_nummer)
    garden.bemest(plant_nummer)
```
### optie 4:
```python
import garden

plant_nummer = 1

for i in range(plant_nummer, 16):
    garden.water(plant_nummer)

garden.bemest(plant_nummer)
```