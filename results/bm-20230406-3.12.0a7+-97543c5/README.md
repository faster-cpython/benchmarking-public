# Results

- fork: brandtbucher
- version: 3.12.0a7+
- commit hash: [97543c5](https://github.com/brandtbucher/cpython/commit/97543c5)
- commit date: 2023-04-06T04:22:59-07:00
- commit merge base: [affedee8bf2ec00c404ffa39342a593a66bf95bd](https://github.com/brandtbucher/cpython/commit/affedee8bf2ec00c404ffa39342a593a66bf95bd)
- ref: fold_slices_more

## linux x86_64 (azure)

- [pystats raw](bm-20230406-azure-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-pystats.json)
- [pystats table](bm-20230406-azure-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4639091015)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-3.10.4.md)
- [plot](bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-3.11.0.md)
- [plot](bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-base.md)
- [plot](bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-base.png)

