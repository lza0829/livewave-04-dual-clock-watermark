"""水位线读写辅助（口径与推进主逻辑在 modules/双钟水位线 与 services/装载）。"""


def 读(conn, 房间键: str):
    return conn.execute("SELECT * FROM 水位线 WHERE 房间键=?", (房间键,)).fetchone()
