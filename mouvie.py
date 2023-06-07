import cv2
import numpy as np
from base_pyfile import get_all_files, get_files, read_text_file, unique_path


def crf2movie(ext=".mp4"):
    # 動画のフレームサイズとFPSを設定
    frame_width = 1280
    frame_height = 720
    fps = 30.0

    # 出力ファイル名とコーデックを指定して動画ファイルを作成
    if not "." in ext:
        ext = "." + ext

    output_filename = unique_path(f"video{ext}")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

    for video_path in get_all_files(
        r"C:\Users\yamamotok\AppData\Roaming\カメラ一発!\Recording\L@012069226-012069226\20230531",
        ".crf",
    ):
        cap = cv2.VideoCapture(str(video_path))
        while cap.isOpened():
            # フレームを1つずつ読み込む
            ret, frame = cap.read()

            # フレームが正常に読み込まれた場合
            if ret:
                # ここでフレームに対して処理を行います
                # 例えば、フレームを表示する場合は、以下のようになります:
                # cv2.imshow('Frame', frame)
                video_writer.write(frame)

                # cv2.imwrite(unique_path("F:\camera\{:05}.png"),frame)

                # # 'q'キーが押されたらループを抜ける
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break
            else:
                break
    # cv2.destroyAllWindows()

    # 動画ファイルをクローズ
    video_writer.release()
    cap.release()
