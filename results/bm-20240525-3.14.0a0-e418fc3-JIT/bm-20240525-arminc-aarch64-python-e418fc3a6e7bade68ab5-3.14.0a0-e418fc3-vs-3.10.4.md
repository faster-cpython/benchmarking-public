# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 360 ms: 1.06x faster                                                    |
| chameleon      | 10.8 ms                                                               | 9.19 ms: 1.18x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.58 sec: 1.02x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.3 ms: 1.21x faster                                                   |
| tornado_http   | 178 ms                                                                | 140 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 508 ms: 1.87x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.27 sec: 1.80x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 685 ms: 1.66x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 822 ms: 1.55x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.71x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.3 ms: 1.51x faster                                                   |
| nbody          | 166 ms                                                                | 115 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.2 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 251 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 275 us: 1.33x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 405 us: 1.31x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.43 us: 1.09x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 196 ms: 1.08x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.06x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.27 us: 1.01x slower                                                   |
| json_loads           | 30.9 us                                                               | 32.0 us: 1.04x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.07x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.35x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 10.7 ms: 1.56x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                                   |
| django_template | 53.3 ms                                                               | 50.4 ms: 1.06x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.8 ms: 1.01x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 81.7 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 212 us: 3.11x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.69 ms: 1.91x faster                                                   |
| async_tree_none          | 950 ms                                                                | 508 ms: 1.87x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.27 sec: 1.80x faster                                                  |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 8.41 ms: 1.73x faster                                                   |
| richards_super           | 107 ms                                                                | 62.4 ms: 1.72x faster                                                   |
| generators               | 68.1 ms                                                               | 39.9 ms: 1.71x faster                                                   |
| richards                 | 91.7 ms                                                               | 54.7 ms: 1.67x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 685 ms: 1.66x faster                                                    |
| logging_silent           | 222 ns                                                                | 138 ns: 1.61x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 822 ms: 1.55x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 611 ms: 1.55x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.57 ms: 1.53x faster                                                   |
| float                    | 135 ms                                                                | 89.3 ms: 1.51x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 89.5 ms: 1.50x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.23 sec: 1.47x faster                                                  |
| go                       | 264 ms                                                                | 179 ms: 1.47x faster                                                    |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                                   |
| nbody                    | 166 ms                                                                | 115 ms: 1.45x faster                                                    |
| comprehensions           | 33.1 us                                                               | 22.9 us: 1.44x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 88.6 ms: 1.44x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.98 ms: 1.43x faster                                                   |
| scimark_sor              | 246 ms                                                                | 173 ms: 1.42x faster                                                    |
| chaos                    | 121 ms                                                                | 88.2 ms: 1.37x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 275 us: 1.33x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.38 us: 1.32x faster                                                   |
| thrift                   | 1.26 ms                                                               | 962 us: 1.31x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 405 us: 1.31x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.13 us: 1.31x faster                                                   |
| pyflate                  | 795 ms                                                                | 616 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.28x faster                                                   |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                    |
| tornado_http             | 178 ms                                                                | 140 ms: 1.28x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                                  |
| scimark_lu               | 227 ms                                                                | 181 ms: 1.25x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 49.7 us: 1.24x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 8.96 ms: 1.22x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.3 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.18x faster                                                   |
| chameleon                | 10.8 ms                                                               | 9.19 ms: 1.18x faster                                                   |
| dask                     | 450 ms                                                                | 391 ms: 1.15x faster                                                    |
| fannkuch                 | 546 ms                                                                | 475 ms: 1.15x faster                                                    |
| pylint                   | 485 ms                                                                | 423 ms: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.95 ms: 1.10x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.43 us: 1.09x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 69.5 ms: 1.09x faster                                                   |
| scimark_fft              | 500 ms                                                                | 462 ms: 1.08x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 196 ms: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.43 sec: 1.08x faster                                                  |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.2 ms: 1.06x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.06x faster                                                    |
| 2to3                     | 381 ms                                                                | 360 ms: 1.06x faster                                                    |
| django_template          | 53.3 ms                                                               | 50.4 ms: 1.06x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.89 us: 1.06x faster                                                   |
| json                     | 5.88 ms                                                               | 5.62 ms: 1.05x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 70.8 ms: 1.04x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.03x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.30 sec: 1.03x faster                                                  |
| deepcopy                 | 511 us                                                                | 499 us: 1.02x faster                                                    |
| regex_dna                | 257 ms                                                                | 251 ms: 1.02x faster                                                    |
| sympy_str                | 329 ms                                                                | 323 ms: 1.02x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.8 ms: 1.01x faster                                                   |
| pickle_list              | 5.24 us                                                               | 5.27 us: 1.01x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| sympy_expand             | 543 ms                                                                | 548 ms: 1.01x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.58 sec: 1.02x slower                                                  |
| nqueens                  | 117 ms                                                                | 120 ms: 1.02x slower                                                    |
| flaskblogging            | 4.83 ms                                                               | 4.96 ms: 1.03x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.74 us: 1.03x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.0 us: 1.04x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.36 ms: 1.05x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.07x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| async_generators         | 452 ms                                                                | 505 ms: 1.12x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 81.7 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.5 ms: 1.19x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.20x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.25 ms: 1.26x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.35x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 10.7 ms: 1.56x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (4): regex_compile, sympy_integrate, pidigits, sympy_sum
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.24x