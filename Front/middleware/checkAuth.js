export default function  (context) {
      if (process.client){
            context.store.dispatch("authModule/initAuth")
            console.log("[CheckAuth-Module]Auth Checks");
      }
}