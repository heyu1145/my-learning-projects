const PENDING = 'pending'
const RESOLVED = 'fulfilled'
const REJECTED = 'rejected'

class MyPromise {
    #status = PENDING
    #result = void 0
    #callbacks = []
    #handled = false
    #runthen() {
        if (this.#status === PENDING) return;

        queueMicrotask(() => {
            for (const [onFulfilled, onRejected, resolve, reject] of this.#callbacks) {
                try {
                    if (this.#status === RESOLVED) {
                        const result = this.#handleCallback(onFulfilled?.(this.#result))
                        resolve(result)
                    } else {
                        if (!onRejected) {
                            reject(this.#result)
                        } else {
                            const result = this.#handleCallback(onRejected(this.#result))
                            resolve(result)
                            this.#handled = true
                        }
                    }
                } catch (e) {
                    reject(e)
                }
            }
        })

        setTimeout(() => {
            if (this.#handled) return;
            if (window) {
                const event = new PromiseRejectionEvent('unhandledrejection', {
                    promise: this,
                    reason: this.#result
                })
                window.dispatchEvent(event)
            } else if (process) {
                process.emit('unhandledrejection', this.#result, this)
            }
        }, 0)
    }

    #handleCallback(value, reject) {
        let result;
        if (typeof value?.then !== 'function') return value;
        try {
            value.then(v => {
                result = this.#handleCallback(v, reject)
            }, (e) => {
                result = e
                reject(e)
            })
        } catch (e) {
            result = e
            reject(e)
        }
        return result
    }

    constructor(callback) {
        if (typeof callback !== 'function') throw new TypeError('callback must be a function')
        const resolve = v => {
            if (this.#status !== PENDING) return;
            v = this.#handleCallback(v, reject)
            this.#status = RESOLVED
            this.#result = v
            this.#runthen()
        }
        const reject = e => {
            if (this.#status !== PENDING) return;
            e = this.#handleCallback(e, reject)
            this.#status = REJECTED
            this.#result = e
            this.#runthen()
        }

        try {
            callback(resolve, reject)
        } catch (e) {
            reject(e)
        }
    }
    static resolve(value) {
        return new MyPromise(res => res(value))
    }
    static reject(err) {
        return new MyPromise(_, rej => rej(err))
    }
    then(onFulfilled, onRejected) {
        return new MyPromise((res, rej) => {
            this.#callbacks.push([
                typeof onFulfilled === 'function'
                    ? onFulfilled
                    : undefined,
                typeof onRejected === 'function'
                    ? onRejected
                    : undefined,
                res,
                rej
            ])
        })
    }
    catch(callback) {
        return new this.then(undefined, callback)
    }
    finally(callback) {
        return this.then(callback, callback)
    }
}
