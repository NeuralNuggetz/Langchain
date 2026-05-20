from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class CourtDetector:
 
    def __init__(self, model_path: str = COURT_MODEL_PATH):
        self.model_path = model_path
        self.model      = YOLO(model_path)
 
        # ── Public attributes populated after first detect() ──────────────
        self.is_detected        = False
        self.court_polygon      = None   # np.ndarray shape (N, 2)
        self.homography_matrix  = None   # 3×3 float64
        self.net_keypoints      = None   # {"left": (x,y), "right": (x,y)}
        self.all_keypoints      = None   # all detected keypoints (M, 2)
 
        # ── Internal ───────────────────────────────────────────────────────
        self._raw_result        = None
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    
    language=Language.PYTHON, 
    chunk_size=300, 
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(chunks)
print(len(chunks))