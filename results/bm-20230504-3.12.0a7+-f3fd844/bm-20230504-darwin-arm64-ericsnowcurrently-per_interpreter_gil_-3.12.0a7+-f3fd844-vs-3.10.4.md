
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: darwin-arm64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 174 ms: 1.16x faster                                                              |
| docutils       | 1.78 sec                                               | 1.57 sec: 1.13x faster                                                            |
| tornado_http   | 91.5 ms                                                | 70.4 ms: 1.30x faster                                                             |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 70.3 ms: 1.33x faster                                                             |
| float          | 72.4 ms                                                | 58.9 ms: 1.23x faster                                                             |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 78.6 ms: 1.23x faster                                                             |
| regex_dna      | 162 ms                                                 | 150 ms: 1.08x faster                                                              |
| regex_v8       | 17.6 ms                                                | 16.3 ms: 1.08x faster                                                             |
| regex_effbot   | 2.46 ms                                                | 2.78 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 193 us: 1.47x faster                                                              |
| unpickle_pure_python | 203 us                                                 | 150 us: 1.35x faster                                                              |
| json_dumps           | 8.40 ms                                                | 6.98 ms: 1.20x faster                                                             |
| xml_etree_process    | 44.8 ms                                                | 40.4 ms: 1.11x faster                                                             |
| unpickle             | 9.89 us                                                | 10.0 us: 1.02x slower                                                             |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                                              |
| xml_etree_iterparse  | 72.3 ms                                                | 75.1 ms: 1.04x slower                                                             |
| json_loads           | 16.9 us                                                | 17.9 us: 1.06x slower                                                             |
| pickle_dict          | 17.9 us                                                | 19.0 us: 1.06x slower                                                             |
| xml_etree_generate   | 54.2 ms                                                | 58.2 ms: 1.07x slower                                                             |
| pickle               | 7.35 us                                                | 8.00 us: 1.09x slower                                                             |
| pickle_list          | 2.80 us                                                | 3.07 us: 1.09x slower                                                             |
| unpickle_list        | 2.69 us                                                | 3.21 us: 1.19x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.6 ms: 1.06x slower                                                             |
| python_startup_no_site | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.82 ms: 1.34x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.46 ms: 2.09x faster                                                             |
| logging_silent          | 119 ns                                                 | 69.5 ns: 1.72x faster                                                             |
| richards                | 51.4 ms                                                | 32.0 ms: 1.61x faster                                                             |
| sqlglot_parse           | 1.37 ms                                                | 900 us: 1.52x faster                                                              |
| go                      | 165 ms                                                 | 109 ms: 1.52x faster                                                              |
| asyncio_tcp             | 670 ms                                                 | 451 ms: 1.48x faster                                                              |
| pickle_pure_python      | 283 us                                                 | 193 us: 1.47x faster                                                              |
| scimark_sor             | 126 ms                                                 | 86.0 ms: 1.47x faster                                                             |
| hexiom                  | 6.32 ms                                                | 4.31 ms: 1.47x faster                                                             |
| sqlglot_transpile       | 1.57 ms                                                | 1.07 ms: 1.46x faster                                                             |
| async_tree_memoization  | 490 ms                                                 | 336 ms: 1.46x faster                                                              |
| async_tree_io           | 1.02 sec                                               | 715 ms: 1.43x faster                                                              |
| async_tree_none         | 400 ms                                                 | 284 ms: 1.41x faster                                                              |
| crypto_pyaes            | 78.1 ms                                                | 55.8 ms: 1.40x faster                                                             |
| scimark_monte_carlo     | 72.5 ms                                                | 52.3 ms: 1.39x faster                                                             |
| chaos                   | 66.7 ms                                                | 48.1 ms: 1.39x faster                                                             |
| unpickle_pure_python    | 203 us                                                 | 150 us: 1.35x faster                                                              |
| mako                    | 10.5 ms                                                | 7.82 ms: 1.34x faster                                                             |
| unpack_sequence         | 37.4 ns                                                | 28.1 ns: 1.33x faster                                                             |
| scimark_lu              | 109 ms                                                 | 82.1 ms: 1.33x faster                                                             |
| nbody                   | 93.3 ms                                                | 70.3 ms: 1.33x faster                                                             |
| pyflate                 | 453 ms                                                 | 343 ms: 1.32x faster                                                              |
| pycparser               | 916 ms                                                 | 698 ms: 1.31x faster                                                              |
| generators              | 32.7 ms                                                | 25.0 ms: 1.31x faster                                                             |
| raytrace                | 325 ms                                                 | 250 ms: 1.30x faster                                                              |
| tornado_http            | 91.5 ms                                                | 70.4 ms: 1.30x faster                                                             |
| deepcopy_memo           | 34.4 us                                                | 26.5 us: 1.30x faster                                                             |
| create_gc_cycles        | 880 us                                                 | 696 us: 1.26x faster                                                              |
| logging_simple          | 4.63 us                                                | 3.70 us: 1.25x faster                                                             |
| async_tree_cpu_io_mixed | 669 ms                                                 | 535 ms: 1.25x faster                                                              |
| logging_format          | 4.97 us                                                | 3.99 us: 1.25x faster                                                             |
| float                   | 72.4 ms                                                | 58.9 ms: 1.23x faster                                                             |
| regex_compile           | 96.4 ms                                                | 78.6 ms: 1.23x faster                                                             |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.29 ms: 1.22x faster                                                             |
| spectral_norm           | 95.8 ms                                                | 79.0 ms: 1.21x faster                                                             |
| dulwich_log             | 37.1 ms                                                | 30.6 ms: 1.21x faster                                                             |
| json_dumps              | 8.40 ms                                                | 6.98 ms: 1.20x faster                                                             |
| pprint_pformat          | 1.23 sec                                               | 1.03 sec: 1.20x faster                                                            |
| pprint_safe_repr        | 606 ms                                                 | 506 ms: 1.20x faster                                                              |
| deepcopy                | 281 us                                                 | 241 us: 1.17x faster                                                              |
| fannkuch                | 317 ms                                                 | 274 ms: 1.16x faster                                                              |
| 2to3                    | 201 ms                                                 | 174 ms: 1.16x faster                                                              |
| mypy2                   | 307 ms                                                 | 266 ms: 1.15x faster                                                              |
| docutils                | 1.78 sec                                               | 1.57 sec: 1.13x faster                                                            |
| coroutines              | 20.2 ms                                                | 18.1 ms: 1.11x faster                                                             |
| xml_etree_process       | 44.8 ms                                                | 40.4 ms: 1.11x faster                                                             |
| deepcopy_reduce         | 2.37 us                                                | 2.14 us: 1.11x faster                                                             |
| bench_thread_pool       | 546 us                                                 | 499 us: 1.09x faster                                                              |
| sqlalchemy_declarative  | 74.9 ms                                                | 69.2 ms: 1.08x faster                                                             |
| scimark_fft             | 230 ms                                                 | 213 ms: 1.08x faster                                                              |
| regex_dna               | 162 ms                                                 | 150 ms: 1.08x faster                                                              |
| regex_v8                | 17.6 ms                                                | 16.3 ms: 1.08x faster                                                             |
| nqueens                 | 68.2 ms                                                | 63.8 ms: 1.07x faster                                                             |
| mdp                     | 1.66 sec                                               | 1.59 sec: 1.05x faster                                                            |
| sqlglot_optimize        | 38.0 ms                                                | 36.5 ms: 1.04x faster                                                             |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.33 ms: 1.04x faster                                                             |
| json                    | 3.08 ms                                                | 3.02 ms: 1.02x faster                                                             |
| pathlib                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                                             |
| meteor_contest          | 78.1 ms                                                | 77.2 ms: 1.01x faster                                                             |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                              |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                                             |
| sqlglot_normalize       | 196 ms                                                 | 199 ms: 1.01x slower                                                              |
| comprehensions          | 17.6 us                                                | 17.8 us: 1.01x slower                                                             |
| unpickle                | 9.89 us                                                | 10.0 us: 1.02x slower                                                             |
| xml_etree_parse         | 106 ms                                                 | 109 ms: 1.02x slower                                                              |
| xml_etree_iterparse     | 72.3 ms                                                | 75.1 ms: 1.04x slower                                                             |
| python_startup          | 11.9 ms                                                | 12.6 ms: 1.06x slower                                                             |
| json_loads              | 16.9 us                                                | 17.9 us: 1.06x slower                                                             |
| pickle_dict             | 17.9 us                                                | 19.0 us: 1.06x slower                                                             |
| xml_etree_generate      | 54.2 ms                                                | 58.2 ms: 1.07x slower                                                             |
| sqlite_synth            | 1.47 us                                                | 1.59 us: 1.08x slower                                                             |
| telco                   | 3.63 ms                                                | 3.95 ms: 1.09x slower                                                             |
| pickle                  | 7.35 us                                                | 8.00 us: 1.09x slower                                                             |
| pickle_list             | 2.80 us                                                | 3.07 us: 1.09x slower                                                             |
| regex_effbot            | 2.46 ms                                                | 2.78 ms: 1.13x slower                                                             |
| python_startup_no_site  | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                             |
| unpickle_list           | 2.69 us                                                | 3.21 us: 1.19x slower                                                             |
| bench_mp_pool           | 39.7 ms                                                | 48.7 ms: 1.23x slower                                                             |
| dask                    | 265 ms                                                 | 334 ms: 1.26x slower                                                              |
| async_generators        | 234 ms                                                 | 318 ms: 1.36x slower                                                              |
| coverage                | 42.0 ms                                                | 59.1 ms: 1.41x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.15x faster                                                                      |
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
