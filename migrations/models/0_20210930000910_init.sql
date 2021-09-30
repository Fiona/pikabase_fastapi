-- upgrade --
CREATE TABLE IF NOT EXISTS "elementtype" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "slug" VARCHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
