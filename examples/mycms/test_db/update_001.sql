alter table `zcms_language` add `fallback_id` integer NULL;
alter table `zcms_cmscomponent` drop `language_id`;
alter table `zcms_cmstoken` drop `value`;
alter table `zcms_cmstoken` add `value` longtext NOT NULL;
