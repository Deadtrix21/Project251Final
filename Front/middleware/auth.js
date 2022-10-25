export default function  (context) {
      const authed = context.store.getters['authModule/isAuthed']
      console.log(authed);
      if (!authed){
            context.redirect("/Login")

      }

}