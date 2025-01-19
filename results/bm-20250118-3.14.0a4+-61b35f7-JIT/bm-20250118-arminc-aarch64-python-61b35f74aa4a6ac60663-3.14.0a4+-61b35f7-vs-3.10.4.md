# Results vs. 3.10.4

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.218x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 329 ms: 1.16x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.24 sec: 1.09x faster                                                   |
| html5lib       | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 921 ms: 2.48x faster                                                     |
| async_tree_none         | 950 ms                                                                | 406 ms: 2.34x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 519 ms: 2.18x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 701 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.5 ms: 1.52x faster                                                    |
| nbody          | 166 ms                                                                | 124 ms: 1.34x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 144 ms: 1.23x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                    |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 264 us: 1.39x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 405 us: 1.31x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 81.8 ms: 1.22x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.17x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.66 us: 1.05x faster                                                    |
| unpickle             | 17.5 us                                                               | 18.5 us: 1.06x slower                                                    |
| json_loads           | 30.9 us                                                               | 33.6 us: 1.09x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 39.4 us: 1.12x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.08 us: 1.16x slower                                                    |
| pickle               | 12.5 us                                                               | 15.8 us: 1.27x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.10 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| django_template | 53.3 ms                                                               | 48.8 ms: 1.09x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 33.7 ms: 1.04x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 87.0 ms: 1.25x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 222 us: 2.98x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 921 ms: 2.48x faster                                                     |
| async_tree_none          | 950 ms                                                                | 406 ms: 2.34x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 519 ms: 2.18x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.38 ms: 2.04x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 701 ms: 1.81x faster                                                     |
| richards_super           | 107 ms                                                                | 63.8 ms: 1.68x faster                                                    |
| raytrace                 | 573 ms                                                                | 347 ms: 1.65x faster                                                     |
| richards                 | 91.7 ms                                                               | 56.3 ms: 1.63x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 594 ms: 1.59x faster                                                     |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                     |
| float                    | 135 ms                                                                | 88.5 ms: 1.52x faster                                                    |
| logging_silent           | 222 ns                                                                | 150 ns: 1.48x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.63 ms: 1.48x faster                                                    |
| chaos                    | 121 ms                                                                | 82.3 ms: 1.47x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.5 ms: 1.46x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.96 ms: 1.45x faster                                                    |
| scimark_lu               | 227 ms                                                                | 157 ms: 1.45x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 43.2 us: 1.43x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 94.0 ms: 1.43x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.33 sec: 1.41x faster                                                   |
| go                       | 264 ms                                                                | 188 ms: 1.41x faster                                                     |
| pylint                   | 485 ms                                                                | 349 ms: 1.39x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.39x faster                                                     |
| spectral_norm            | 186 ms                                                                | 135 ms: 1.38x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| nbody                    | 166 ms                                                                | 124 ms: 1.34x faster                                                     |
| comprehensions           | 33.1 us                                                               | 24.8 us: 1.33x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 405 us: 1.31x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 153 ms: 1.29x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                    |
| thrift                   | 1.26 ms                                                               | 985 us: 1.28x faster                                                     |
| pyflate                  | 795 ms                                                                | 624 ms: 1.27x faster                                                     |
| deepcopy                 | 511 us                                                                | 411 us: 1.24x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                    |
| generators               | 68.1 ms                                                               | 55.5 ms: 1.23x faster                                                    |
| regex_compile            | 177 ms                                                                | 144 ms: 1.23x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 81.8 ms: 1.22x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.0 ms: 1.21x faster                                                    |
| logging_simple           | 9.78 us                                                               | 8.19 us: 1.19x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.91 us: 1.19x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.17x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                                    |
| scimark_fft              | 500 ms                                                                | 432 ms: 1.16x faster                                                     |
| 2to3                     | 381 ms                                                                | 329 ms: 1.16x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 23.0 ms: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.68 ms: 1.14x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.40 ms: 1.13x faster                                                    |
| sympy_sum                | 184 ms                                                                | 162 ms: 1.13x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.71 ms: 1.12x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.54 sec: 1.10x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| django_template          | 53.3 ms                                                               | 48.8 ms: 1.09x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.09x faster                                                     |
| sympy_str                | 329 ms                                                                | 301 ms: 1.09x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.24 sec: 1.09x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.26 us: 1.08x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 70.2 ms: 1.07x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| fannkuch                 | 546 ms                                                                | 515 ms: 1.06x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.66 us: 1.05x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 33.7 ms: 1.04x faster                                                    |
| sympy_expand             | 543 ms                                                                | 526 ms: 1.03x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.59 sec: 1.03x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 4.02 us: 1.02x faster                                                    |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 674 ms: 1.03x slower                                                     |
| json                     | 5.88 ms                                                               | 6.17 ms: 1.05x slower                                                    |
| unpickle                 | 17.5 us                                                               | 18.5 us: 1.06x slower                                                    |
| nqueens                  | 117 ms                                                                | 126 ms: 1.07x slower                                                     |
| json_loads               | 30.9 us                                                               | 33.6 us: 1.09x slower                                                    |
| async_generators         | 452 ms                                                                | 497 ms: 1.10x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 39.4 us: 1.12x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.29 sec: 1.12x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.65 sec: 1.12x slower                                                   |
| pickle_list              | 5.24 us                                                               | 6.08 us: 1.16x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                    |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 87.0 ms: 1.25x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.8 us: 1.27x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.10 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.65 ms: 1.61x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 7.00 ms: 1.68x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.21 sec: 152.18x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                             |

Benchmark hidden because not significant (5): json_dumps, dulwich_log, meteor_contest, regex_v8, pidigits
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.218x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.32x