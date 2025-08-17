"""
Script for building vector store for the first time.
"""

from dotenv import load_dotenv
from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from utils.logger import get_logger
from utils.custom_exception import CustomException


load_dotenv()

logger = get_logger(__name__)


def main():
    try:
        logger.info("Building pipeline...")
        # Initialize dataloader:
        loader = AnimeDataLoader(
            "data/anime_with_synopsis.csv", "data/anime_updated.csv"
        )
        processed_csv = loader.load_and_process()
        logger.info("Data loaded and processed")

        # Build Chroma vectorstore:
        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()
        logger.info("Vector store built successfully.")

        logger.info("Pipeline built successfully.")

    except Exception as e:
        print(f"Error building pipeline: {str(e)}")


if __name__ == "__main__":
    main()
