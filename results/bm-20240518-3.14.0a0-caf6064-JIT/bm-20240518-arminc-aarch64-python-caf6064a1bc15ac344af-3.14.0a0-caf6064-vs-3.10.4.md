# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 360 ms: 1.06x faster                                                    |
| chameleon      | 10.8 ms                                                               | 9.20 ms: 1.18x faster                                                   |
| html5lib       | 86.5 ms                                                               | 70.6 ms: 1.22x faster                                                   |
| tornado_http   | 178 ms                                                                | 145 ms: 1.23x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 497 ms: 1.91x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.23 sec: 1.85x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 655 ms: 1.73x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 807 ms: 1.58x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.76x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.4 ms: 1.49x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_compile  | 177 ms                                                                | 171 ms: 1.03x faster                                                    |
| regex_dna      | 257 ms                                                                | 251 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 387 us: 1.37x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 276 us: 1.32x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.55 us: 1.07x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 117 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.32 us: 1.02x slower                                                   |
| json_loads           | 30.9 us                                                               | 32.1 us: 1.04x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.2 us: 1.09x slower                                                   |
| pickle               | 12.5 us                                                               | 13.8 us: 1.11x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 14.9 ms: 1.33x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 10.8 ms: 1.56x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.44x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| django_template | 53.3 ms                                                               | 49.6 ms: 1.08x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 83.5 ms: 1.19x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.17x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.58 ms: 1.95x faster                                                   |
| async_tree_none          | 950 ms                                                                | 497 ms: 1.91x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.23 sec: 1.85x faster                                                  |
| generators               | 68.1 ms                                                               | 38.3 ms: 1.78x faster                                                   |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                    |
| richards_super           | 107 ms                                                                | 61.7 ms: 1.74x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 655 ms: 1.73x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.1 ms: 1.70x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 8.66 ms: 1.68x faster                                                   |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 807 ms: 1.58x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 87.2 ms: 1.54x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 615 ms: 1.53x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.58 ms: 1.52x faster                                                   |
| float                    | 135 ms                                                                | 90.4 ms: 1.49x faster                                                   |
| go                       | 264 ms                                                                | 179 ms: 1.47x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.5 ms: 1.46x faster                                                   |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.44x faster                                                  |
| comprehensions           | 33.1 us                                                               | 23.0 us: 1.44x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.41x faster                                                   |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                    |
| chaos                    | 121 ms                                                                | 88.5 ms: 1.37x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 387 us: 1.37x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.79 us: 1.36x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.24 us: 1.35x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 276 us: 1.32x faster                                                    |
| thrift                   | 1.26 ms                                                               | 953 us: 1.32x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                   |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                    |
| pyflate                  | 795 ms                                                                | 623 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| scimark_lu               | 227 ms                                                                | 182 ms: 1.25x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 50.0 us: 1.23x faster                                                   |
| tornado_http             | 178 ms                                                                | 145 ms: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.6 ms: 1.22x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.07 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                   |
| pylint                   | 485 ms                                                                | 411 ms: 1.18x faster                                                    |
| chameleon                | 10.8 ms                                                               | 9.20 ms: 1.18x faster                                                   |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.15x faster                                                    |
| dask                     | 450 ms                                                                | 393 ms: 1.14x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.88 ms: 1.11x faster                                                   |
| scimark_fft              | 500 ms                                                                | 456 ms: 1.10x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 69.8 ms: 1.08x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.82 us: 1.08x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 145 ms: 1.08x faster                                                    |
| django_template          | 53.3 ms                                                               | 49.6 ms: 1.08x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.55 us: 1.07x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.48 sec: 1.06x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| meteor_contest           | 126 ms                                                                | 119 ms: 1.06x faster                                                    |
| 2to3                     | 381 ms                                                                | 360 ms: 1.06x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 69.7 ms: 1.06x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 117 ms: 1.05x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.10 sec: 1.04x faster                                                  |
| sympy_str                | 329 ms                                                                | 317 ms: 1.04x faster                                                    |
| regex_compile            | 177 ms                                                                | 171 ms: 1.03x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.28 sec: 1.03x faster                                                  |
| deepcopy                 | 511 us                                                                | 494 us: 1.03x faster                                                    |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 251 ms: 1.02x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 26.0 ms: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                    |
| nqueens                  | 117 ms                                                                | 119 ms: 1.01x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.67 us: 1.02x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.32 us: 1.02x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.1 us: 1.04x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.42 ms: 1.07x slower                                                   |
| flaskblogging            | 4.83 ms                                                               | 5.23 ms: 1.08x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.2 us: 1.09x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.11x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| async_generators         | 452 ms                                                                | 514 ms: 1.14x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 83.5 ms: 1.19x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.18 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 14.9 ms: 1.33x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 10.8 ms: 1.56x slower                                                   |
| telco                    | 8.49 ms                                                               | 167 ms: 19.63x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.15x faster                                                            |

Benchmark hidden because not significant (6): xml_etree_iterparse, sympy_expand, sympy_sum, genshi_text, docutils, pidigits
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.25x