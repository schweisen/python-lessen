# vraag 2:
### optie 1:
```python
while dagen < 10:
    regenval = random.randint(0, 30)
    water_hoeveelheid = water_hoeveelheid + regenval

    if water_hoeveelheid > 100:
        break

    dagen = dagen + 1
```
### optie 2:
```python
while dagen < 10:>
    regenval = random.randint(0, 30)
    water_hoeveelheid = water_hoeveelheid + regenval
    dagen = dagen + 1

    if water_hoeveelheid > 100:
        continue
```
### optie 3:
```python
while dagen < 10:
    regenval = random.randint(0, 30)
    water_hoeveelheid = water_hoeveelheid + regenval
    dagen = dagen + 1

    if water_hoeveelheid > 100:
        break
```
### optie 4:
```python
while dagen < 10:
    regenval = random.randint(0, 30)
    water_hoeveelheid = water_hoeveelheid + regenval

    if water_hoeveelheid > 100:
        continue

    dagen = dagen + 1
```
