export default function  (context) {
      const authed = context.store.getters['authModule/isAdmin']
      if (authed.details != null && authed.details != "null")
      {console.log(authed);}
      if (authed.isAdmin == false){context.redirect("/Login")}
      if (authed.details == null ){context.redirect("/Login")}
}