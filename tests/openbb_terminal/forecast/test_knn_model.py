from openbb_terminal.forecast import knn_model


def test_get_knn_model(tsla_csv):
    df = tsla_csv.set_index("date")
    knn_model.get_knn_model_data(
        df["close"],
        input_chunk_length=5,
        n_neighbors=5,
        test_size=0.5,
        end_date=None,
        no_shuffle=True,
    )
