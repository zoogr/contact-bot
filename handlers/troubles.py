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
    await state.set_state(Form.image)

@user_private_router.message(Form.image, F.photo, F.text.casefold() == "да")
async def add_image(message: types.Message, state: FSMContext):
    if message.text.casefold() == "нет":
        await state.update_data(image=message.text)
        await message.answer("Хорошо, можете оставить свои контакты для связи?", reply_markup=get_keyboard(
            "Отмена",
            # "Предыдущий вопрос",
            placeholder="Оставь контакт для связи",
            sizes=(1,)))
        await state.set_state(Form.contact)
    else:
        await state.update_data(image=message.photo[-1].file_id)
        await message.answer("Хорошо, можете оставить свои контакты для связи?", reply_markup=get_keyboard(
            "Отмена",
            # "Предыдущий вопрос",
            placeholder="Оставь контакт для связи",
            sizes=(1,)))
        await state.set_state(Form.contact)

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


@user_private_router.message(Form.image, F.photo, F.text)
async def question2(message: types.Message, state: FSMContext):
    await state.update_data(purpose=message.text)
    if F.text == "Да":
        await message.answer("Добавьте фото")
        await state.set_state(Form.image)
    elif F.text == "Нет":
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





@user_private_router.message(Form.purpose, F.text)
async def add_purpose(message: types.Message, state: FSMContext):
    await state.update_data(purpose=message.text)
    await message.answer("Хорошо, можете оставить свои контакты для связи?", reply_markup=get_keyboard(
        "Отмена",
        # "Предыдущий вопрос",
        placeholder="Оставь контакт для связи",
        sizes=(1,)))
    await state.set_state(Form.contact)





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
    if message.text == "Да":
        await state.set_state(Form.image)
        await message.answer("Добавьте фото")
    else:
        await state.set_state(Form.image2)


@user_private_router.message(Form.image, F.photo, F.text.casefold() == "да")
async def add_image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    await message.answer("Хорошо, можете оставить свои контакты для связи?", reply_markup=get_keyboard(
        "Отмена",
        # "Предыдущий вопрос",
        placeholder="Оставь контакт для связи",
        sizes=(1,)))
    await state.set_state(Form.contact)


@user_private_router.message(Form.image2, F.text, F.text.casefold() == "нет")
async def add_image2(message: types.Message, state: FSMContext):
    await state.update_data(image=message.text)
    await message.answer("Хорошо, можете оставить свои контакты для связи?", reply_markup=get_keyboard(
        "Отмена",
        # "Предыдущий вопрос",
        placeholder="Оставь контакт для связи",
        sizes=(1,)))
    await state.set_state(Form.contact)
