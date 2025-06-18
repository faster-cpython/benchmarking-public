# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.076x slower
- HPT reliability: 98.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.71x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 446 ms: 1.17x slower                                                    |
| docutils       | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                  |
| html5lib       | 86.5 ms                                                               | 84.1 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.03 sec: 2.23x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 557 ms: 2.03x faster                                                    |
| async_tree_none         | 950 ms                                                                | 469 ms: 2.02x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 859 ms: 1.48x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.92x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 106 ms: 1.28x faster                                                    |
| nbody          | 166 ms                                                                | 191 ms: 1.15x slower                                                    |
| pidigits       | 235 ms                                                                | 282 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 235 ms: 1.09x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| regex_compile  | 177 ms                                                                | 201 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 159 ms: 1.02x slower                                                    |
| tomli_loads          | 3.36 sec                                                              | 3.61 sec: 1.07x slower                                                  |
| unpickle_list        | 6.99 us                                                               | 7.58 us: 1.08x slower                                                   |
| pickle_pure_python   | 529 us                                                                | 593 us: 1.12x slower                                                    |
| xml_etree_parse      | 212 ms                                                                | 239 ms: 1.13x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 418 us: 1.14x slower                                                    |
| json_dumps           | 16.7 ms                                                               | 19.7 ms: 1.18x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 43.4 us: 1.24x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 128 ms: 1.29x slower                                                    |
| pickle_list          | 5.24 us                                                               | 7.08 us: 1.35x slower                                                   |
| json_loads           | 30.9 us                                                               | 44.6 us: 1.44x slower                                                   |
| unpickle             | 17.5 us                                                               | 26.4 us: 1.51x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 189 ms: 1.53x slower                                                    |
| pickle               | 12.5 us                                                               | 20.0 us: 1.60x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.25x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 13.8 ms: 2.00x slower                                                   |
| python_startup         | 11.2 ms                                                               | 23.3 ms: 2.08x slower                                                   |
| Geometric mean         | (ref)                                                                 | 2.04x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 23.8 ms: 1.26x slower                                                   |
| genshi_text     | 35.2 ms                                                               | 46.5 ms: 1.32x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 98.2 ms: 1.41x slower                                                   |
| django_template | 53.3 ms                                                               | 75.2 ms: 1.41x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.35x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 1.03 sec: 2.23x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 557 ms: 2.03x faster                                                    |
| async_tree_none          | 950 ms                                                                | 469 ms: 2.02x faster                                                    |
| typing_runtime_protocols | 661 us                                                                | 358 us: 1.84x faster                                                    |
| deltablue                | 8.94 ms                                                               | 5.55 ms: 1.61x faster                                                   |
| go                       | 264 ms                                                                | 178 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 859 ms: 1.48x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 639 ms: 1.48x faster                                                    |
| mdp                      | 3.70 sec                                                              | 2.52 sec: 1.46x faster                                                  |
| generators               | 68.1 ms                                                               | 47.0 ms: 1.45x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.54 sec: 1.29x faster                                                  |
| float                    | 135 ms                                                                | 106 ms: 1.28x faster                                                    |
| scimark_sor              | 246 ms                                                                | 194 ms: 1.27x faster                                                    |
| chaos                    | 121 ms                                                                | 99.4 ms: 1.22x faster                                                   |
| pyflate                  | 795 ms                                                                | 664 ms: 1.20x faster                                                    |
| raytrace                 | 573 ms                                                                | 498 ms: 1.15x faster                                                    |
| gc_traversal             | 4.15 ms                                                               | 3.70 ms: 1.12x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.96 ms: 1.10x faster                                                   |
| regex_dna                | 257 ms                                                                | 235 ms: 1.09x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 56.7 us: 1.09x faster                                                   |
| richards                 | 91.7 ms                                                               | 84.8 ms: 1.08x faster                                                   |
| comprehensions           | 33.1 us                                                               | 30.8 us: 1.07x faster                                                   |
| pylint                   | 485 ms                                                                | 457 ms: 1.06x faster                                                    |
| richards_super           | 107 ms                                                                | 101 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 84.1 ms: 1.03x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 159 ms: 1.02x slower                                                    |
| pycparser                | 1.69 sec                                                              | 1.76 sec: 1.04x slower                                                  |
| deepcopy                 | 511 us                                                                | 534 us: 1.05x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.61 sec: 1.07x slower                                                  |
| sqlite_synth             | 4.12 us                                                               | 4.43 us: 1.08x slower                                                   |
| unpickle_list            | 6.99 us                                                               | 7.58 us: 1.08x slower                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 139 ms: 1.09x slower                                                    |
| crypto_pyaes             | 134 ms                                                                | 148 ms: 1.10x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 2.53 ms: 1.12x slower                                                   |
| pickle_pure_python       | 529 us                                                                | 593 us: 1.12x slower                                                    |
| xml_etree_parse          | 212 ms                                                                | 239 ms: 1.13x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 83.3 ms: 1.13x slower                                                   |
| regex_compile            | 177 ms                                                                | 201 ms: 1.14x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 418 us: 1.14x slower                                                    |
| pathlib                  | 26.3 ms                                                               | 30.2 ms: 1.15x slower                                                   |
| nbody                    | 166 ms                                                                | 191 ms: 1.15x slower                                                    |
| scimark_fft              | 500 ms                                                                | 580 ms: 1.16x slower                                                    |
| 2to3                     | 381 ms                                                                | 446 ms: 1.17x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 19.7 ms: 1.18x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 9.05 ms: 1.19x slower                                                   |
| pidigits                 | 235 ms                                                                | 282 ms: 1.20x slower                                                    |
| logging_simple           | 9.78 us                                                               | 11.8 us: 1.21x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 32.0 ms: 1.21x slower                                                   |
| logging_format           | 10.6 us                                                               | 13.1 us: 1.23x slower                                                   |
| meteor_contest           | 126 ms                                                                | 156 ms: 1.23x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.96 ms: 1.23x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 43.4 us: 1.24x slower                                                   |
| mako                     | 18.9 ms                                                               | 23.8 ms: 1.26x slower                                                   |
| fannkuch                 | 546 ms                                                                | 693 ms: 1.27x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 128 ms: 1.29x slower                                                    |
| sympy_sum                | 184 ms                                                                | 239 ms: 1.30x slower                                                    |
| nqueens                  | 117 ms                                                                | 153 ms: 1.31x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 46.5 ms: 1.32x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.69 ms: 1.34x slower                                                   |
| pickle_list              | 5.24 us                                                               | 7.08 us: 1.35x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 6.22 us: 1.35x slower                                                   |
| json                     | 5.88 ms                                                               | 7.96 ms: 1.35x slower                                                   |
| async_generators         | 452 ms                                                                | 613 ms: 1.36x slower                                                    |
| sympy_str                | 329 ms                                                                | 450 ms: 1.37x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 3.27 sec: 1.39x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.60 sec: 1.39x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 98.2 ms: 1.41x slower                                                   |
| django_template          | 53.3 ms                                                               | 75.2 ms: 1.41x slower                                                   |
| json_loads               | 30.9 us                                                               | 44.6 us: 1.44x slower                                                   |
| sympy_expand             | 543 ms                                                                | 807 ms: 1.49x slower                                                    |
| unpickle                 | 17.5 us                                                               | 26.4 us: 1.51x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 189 ms: 1.53x slower                                                    |
| pickle                   | 12.5 us                                                               | 20.0 us: 1.60x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 13.8 ms: 2.00x slower                                                   |
| python_startup           | 11.2 ms                                                               | 23.3 ms: 2.08x slower                                                   |
| telco                    | 8.49 ms                                                               | 17.8 ms: 2.10x slower                                                   |
| coverage                 | 83.6 ms                                                               | 177 ms: 2.12x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 72.7 ms: 5.00x slower                                                   |
| logging_silent           | 222 ns                                                                | 1.13 us: 5.11x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (4): regex_effbot, spectral_norm, scimark_lu, coroutines
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.076x slower

# HPT report

- Reliability score: 98.38% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.71x