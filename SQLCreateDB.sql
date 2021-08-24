CREATE DATABASE IF NOT EXISTS `daisyKnitSurvey` DEFAULT CHARACTER SET utf8mb4 ;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`user` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id_tel` INT UNSIGNED NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `middle_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `telephone` VARCHAR(16) NOT NULL,
  `authorized` BOOLEAN NULL,
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id_tel` ASC) VISIBLE,
  UNIQUE INDEX `telephone_UNIQUE` (`telephone` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`survey` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `description` VARCHAR(255) NULL,
  `updated` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`question_type` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` ENUM('callback', 'quiz', 'message') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`response_choice` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`question` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `name_eng` VARCHAR(255) NOT NULL,
  `question_type_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  UNIQUE INDEX `name_eng_UNIQUE` (`name_eng` ASC) VISIBLE,
  INDEX `fk_question_type_id_idx` (`question_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_question_type_id`
    FOREIGN KEY (`question_type_id`)
    REFERENCES `daisyKnitSurvey`.`question_type` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`response_choice_order` (
  `question_id` INT UNSIGNED NOT NULL,
  `response_choice_id` INT UNSIGNED NOT NULL,
  `order` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`question_id`, `response_choice_id`),
  INDEX `fk_response_choice_id_idx` (`response_choice_id` ASC) VISIBLE,
  CONSTRAINT `fk_question_id`
    FOREIGN KEY (`question_id`)
    REFERENCES `daisyKnitSurvey`.`question` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_response_choice_id`
    FOREIGN KEY (`response_choice_id`)
    REFERENCES `daisyKnitSurvey`.`response_choice` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`question_order` (
  `question_id` INT UNSIGNED NOT NULL,
  `survey_id` INT UNSIGNED NOT NULL,
  `order` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`question_id`, `survey_id`, `order`),
  INDEX `fk_survey_id_idx` (`survey_id` ASC) VISIBLE,
  CONSTRAINT `fk_qo_question_id`
    FOREIGN KEY (`question_id`)
    REFERENCES `daisyKnitSurvey`.`question` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_survey_id`
    FOREIGN KEY (`survey_id`)
    REFERENCES `daisyKnitSurvey`.`survey` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`survey_response` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `survey_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sr_survey_id_idx` (`survey_id` ASC) VISIBLE,
  INDEX `fk_user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_sr_survey_id`
    FOREIGN KEY (`survey_id`)
    REFERENCES `daisyKnitSurvey`.`survey` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `daisyKnitSurvey`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `daisyKnitSurvey`.`response` (
  `user_id` INT UNSIGNED NOT NULL,
  `question_id` INT UNSIGNED NOT NULL,
  `survey_response_id` INT UNSIGNED NOT NULL,
  `answer` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`user_id`, `question_id`, `survey_response_id`),
  INDEX `fk_r_question_id_idx` (`question_id` ASC) VISIBLE,
  INDEX `fk_r_survey_response_id_idx` (`survey_response_id` ASC) VISIBLE,
  CONSTRAINT `fk_r_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `daisyKnitSurvey`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_r_question_id`
    FOREIGN KEY (`question_id`)
    REFERENCES `daisyKnitSurvey`.`question` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_r_survey_response_id`
    FOREIGN KEY (`survey_response_id`)
    REFERENCES `daisyKnitSurvey`.`survey_response` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
