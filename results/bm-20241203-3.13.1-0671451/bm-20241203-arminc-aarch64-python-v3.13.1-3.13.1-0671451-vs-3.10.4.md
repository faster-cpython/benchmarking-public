# Results vs. 3.10.4

- fork: python
- ref: v3.13.1
- machine: linux-aarch64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.270x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 319 ms: 1.19x faster                                     |
| chameleon      | 10.8 ms                                                               | 9.41 ms: 1.15x faster                                    |
| docutils       | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                   |
| html5lib       | 86.5 ms                                                               | 66.7 ms: 1.30x faster                                    |
| tornado_http   | 178 ms                                                                | 130 ms: 1.37x faster                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.16 sec: 1.97x faster                                   |
| async_tree_none         | 950 ms                                                                | 517 ms: 1.84x faster                                     |
| async_tree_memoization  | 1.13 sec                                                              | 664 ms: 1.71x faster                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 766 ms: 1.66x faster                                     |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 135 ms                                                                | 97.4 ms: 1.38x faster                                    |
| nbody          | 166 ms                                                                | 121 ms: 1.37x faster                                     |
| Geometric mean | (ref)                                                                 | 1.23x faster                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 131 ms: 1.35x faster                                     |
| regex_effbot   | 4.25 ms                                                               | 4.06 ms: 1.05x faster                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 375 us: 1.41x faster                                     |
| unpickle_pure_python | 366 us                                                                | 261 us: 1.40x faster                                     |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                   |
| xml_etree_process    | 99.5 ms                                                               | 84.5 ms: 1.18x faster                                    |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                    |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                     |
| xml_etree_parse      | 212 ms                                                                | 201 ms: 1.05x faster                                     |
| json_loads           | 30.9 us                                                               | 34.3 us: 1.11x slower                                    |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.86 ms: 1.29x slower                                    |
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.36x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                    |
| django_template | 53.3 ms                                                               | 41.8 ms: 1.28x faster                                    |
| genshi_text     | 35.2 ms                                                               | 30.3 ms: 1.16x faster                                    |
| genshi_xml      | 69.8 ms                                                               | 62.5 ms: 1.12x faster                                    |
| Geometric mean  | (ref)                                                                 | 1.22x faster                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 200 us: 3.30x faster                                     |
| deltablue                | 8.94 ms                                                               | 4.01 ms: 2.23x faster                                    |
| async_tree_io            | 2.28 sec                                                              | 1.16 sec: 1.97x faster                                   |
| raytrace                 | 573 ms                                                                | 304 ms: 1.88x faster                                     |
| async_tree_none          | 950 ms                                                                | 517 ms: 1.84x faster                                     |
| richards_super           | 107 ms                                                                | 61.9 ms: 1.73x faster                                    |
| chaos                    | 121 ms                                                                | 70.2 ms: 1.73x faster                                    |
| async_tree_memoization   | 1.13 sec                                                              | 664 ms: 1.71x faster                                     |
| bench_mp_pool            | 14.5 ms                                                               | 8.56 ms: 1.70x faster                                    |
| richards                 | 91.7 ms                                                               | 54.4 ms: 1.69x faster                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.44 ms: 1.67x faster                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 766 ms: 1.66x faster                                     |
| generators               | 68.1 ms                                                               | 41.2 ms: 1.65x faster                                    |
| scimark_lu               | 227 ms                                                                | 143 ms: 1.59x faster                                     |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                     |
| go                       | 264 ms                                                                | 167 ms: 1.58x faster                                     |
| crypto_pyaes             | 134 ms                                                                | 84.8 ms: 1.58x faster                                    |
| comprehensions           | 33.1 us                                                               | 21.6 us: 1.53x faster                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.86 ms: 1.52x faster                                    |
| hexiom                   | 10.9 ms                                                               | 7.38 ms: 1.48x faster                                    |
| scimark_monte_carlo      | 128 ms                                                                | 88.1 ms: 1.45x faster                                    |
| scimark_sor              | 246 ms                                                                | 171 ms: 1.44x faster                                     |
| pickle_pure_python       | 529 us                                                                | 375 us: 1.41x faster                                     |
| unpickle_pure_python     | 366 us                                                                | 261 us: 1.40x faster                                     |
| float                    | 135 ms                                                                | 97.4 ms: 1.38x faster                                    |
| tornado_http             | 178 ms                                                                | 130 ms: 1.37x faster                                     |
| nbody                    | 166 ms                                                                | 121 ms: 1.37x faster                                     |
| pylint                   | 485 ms                                                                | 358 ms: 1.36x faster                                     |
| regex_compile            | 177 ms                                                                | 131 ms: 1.35x faster                                     |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                    |
| logging_simple           | 9.78 us                                                               | 7.38 us: 1.32x faster                                    |
| logging_format           | 10.6 us                                                               | 8.08 us: 1.31x faster                                    |
| html5lib                 | 86.5 ms                                                               | 66.7 ms: 1.30x faster                                    |
| pyflate                  | 795 ms                                                                | 614 ms: 1.30x faster                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                    |
| pycparser                | 1.69 sec                                                              | 1.32 sec: 1.28x faster                                   |
| django_template          | 53.3 ms                                                               | 41.8 ms: 1.28x faster                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 156 ms: 1.27x faster                                     |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                     |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                   |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.24x faster                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.5 ms: 1.24x faster                                    |
| coroutines               | 37.2 ms                                                               | 30.2 ms: 1.23x faster                                    |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.23x faster                                    |
| thrift                   | 1.26 ms                                                               | 1.03 ms: 1.22x faster                                    |
| docutils                 | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                   |
| 2to3                     | 381 ms                                                                | 319 ms: 1.19x faster                                     |
| sqlglot_normalize        | 156 ms                                                                | 132 ms: 1.18x faster                                     |
| xml_etree_process        | 99.5 ms                                                               | 84.5 ms: 1.18x faster                                    |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.01 sec: 1.17x faster                                   |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 64.5 ms: 1.17x faster                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 987 ms: 1.16x faster                                     |
| genshi_text              | 35.2 ms                                                               | 30.3 ms: 1.16x faster                                    |
| deepcopy_memo            | 61.7 us                                                               | 53.4 us: 1.16x faster                                    |
| chameleon                | 10.8 ms                                                               | 9.41 ms: 1.15x faster                                    |
| gunicorn                 | 1.45 ms                                                               | 1.27 ms: 1.14x faster                                    |
| fannkuch                 | 546 ms                                                                | 482 ms: 1.13x faster                                     |
| sympy_expand             | 543 ms                                                                | 481 ms: 1.13x faster                                     |
| genshi_xml               | 69.8 ms                                                               | 62.5 ms: 1.12x faster                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.87 ms: 1.11x faster                                    |
| pathlib                  | 26.3 ms                                                               | 24.0 ms: 1.10x faster                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.27 us: 1.08x faster                                    |
| deepcopy                 | 511 us                                                                | 476 us: 1.07x faster                                     |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                   |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                     |
| scimark_fft              | 500 ms                                                                | 472 ms: 1.06x faster                                     |
| xml_etree_parse          | 212 ms                                                                | 201 ms: 1.05x faster                                     |
| regex_effbot             | 4.25 ms                                                               | 4.06 ms: 1.05x faster                                    |
| asyncio_websockets       | 657 ms                                                                | 677 ms: 1.03x slower                                     |
| json_loads               | 30.9 us                                                               | 34.3 us: 1.11x slower                                    |
| async_generators         | 452 ms                                                                | 517 ms: 1.14x slower                                     |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.24x slower                                     |
| telco                    | 8.49 ms                                                               | 10.8 ms: 1.27x slower                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.86 ms: 1.29x slower                                    |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                    |
| gc_traversal             | 4.15 ms                                                               | 5.97 ms: 1.44x slower                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.42 ms: 1.51x slower                                    |
| Geometric mean           | (ref)                                                                 | 1.25x faster                                             |

Benchmark hidden because not significant (7): meteor_contest, xml_etree_iterparse, pidigits, json, regex_v8, regex_dna, sqlite_synth
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241203-3.13.1-0671451/bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.270x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.27x