@app.get("/maintenance/calendar")
def calendar(db=Depends(get_db)):
    rows = db.execute(text("""
      SELECT asset_id, ts::date AS day, corrosion_index
      FROM inspections
      WHERE corrosion_index > 0.7
      ORDER BY day
    """)).fetchall()
    return rows
