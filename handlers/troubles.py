# Тут части кода, которые дорабатываются


@user_private_router.message(Form.purpose, F.text)
async def question(message: types.Message, state: FSMContext):
    await state.update_data(purpose=message.text)
    await message.answer("Добавим фото?", reply_markup=get_keyboard(
        "Да",
        "Нет",
        "Отмена",
        # "Предыдущий вопрос",
        placeholder="Выбери вариант ответа",
        sizes=(2, 1)))
    await state.set_state(Form.image)


@user_private_router.message(Form.image, F.photo, F.text)
async def question2(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await message.answer("Добавьте фото")
        await state.set_state(Form.image)
    elif message.text == "Нет":
        await state.update_data(image=message.text)
        await message.answer("Хорошо, можете оставить свои контакты для связи?", reply_markup=get_keyboard(
            "Отмена",
            # "Предыдущий вопрос",
            placeholder="Оставь контакт для связи",
            sizes=(1,)))
        await state.set_state(Form.contact)
    else:
        await message.answer("Пожалуйста, выберите 'Да' или 'Нет'.")


@user_private_router.message(Form.image, F.photo)
async def add_image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    await message.answer("Хорошо, можете оставить свои контакты для связи?", reply_markup=get_keyboard(
        "Отмена",
        # "Предыдущий вопрос",
        placeholder="Оставь контакт для связи",
        sizes=(1,)))
    await state.set_state(Form.contact)