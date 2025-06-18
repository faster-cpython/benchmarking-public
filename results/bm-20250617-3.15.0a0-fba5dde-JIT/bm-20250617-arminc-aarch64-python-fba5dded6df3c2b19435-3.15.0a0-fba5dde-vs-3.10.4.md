# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.055x faster
- HPT reliability: 98.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 369 ms: 1.03x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.63 sec: 1.03x slower                                                  |
| html5lib       | 86.5 ms                                                               | 68.6 ms: 1.26x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.02 sec: 2.25x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 531 ms: 2.13x faster                                                    |
| async_tree_none         | 950 ms                                                                | 446 ms: 2.13x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 818 ms: 1.56x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 94.8 ms: 1.42x faster                                                   |
| nbody          | 166 ms                                                                | 132 ms: 1.25x faster                                                    |
| pidigits       | 235 ms                                                                | 282 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 154 ms: 1.15x faster                                                    |
| regex_dna      | 257 ms                                                                | 229 ms: 1.12x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.09 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.72 sec: 1.24x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 308 us: 1.19x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 474 us: 1.12x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.72 us: 1.04x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 16.8 ms: 1.01x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 103 ms: 1.03x slower                                                    |
| xml_etree_parse      | 212 ms                                                                | 229 ms: 1.08x slower                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 173 ms: 1.11x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 42.3 us: 1.20x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 150 ms: 1.22x slower                                                    |
| json_loads           | 30.9 us                                                               | 37.8 us: 1.22x slower                                                   |
| unpickle             | 17.5 us                                                               | 22.5 us: 1.29x slower                                                   |
| pickle_list          | 5.24 us                                                               | 7.18 us: 1.37x slower                                                   |
| pickle               | 12.5 us                                                               | 20.1 us: 1.61x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.74 ms: 1.41x slower                                                   |
| python_startup         | 11.2 ms                                                               | 17.1 ms: 1.53x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 17.0 ms: 1.12x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 33.0 ms: 1.07x faster                                                   |
| django_template | 53.3 ms                                                               | 53.1 ms: 1.00x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 76.5 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 275 us: 2.41x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.02 sec: 2.25x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 531 ms: 2.13x faster                                                    |
| async_tree_none          | 950 ms                                                                | 446 ms: 2.13x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.37 ms: 2.05x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.99 sec: 1.86x faster                                                  |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                                   |
| richards_super           | 107 ms                                                                | 62.3 ms: 1.72x faster                                                   |
| generators               | 68.1 ms                                                               | 39.7 ms: 1.71x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 575 ms: 1.64x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 818 ms: 1.56x faster                                                    |
| go                       | 264 ms                                                                | 172 ms: 1.54x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.45x faster                                                  |
| raytrace                 | 573 ms                                                                | 400 ms: 1.43x faster                                                    |
| scimark_sor              | 246 ms                                                                | 172 ms: 1.43x faster                                                    |
| chaos                    | 121 ms                                                                | 84.9 ms: 1.43x faster                                                   |
| float                    | 135 ms                                                                | 94.8 ms: 1.42x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 43.7 us: 1.41x faster                                                   |
| pyflate                  | 795 ms                                                                | 584 ms: 1.36x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.7 us: 1.34x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 95.8 ms: 1.33x faster                                                   |
| pylint                   | 485 ms                                                                | 376 ms: 1.29x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 68.6 ms: 1.26x faster                                                   |
| nbody                    | 166 ms                                                                | 132 ms: 1.25x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.71 ms: 1.25x faster                                                   |
| deepcopy                 | 511 us                                                                | 408 us: 1.25x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 107 ms: 1.25x faster                                                    |
| spectral_norm            | 186 ms                                                                | 151 ms: 1.24x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.72 sec: 1.24x faster                                                  |
| scimark_lu               | 227 ms                                                                | 189 ms: 1.20x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 308 us: 1.19x faster                                                    |
| regex_compile            | 177 ms                                                                | 154 ms: 1.15x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 64.2 ms: 1.14x faster                                                   |
| regex_dna                | 257 ms                                                                | 229 ms: 1.12x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 474 us: 1.12x faster                                                    |
| mako                     | 18.9 ms                                                               | 17.0 ms: 1.12x faster                                                   |
| coroutines               | 37.2 ms                                                               | 33.8 ms: 1.10x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 24.3 ms: 1.09x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 33.0 ms: 1.07x faster                                                   |
| scimark_fft              | 500 ms                                                                | 470 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                   |
| logging_simple           | 9.78 us                                                               | 9.27 us: 1.06x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.51 ms: 1.05x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.72 us: 1.04x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.09 ms: 1.04x faster                                                   |
| logging_format           | 10.6 us                                                               | 10.2 us: 1.04x faster                                                   |
| 2to3                     | 381 ms                                                                | 369 ms: 1.03x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.65 sec: 1.03x faster                                                  |
| thrift                   | 1.26 ms                                                               | 1.25 ms: 1.01x faster                                                   |
| django_template          | 53.3 ms                                                               | 53.1 ms: 1.00x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 16.8 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.71 ms: 1.01x slower                                                   |
| pathlib                  | 26.3 ms                                                               | 26.7 ms: 1.01x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.63 sec: 1.03x slower                                                  |
| xml_etree_process        | 99.5 ms                                                               | 103 ms: 1.03x slower                                                    |
| fannkuch                 | 546 ms                                                                | 564 ms: 1.03x slower                                                    |
| sympy_str                | 329 ms                                                                | 345 ms: 1.05x slower                                                    |
| xml_etree_parse          | 212 ms                                                                | 229 ms: 1.08x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 76.5 ms: 1.09x slower                                                   |
| nqueens                  | 117 ms                                                                | 130 ms: 1.11x slower                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 173 ms: 1.11x slower                                                    |
| sympy_expand             | 543 ms                                                                | 624 ms: 1.15x slower                                                    |
| sqlite_synth             | 4.12 us                                                               | 4.76 us: 1.16x slower                                                   |
| json                     | 5.88 ms                                                               | 6.95 ms: 1.18x slower                                                   |
| async_generators         | 452 ms                                                                | 540 ms: 1.19x slower                                                    |
| pidigits                 | 235 ms                                                                | 282 ms: 1.20x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 42.3 us: 1.20x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 150 ms: 1.22x slower                                                    |
| json_loads               | 30.9 us                                                               | 37.8 us: 1.22x slower                                                   |
| unpickle                 | 17.5 us                                                               | 22.5 us: 1.29x slower                                                   |
| pickle_list              | 5.24 us                                                               | 7.18 us: 1.37x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 3.24 sec: 1.37x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.58 sec: 1.38x slower                                                  |
| python_startup_no_site   | 6.89 ms                                                               | 9.74 ms: 1.41x slower                                                   |
| python_startup           | 11.2 ms                                                               | 17.1 ms: 1.53x slower                                                   |
| telco                    | 8.49 ms                                                               | 13.6 ms: 1.60x slower                                                   |
| pickle                   | 12.5 us                                                               | 20.1 us: 1.61x slower                                                   |
| coverage                 | 83.6 ms                                                               | 135 ms: 1.61x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.83 ms: 1.70x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.22 ms: 1.74x slower                                                   |
| logging_silent           | 222 ns                                                                | 912 ns: 4.11x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 3.00 sec: 206.31x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (3): sympy_sum, deepcopy_reduce, meteor_contest
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 98.52% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.41x