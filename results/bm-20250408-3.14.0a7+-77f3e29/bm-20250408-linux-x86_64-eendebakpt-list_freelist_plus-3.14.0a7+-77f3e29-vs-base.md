# Results vs. base

- fork: eendebakpt
- ref: list_freelist_plus
- machine: linux-x86_64
- commit hash: 77f3e29
- commit date: 2025-04-08
- overall geometric mean: 1.003x slower
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7+-f5f1ac8 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 252 ms: 1.01x slower                                                     |
| docutils       | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                                   |
| html5lib       | 60.5 ms                                                                | 62.0 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7+-f5f1ac8 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators        | 396 ms                                                                 | 388 ms: 1.02x faster                                                     |
| coroutines              | 23.2 ms                                                                | 23.3 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed | 477 ms                                                                 | 481 ms: 1.01x slower                                                     |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (8): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none, asyncio_websockets, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7+-f5f1ac8 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                     |
| float          | 66.6 ms                                                                | 68.3 ms: 1.03x slower                                                    |
| nbody          | 92.9 ms                                                                | 95.5 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7+-f5f1ac8 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 22.8 ms: 1.05x faster                                                    |
| regex_effbot   | 3.23 ms                                                                | 3.10 ms: 1.04x faster                                                    |
| regex_dna      | 212 ms                                                                 | 204 ms: 1.04x faster                                                     |
| regex_compile  | 123 ms                                                                 | 125 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7+-f5f1ac8 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.94 sec: 1.01x faster                                                   |
| json_loads           | 29.4 us                                                                | 29.2 us: 1.01x faster                                                    |
| pickle_pure_python   | 311 us                                                                 | 312 us: 1.00x slower                                                     |
| xml_etree_iterparse  | 98.7 ms                                                                | 99.3 ms: 1.01x slower                                                    |
| unpickle_pure_python | 215 us                                                                 | 217 us: 1.01x slower                                                     |
| xml_etree_parse      | 142 ms                                                                 | 143 ms: 1.01x slower                                                     |
| xml_etree_generate   | 84.0 ms                                                                | 85.1 ms: 1.01x slower                                                    |
| xml_etree_process    | 58.3 ms                                                                | 59.9 ms: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7+-f5f1ac8 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.21 ms                                                                | 8.21 ms: 1.00x slower                                                    |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7+-f5f1ac8 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 31.8 ms                                                                | 31.4 ms: 1.01x faster                                                    |
| genshi_xml      | 48.6 ms                                                                | 49.0 ms: 1.01x slower                                                    |
| genshi_text     | 20.6 ms                                                                | 20.9 ms: 1.01x slower                                                    |
| mako            | 11.0 ms                                                                | 11.2 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7+-f5f1ac8 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| fannkuch                 | 407 ms                                                                 | 381 ms: 1.07x faster                                                     |
| gc_traversal             | 4.95 ms                                                                | 4.64 ms: 1.07x faster                                                    |
| regex_v8                 | 23.9 ms                                                                | 22.8 ms: 1.05x faster                                                    |
| scimark_lu               | 121 ms                                                                 | 115 ms: 1.05x faster                                                     |
| regex_effbot             | 3.23 ms                                                                | 3.10 ms: 1.04x faster                                                    |
| regex_dna                | 212 ms                                                                 | 204 ms: 1.04x faster                                                     |
| crypto_pyaes             | 71.9 ms                                                                | 69.9 ms: 1.03x faster                                                    |
| nqueens                  | 79.9 ms                                                                | 77.7 ms: 1.03x faster                                                    |
| async_generators         | 396 ms                                                                 | 388 ms: 1.02x faster                                                     |
| hexiom                   | 6.08 ms                                                                | 5.99 ms: 1.02x faster                                                    |
| django_template          | 31.8 ms                                                                | 31.4 ms: 1.01x faster                                                    |
| deepcopy_memo            | 29.1 us                                                                | 28.8 us: 1.01x faster                                                    |
| logging_format           | 6.10 us                                                                | 6.04 us: 1.01x faster                                                    |
| mdp                      | 1.22 sec                                                               | 1.21 sec: 1.01x faster                                                   |
| tomli_loads              | 1.96 sec                                                               | 1.94 sec: 1.01x faster                                                   |
| json_loads               | 29.4 us                                                                | 29.2 us: 1.01x faster                                                    |
| sqlglot_v2_normalize     | 105 ms                                                                 | 105 ms: 1.00x faster                                                     |
| create_gc_cycles         | 2.45 ms                                                                | 2.45 ms: 1.00x faster                                                    |
| python_startup_no_site   | 8.21 ms                                                                | 8.21 ms: 1.00x slower                                                    |
| python_startup           | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                    |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                                     |
| sqlglot_v2_optimize      | 52.0 ms                                                                | 52.1 ms: 1.00x slower                                                    |
| docutils                 | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                                   |
| pickle_pure_python       | 311 us                                                                 | 312 us: 1.00x slower                                                     |
| chaos                    | 54.4 ms                                                                | 54.6 ms: 1.00x slower                                                    |
| pathlib                  | 16.5 ms                                                                | 16.6 ms: 1.00x slower                                                    |
| sympy_integrate          | 19.1 ms                                                                | 19.2 ms: 1.00x slower                                                    |
| xml_etree_iterparse      | 98.7 ms                                                                | 99.3 ms: 1.01x slower                                                    |
| coroutines               | 23.2 ms                                                                | 23.3 ms: 1.01x slower                                                    |
| unpickle_pure_python     | 215 us                                                                 | 217 us: 1.01x slower                                                     |
| raytrace                 | 255 ms                                                                 | 257 ms: 1.01x slower                                                     |
| deepcopy                 | 249 us                                                                 | 251 us: 1.01x slower                                                     |
| async_tree_cpu_io_mixed  | 477 ms                                                                 | 481 ms: 1.01x slower                                                     |
| genshi_xml               | 48.6 ms                                                                | 49.0 ms: 1.01x slower                                                    |
| xml_etree_parse          | 142 ms                                                                 | 143 ms: 1.01x slower                                                     |
| sqlite_synth             | 2.76 us                                                                | 2.79 us: 1.01x slower                                                    |
| sympy_expand             | 452 ms                                                                 | 455 ms: 1.01x slower                                                     |
| 2to3                     | 250 ms                                                                 | 252 ms: 1.01x slower                                                     |
| many_optionals           | 927 us                                                                 | 935 us: 1.01x slower                                                     |
| generators               | 29.2 ms                                                                | 29.5 ms: 1.01x slower                                                    |
| sympy_sum                | 147 ms                                                                 | 148 ms: 1.01x slower                                                     |
| shortest_path            | 489 ms                                                                 | 493 ms: 1.01x slower                                                     |
| sqlalchemy_imperative    | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                                    |
| richards                 | 42.7 ms                                                                | 43.1 ms: 1.01x slower                                                    |
| regex_compile            | 123 ms                                                                 | 125 ms: 1.01x slower                                                     |
| sqlalchemy_declarative   | 131 ms                                                                 | 132 ms: 1.01x slower                                                     |
| genshi_text              | 20.6 ms                                                                | 20.9 ms: 1.01x slower                                                    |
| scimark_monte_carlo      | 64.5 ms                                                                | 65.3 ms: 1.01x slower                                                    |
| mako                     | 11.0 ms                                                                | 11.2 ms: 1.01x slower                                                    |
| comprehensions           | 16.6 us                                                                | 16.8 us: 1.01x slower                                                    |
| xml_etree_generate       | 84.0 ms                                                                | 85.1 ms: 1.01x slower                                                    |
| scimark_sor              | 117 ms                                                                 | 119 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult  | 4.73 ms                                                                | 4.80 ms: 1.01x slower                                                    |
| richards_super           | 48.7 ms                                                                | 49.4 ms: 1.01x slower                                                    |
| sympy_str                | 264 ms                                                                 | 268 ms: 1.02x slower                                                     |
| scimark_fft              | 339 ms                                                                 | 344 ms: 1.02x slower                                                     |
| pyflate                  | 439 ms                                                                 | 446 ms: 1.02x slower                                                     |
| dulwich_log              | 58.4 ms                                                                | 59.3 ms: 1.02x slower                                                    |
| coverage                 | 84.9 ms                                                                | 86.3 ms: 1.02x slower                                                    |
| sqlglot_v2_transpile     | 1.51 ms                                                                | 1.54 ms: 1.02x slower                                                    |
| logging_simple           | 5.45 us                                                                | 5.55 us: 1.02x slower                                                    |
| sqlglot_v2_parse         | 1.21 ms                                                                | 1.23 ms: 1.02x slower                                                    |
| typing_runtime_protocols | 162 us                                                                 | 166 us: 1.02x slower                                                     |
| html5lib                 | 60.5 ms                                                                | 62.0 ms: 1.02x slower                                                    |
| float                    | 66.6 ms                                                                | 68.3 ms: 1.03x slower                                                    |
| go                       | 109 ms                                                                 | 112 ms: 1.03x slower                                                     |
| pprint_safe_repr         | 706 ms                                                                 | 725 ms: 1.03x slower                                                     |
| nbody                    | 92.9 ms                                                                | 95.5 ms: 1.03x slower                                                    |
| xml_etree_process        | 58.3 ms                                                                | 59.9 ms: 1.03x slower                                                    |
| deltablue                | 3.27 ms                                                                | 3.36 ms: 1.03x slower                                                    |
| pprint_pformat           | 1.44 sec                                                               | 1.49 sec: 1.03x slower                                                   |
| logging_silent           | 95.1 ns                                                                | 98.2 ns: 1.03x slower                                                    |
| spectral_norm            | 96.6 ms                                                                | 100.0 ms: 1.04x slower                                                   |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (22): json, async_tree_io, meteor_contest, async_tree_cpu_io_mixed_tg, deepcopy_reduce, pycparser, async_tree_memoization_tg, async_tree_memoization, telco, async_tree_none, bench_thread_pool, sphinx, connected_components, bpe_tokeniser, k_core, json_dumps, bench_mp_pool, asyncio_websockets, async_tree_none_tg, subparsers, async_tree_io_tg, pylint

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x