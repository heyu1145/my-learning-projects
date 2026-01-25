type JSTypeMap = {
  'string': string;
  'number': number;
  'boolean': boolean;
  'object': object;
}

type JSType = keyof JSTypeMap;

type MapTypes<T extends readonly JSType[]> = {
  [K in keyof T]: T[K] extends JSType ? JSTypeMap[T[K]] : never;
}

declare function impl<T extends readonly JSType[], R>(
  ...args: [...types: T, func: (...args: MapTypes<T>) => R]
): (...runtimeArgs: MapTypes<T>) => R;
