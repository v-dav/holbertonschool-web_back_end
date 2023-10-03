import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const theObject = {
    photo: null,
    user: null,
  };
  try {
    const photo = await uploadPhoto().then((result) => result);
    const user = await createUser().then((result) => result);
    if (photo !== undefined && user !== undefined) {
      theObject.photo = photo;
      theObject.user = user;
    }
  } catch (error) {
    console.log(error);
  }
  return theObject;
}
