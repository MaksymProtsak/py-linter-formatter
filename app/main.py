def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8"
            }
            for error in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": [
            {
                "line": error_descr["line_number"],
                "column": error_descr["column_number"],
                "message": error_descr["text"],
                "name": error_descr["code"],
                "source": "flake8",
            }
            for error_descr in linter_report[source_code_key]]
            if linter_report[source_code_key] != [] else [],
         "path": source_code_key,
         "status": "passed" if linter_report[source_code_key] == []
         else "failed"}
        for source_code_key in linter_report
    ]
