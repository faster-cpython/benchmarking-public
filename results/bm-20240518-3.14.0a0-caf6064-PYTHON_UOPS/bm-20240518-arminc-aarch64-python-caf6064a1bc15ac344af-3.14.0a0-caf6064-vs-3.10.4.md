# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 353 ms: 1.08x faster                                                    |
| chameleon      | 10.8 ms                                                               | 9.93 ms: 1.09x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.51 sec: 1.01x faster                                                  |
| html5lib       | 86.5 ms                                                               | 73.7 ms: 1.17x faster                                                   |
| tornado_http   | 178 ms                                                                | 139 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 507 ms: 1.87x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 665 ms: 1.70x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 814 ms: 1.56x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.74x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 137 ms: 1.21x faster                                                    |
| float          | 135 ms                                                                | 113 ms: 1.19x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 166 ms: 1.06x faster                                                    |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.2 ms: 1.03x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 440 us: 1.20x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 87.2 ms: 1.14x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 195 ms: 1.09x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 3.09 sec: 1.09x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 349 us: 1.05x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.77 us: 1.03x faster                                                   |
| pickle_list          | 5.24 us                                                               | 5.28 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 162 ms: 1.04x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.11x slower                                                   |
| pickle               | 12.5 us                                                               | 14.0 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.6 ms: 1.13x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 16.8 ms: 1.13x faster                                                   |
| django_template | 53.3 ms                                                               | 48.9 ms: 1.09x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 35.6 ms: 1.01x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 76.1 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 227 us: 2.91x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.71 ms: 1.88x faster                                                   |
| async_tree_none          | 950 ms                                                                | 507 ms: 1.87x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                  |
| deltablue                | 8.94 ms                                                               | 5.14 ms: 1.74x faster                                                   |
| generators               | 68.1 ms                                                               | 39.5 ms: 1.72x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 665 ms: 1.70x faster                                                    |
| raytrace                 | 573 ms                                                                | 342 ms: 1.68x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 592 ms: 1.59x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 814 ms: 1.56x faster                                                    |
| richards_super           | 107 ms                                                                | 72.5 ms: 1.48x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.46x faster                                                  |
| richards                 | 91.7 ms                                                               | 64.4 ms: 1.42x faster                                                   |
| chaos                    | 121 ms                                                                | 85.6 ms: 1.42x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.77 ms: 1.36x faster                                                   |
| go                       | 264 ms                                                                | 195 ms: 1.35x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.38 us: 1.33x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 101 ms: 1.32x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.07 us: 1.31x faster                                                   |
| tornado_http             | 178 ms                                                                | 139 ms: 1.28x faster                                                    |
| thrift                   | 1.26 ms                                                               | 983 us: 1.28x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.22 ms: 1.28x faster                                                   |
| scimark_sor              | 246 ms                                                                | 198 ms: 1.25x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.37 sec: 1.23x faster                                                  |
| pylint                   | 485 ms                                                                | 396 ms: 1.23x faster                                                    |
| nbody                    | 166 ms                                                                | 137 ms: 1.21x faster                                                    |
| coroutines               | 37.2 ms                                                               | 30.8 ms: 1.21x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 440 us: 1.20x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                   |
| float                    | 135 ms                                                                | 113 ms: 1.19x faster                                                    |
| logging_silent           | 222 ns                                                                | 189 ns: 1.18x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 73.7 ms: 1.17x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.15x faster                                                   |
| dask                     | 450 ms                                                                | 391 ms: 1.15x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 87.2 ms: 1.14x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 65.2 ms: 1.13x faster                                                   |
| mako                     | 18.9 ms                                                               | 16.8 ms: 1.13x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 114 ms: 1.12x faster                                                    |
| comprehensions           | 33.1 us                                                               | 30.1 us: 1.10x faster                                                   |
| scimark_lu               | 227 ms                                                                | 207 ms: 1.10x faster                                                    |
| pyflate                  | 795 ms                                                                | 727 ms: 1.09x faster                                                    |
| chameleon                | 10.8 ms                                                               | 9.93 ms: 1.09x faster                                                   |
| django_template          | 53.3 ms                                                               | 48.9 ms: 1.09x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 195 ms: 1.09x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.09 sec: 1.09x faster                                                  |
| 2to3                     | 381 ms                                                                | 353 ms: 1.08x faster                                                    |
| regex_compile            | 177 ms                                                                | 166 ms: 1.06x faster                                                    |
| sympy_sum                | 184 ms                                                                | 175 ms: 1.05x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 349 us: 1.05x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 72.3 ms: 1.04x faster                                                   |
| sympy_expand             | 543 ms                                                                | 522 ms: 1.04x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.5 ms: 1.04x faster                                                   |
| sympy_str                | 329 ms                                                                | 317 ms: 1.04x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.98 us: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.2 ms: 1.03x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.77 us: 1.03x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.59 sec: 1.03x faster                                                  |
| sympy_integrate          | 26.5 ms                                                               | 25.9 ms: 1.02x faster                                                   |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.51 sec: 1.01x faster                                                  |
| pickle_list              | 5.24 us                                                               | 5.28 us: 1.01x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 35.6 ms: 1.01x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.41 sec: 1.02x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.18 sec: 1.03x slower                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 162 ms: 1.04x slower                                                    |
| flaskblogging            | 4.83 ms                                                               | 5.02 ms: 1.04x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.80 us: 1.04x slower                                                   |
| deepcopy                 | 511 us                                                                | 535 us: 1.05x slower                                                    |
| fannkuch                 | 546 ms                                                                | 574 ms: 1.05x slower                                                    |
| meteor_contest           | 126 ms                                                                | 133 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.05 ms: 1.06x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                                   |
| scimark_fft              | 500 ms                                                                | 539 ms: 1.08x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 76.1 ms: 1.09x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.47 ms: 1.09x slower                                                   |
| nqueens                  | 117 ms                                                                | 130 ms: 1.11x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.11x slower                                                   |
| pickle                   | 12.5 us                                                               | 14.0 us: 1.12x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.6 ms: 1.13x slower                                                   |
| async_generators         | 452 ms                                                                | 517 ms: 1.14x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| deepcopy_memo            | 61.7 us                                                               | 71.9 us: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.25 ms: 1.26x slower                                                   |
| telco                    | 8.49 ms                                                               | 168 ms: 19.81x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (3): spectral_norm, pidigits, xml_etree_generate
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.15x