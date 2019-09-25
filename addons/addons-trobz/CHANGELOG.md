# Addons Trobz Change Logs
## 12.0-Trobz
- 20181010: Migrate trobz-modules to V12
## 11.0-Trobz
- 20180423: Fix the issue "global name 'unicode' is not defined"
- 20180420: Fix the issue when update company logo
- 20180417: Fix the issue of missing field Profile Group in the form view of User.
- 20171127: Migrate addons-trobz to Odoo 11

## 10.0-Trobz
- 20170605: Fix issue when modify inherited group.
    - Case issue: g1 inherit g3, g2 inherit g3. If user `fa` in profile `Function Admin` has two groups: `g1`, `g2`, the represent of `g3` and user `fa` in `res_group_res_users_rel` relationship table exist just 1: `fa` - `g3`, so if we removed `g1` from `FA`, `g3` - `fa` is removed also => It's not correct because `g2` is still in `FA` profile, so must keep `g3` - `fa`.

- 20170602: Add `worker-loger` module
- 20170601: Improve function `update_config` to support all types of config
- 20161110: Only superuser can edit only group of superuser
- 20161102: Fix issue should display model_name when input incorrect `model` in module `access_right_generator`
- 20161030:
    - Use `_register_hook` to run pos_object instead of tag `function` in `trobz_base` and `trobz_report_base`.
    - Fix missing description warning of modules `user_profile` and `trobz_report_base`
- 20161024: Move `advance_language_export` to `dev-tools` repo.
- 20161018:
    - Can't login after creating new user or re-set password because the change of odoo 10.
    - Auto support create profile "Functional Admin" and create manager account with this profile
    after install module `trobz_base`.
- 20161014:
    - Temporay migrate addons-trobz repo to version 10:
        - access_right_generator (need to test carefully)
        - advance_language_export (need to test carefully)
        - user_profile (need to test carefully)
    - Fix Warning syntax for all modules
    - In `user_profile` module:
        - move `_is_admin` function to `trobz_base` because this function needs group `trobz_base.group_configure_user` in `trobz_base`.
        - remove `update_user_groups_view` function because of overriding whole core function, in v10 funtion change name to
        `_update_user_groups_view` => Override `field_view_get` to make readonly all fields on tab `access_right`
        - migrate `check_recursive` to new `api.constrain`.
        - fix bug when removing inheritance group of defined profile.
    - In `trobz_base` module:
        - move `_get_all_users_ids_by_logins` function to `user_profile` because this function is only used in `user_profile`
        but `user_profile` must NOT depend on `trobz_base
        - move `tz` field to model `res.partner`, implement default as new api


## 9.0-Trobz
- 20160819: Remove module `connector_enhance` because it's depends on `connector` module, move it to [`connector`](https://gitlab.trobz.com/odoo/connector) repo
- 20160815: Add module `connector_enhance`
- 20160713: `F#15377` [commit 1](https://gitlab.trobz.com/odoo/addons-trobz/commit/8df2d28518c10c1e0251127bf6158bdfb16094f3) [commit 2](https://gitlab.trobz.com/odoo/addons-trobz/commit/d6dba3cbf1ebf4b5deff57588ecde6bdd636eb42)
    - when upgrading `trobz_base` by `emoi`, upgrading all trobz modules also
- 20160705: [commit](https://gitlab.trobz.com/odoo/addons-trobz/commit/9b6f230bc5dcea0f7d7eb44395a96ff430592b26)
    - Move `module_category_profile` from `trobz_base to user_profile`. This category record should be placed `user_profile` module
    - Adjust the related source code in function `make_default_manager_groups`
    - For function `create_profiles`, please keep it temporarily, then we will discuss whether keep it or not. Currently, project Manuchar is using this function.
- 20160627 - Refactor `security_safe_password`:
    - Add controller to avoid `change_password` router to show message from `security_safe_password`.
    - Fix message enter character.
    - Fix change_password_button method.
- 20160616 - Change dependency module `disable_openerp_online` to `disable_odoo_online` because the change of module name in `server-tools` repo
    - Fix for database on existing instance:
        - update ir_module_module set name='disable_odoo_online' where name = 'disable_openerp_online'
        - update ir_module_module_dependency set name='disable_odoo_online' where name ilike 'disable_openerp_online'
- [F#15957](https://tms.trobz.com/web?#id=15957&view_type=form&model=tms.forge.ticket&action=257) - [`trobz_base`] Remove maintenance error

## 8.0 Master
[F#15957](https://tms.trobz.com/web?#id=15957&view_type=form&model=tms.forge.ticket&action=257) - [`trobz_base`] Remove maintenance error

## 7.0 Master
[F#15957](https://tms.trobz.com/web?#id=15957&view_type=form&model=tms.forge.ticket&action=257) - [`trobz_base`] Remove maintenance error

