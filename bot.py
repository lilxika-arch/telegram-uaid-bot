"""
Основной модуль Telegram бота
"""
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import config
from handlers import router

# Настройка логгера
logger = logging.getLogger(__name__)

async def main():
    """
    Основная функция для запуска бота
    """
    try:
        # Создаем объект бота с настройками по умолчанию
        bot = Bot(
            token=config.BOT_TOKEN,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML
            )
        )
        
        # Создаем диспетчер
        dp = Dispatcher()
        
        # Регистрируем роутер с обработчиками
        dp.include_router(router)
        
        logger.info("Бот запускается...")
        
        # Удаляем webhook и очищаем очередь обновлений
        await bot.delete_webhook(drop_pending_updates=True)
        
        logger.info("Бот успешно запущен и готов к работе!")
        
        # Запускаем polling
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"Критическая ошибка при запуске бота: {e}")
        sys.exit(1)
    finally:
        # Закрываем сессию бота при завершении
        if 'bot' in locals():
            await bot.session.close()
            logger.info("Сессия бота закрыта")

if __name__ == "__main__":
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )
    
    # Запуск бота
    asyncio.run(main())
