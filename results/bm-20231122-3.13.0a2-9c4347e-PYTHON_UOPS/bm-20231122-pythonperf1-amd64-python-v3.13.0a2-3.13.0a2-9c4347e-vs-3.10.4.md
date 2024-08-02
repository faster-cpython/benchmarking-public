
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                            |
| chameleon      | 5.79 ms                                                     | 4.84 ms: 1.20x faster                                           |
| docutils       | 1.92 sec                                                    | 1.55 sec: 1.24x faster                                          |
| tornado_http   | 108 ms                                                      | 89.4 ms: 1.21x faster                                           |
| Geometric mean | (ref)                                                       | 1.19x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 267 ms: 1.63x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 729 ms: 1.52x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 346 ms: 1.52x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 454 ms: 1.41x faster                                            |
| Geometric mean          | (ref)                                                       | 1.52x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 57.1 ms: 1.08x faster                                           |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| nbody          | 71.3 ms                                                     | 81.4 ms: 1.14x slower                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.1 ms: 1.20x faster                                           |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                           |
| regex_v8       | 15.4 ms                                                     | 17.9 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.46 ms: 1.68x faster                                           |
| pickle_pure_python   | 270 us                                                      | 175 us: 1.54x faster                                            |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 37.6 ms: 1.18x faster                                           |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                          |
| unpickle             | 9.09 us                                                     | 8.09 us: 1.12x faster                                           |
| json_loads           | 14.0 us                                                     | 13.4 us: 1.04x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                           |
| unpickle_list        | 2.71 us                                                     | 2.62 us: 1.04x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 55.1 ms: 1.01x faster                                           |
| pickle               | 6.85 us                                                     | 6.96 us: 1.02x slower                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.5 ms: 1.04x slower                                           |
| pickle_dict          | 17.2 us                                                     | 18.6 us: 1.08x slower                                           |
| pickle_list          | 2.75 us                                                     | 3.32 us: 1.21x slower                                           |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                           |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 9.03 ms                                                     | 7.38 ms: 1.22x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 77.0 us: 4.37x faster                                           |
| richards_super           | 52.2 ms                                                     | 30.1 ms: 1.74x faster                                           |
| logging_silent           | 94.6 ns                                                     | 55.5 ns: 1.71x faster                                           |
| json_dumps               | 9.16 ms                                                     | 5.46 ms: 1.68x faster                                           |
| async_tree_none          | 435 ms                                                      | 267 ms: 1.63x faster                                            |
| generators               | 32.4 ms                                                     | 20.3 ms: 1.60x faster                                           |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 779 us: 1.56x faster                                            |
| pickle_pure_python       | 270 us                                                      | 175 us: 1.54x faster                                            |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                            |
| deltablue                | 4.19 ms                                                     | 2.72 ms: 1.54x faster                                           |
| asyncio_tcp              | 732 ms                                                      | 477 ms: 1.54x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 729 ms: 1.52x faster                                            |
| async_tree_memoization   | 526 ms                                                      | 346 ms: 1.52x faster                                            |
| go                       | 139 ms                                                      | 92.1 ms: 1.51x faster                                           |
| scimark_lu               | 85.8 ms                                                     | 57.6 ms: 1.49x faster                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 1.01 ms: 1.46x faster                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 454 ms: 1.41x faster                                            |
| chaos                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                           |
| pycparser                | 930 ms                                                      | 675 ms: 1.38x faster                                            |
| scimark_sor              | 106 ms                                                      | 78.6 ms: 1.35x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                            |
| comprehensions           | 16.5 us                                                     | 12.9 us: 1.28x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 49.2 ms: 1.27x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.66 sec: 1.27x faster                                          |
| pyflate                  | 409 ms                                                      | 324 ms: 1.26x faster                                            |
| deepcopy_memo            | 28.8 us                                                     | 22.9 us: 1.26x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.24x faster                                          |
| docutils                 | 1.92 sec                                                    | 1.55 sec: 1.24x faster                                          |
| dask                     | 313 ms                                                      | 254 ms: 1.23x faster                                            |
| mako                     | 9.03 ms                                                     | 7.38 ms: 1.22x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                           |
| tornado_http             | 108 ms                                                      | 89.4 ms: 1.21x faster                                           |
| regex_compile            | 106 ms                                                      | 88.1 ms: 1.20x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                           |
| sympy_sum                | 107 ms                                                      | 89.1 ms: 1.20x faster                                           |
| chameleon                | 5.79 ms                                                     | 4.84 ms: 1.20x faster                                           |
| xml_etree_process        | 44.5 ms                                                     | 37.6 ms: 1.18x faster                                           |
| deepcopy                 | 255 us                                                      | 216 us: 1.18x faster                                            |
| dulwich_log              | 50.5 ms                                                     | 42.8 ms: 1.18x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.4 ms: 1.16x faster                                           |
| sympy_str                | 194 ms                                                      | 168 ms: 1.15x faster                                            |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 34.8 ms: 1.14x faster                                           |
| hexiom                   | 5.74 ms                                                     | 5.03 ms: 1.14x faster                                           |
| pprint_safe_repr         | 592 ms                                                      | 519 ms: 1.14x faster                                            |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                            |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                          |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.13x faster                                           |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                            |
| unpickle                 | 9.09 us                                                     | 8.09 us: 1.12x faster                                           |
| sqlglot_normalize        | 205 ms                                                      | 183 ms: 1.12x faster                                            |
| sympy_expand             | 314 ms                                                      | 281 ms: 1.12x faster                                            |
| bench_thread_pool        | 958 us                                                      | 858 us: 1.12x faster                                            |
| create_gc_cycles         | 800 us                                                      | 732 us: 1.09x faster                                            |
| float                    | 61.7 ms                                                     | 57.1 ms: 1.08x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                           |
| json_loads               | 14.0 us                                                     | 13.4 us: 1.04x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                           |
| unpickle_list            | 2.71 us                                                     | 2.62 us: 1.04x faster                                           |
| nqueens                  | 66.6 ms                                                     | 65.3 ms: 1.02x faster                                           |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| xml_etree_generate       | 55.5 ms                                                     | 55.1 ms: 1.01x faster                                           |
| unpack_sequence          | 39.6 ns                                                     | 40.1 ns: 1.01x slower                                           |
| pickle                   | 6.85 us                                                     | 6.96 us: 1.02x slower                                           |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                           |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                            |
| pathlib                  | 75.7 ms                                                     | 78.5 ms: 1.04x slower                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.5 ms: 1.04x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 64.9 ms: 1.05x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.49 ms: 1.06x slower                                           |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                            |
| pickle_dict              | 17.2 us                                                     | 18.6 us: 1.08x slower                                           |
| spectral_norm            | 77.3 ms                                                     | 84.1 ms: 1.09x slower                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.09 ms: 1.14x slower                                           |
| scimark_fft              | 187 ms                                                      | 213 ms: 1.14x slower                                            |
| nbody                    | 71.3 ms                                                     | 81.4 ms: 1.14x slower                                           |
| regex_v8                 | 15.4 ms                                                     | 17.9 ms: 1.16x slower                                           |
| coverage                 | 39.0 ms                                                     | 45.2 ms: 1.16x slower                                           |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                           |
| pickle_list              | 2.75 us                                                     | 3.32 us: 1.21x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                           |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                    |

Benchmark hidden because not significant (5): json, logging_format, logging_simple, python_startup, mypy2
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.13x


# Memory

- memory change: unknown