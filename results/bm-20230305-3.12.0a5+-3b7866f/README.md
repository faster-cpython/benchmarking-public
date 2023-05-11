# Results

- fork: gvanrossum
- version: 3.12.0a5+
- commit hash: [3b7866f](https://github.com/gvanrossum/cpython/commit/3b7866f)
- commit date: 2023-03-05T11:34:50-08:00
- commit merge base: [cb944d0be869dfb1189265467ec8a986176cc104](https://github.com/gvanrossum/cpython/commit/cb944d0be869dfb1189265467ec8a986176cc104)
- ref: tagged_ptrs

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4340750647)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5%2B-3b7866f.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5%2B-3b7866f-vs-3.10.4.md)
- [plot](bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5%2B-3b7866f-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5%2B-3b7866f-vs-3.11.0.md)
- [plot](bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5%2B-3b7866f-vs-3.11.0.png)

### vs. base

- 1.02x slower
- [table](bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5%2B-3b7866f-vs-base.md)
- [plot](bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5%2B-3b7866f-vs-base.png)

