# О приложении
Приложение создано для генерации и редктирования изображений, используя обработанный шум.

## Использование

<details>
<summary>Основа выглядит так</summary>

```
noizy.py [-h] {gen,edit} ...
```
Где вместо `...` пишутся параметры, зависящие от режима (`gen` или `edit`).
</details>

Подробнее можо почитать [тут][full-usage].

#### Примеры

###### Генерация

Запустим приложение со следующими параметрами:

```
gen grayscale lines-many /path/to/destination --width 500 --height 500 -t png -s 50
```
Получим:

![Полученное изображение](./examples/gen__grayscale__lines-many__--width_500__--height_500__-t_png__-s_50.png)

Попробуем:

```
gen color levels /path/to/destination --width 500 --height 500 -t png -s 50
```
Получим:

![Полученное изображение](./examples/gen__color__levels__--width_500__--height_500__-t_png__-s_50.png)


###### Изменение

В отличие от генерации, высота и ширина берутся из исходного изображения. В качестве примером будем брать изображения [отсюда][images-source].

Запустим приложение со следующими параметрами:

```
edit channels levels-ymc /path/to/source_image1.jpg /path/to/destination -t png -s 50
```
<details>
<summary>Исходное изображение</summary>

![Полученное изображение](./examples/source_image1.jpg)
</details>

Результат:
![Полученное изображение](./examples/edit__channels__levels-ymc__-t_png__-s__50.png)

Теперь попробуем:

```
edit channels levels-bmc /path/to/source_image2.jpg /path/to/destination -t png -s 20
```
<details>
<summary>Исходное изображение</summary>

![Полученное изображение](./examples/source_image2.jpg)
</details>

Результат:
![Полученное изображение](./examples/edit__channels__levels-bmc__-t_png__-s__20.png)


[images-source]: https://thispersondoesnotexist.com/ "Источник изображений"
[full-usage]: ./USAGE.md