# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: linux-aarch64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.25x faster                                         |
| chameleon      | 10.8 ms                                                               | 8.93 ms: 1.21x faster                                        |
| docutils       | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                       |
| html5lib       | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                        |
| tornado_http   | 178 ms                                                                | 133 ms: 1.34x faster                                         |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 564 ms: 1.68x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.42 sec: 1.60x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 737 ms: 1.54x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 880 ms: 1.45x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.57x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 106 ms: 1.57x faster                                         |
| float          | 135 ms                                                                | 93.1 ms: 1.45x faster                                        |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                         |
| regex_v8       | 32.2 ms                                                               | 30.2 ms: 1.07x faster                                        |
| regex_dna      | 257 ms                                                                | 253 ms: 1.01x faster                                         |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 351 us: 1.51x faster                                         |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                         |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                       |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                        |
| xml_etree_process    | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                        |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                         |
| unpickle_list        | 6.99 us                                                               | 6.46 us: 1.08x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 198 ms: 1.07x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                         |
| pickle_list          | 5.24 us                                                               | 5.22 us: 1.00x faster                                        |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                        |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                        |
| pickle               | 12.5 us                                                               | 13.5 us: 1.09x slower                                        |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.1 ms: 1.08x slower                                        |
| python_startup_no_site | 6.89 ms                                                               | 10.5 ms: 1.53x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                        |
| django_template | 53.3 ms                                                               | 40.3 ms: 1.32x faster                                        |
| genshi_text     | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 59.7 ms: 1.17x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 133 us: 4.98x faster                                         |
| deltablue                | 8.94 ms                                                               | 4.03 ms: 2.22x faster                                        |
| bench_mp_pool            | 14.5 ms                                                               | 6.96 ms: 2.09x faster                                        |
| raytrace                 | 573 ms                                                                | 295 ms: 1.94x faster                                         |
| generators               | 68.1 ms                                                               | 36.2 ms: 1.88x faster                                        |
| chaos                    | 121 ms                                                                | 67.1 ms: 1.81x faster                                        |
| richards_super           | 107 ms                                                                | 60.6 ms: 1.77x faster                                        |
| logging_silent           | 222 ns                                                                | 126 ns: 1.76x faster                                         |
| sqlglot_parse            | 2.40 ms                                                               | 1.36 ms: 1.76x faster                                        |
| asyncio_tcp              | 944 ms                                                                | 553 ms: 1.71x faster                                         |
| crypto_pyaes             | 134 ms                                                                | 78.8 ms: 1.70x faster                                        |
| richards                 | 91.7 ms                                                               | 54.2 ms: 1.69x faster                                        |
| async_tree_none          | 950 ms                                                                | 564 ms: 1.68x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.65x faster                                        |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                         |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.65x faster                                         |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.64x faster                                        |
| async_tree_io            | 2.28 sec                                                              | 1.42 sec: 1.60x faster                                       |
| nbody                    | 166 ms                                                                | 106 ms: 1.57x faster                                         |
| hexiom                   | 10.9 ms                                                               | 6.98 ms: 1.56x faster                                        |
| async_tree_memoization   | 1.13 sec                                                              | 737 ms: 1.54x faster                                         |
| scimark_monte_carlo      | 128 ms                                                                | 84.0 ms: 1.52x faster                                        |
| pickle_pure_python       | 529 us                                                                | 351 us: 1.51x faster                                         |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                       |
| scimark_sor              | 246 ms                                                                | 166 ms: 1.49x faster                                         |
| pylint                   | 485 ms                                                                | 334 ms: 1.45x faster                                         |
| float                    | 135 ms                                                                | 93.1 ms: 1.45x faster                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 880 ms: 1.45x faster                                         |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                         |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                         |
| spectral_norm            | 186 ms                                                                | 135 ms: 1.38x faster                                         |
| thrift                   | 1.26 ms                                                               | 926 us: 1.36x faster                                         |
| logging_simple           | 9.78 us                                                               | 7.26 us: 1.35x faster                                        |
| tornado_http             | 178 ms                                                                | 133 ms: 1.34x faster                                         |
| logging_format           | 10.6 us                                                               | 7.92 us: 1.34x faster                                        |
| pyflate                  | 795 ms                                                                | 597 ms: 1.33x faster                                         |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                       |
| django_template          | 53.3 ms                                                               | 40.3 ms: 1.32x faster                                        |
| sympy_sum                | 184 ms                                                                | 139 ms: 1.32x faster                                         |
| html5lib                 | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                       |
| genshi_text              | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                        |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.28x faster                                        |
| sympy_str                | 329 ms                                                                | 257 ms: 1.28x faster                                         |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                        |
| deepcopy_memo            | 61.7 us                                                               | 48.5 us: 1.27x faster                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 903 ms: 1.27x faster                                         |
| pprint_pformat           | 2.36 sec                                                              | 1.86 sec: 1.27x faster                                       |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                        |
| xml_etree_process        | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                        |
| sqlglot_normalize        | 156 ms                                                                | 125 ms: 1.25x faster                                         |
| 2to3                     | 381 ms                                                                | 306 ms: 1.25x faster                                         |
| dulwich_log              | 73.5 ms                                                               | 59.4 ms: 1.24x faster                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 61.0 ms: 1.24x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.23x faster                                        |
| nqueens                  | 117 ms                                                                | 96.6 ms: 1.22x faster                                        |
| docutils                 | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                       |
| chameleon                | 10.8 ms                                                               | 8.93 ms: 1.21x faster                                        |
| sympy_expand             | 543 ms                                                                | 448 ms: 1.21x faster                                         |
| gunicorn                 | 1.45 ms                                                               | 1.22 ms: 1.19x faster                                        |
| fannkuch                 | 546 ms                                                                | 461 ms: 1.18x faster                                         |
| deepcopy                 | 511 us                                                                | 434 us: 1.18x faster                                         |
| genshi_xml               | 69.8 ms                                                               | 59.7 ms: 1.17x faster                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.53 ms: 1.17x faster                                        |
| aiohttp                  | 1.39 ms                                                               | 1.19 ms: 1.17x faster                                        |
| deepcopy_reduce          | 4.60 us                                                               | 3.94 us: 1.17x faster                                        |
| create_gc_cycles         | 2.26 ms                                                               | 1.96 ms: 1.15x faster                                        |
| scimark_fft              | 500 ms                                                                | 442 ms: 1.13x faster                                         |
| pathlib                  | 26.3 ms                                                               | 23.7 ms: 1.11x faster                                        |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                       |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.10x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                         |
| unpickle_list            | 6.99 us                                                               | 6.46 us: 1.08x faster                                        |
| sqlite_synth             | 4.12 us                                                               | 3.84 us: 1.07x faster                                        |
| xml_etree_parse          | 212 ms                                                                | 198 ms: 1.07x faster                                         |
| regex_v8                 | 32.2 ms                                                               | 30.2 ms: 1.07x faster                                        |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                         |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                        |
| regex_dna                | 257 ms                                                                | 253 ms: 1.01x faster                                         |
| pickle_list              | 5.24 us                                                               | 5.22 us: 1.00x faster                                        |
| asyncio_websockets       | 657 ms                                                                | 660 ms: 1.01x slower                                         |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 4.39 ms: 1.06x slower                                        |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                        |
| async_generators         | 452 ms                                                                | 487 ms: 1.08x slower                                         |
| python_startup           | 11.2 ms                                                               | 12.1 ms: 1.08x slower                                        |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.09x slower                                        |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                        |
| telco                    | 8.49 ms                                                               | 9.57 ms: 1.13x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                        |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                         |
| python_startup_no_site   | 6.89 ms                                                               | 10.5 ms: 1.53x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                 |

Benchmark hidden because not significant (3): mypy2, flaskblogging, pidigits
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.09x