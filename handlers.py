"""
Обработчики команд для Telegram бота
"""
import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from config import config

# Настройка логгера
logger = logging.getLogger(__name__)

# Создаем роутер для обработчиков
router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    """
    Обработчик команды /start
    Отправляет приветственное сообщение с информацией о доступных командах
    """
    try:
        await message.answer(config.START_MESSAGE)
        logger.info(f"Пользователь {message.from_user.id} выполнил команду /start")
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /start: {e}")
        await message.answer("An error occurred while processing the command. Please try again later.")

@router.message(Command("support"))
async def cmd_support(message: Message):
    """
    Обработчик команды /support
    Отправляет информацию о поддержке
    """
    try:
        await message.answer(config.SUPPORT_MESSAGE)
        logger.info(f"Пользователь {message.from_user.id} выполнил команду /support")
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /support: {e}")
        await message.answer("An error occurred while processing the command. Please try again later.")

@router.message(Command("check"))
async def cmd_check(message: Message):
    """
    Обработчик команды /check
    Отправляет статусное сообщение с текущим временем
    """
    try:
        await message.answer(config.CHECK_MESSAGE)
        logger.info(f"Пользователь {message.from_user.id} выполнил команду /check")
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /check: {e}")
        await message.answer("An error occurred while processing the command. Please try again later.")

@router.message()
async def handle_unknown_message(message: Message):
    """
    Обработчик для всех остальных сообщений
    Информирует пользователя о доступных командах
    """
    try:
        unknown_message = (
            "❓ Unknown command.\n\n"
            "Please use one of the available commands:\n"
            "/start - start working with the bot\n"
            "/support - get help\n"
            "/check - check status"
        )
        await message.answer(unknown_message)
        logger.info(f"Пользователь {message.from_user.id} отправил неизвестное сообщение: {message.text}")
    except Exception as e:
        logger.error(f"Ошибка при обработке неизвестного сообщения: {e}")
        await message.answer("An error occurred. Please try using the /start command")
