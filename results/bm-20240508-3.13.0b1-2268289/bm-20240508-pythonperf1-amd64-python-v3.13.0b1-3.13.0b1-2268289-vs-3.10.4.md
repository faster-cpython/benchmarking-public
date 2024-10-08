# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b1
- machine: windows-amd64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 212 ms: 1.16x faster                                            |
| chameleon      | 5.79 ms                                                     | 4.75 ms: 1.22x faster                                           |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                          |
| html5lib       | 51.0 ms                                                     | 35.0 ms: 1.46x faster                                           |
| tornado_http   | 108 ms                                                      | 82.5 ms: 1.31x faster                                           |
| Geometric mean | (ref)                                                       | 1.26x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 219 ms: 1.98x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 266 ms: 1.98x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 582 ms: 1.91x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                            |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.5 ms: 1.27x faster                                           |
| nbody          | 71.3 ms                                                     | 67.1 ms: 1.06x faster                                           |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.5 ms: 1.35x faster                                           |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                            |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                           |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                       | 1.15x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                           |
| pickle_pure_python   | 270 us                                                      | 177 us: 1.52x faster                                            |
| unpickle_pure_python | 183 us                                                      | 127 us: 1.45x faster                                            |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                          |
| xml_etree_process    | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                           |
| unpickle             | 9.09 us                                                     | 8.44 us: 1.08x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 53.7 ms: 1.03x faster                                           |
| json_loads           | 14.0 us                                                     | 13.7 us: 1.02x faster                                           |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                           |
| pickle               | 6.85 us                                                     | 7.17 us: 1.05x slower                                           |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                           |
| pickle_list          | 2.75 us                                                     | 3.02 us: 1.10x slower                                           |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.4 ms: 1.01x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 16.5 ms: 1.06x slower                                           |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.28 ms: 1.44x faster                                           |
| django_template | 28.9 ms                                                     | 21.5 ms: 1.35x faster                                           |
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.34x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 32.2 ms: 1.27x faster                                           |
| Geometric mean  | (ref)                                                       | 1.35x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                            |
| deltablue                | 4.19 ms                                                     | 1.90 ms: 2.20x faster                                           |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.98x faster                                            |
| async_tree_memoization   | 526 ms                                                      | 266 ms: 1.98x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 582 ms: 1.91x faster                                            |
| logging_silent           | 94.6 ns                                                     | 51.7 ns: 1.83x faster                                           |
| raytrace                 | 273 ms                                                      | 154 ms: 1.78x faster                                            |
| richards_super           | 52.2 ms                                                     | 29.9 ms: 1.75x faster                                           |
| generators               | 32.4 ms                                                     | 18.6 ms: 1.74x faster                                           |
| pylint                   | 350 ms                                                      | 209 ms: 1.67x faster                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                            |
| go                       | 139 ms                                                      | 84.3 ms: 1.65x faster                                           |
| json_dumps               | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                           |
| chaos                    | 61.7 ms                                                     | 38.3 ms: 1.61x faster                                           |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 754 us: 1.61x faster                                            |
| richards                 | 42.4 ms                                                     | 26.6 ms: 1.60x faster                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 962 us: 1.53x faster                                            |
| hexiom                   | 5.74 ms                                                     | 3.76 ms: 1.53x faster                                           |
| pickle_pure_python       | 270 us                                                      | 177 us: 1.52x faster                                            |
| asyncio_tcp              | 732 ms                                                      | 482 ms: 1.52x faster                                            |
| scimark_lu               | 85.8 ms                                                     | 56.8 ms: 1.51x faster                                           |
| html5lib                 | 51.0 ms                                                     | 35.0 ms: 1.46x faster                                           |
| pyflate                  | 409 ms                                                      | 280 ms: 1.46x faster                                            |
| unpickle_pure_python     | 183 us                                                      | 127 us: 1.45x faster                                            |
| mako                     | 9.03 ms                                                     | 6.28 ms: 1.44x faster                                           |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.41x faster                                           |
| scimark_sor              | 106 ms                                                      | 75.9 ms: 1.40x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.51 sec: 1.40x faster                                          |
| pycparser                | 930 ms                                                      | 669 ms: 1.39x faster                                            |
| mdp                      | 1.78 sec                                                    | 1.31 sec: 1.36x faster                                          |
| regex_compile            | 106 ms                                                      | 78.5 ms: 1.35x faster                                           |
| django_template          | 28.9 ms                                                     | 21.5 ms: 1.35x faster                                           |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.34x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                           |
| tornado_http             | 108 ms                                                      | 82.5 ms: 1.31x faster                                           |
| mypy2                    | 555 ms                                                      | 427 ms: 1.30x faster                                            |
| dulwich_log              | 50.5 ms                                                     | 39.6 ms: 1.27x faster                                           |
| genshi_xml               | 41.0 ms                                                     | 32.2 ms: 1.27x faster                                           |
| float                    | 61.7 ms                                                     | 48.5 ms: 1.27x faster                                           |
| coroutines               | 16.0 ms                                                     | 12.6 ms: 1.27x faster                                           |
| sympy_sum                | 107 ms                                                      | 85.2 ms: 1.26x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 61.9 ms: 1.25x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 23.1 us: 1.25x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 982 ms: 1.24x faster                                            |
| pprint_safe_repr         | 592 ms                                                      | 481 ms: 1.23x faster                                            |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.23x faster                                           |
| chameleon                | 5.79 ms                                                     | 4.75 ms: 1.22x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 32.9 ms: 1.21x faster                                           |
| bench_thread_pool        | 958 us                                                      | 793 us: 1.21x faster                                            |
| xml_etree_process        | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                           |
| sympy_str                | 194 ms                                                      | 162 ms: 1.20x faster                                            |
| sqlglot_normalize        | 205 ms                                                      | 172 ms: 1.19x faster                                            |
| nqueens                  | 66.6 ms                                                     | 56.2 ms: 1.19x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                           |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                          |
| 2to3                     | 246 ms                                                      | 212 ms: 1.16x faster                                            |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                            |
| deepcopy                 | 255 us                                                      | 223 us: 1.14x faster                                            |
| sympy_expand             | 314 ms                                                      | 275 ms: 1.14x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.11x faster                                           |
| aiohttp                  | 995 us                                                      | 908 us: 1.10x faster                                            |
| logging_format           | 6.76 us                                                     | 6.22 us: 1.09x faster                                           |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                           |
| unpickle                 | 9.09 us                                                     | 8.44 us: 1.08x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                           |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                            |
| logging_simple           | 6.22 us                                                     | 5.80 us: 1.07x faster                                           |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 71.3 ms: 1.07x faster                                           |
| nbody                    | 71.3 ms                                                     | 67.1 ms: 1.06x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                           |
| fannkuch                 | 256 ms                                                      | 244 ms: 1.05x faster                                            |
| xml_etree_generate       | 55.5 ms                                                     | 53.7 ms: 1.03x faster                                           |
| json_loads               | 14.0 us                                                     | 13.7 us: 1.02x faster                                           |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                            |
| python_startup           | 20.6 ms                                                     | 20.4 ms: 1.01x faster                                           |
| async_generators         | 222 ms                                                      | 225 ms: 1.01x slower                                            |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                           |
| pickle                   | 6.85 us                                                     | 7.17 us: 1.05x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 65.3 ms: 1.05x slower                                           |
| pathlib                  | 75.7 ms                                                     | 80.1 ms: 1.06x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 16.5 ms: 1.06x slower                                           |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                           |
| pickle_list              | 2.75 us                                                     | 3.02 us: 1.10x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                           |
| create_gc_cycles         | 800 us                                                      | 893 us: 1.12x slower                                            |
| coverage                 | 39.0 ms                                                     | 45.3 ms: 1.16x slower                                           |
| telco                    | 3.94 ms                                                     | 4.72 ms: 1.20x slower                                           |
| thrift                   | 617 us                                                      | 8.23 ms: 13.32x slower                                          |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                    |

Benchmark hidden because not significant (2): flaskblogging, dask
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown