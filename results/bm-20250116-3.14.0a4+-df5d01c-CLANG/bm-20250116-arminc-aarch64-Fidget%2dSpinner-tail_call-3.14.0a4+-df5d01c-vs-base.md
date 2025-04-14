# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-aarch64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 325 ms                                                                   | 298 ms: 1.09x faster                                                    |
| docutils       | 3.13 sec                                                                 | 3.00 sec: 1.04x faster                                                  |
| html5lib       | 65.5 ms                                                                  | 60.3 ms: 1.09x faster                                                   |
| sphinx         | 1.20 sec                                                                 | 1.14 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                                    | 1.07x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators           | 462 ms                                                                   | 419 ms: 1.10x faster                                                    |
| coroutines                 | 30.7 ms                                                                  | 28.2 ms: 1.09x faster                                                   |
| async_tree_none_tg         | 396 ms                                                                   | 368 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 927 ms                                                                   | 867 ms: 1.07x faster                                                    |
| async_tree_io              | 931 ms                                                                   | 876 ms: 1.06x faster                                                    |
| async_tree_memoization_tg  | 486 ms                                                                   | 460 ms: 1.06x faster                                                    |
| async_tree_none            | 409 ms                                                                   | 388 ms: 1.05x faster                                                    |
| async_tree_memoization     | 513 ms                                                                   | 487 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 765 ms                                                                   | 735 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 135 ms                                                                   | 108 ms: 1.24x faster                                                    |
| float          | 93.7 ms                                                                  | 83.8 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                   | 125 ms: 1.14x faster                                                    |
| regex_dna      | 243 ms                                                                   | 266 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                                   | 254 us: 1.23x faster                                                    |
| tomli_loads          | 2.90 sec                                                                 | 2.46 sec: 1.18x faster                                                  |
| pickle_pure_python   | 449 us                                                                   | 388 us: 1.16x faster                                                    |
| xml_etree_process    | 84.3 ms                                                                  | 77.2 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 160 ms                                                                   | 152 ms: 1.05x faster                                                    |
| Geometric mean       | (ref)                                                                    | 1.10x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, json_dumps, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 31.0 ms                                                                  | 26.8 ms: 1.16x faster                                                   |
| genshi_xml      | 70.0 ms                                                                  | 60.5 ms: 1.16x faster                                                   |
| mako            | 15.5 ms                                                                  | 14.1 ms: 1.10x faster                                                   |
| django_template | 45.3 ms                                                                  | 41.4 ms: 1.09x faster                                                   |
| Geometric mean  | (ref)                                                                    | 1.13x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| richards                   | 61.3 ms                                                                  | 47.9 ms: 1.28x faster                                                   |
| scimark_sor                | 179 ms                                                                   | 141 ms: 1.27x faster                                                    |
| go                         | 165 ms                                                                   | 132 ms: 1.25x faster                                                    |
| nbody                      | 135 ms                                                                   | 108 ms: 1.24x faster                                                    |
| deepcopy_memo              | 45.5 us                                                                  | 36.7 us: 1.24x faster                                                   |
| logging_silent             | 144 ns                                                                   | 117 ns: 1.23x faster                                                    |
| unpickle_pure_python       | 312 us                                                                   | 254 us: 1.23x faster                                                    |
| hexiom                     | 8.58 ms                                                                  | 7.08 ms: 1.21x faster                                                   |
| scimark_monte_carlo        | 91.0 ms                                                                  | 75.3 ms: 1.21x faster                                                   |
| deltablue                  | 4.53 ms                                                                  | 3.76 ms: 1.20x faster                                                   |
| fannkuch                   | 578 ms                                                                   | 487 ms: 1.19x faster                                                    |
| richards_super             | 66.9 ms                                                                  | 56.7 ms: 1.18x faster                                                   |
| tomli_loads                | 2.90 sec                                                                 | 2.46 sec: 1.18x faster                                                  |
| generators                 | 43.1 ms                                                                  | 36.6 ms: 1.18x faster                                                   |
| sqlglot_parse              | 1.61 ms                                                                  | 1.37 ms: 1.17x faster                                                   |
| genshi_text                | 31.0 ms                                                                  | 26.8 ms: 1.16x faster                                                   |
| pickle_pure_python         | 449 us                                                                   | 388 us: 1.16x faster                                                    |
| genshi_xml                 | 70.0 ms                                                                  | 60.5 ms: 1.16x faster                                                   |
| chaos                      | 77.4 ms                                                                  | 67.5 ms: 1.15x faster                                                   |
| regex_compile              | 142 ms                                                                   | 125 ms: 1.14x faster                                                    |
| comprehensions             | 23.0 us                                                                  | 20.2 us: 1.14x faster                                                   |
| pprint_safe_repr           | 1.11 sec                                                                 | 970 ms: 1.14x faster                                                    |
| pprint_pformat             | 2.25 sec                                                                 | 1.98 sec: 1.14x faster                                                  |
| scimark_lu                 | 154 ms                                                                   | 136 ms: 1.13x faster                                                    |
| spectral_norm              | 131 ms                                                                   | 116 ms: 1.13x faster                                                    |
| sympy_str                  | 294 ms                                                                   | 261 ms: 1.13x faster                                                    |
| logging_simple             | 7.72 us                                                                  | 6.86 us: 1.13x faster                                                   |
| telco                      | 10.3 ms                                                                  | 9.16 ms: 1.12x faster                                                   |
| pyflate                    | 596 ms                                                                   | 531 ms: 1.12x faster                                                    |
| sqlglot_transpile          | 2.01 ms                                                                  | 1.79 ms: 1.12x faster                                                   |
| float                      | 93.7 ms                                                                  | 83.8 ms: 1.12x faster                                                   |
| sqlalchemy_imperative      | 17.3 ms                                                                  | 15.5 ms: 1.12x faster                                                   |
| deepcopy_reduce            | 3.86 us                                                                  | 3.49 us: 1.11x faster                                                   |
| sqlglot_optimize           | 69.6 ms                                                                  | 62.9 ms: 1.11x faster                                                   |
| sqlglot_normalize          | 145 ms                                                                   | 132 ms: 1.10x faster                                                    |
| async_generators           | 462 ms                                                                   | 419 ms: 1.10x faster                                                    |
| mako                       | 15.5 ms                                                                  | 14.1 ms: 1.10x faster                                                   |
| deepcopy                   | 369 us                                                                   | 335 us: 1.10x faster                                                    |
| django_template            | 45.3 ms                                                                  | 41.4 ms: 1.09x faster                                                   |
| pylint                     | 331 ms                                                                   | 303 ms: 1.09x faster                                                    |
| raytrace                   | 341 ms                                                                   | 312 ms: 1.09x faster                                                    |
| xml_etree_process          | 84.3 ms                                                                  | 77.2 ms: 1.09x faster                                                   |
| 2to3                       | 325 ms                                                                   | 298 ms: 1.09x faster                                                    |
| coroutines                 | 30.7 ms                                                                  | 28.2 ms: 1.09x faster                                                   |
| html5lib                   | 65.5 ms                                                                  | 60.3 ms: 1.09x faster                                                   |
| subparsers                 | 28.9 ms                                                                  | 26.7 ms: 1.08x faster                                                   |
| sympy_expand               | 515 ms                                                                   | 476 ms: 1.08x faster                                                    |
| nqueens                    | 109 ms                                                                   | 101 ms: 1.08x faster                                                    |
| bpe_tokeniser              | 6.00 sec                                                                 | 5.55 sec: 1.08x faster                                                  |
| crypto_pyaes               | 91.7 ms                                                                  | 85.0 ms: 1.08x faster                                                   |
| typing_runtime_protocols   | 209 us                                                                   | 194 us: 1.08x faster                                                    |
| async_tree_none_tg         | 396 ms                                                                   | 368 ms: 1.08x faster                                                    |
| many_optionals             | 776 us                                                                   | 725 us: 1.07x faster                                                    |
| async_tree_io_tg           | 927 ms                                                                   | 867 ms: 1.07x faster                                                    |
| pycparser                  | 1.35 sec                                                                 | 1.27 sec: 1.07x faster                                                  |
| connected_components       | 568 ms                                                                   | 532 ms: 1.07x faster                                                    |
| scimark_sparse_mat_mult    | 6.04 ms                                                                  | 5.67 ms: 1.07x faster                                                   |
| logging_format             | 8.25 us                                                                  | 7.75 us: 1.06x faster                                                   |
| async_tree_io              | 931 ms                                                                   | 876 ms: 1.06x faster                                                    |
| sympy_sum                  | 153 ms                                                                   | 144 ms: 1.06x faster                                                    |
| async_tree_memoization_tg  | 486 ms                                                                   | 460 ms: 1.06x faster                                                    |
| xml_etree_iterparse        | 160 ms                                                                   | 152 ms: 1.05x faster                                                    |
| async_tree_none            | 409 ms                                                                   | 388 ms: 1.05x faster                                                    |
| sympy_integrate            | 22.0 ms                                                                  | 20.9 ms: 1.05x faster                                                   |
| async_tree_memoization     | 513 ms                                                                   | 487 ms: 1.05x faster                                                    |
| dulwich_log                | 61.7 ms                                                                  | 58.7 ms: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                                 | 1.14 sec: 1.05x faster                                                  |
| docutils                   | 3.13 sec                                                                 | 3.00 sec: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 765 ms                                                                   | 735 ms: 1.04x faster                                                    |
| shortest_path              | 585 ms                                                                   | 570 ms: 1.03x faster                                                    |
| k_core                     | 2.87 sec                                                                 | 2.81 sec: 1.02x faster                                                  |
| regex_dna                  | 243 ms                                                                   | 266 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (24): xml_etree_generate, json_dumps, scimark_fft, meteor_contest, thrift, pathlib, xml_etree_parse, async_tree_cpu_io_mixed, json_loads, sqlalchemy_declarative, json, sqlite_synth, python_startup_no_site, python_startup, coverage, gc_traversal, bench_thread_pool, asyncio_websockets, mdp, regex_v8, create_gc_cycles, pidigits, regex_effbot, bench_mp_pool

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.00x