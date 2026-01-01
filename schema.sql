PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS problems (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  name          TEXT NOT NULL UNIQUE,
  link          TEXT,
  difficulty    TEXT CHECK(difficulty IN ('Easy','Medium','Hard')) NOT NULL,
  tags          TEXT DEFAULT '',
  created_at    TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS attempts (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  problem_id     INTEGER NOT NULL,
  attempt_date   TEXT NOT NULL, -- YYYY-MM-DD
  result         TEXT CHECK(result IN ('pass','fail')) NOT NULL,
  time_spent_min INTEGER NOT NULL DEFAULT 0,
  notes          TEXT DEFAULT '',
  mistake_type   TEXT DEFAULT '',
  created_at     TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY(problem_id) REFERENCES problems(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS redo_schedule (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  attempt_id    INTEGER NOT NULL,
  problem_id    INTEGER NOT NULL,
  due_date      TEXT NOT NULL, -- YYYY-MM-DD
  status        TEXT CHECK(status IN ('pending','done','skipped')) NOT NULL DEFAULT 'pending',
  completed_at  TEXT,
  created_at    TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY(attempt_id) REFERENCES attempts(id) ON DELETE CASCADE,
  FOREIGN KEY(problem_id) REFERENCES problems(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_attempts_date ON attempts(attempt_date);
CREATE INDEX IF NOT EXISTS idx_schedule_due ON redo_schedule(due_date, status);
