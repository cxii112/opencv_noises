# О приложении
Приложение создано для генерации и редактирования изображений, используя обработанный шум.

## Использование

Убедитесь, что у Вас уже установленны необходимые [зависимости][requirements]. 
Подробнее про использование можно почитать [тут][full-usage], полный список эффектов с примерами [здесь][full-effects].
Чтобы создать изображение, достаточно запустить:

```
noizy.py gen grayscale lines /path/to/destination
```
Получим:

![Полученное изображение](./examples/gen__grayscale__lines.png)

Для изменения:
```
noizy.py edit channels levels-rgb /path/to/source.image /path/to/destination
```
Получим:

![Полученное изображение](./examples/edit__channels__levels-ymc.png)

[images-source]: https://thispersondoesnotexist.com/ "Источник изображений"
[full-usage]: ./USAGE.md
[full-effects]: ./EFFECTS.md
[requirements]: ./requirements.txt