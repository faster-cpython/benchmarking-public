# Results

- fork: eduardo-elizondo
- version: 3.12.0a4+
- commit hash: [a748e80](https://github.com/eduardo%2delizondo/cpython/commit/a748e80)
- commit date: 2023-01-29T16:15:56-05:00
- commit merge base: [666c0840dcac9941fa41ec619fef8d45cd849a0b](https://github.com/eduardo%2delizondo/cpython/commit/666c0840dcac9941fa41ec619fef8d45cd849a0b)
- ref: immortal_references

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4418536675)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230129-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a4%2B-a748e80.json)

### vs. 3.10.4

- 1.23x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230129-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a4%2B-a748e80-vs-3.10.4.md)
- [plot](bm-20230129-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a4%2B-a748e80-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230129-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a4%2B-a748e80-vs-3.11.0.md)
- [plot](bm-20230129-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a4%2B-a748e80-vs-3.11.0.png)

### vs. base

- 1.05x slower \*
- missing benchmarks: 🔴 aiohttp, gunicorn, mypy
- new benchmarks: comprehensions, mypy2
- [table](bm-20230129-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a4%2B-a748e80-vs-base.md)
- [plot](bm-20230129-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a4%2B-a748e80-vs-base.png)

