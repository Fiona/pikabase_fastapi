-- upgrade --
CREATE TABLE IF NOT EXISTS "pokemon" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "number_national" INT NOT NULL,
    "slug" VARCHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "element_1_id" INT NOT NULL REFERENCES "elementtype" ("id") ON DELETE CASCADE,
    "element_2_id" INT REFERENCES "elementtype" ("id") ON DELETE CASCADE
);
-- downgrade --
DROP TABLE IF EXISTS "pokemon";
