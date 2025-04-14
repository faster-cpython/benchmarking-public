# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: linux-aarch64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.274x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 313 ms: 1.22x faster                                     |
| chameleon      | 10.8 ms                                                               | 9.22 ms: 1.18x faster                                    |
| docutils       | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                   |
| html5lib       | 86.5 ms                                                               | 65.6 ms: 1.32x faster                                    |
| tornado_http   | 178 ms                                                                | 132 ms: 1.35x faster                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                   |
| async_tree_none         | 950 ms                                                                | 504 ms: 1.88x faster                                     |
| async_tree_memoization  | 1.13 sec                                                              | 664 ms: 1.71x faster                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 789 ms: 1.61x faster                                     |
| Geometric mean          | (ref)                                                                 | 1.80x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 135 ms                                                                | 95.8 ms: 1.41x faster                                    |
| nbody          | 166 ms                                                                | 118 ms: 1.40x faster                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 134 ms: 1.32x faster                                     |
| regex_dna      | 257 ms                                                                | 263 ms: 1.02x slower                                     |
| regex_effbot   | 4.25 ms                                                               | 5.10 ms: 1.20x slower                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 374 us: 1.42x faster                                     |
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                     |
| tomli_loads          | 3.36 sec                                                              | 2.67 sec: 1.26x faster                                   |
| xml_etree_process    | 99.5 ms                                                               | 82.1 ms: 1.21x faster                                    |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                    |
| xml_etree_parse      | 212 ms                                                                | 203 ms: 1.05x faster                                     |
| json_loads           | 30.9 us                                                               | 32.8 us: 1.06x slower                                    |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                             |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                    |
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.35x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                    |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                    |
| genshi_text     | 35.2 ms                                                               | 28.6 ms: 1.23x faster                                    |
| genshi_xml      | 69.8 ms                                                               | 61.6 ms: 1.13x faster                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                     |
| deltablue                | 8.94 ms                                                               | 3.97 ms: 2.26x faster                                    |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                   |
| async_tree_none          | 950 ms                                                                | 504 ms: 1.88x faster                                     |
| raytrace                 | 573 ms                                                                | 310 ms: 1.85x faster                                     |
| bench_mp_pool            | 14.5 ms                                                               | 8.07 ms: 1.80x faster                                    |
| richards_super           | 107 ms                                                                | 60.8 ms: 1.76x faster                                    |
| chaos                    | 121 ms                                                                | 70.7 ms: 1.71x faster                                    |
| async_tree_memoization   | 1.13 sec                                                              | 664 ms: 1.71x faster                                     |
| generators               | 68.1 ms                                                               | 40.3 ms: 1.69x faster                                    |
| richards                 | 91.7 ms                                                               | 54.5 ms: 1.68x faster                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                    |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 789 ms: 1.61x faster                                     |
| go                       | 264 ms                                                                | 164 ms: 1.61x faster                                     |
| comprehensions           | 33.1 us                                                               | 20.8 us: 1.59x faster                                    |
| crypto_pyaes             | 134 ms                                                                | 84.9 ms: 1.58x faster                                    |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.55x faster                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.84 ms: 1.55x faster                                    |
| scimark_sor              | 246 ms                                                                | 164 ms: 1.50x faster                                     |
| hexiom                   | 10.9 ms                                                               | 7.34 ms: 1.49x faster                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.8 ms: 1.46x faster                                    |
| pickle_pure_python       | 529 us                                                                | 374 us: 1.42x faster                                     |
| float                    | 135 ms                                                                | 95.8 ms: 1.41x faster                                    |
| pylint                   | 485 ms                                                                | 345 ms: 1.41x faster                                     |
| nbody                    | 166 ms                                                                | 118 ms: 1.40x faster                                     |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                     |
| pyflate                  | 795 ms                                                                | 582 ms: 1.37x faster                                     |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                    |
| tornado_http             | 178 ms                                                                | 132 ms: 1.35x faster                                     |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                    |
| logging_simple           | 9.78 us                                                               | 7.25 us: 1.35x faster                                    |
| regex_compile            | 177 ms                                                                | 134 ms: 1.32x faster                                     |
| html5lib                 | 86.5 ms                                                               | 65.6 ms: 1.32x faster                                    |
| logging_format           | 10.6 us                                                               | 8.10 us: 1.31x faster                                    |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.30x faster                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 154 ms: 1.28x faster                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.27x faster                                    |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                    |
| tomli_loads              | 3.36 sec                                                              | 2.67 sec: 1.26x faster                                   |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.26x faster                                   |
| thrift                   | 1.26 ms                                                               | 1.01 ms: 1.25x faster                                    |
| gunicorn                 | 1.45 ms                                                               | 1.17 ms: 1.24x faster                                    |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.4 ms: 1.24x faster                                    |
| genshi_text              | 35.2 ms                                                               | 28.6 ms: 1.23x faster                                    |
| 2to3                     | 381 ms                                                                | 313 ms: 1.22x faster                                     |
| sympy_sum                | 184 ms                                                                | 151 ms: 1.22x faster                                     |
| xml_etree_process        | 99.5 ms                                                               | 82.1 ms: 1.21x faster                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 962 ms: 1.19x faster                                     |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                    |
| docutils                 | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.99 sec: 1.19x faster                                   |
| chameleon                | 10.8 ms                                                               | 9.22 ms: 1.18x faster                                    |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                    |
| deepcopy_memo            | 61.7 us                                                               | 53.0 us: 1.16x faster                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 65.2 ms: 1.16x faster                                    |
| sympy_expand             | 543 ms                                                                | 472 ms: 1.15x faster                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.66 ms: 1.15x faster                                    |
| fannkuch                 | 546 ms                                                                | 478 ms: 1.14x faster                                     |
| genshi_xml               | 69.8 ms                                                               | 61.6 ms: 1.13x faster                                    |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.24 us: 1.08x faster                                    |
| scimark_fft              | 500 ms                                                                | 463 ms: 1.08x faster                                     |
| pathlib                  | 26.3 ms                                                               | 24.3 ms: 1.08x faster                                    |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                     |
| mdp                      | 3.70 sec                                                              | 3.45 sec: 1.07x faster                                   |
| deepcopy                 | 511 us                                                                | 479 us: 1.07x faster                                     |
| xml_etree_parse          | 212 ms                                                                | 203 ms: 1.05x faster                                     |
| regex_dna                | 257 ms                                                                | 263 ms: 1.02x slower                                     |
| asyncio_websockets       | 657 ms                                                                | 674 ms: 1.03x slower                                     |
| json_loads               | 30.9 us                                                               | 32.8 us: 1.06x slower                                    |
| async_generators         | 452 ms                                                                | 500 ms: 1.11x slower                                     |
| regex_effbot             | 4.25 ms                                                               | 5.10 ms: 1.20x slower                                    |
| telco                    | 8.49 ms                                                               | 10.5 ms: 1.23x slower                                    |
| coverage                 | 83.6 ms                                                               | 106 ms: 1.26x slower                                     |
| python_startup_no_site   | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                    |
| gc_traversal             | 4.15 ms                                                               | 5.92 ms: 1.43x slower                                    |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.39 ms: 1.50x slower                                    |
| Geometric mean           | (ref)                                                                 | 1.25x faster                                             |

Benchmark hidden because not significant (6): xml_etree_generate, sqlite_synth, json, regex_v8, pidigits, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.274x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.26x