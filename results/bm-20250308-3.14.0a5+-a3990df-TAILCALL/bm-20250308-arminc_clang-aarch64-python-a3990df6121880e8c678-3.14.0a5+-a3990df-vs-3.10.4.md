# Results vs. 3.10.4

- fork: python
- ref: a3990df6121880e8c678
- machine: linux-aarch64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.393x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 284 ms: 1.34x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.87 sec: 1.23x faster                                                   |
| html5lib       | 86.5 ms                                                               | 57.3 ms: 1.51x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.36x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 861 ms: 2.65x faster                                                     |
| async_tree_none         | 950 ms                                                                | 364 ms: 2.61x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 453 ms: 2.50x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 712 ms: 1.79x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.4 ms: 1.60x faster                                                    |
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                     |
| pidigits       | 235 ms                                                                | 296 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 121 ms: 1.45x faster                                                     |
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 32.3 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.29 sec: 1.47x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 256 us: 1.43x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 375 us: 1.41x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 72.1 ms: 1.38x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 100 ms: 1.23x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 5.75 us: 1.22x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| unpickle             | 17.5 us                                                               | 16.5 us: 1.06x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 207 ms: 1.02x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.35 us: 1.02x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                    |
| pickle               | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 37.2 ms: 1.43x faster                                                    |
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.3 ms: 1.34x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 57.2 ms: 1.22x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.35x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 174 us: 3.79x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 861 ms: 2.65x faster                                                     |
| async_tree_none          | 950 ms                                                                | 364 ms: 2.61x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 453 ms: 2.50x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.78 ms: 2.37x faster                                                    |
| go                       | 264 ms                                                                | 131 ms: 2.01x faster                                                     |
| richards_super           | 107 ms                                                                | 53.9 ms: 1.99x faster                                                    |
| logging_silent           | 222 ns                                                                | 114 ns: 1.95x faster                                                     |
| generators               | 68.1 ms                                                               | 35.4 ms: 1.92x faster                                                    |
| richards                 | 91.7 ms                                                               | 48.0 ms: 1.91x faster                                                    |
| raytrace                 | 573 ms                                                                | 302 ms: 1.90x faster                                                     |
| chaos                    | 121 ms                                                                | 63.9 ms: 1.90x faster                                                    |
| scimark_sor              | 246 ms                                                                | 135 ms: 1.83x faster                                                     |
| spectral_norm            | 186 ms                                                                | 102 ms: 1.83x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.34 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 712 ms: 1.79x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 34.6 us: 1.78x faster                                                    |
| comprehensions           | 33.1 us                                                               | 18.8 us: 1.77x faster                                                    |
| deepcopy                 | 511 us                                                                | 292 us: 1.75x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 542 ms: 1.74x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.64 ms: 1.73x faster                                                    |
| scimark_lu               | 227 ms                                                                | 132 ms: 1.72x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 75.2 ms: 1.70x faster                                                    |
| pylint                   | 485 ms                                                                | 299 ms: 1.62x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 83.5 ms: 1.61x faster                                                    |
| float                    | 135 ms                                                                | 84.4 ms: 1.60x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 6.90 ms: 1.58x faster                                                    |
| pyflate                  | 795 ms                                                                | 506 ms: 1.57x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.17 sec: 1.52x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 57.3 ms: 1.51x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.58 us: 1.49x faster                                                    |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.29 sec: 1.47x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.26 us: 1.46x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 50.5 ms: 1.45x faster                                                    |
| regex_compile            | 177 ms                                                                | 121 ms: 1.45x faster                                                     |
| django_template          | 53.3 ms                                                               | 37.2 ms: 1.43x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 256 us: 1.43x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 140 ms: 1.41x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 375 us: 1.41x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.26 us: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.40x faster                                                   |
| sqlalchemy_imperative    | 20.5 ms                                                               | 14.7 ms: 1.40x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 72.1 ms: 1.38x faster                                                    |
| scimark_fft              | 500 ms                                                                | 363 ms: 1.38x faster                                                     |
| thrift                   | 1.26 ms                                                               | 918 us: 1.37x faster                                                     |
| coroutines               | 37.2 ms                                                               | 27.4 ms: 1.36x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 19.7 ms: 1.35x faster                                                    |
| 2to3                     | 381 ms                                                                | 284 ms: 1.34x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 26.3 ms: 1.34x faster                                                    |
| sympy_sum                | 184 ms                                                                | 139 ms: 1.32x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 118 ms: 1.32x faster                                                     |
| sympy_str                | 329 ms                                                                | 255 ms: 1.29x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.84 sec: 1.28x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 5.98 ms: 1.28x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 903 ms: 1.27x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 59.4 ms: 1.27x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.24x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.87 sec: 1.23x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 100 ms: 1.23x faster                                                     |
| sympy_expand             | 543 ms                                                                | 444 ms: 1.22x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 57.2 ms: 1.22x faster                                                    |
| nqueens                  | 117 ms                                                                | 96.5 ms: 1.22x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 5.75 us: 1.22x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.16 sec: 1.17x faster                                                   |
| fannkuch                 | 546 ms                                                                | 475 ms: 1.15x faster                                                     |
| async_generators         | 452 ms                                                                | 395 ms: 1.15x faster                                                     |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.74 us: 1.10x faster                                                    |
| unpickle                 | 17.5 us                                                               | 16.5 us: 1.06x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                     |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 207 ms: 1.02x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 32.3 ms: 1.01x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.35 us: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.24 ms: 1.09x slower                                                    |
| coverage                 | 83.6 ms                                                               | 91.3 ms: 1.09x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| pidigits                 | 235 ms                                                                | 296 ms: 1.26x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.62 ms: 1.59x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.61 ms: 1.60x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.87 sec: 403.66x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                             |

Benchmark hidden because not significant (3): regex_effbot, asyncio_websockets, pickle_dict
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.393x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.35x