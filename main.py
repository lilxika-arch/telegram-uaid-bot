#!/usr/bin/env python3
"""
Точка входа для Telegram бота
"""
import asyncio
import logging
from bot import main

if __name__ == "__main__":
    # Настройка базового логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Запуск бота
    asyncio.run(main())
