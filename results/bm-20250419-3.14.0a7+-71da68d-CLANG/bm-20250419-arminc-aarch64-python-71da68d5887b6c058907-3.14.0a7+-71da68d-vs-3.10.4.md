# Results vs. 3.10.4

- fork: python
- ref: 71da68d5887b6c058907
- machine: linux-aarch64
- commit hash: 71da68d
- commit date: 2025-04-19
- overall geometric mean: 1.365x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 289 ms: 1.32x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.90 sec: 1.22x faster                                                   |
| html5lib       | 86.5 ms                                                               | 58.6 ms: 1.48x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.33x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 861 ms: 2.65x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 455 ms: 2.49x faster                                                     |
| async_tree_none         | 950 ms                                                                | 381 ms: 2.49x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 727 ms: 1.75x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.32x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.0 ms: 1.60x faster                                                    |
| nbody          | 166 ms                                                                | 126 ms: 1.31x faster                                                     |
| pidigits       | 235 ms                                                                | 291 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.44x faster                                                     |
| regex_dna      | 257 ms                                                                | 232 ms: 1.11x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 367 us: 1.44x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 74.9 ms: 1.33x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.72 us: 1.22x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 104 ms: 1.18x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| unpickle             | 17.5 us                                                               | 16.4 us: 1.06x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 207 ms: 1.02x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.32 us: 1.02x slower                                                    |
| json_loads           | 30.9 us                                                               | 33.5 us: 1.08x slower                                                    |
| pickle               | 12.5 us                                                               | 15.4 us: 1.23x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.13x faster                                                             |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                    |
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.1 ms: 1.35x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 58.6 ms: 1.19x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 188 us: 3.51x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 861 ms: 2.65x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 455 ms: 2.49x faster                                                     |
| async_tree_none          | 950 ms                                                                | 381 ms: 2.49x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.61 sec: 2.30x faster                                                   |
| go                       | 264 ms                                                                | 129 ms: 2.05x faster                                                     |
| logging_silent           | 222 ns                                                                | 114 ns: 1.94x faster                                                     |
| generators               | 68.1 ms                                                               | 35.2 ms: 1.93x faster                                                    |
| richards_super           | 107 ms                                                                | 56.8 ms: 1.89x faster                                                    |
| richards                 | 91.7 ms                                                               | 48.7 ms: 1.88x faster                                                    |
| chaos                    | 121 ms                                                                | 65.1 ms: 1.86x faster                                                    |
| raytrace                 | 573 ms                                                                | 318 ms: 1.80x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 533 ms: 1.77x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 727 ms: 1.75x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 35.6 us: 1.73x faster                                                    |
| scimark_sor              | 246 ms                                                                | 144 ms: 1.71x faster                                                     |
| comprehensions           | 33.1 us                                                               | 20.0 us: 1.66x faster                                                    |
| deepcopy                 | 511 us                                                                | 308 us: 1.66x faster                                                     |
| float                    | 135 ms                                                                | 84.0 ms: 1.60x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 84.3 ms: 1.59x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 6.94 ms: 1.57x faster                                                    |
| spectral_norm            | 186 ms                                                                | 119 ms: 1.57x faster                                                     |
| pylint                   | 485 ms                                                                | 310 ms: 1.57x faster                                                     |
| scimark_lu               | 227 ms                                                                | 145 ms: 1.57x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 83.0 ms: 1.54x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.16 sec: 1.52x faster                                                   |
| pyflate                  | 795 ms                                                                | 527 ms: 1.51x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 58.6 ms: 1.48x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 50.7 ms: 1.45x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 367 us: 1.44x faster                                                     |
| regex_compile            | 177 ms                                                                | 123 ms: 1.44x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.27 us: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.96 us: 1.41x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.56 us: 1.40x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 19.4 ms: 1.37x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| sympy_sum                | 184 ms                                                                | 136 ms: 1.35x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 26.1 ms: 1.35x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 74.9 ms: 1.33x faster                                                    |
| 2to3                     | 381 ms                                                                | 289 ms: 1.32x faster                                                     |
| nbody                    | 166 ms                                                                | 126 ms: 1.31x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                    |
| sympy_str                | 329 ms                                                                | 257 ms: 1.28x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.27x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 913 ms: 1.26x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.25x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 5.72 us: 1.22x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.90 sec: 1.22x faster                                                   |
| sympy_expand             | 543 ms                                                                | 451 ms: 1.20x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                    |
| nqueens                  | 117 ms                                                                | 98.2 ms: 1.20x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 58.6 ms: 1.19x faster                                                    |
| scimark_fft              | 500 ms                                                                | 422 ms: 1.19x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 104 ms: 1.18x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.62 ms: 1.15x faster                                                    |
| regex_dna                | 257 ms                                                                | 232 ms: 1.11x faster                                                     |
| fannkuch                 | 546 ms                                                                | 495 ms: 1.10x faster                                                     |
| async_generators         | 452 ms                                                                | 416 ms: 1.09x faster                                                     |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                    |
| unpickle                 | 17.5 us                                                               | 16.4 us: 1.06x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 207 ms: 1.02x faster                                                     |
| json                     | 5.88 ms                                                               | 5.84 ms: 1.01x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.32 us: 1.02x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.18 ms: 1.08x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.5 us: 1.08x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.4 us: 1.23x slower                                                    |
| pidigits                 | 235 ms                                                                | 291 ms: 1.24x slower                                                     |
| coverage                 | 83.6 ms                                                               | 106 ms: 1.27x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.64 ms: 1.60x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.73 ms: 1.65x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.85 sec: 127.30x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.365x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.36x