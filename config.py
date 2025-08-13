"""
Конфигурация бота
"""
import os
import logging

# Настройка логгера
logger = logging.getLogger(__name__)

class Config:
    """Класс конфигурации бота"""
    
    def __init__(self):
        # Получаем токен бота из переменных окружения
        self.BOT_TOKEN = os.getenv("BOT_TOKEN", "")
        
        if not self.BOT_TOKEN:
            logger.error("BOT_TOKEN не найден в переменных окружения!")
            raise ValueError("BOT_TOKEN обязателен для работы бота")
        
        # Bot messages
        self.START_MESSAGE = (
            "Hi! 👋\n\n"
            "This bot is currently under development, so some features may not be available yet.\n\n"
            "- Use /check to verify any UAID Roblox limited item for potential issues or if it's \"poisoned\".\n"
            "- If you need assistance or have any questions, you can use /support to contact our support team.\n\n"
            "Thank you for your patience and understanding! 😊"
        )
        
        self.SUPPORT_MESSAGE = (
            "💬 For any questions, contact @UAIDSupport"
        )
        
        self.CHECK_MESSAGE = (
            "This command is currently unavailable. The bot is still under development. Sorry for the inconvenience."
        )

# Создаем глобальный экземпляр конфигурации
config = Config()
