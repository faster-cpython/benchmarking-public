# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                            |
| chameleon      | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                           |
| docutils       | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                          |
| tornado_http   | 108 ms                                                      | 85.5 ms: 1.27x faster                                           |
| Geometric mean | (ref)                                                       | 1.21x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 266 ms: 1.63x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 341 ms: 1.54x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 726 ms: 1.53x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 455 ms: 1.40x faster                                            |
| Geometric mean          | (ref)                                                       | 1.52x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.4 ms: 1.20x faster                                           |
| nbody          | 71.3 ms                                                     | 61.0 ms: 1.17x faster                                           |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.3 ms: 1.34x faster                                           |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                            |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                           |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                       | 1.15x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.54 ms: 1.65x faster                                           |
| pickle_pure_python   | 270 us                                                      | 174 us: 1.55x faster                                            |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.45x faster                                            |
| tomli_loads          | 1.67 sec                                                    | 1.30 sec: 1.29x faster                                          |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                           |
| unpickle             | 9.09 us                                                     | 8.41 us: 1.08x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 51.9 ms: 1.07x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                           |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.01x faster                                           |
| unpickle_list        | 2.71 us                                                     | 2.74 us: 1.01x slower                                           |
| pickle_list          | 2.75 us                                                     | 2.78 us: 1.01x slower                                           |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.02x slower                                           |
| pickle               | 6.85 us                                                     | 7.32 us: 1.07x slower                                           |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.5 ms: 1.20x slower                                           |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 9.03 ms                                                     | 6.71 ms: 1.35x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 69.7 us: 4.82x faster                                           |
| deltablue                | 4.19 ms                                                     | 1.99 ms: 2.11x faster                                           |
| richards_super           | 52.2 ms                                                     | 28.2 ms: 1.86x faster                                           |
| logging_silent           | 94.6 ns                                                     | 54.0 ns: 1.75x faster                                           |
| richards                 | 42.4 ms                                                     | 24.8 ms: 1.71x faster                                           |
| json_dumps               | 9.16 ms                                                     | 5.54 ms: 1.65x faster                                           |
| raytrace                 | 273 ms                                                      | 166 ms: 1.65x faster                                            |
| async_tree_none          | 435 ms                                                      | 266 ms: 1.63x faster                                            |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 755 us: 1.61x faster                                            |
| pickle_pure_python       | 270 us                                                      | 174 us: 1.55x faster                                            |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                           |
| scimark_lu               | 85.8 ms                                                     | 55.3 ms: 1.55x faster                                           |
| async_tree_memoization   | 526 ms                                                      | 341 ms: 1.54x faster                                            |
| asyncio_tcp              | 732 ms                                                      | 477 ms: 1.53x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 726 ms: 1.53x faster                                            |
| sqlglot_transpile        | 1.48 ms                                                     | 978 us: 1.51x faster                                            |
| chaos                    | 61.7 ms                                                     | 41.7 ms: 1.48x faster                                           |
| go                       | 139 ms                                                      | 94.8 ms: 1.47x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.45x faster                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 455 ms: 1.40x faster                                            |
| scimark_sor              | 106 ms                                                      | 76.0 ms: 1.40x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 45.8 ms: 1.37x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 21.3 us: 1.35x faster                                           |
| mako                     | 9.03 ms                                                     | 6.71 ms: 1.35x faster                                           |
| regex_compile            | 106 ms                                                      | 79.3 ms: 1.34x faster                                           |
| pyflate                  | 409 ms                                                      | 308 ms: 1.33x faster                                            |
| mypy2                    | 555 ms                                                      | 423 ms: 1.31x faster                                            |
| tomli_loads              | 1.67 sec                                                    | 1.30 sec: 1.29x faster                                          |
| tornado_http             | 108 ms                                                      | 85.5 ms: 1.27x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.51 us: 1.26x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 980 ms: 1.24x faster                                            |
| pycparser                | 930 ms                                                      | 748 ms: 1.24x faster                                            |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.70 sec: 1.24x faster                                          |
| docutils                 | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                          |
| pprint_safe_repr         | 592 ms                                                      | 480 ms: 1.23x faster                                            |
| sympy_sum                | 107 ms                                                      | 86.8 ms: 1.23x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 63.3 ms: 1.22x faster                                           |
| chameleon                | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                           |
| float                    | 61.7 ms                                                     | 51.4 ms: 1.20x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                          |
| sympy_str                | 194 ms                                                      | 163 ms: 1.19x faster                                            |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                           |
| sqlglot_normalize        | 205 ms                                                      | 173 ms: 1.19x faster                                            |
| sqlglot_optimize         | 39.8 ms                                                     | 33.5 ms: 1.19x faster                                           |
| deepcopy                 | 255 us                                                      | 217 us: 1.18x faster                                            |
| bench_thread_pool        | 958 us                                                      | 817 us: 1.17x faster                                            |
| nbody                    | 71.3 ms                                                     | 61.0 ms: 1.17x faster                                           |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                           |
| sympy_expand             | 314 ms                                                      | 277 ms: 1.13x faster                                            |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                            |
| hexiom                   | 5.74 ms                                                     | 5.14 ms: 1.12x faster                                           |
| nqueens                  | 66.6 ms                                                     | 59.7 ms: 1.12x faster                                           |
| create_gc_cycles         | 800 us                                                      | 736 us: 1.09x faster                                            |
| unpickle                 | 9.09 us                                                     | 8.41 us: 1.08x faster                                           |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                           |
| xml_etree_generate       | 55.5 ms                                                     | 51.9 ms: 1.07x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                           |
| logging_format           | 6.76 us                                                     | 6.39 us: 1.06x faster                                           |
| fannkuch                 | 256 ms                                                      | 242 ms: 1.06x faster                                            |
| logging_simple           | 6.22 us                                                     | 5.95 us: 1.05x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.65 ms: 1.03x faster                                           |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.01x faster                                           |
| scimark_monte_carlo      | 57.3 ms                                                     | 56.9 ms: 1.01x faster                                           |
| pathlib                  | 75.7 ms                                                     | 75.3 ms: 1.00x faster                                           |
| unpack_sequence          | 39.6 ns                                                     | 40.0 ns: 1.01x slower                                           |
| scimark_fft              | 187 ms                                                      | 189 ms: 1.01x slower                                            |
| unpickle_list            | 2.71 us                                                     | 2.74 us: 1.01x slower                                           |
| meteor_contest           | 75.9 ms                                                     | 76.7 ms: 1.01x slower                                           |
| pickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                           |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                            |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.02x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.51 ms: 1.07x slower                                           |
| pickle                   | 6.85 us                                                     | 7.32 us: 1.07x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 66.6 ms: 1.07x slower                                           |
| async_generators         | 222 ms                                                      | 238 ms: 1.07x slower                                            |
| dask                     | 313 ms                                                      | 360 ms: 1.15x slower                                            |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 18.5 ms: 1.20x slower                                           |
| coverage                 | 39.0 ms                                                     | 48.4 ms: 1.24x slower                                           |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                    |

Benchmark hidden because not significant (2): json, python_startup
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x


# Memory

- memory change: unknown