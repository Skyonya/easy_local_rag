import os

from semantic_text_splitter import HuggingFaceTextSplitter
from tokenizers import Tokenizer


def create_chunks(
        semantic_tokenizer,
        documents_path,
        max_tokens,
        separate_chunk_method,
        separator,
        silent=True
):
    # make chunks
    tokenizer = Tokenizer.from_pretrained(semantic_tokenizer)
    splitter = HuggingFaceTextSplitter(tokenizer, trim_chunks=False)
    chunks = ['']

    # read the files
    for filename in os.listdir(documents_path):
        path = os.path.join(documents_path, filename)
        with open(path, mode='r', encoding='utf=8') as f:
            text = f.read()

        # if separated by separator
        if separate_chunk_method == 'separator':
            chunks = [*chunks, *text.split(separator)]

        # if separated by semantic
        else:
            def text_split(_text, split_max_chat_count):
                return [_text[i: i + split_max_chat_count] for i in range(0, len(text), split_max_chat_count)]

            splits = text_split(text, 10000)
            total_splits = len(splits)
            if not silent:
                print(f'Created {total_splits} splits from {path}')
            for i, split in enumerate(splits):
                current_chunks = len(chunks)
                chunks = [*chunks, *splitter.chunks(split, max_tokens)]
                if not silent:
                    print(f'Created chunks {len(chunks) - current_chunks} for split {i}/{total_splits} of {path}')
                    print(f'Current chunks: {len(chunks)}')

    if not silent:
        print(f'Total chunks: {len(chunks)}')

    return chunks
