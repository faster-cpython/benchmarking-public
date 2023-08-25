
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 60ade0c
- commit date: 2023-07-08
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                       |
| tornado_http   | 152 ms                                                       | 120 ms: 1.27x faster                                         |
| Geometric mean | (ref)                                                        | 1.22x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.3 ms: 1.61x faster                                        |
| float          | 110 ms                                                       | 79.1 ms: 1.39x faster                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 145 ms: 1.34x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                        |
| regex_dna      | 259 ms                                                       | 240 ms: 1.08x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.51 ms: 1.17x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 211 us: 1.52x faster                                         |
| pickle_pure_python   | 457 us                                                       | 324 us: 1.41x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                        |
| tomli_loads          | 2.97 sec                                                     | 2.22 sec: 1.34x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 58.7 ms: 1.30x faster                                        |
| json_loads           | 30.0 us                                                      | 25.3 us: 1.19x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 153 ms: 1.05x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                         |
| unpickle             | 14.2 us                                                      | 14.8 us: 1.05x slower                                        |
| pickle               | 9.94 us                                                      | 10.4 us: 1.05x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.72 us: 1.05x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.47 us: 1.09x slower                                        |
| pickle_dict          | 30.0 us                                                      | 33.1 us: 1.10x slower                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.46 ms: 1.16x slower                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.98 ms: 1.47x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.41x faster                                         |
| deltablue                | 7.47 ms                                                      | 3.22 ms: 2.32x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 379 ms: 2.07x faster                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                       |
| richards_super           | 90.8 ms                                                      | 49.8 ms: 1.82x faster                                        |
| go                       | 259 ms                                                       | 146 ms: 1.78x faster                                         |
| logging_silent           | 166 ns                                                       | 93.2 ns: 1.78x faster                                        |
| chaos                    | 107 ms                                                       | 63.7 ms: 1.68x faster                                        |
| scimark_lu               | 164 ms                                                       | 97.4 ms: 1.68x faster                                        |
| richards                 | 74.1 ms                                                      | 44.2 ms: 1.68x faster                                        |
| scimark_monte_carlo      | 109 ms                                                       | 66.9 ms: 1.64x faster                                        |
| hexiom                   | 9.52 ms                                                      | 5.83 ms: 1.63x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.63x faster                                        |
| raytrace                 | 488 ms                                                       | 301 ms: 1.62x faster                                         |
| scimark_sor              | 177 ms                                                       | 109 ms: 1.62x faster                                         |
| nbody                    | 137 ms                                                       | 85.3 ms: 1.61x faster                                        |
| generators               | 58.0 ms                                                      | 36.1 ms: 1.61x faster                                        |
| pyflate                  | 697 ms                                                       | 439 ms: 1.59x faster                                         |
| async_tree_none          | 700 ms                                                       | 454 ms: 1.54x faster                                         |
| async_tree_io            | 1.61 sec                                                     | 1.05 sec: 1.53x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 211 us: 1.52x faster                                         |
| sqlglot_transpile        | 2.71 ms                                                      | 1.79 ms: 1.52x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 547 ms: 1.51x faster                                         |
| mako                     | 14.7 ms                                                      | 9.98 ms: 1.47x faster                                        |
| spectral_norm            | 136 ms                                                       | 93.4 ms: 1.46x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 82.1 ms: 1.44x faster                                        |
| fannkuch                 | 496 ms                                                       | 350 ms: 1.42x faster                                         |
| pickle_pure_python       | 457 us                                                       | 324 us: 1.41x faster                                         |
| float                    | 110 ms                                                       | 79.1 ms: 1.39x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                        |
| bench_mp_pool            | 7.18 ms                                                      | 5.24 ms: 1.37x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 697 ms: 1.36x faster                                         |
| regex_compile            | 194 ms                                                       | 145 ms: 1.34x faster                                         |
| pycparser                | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                       |
| tomli_loads              | 2.97 sec                                                     | 2.22 sec: 1.34x faster                                       |
| coroutines               | 30.4 ms                                                      | 22.9 ms: 1.33x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 801 ms: 1.31x faster                                         |
| deepcopy_memo            | 48.9 us                                                      | 37.5 us: 1.30x faster                                        |
| logging_simple           | 8.90 us                                                      | 6.83 us: 1.30x faster                                        |
| xml_etree_process        | 76.0 ms                                                      | 58.7 ms: 1.30x faster                                        |
| mypy2                    | 466 ms                                                       | 366 ms: 1.27x faster                                         |
| tornado_http             | 152 ms                                                       | 120 ms: 1.27x faster                                         |
| logging_format           | 9.57 us                                                      | 7.64 us: 1.25x faster                                        |
| nqueens                  | 112 ms                                                       | 90.5 ms: 1.24x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                         |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| comprehensions           | 26.9 us                                                      | 22.0 us: 1.22x faster                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 57.8 ms: 1.22x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 49.1 ns: 1.21x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.53 sec: 1.20x faster                                       |
| dulwich_log              | 80.1 ms                                                      | 66.8 ms: 1.20x faster                                        |
| scimark_fft              | 359 ms                                                       | 302 ms: 1.19x faster                                         |
| bench_thread_pool        | 1.14 ms                                                      | 957 us: 1.19x faster                                         |
| json_loads               | 30.0 us                                                      | 25.3 us: 1.19x faster                                        |
| deepcopy                 | 454 us                                                       | 383 us: 1.18x faster                                         |
| docutils                 | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.44 us: 1.17x faster                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.45 ms: 1.17x faster                                        |
| json                     | 5.96 ms                                                      | 5.12 ms: 1.16x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                        |
| pathlib                  | 21.7 ms                                                      | 19.7 ms: 1.10x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                        |
| meteor_contest           | 137 ms                                                       | 126 ms: 1.08x faster                                         |
| sqlite_synth             | 2.97 us                                                      | 2.74 us: 1.08x faster                                        |
| regex_dna                | 259 ms                                                       | 240 ms: 1.08x faster                                         |
| async_generators         | 422 ms                                                       | 397 ms: 1.06x faster                                         |
| xml_etree_parse          | 162 ms                                                       | 153 ms: 1.05x faster                                         |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.03x faster                                         |
| telco                    | 7.14 ms                                                      | 7.08 ms: 1.01x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                        |
| unpickle                 | 14.2 us                                                      | 14.8 us: 1.05x slower                                        |
| pickle                   | 9.94 us                                                      | 10.4 us: 1.05x slower                                        |
| unpickle_list            | 4.49 us                                                      | 4.72 us: 1.05x slower                                        |
| pickle_list              | 4.11 us                                                      | 4.47 us: 1.09x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 3.76 ms: 1.09x slower                                        |
| pickle_dict              | 30.0 us                                                      | 33.1 us: 1.10x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.46 ms: 1.16x slower                                        |
| regex_effbot             | 2.99 ms                                                      | 3.51 ms: 1.17x slower                                        |
| dask                     | 463 ms                                                       | 563 ms: 1.22x slower                                         |
| coverage                 | 64.0 ms                                                      | 89.2 ms: 1.39x slower                                        |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x
