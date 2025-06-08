# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.078x slower
- HPT reliability: 98.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.71x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 447 ms: 1.17x slower                                                    |
| docutils       | 3.53 sec                                                              | 3.92 sec: 1.11x slower                                                  |
| html5lib       | 86.5 ms                                                               | 82.9 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.01 sec: 2.26x faster                                                  |
| async_tree_none         | 950 ms                                                                | 466 ms: 2.04x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 560 ms: 2.02x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 847 ms: 1.50x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.93x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 106 ms: 1.27x faster                                                    |
| nbody          | 166 ms                                                                | 192 ms: 1.16x slower                                                    |
| pidigits       | 235 ms                                                                | 277 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 233 ms: 1.10x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| regex_compile  | 177 ms                                                                | 196 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 3.55 sec: 1.06x slower                                                  |
| pickle_pure_python   | 529 us                                                                | 580 us: 1.10x slower                                                    |
| unpickle_list        | 6.99 us                                                               | 7.77 us: 1.11x slower                                                   |
| xml_etree_parse      | 212 ms                                                                | 236 ms: 1.11x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 420 us: 1.15x slower                                                    |
| json_dumps           | 16.7 ms                                                               | 19.7 ms: 1.18x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 45.5 us: 1.30x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 129 ms: 1.30x slower                                                    |
| pickle_list          | 5.24 us                                                               | 7.26 us: 1.39x slower                                                   |
| json_loads           | 30.9 us                                                               | 44.9 us: 1.45x slower                                                   |
| unpickle             | 17.5 us                                                               | 26.7 us: 1.53x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 192 ms: 1.56x slower                                                    |
| pickle               | 12.5 us                                                               | 20.0 us: 1.60x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.26x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 13.8 ms: 2.00x slower                                                   |
| python_startup         | 11.2 ms                                                               | 22.9 ms: 2.05x slower                                                   |
| Geometric mean         | (ref)                                                                 | 2.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 24.1 ms: 1.27x slower                                                   |
| genshi_text     | 35.2 ms                                                               | 46.0 ms: 1.31x slower                                                   |
| django_template | 53.3 ms                                                               | 73.3 ms: 1.37x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 97.3 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.34x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 1.01 sec: 2.26x faster                                                  |
| async_tree_none          | 950 ms                                                                | 466 ms: 2.04x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 560 ms: 2.02x faster                                                    |
| typing_runtime_protocols | 661 us                                                                | 354 us: 1.87x faster                                                    |
| deltablue                | 8.94 ms                                                               | 5.68 ms: 1.57x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 627 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 847 ms: 1.50x faster                                                    |
| mdp                      | 3.70 sec                                                              | 2.54 sec: 1.46x faster                                                  |
| go                       | 264 ms                                                                | 182 ms: 1.45x faster                                                    |
| generators               | 68.1 ms                                                               | 46.9 ms: 1.45x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.50 sec: 1.31x faster                                                  |
| float                    | 135 ms                                                                | 106 ms: 1.27x faster                                                    |
| scimark_sor              | 246 ms                                                                | 204 ms: 1.21x faster                                                    |
| chaos                    | 121 ms                                                                | 101 ms: 1.20x faster                                                    |
| pyflate                  | 795 ms                                                                | 685 ms: 1.16x faster                                                    |
| gc_traversal             | 4.15 ms                                                               | 3.58 ms: 1.16x faster                                                   |
| raytrace                 | 573 ms                                                                | 496 ms: 1.16x faster                                                    |
| regex_dna                | 257 ms                                                                | 233 ms: 1.10x faster                                                    |
| comprehensions           | 33.1 us                                                               | 30.2 us: 1.10x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 10.0 ms: 1.09x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 56.9 us: 1.08x faster                                                   |
| richards_super           | 107 ms                                                                | 101 ms: 1.06x faster                                                    |
| richards                 | 91.7 ms                                                               | 86.8 ms: 1.06x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 82.9 ms: 1.04x faster                                                   |
| pylint                   | 485 ms                                                                | 468 ms: 1.04x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                    |
| pycparser                | 1.69 sec                                                              | 1.75 sec: 1.03x slower                                                  |
| scimark_lu               | 227 ms                                                                | 234 ms: 1.03x slower                                                    |
| deepcopy                 | 511 us                                                                | 529 us: 1.04x slower                                                    |
| spectral_norm            | 186 ms                                                                | 193 ms: 1.04x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.55 sec: 1.06x slower                                                  |
| crypto_pyaes             | 134 ms                                                                | 145 ms: 1.08x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 79.5 ms: 1.08x slower                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 139 ms: 1.09x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 580 us: 1.10x slower                                                    |
| sqlite_synth             | 4.12 us                                                               | 4.51 us: 1.10x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.49 ms: 1.10x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.92 sec: 1.11x slower                                                  |
| regex_compile            | 177 ms                                                                | 196 ms: 1.11x slower                                                    |
| unpickle_list            | 6.99 us                                                               | 7.77 us: 1.11x slower                                                   |
| xml_etree_parse          | 212 ms                                                                | 236 ms: 1.11x slower                                                    |
| pathlib                  | 26.3 ms                                                               | 29.9 ms: 1.14x slower                                                   |
| unpickle_pure_python     | 366 us                                                                | 420 us: 1.15x slower                                                    |
| nbody                    | 166 ms                                                                | 192 ms: 1.16x slower                                                    |
| scimark_fft              | 500 ms                                                                | 583 ms: 1.16x slower                                                    |
| 2to3                     | 381 ms                                                                | 447 ms: 1.17x slower                                                    |
| pidigits                 | 235 ms                                                                | 277 ms: 1.18x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 31.3 ms: 1.18x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 19.7 ms: 1.18x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 9.05 ms: 1.19x slower                                                   |
| logging_simple           | 9.78 us                                                               | 11.7 us: 1.19x slower                                                   |
| meteor_contest           | 126 ms                                                                | 154 ms: 1.22x slower                                                    |
| logging_format           | 10.6 us                                                               | 13.0 us: 1.22x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.98 ms: 1.24x slower                                                   |
| mako                     | 18.9 ms                                                               | 24.1 ms: 1.27x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.63 ms: 1.29x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 45.5 us: 1.30x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 129 ms: 1.30x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 5.97 us: 1.30x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 46.0 ms: 1.31x slower                                                   |
| fannkuch                 | 546 ms                                                                | 713 ms: 1.31x slower                                                    |
| nqueens                  | 117 ms                                                                | 156 ms: 1.33x slower                                                    |
| sympy_sum                | 184 ms                                                                | 246 ms: 1.34x slower                                                    |
| sympy_str                | 329 ms                                                                | 449 ms: 1.37x slower                                                    |
| json                     | 5.88 ms                                                               | 8.06 ms: 1.37x slower                                                   |
| django_template          | 53.3 ms                                                               | 73.3 ms: 1.37x slower                                                   |
| async_generators         | 452 ms                                                                | 626 ms: 1.38x slower                                                    |
| pickle_list              | 5.24 us                                                               | 7.26 us: 1.39x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 97.3 ms: 1.39x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 3.31 sec: 1.40x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.62 sec: 1.41x slower                                                  |
| json_loads               | 30.9 us                                                               | 44.9 us: 1.45x slower                                                   |
| sympy_expand             | 543 ms                                                                | 790 ms: 1.46x slower                                                    |
| unpickle                 | 17.5 us                                                               | 26.7 us: 1.53x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 192 ms: 1.56x slower                                                    |
| pickle                   | 12.5 us                                                               | 20.0 us: 1.60x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 13.8 ms: 2.00x slower                                                   |
| python_startup           | 11.2 ms                                                               | 22.9 ms: 2.05x slower                                                   |
| telco                    | 8.49 ms                                                               | 18.1 ms: 2.13x slower                                                   |
| coverage                 | 83.6 ms                                                               | 184 ms: 2.20x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 72.6 ms: 5.00x slower                                                   |
| logging_silent           | 222 ns                                                                | 1.13 us: 5.07x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (3): regex_effbot, xml_etree_iterparse, coroutines
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.078x slower

# HPT report

- Reliability score: 98.26% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.71x