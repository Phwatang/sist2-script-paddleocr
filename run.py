from sist2 import Sist2Index, print_progress
from paddleocr import PaddleOCR
import sys
import typer


def main(
    index_file: str, 
    lang="en",
    append_only=False,
    text_detection_model_name="PP-OCRv5_server_det",
    text_recognition_model_name="PP-OCRv5_server_rec",
    use_doc_orientation_classify=True, 
    use_doc_unwarping=True, 
    use_textline_orientation=True
):
    index = Sist2Index(index_file)

    # Paddle OCR model initialisation
    model = PaddleOCR(
        lang=lang,
        text_detection_model_name=text_detection_model_name,
        text_recognition_model_name=text_recognition_model_name,
        use_doc_orientation_classify=use_doc_orientation_classify,
        use_doc_unwarping=use_doc_unwarping,
        use_textline_orientation=use_textline_orientation,
    )

    # Only consider documents that were modified since the last run of this script
    paddle_version = index.get("paddle_version", default=0)
    where = f"version > {paddle_version} AND EXISTS (" \
            f"SELECT 1 FROM mime WHERE id=document.mime AND" \
            f"(name LIKE 'application/pdf' OR name LIKE 'image/jpg' OR name LIKE 'image/jpeg' OR name LIKE 'image/png'))"
    total = index.document_count(where)
    done = 0

    for doc in index.document_iter(where):
        # Perform PaddleOCR extraction
        output = model.predict(input = doc.path)
        extracts = output[0]["rec_texts"]
        all_text = "\n".join(extracts)

        # Record extracted text
        doc.json_data.setdefault("content", "")
        if append_only:
            doc.json_data["content"] += all_text
        else:
            doc.json_data["content"] = all_text
        index.update_document(doc)
        print(f"Performed PaddleOCR for {doc.rel_path}")

        done += 1
        print_progress(done = done, count = total)
        
    index.set("paddle_version", index.versions[-1].id)
    index.sync_tag_table()
    index.commit()
    print("Done!")

if __name__ == "__main__":
    typer.run(main)