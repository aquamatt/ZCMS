alter table `zcms_cmscomponentvalue` add `site` integer NULL;
alter table `zcms_cmstokenvalue` add `site` integer NULL;
update `zcms_cmscomponentvalue` set site=0;
update `zcms_cmstokenvalue` set site=0;