# Results vs. base

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 2d69c9f
- commit date: 2025-03-25
- overall geometric mean: 1.005x faster
- HPT reliability: 99.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                       |
| html5lib       | 61.5 ms                                                                | 62.5 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines             | 24.1 ms                                                                | 23.3 ms: 1.03x faster                                        |
| async_tree_memoization | 316 ms                                                                 | 318 ms: 1.01x slower                                         |
| async_generators       | 391 ms                                                                 | 396 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_io, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 99.0 ms                                                                | 96.4 ms: 1.03x faster                                        |
| float          | 70.6 ms                                                                | 69.9 ms: 1.01x faster                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.47 ms                                                                | 3.19 ms: 1.09x faster                                        |
| regex_v8       | 23.7 ms                                                                | 22.9 ms: 1.04x faster                                        |
| regex_dna      | 223 ms                                                                 | 217 ms: 1.03x faster                                         |
| regex_compile  | 127 ms                                                                 | 126 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                        |
| unpickle_pure_python | 222 us                                                                 | 220 us: 1.01x faster                                         |
| xml_etree_process    | 58.9 ms                                                                | 58.4 ms: 1.01x faster                                        |
| xml_etree_generate   | 84.2 ms                                                                | 83.6 ms: 1.01x faster                                        |
| json_loads           | 29.9 us                                                                | 29.8 us: 1.00x faster                                        |
| tomli_loads          | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                       |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.19 ms                                                                | 8.17 ms: 1.00x faster                                        |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako           | 11.4 ms                                                                | 11.1 ms: 1.03x faster                                        |
| genshi_text    | 21.5 ms                                                                | 21.4 ms: 1.01x faster                                        |
| genshi_xml     | 49.1 ms                                                                | 49.3 ms: 1.00x slower                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot             | 3.47 ms                                                                | 3.19 ms: 1.09x faster                                        |
| pycparser                | 1.18 sec                                                               | 1.12 sec: 1.05x faster                                       |
| scimark_sparse_mat_mult  | 4.94 ms                                                                | 4.74 ms: 1.04x faster                                        |
| regex_v8                 | 23.7 ms                                                                | 22.9 ms: 1.04x faster                                        |
| coroutines               | 24.1 ms                                                                | 23.3 ms: 1.03x faster                                        |
| regex_dna                | 223 ms                                                                 | 217 ms: 1.03x faster                                         |
| nbody                    | 99.0 ms                                                                | 96.4 ms: 1.03x faster                                        |
| mako                     | 11.4 ms                                                                | 11.1 ms: 1.03x faster                                        |
| scimark_lu               | 118 ms                                                                 | 115 ms: 1.02x faster                                         |
| deltablue                | 3.15 ms                                                                | 3.09 ms: 1.02x faster                                        |
| json                     | 5.36 ms                                                                | 5.27 ms: 1.02x faster                                        |
| scimark_fft              | 351 ms                                                                 | 344 ms: 1.02x faster                                         |
| json_dumps               | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                        |
| pprint_safe_repr         | 734 ms                                                                 | 724 ms: 1.01x faster                                         |
| deepcopy_memo            | 29.4 us                                                                | 29.0 us: 1.01x faster                                        |
| sqlalchemy_imperative    | 16.6 ms                                                                | 16.4 ms: 1.01x faster                                        |
| raytrace                 | 268 ms                                                                 | 264 ms: 1.01x faster                                         |
| logging_silent           | 99.9 ns                                                                | 98.6 ns: 1.01x faster                                        |
| pprint_pformat           | 1.50 sec                                                               | 1.48 sec: 1.01x faster                                       |
| float                    | 70.6 ms                                                                | 69.9 ms: 1.01x faster                                        |
| unpickle_pure_python     | 222 us                                                                 | 220 us: 1.01x faster                                         |
| gc_traversal             | 5.07 ms                                                                | 5.02 ms: 1.01x faster                                        |
| xml_etree_process        | 58.9 ms                                                                | 58.4 ms: 1.01x faster                                        |
| xml_etree_generate       | 84.2 ms                                                                | 83.6 ms: 1.01x faster                                        |
| nqueens                  | 83.4 ms                                                                | 82.7 ms: 1.01x faster                                        |
| chaos                    | 59.7 ms                                                                | 59.3 ms: 1.01x faster                                        |
| scimark_sor              | 117 ms                                                                 | 116 ms: 1.01x faster                                         |
| richards_super           | 49.8 ms                                                                | 49.5 ms: 1.01x faster                                        |
| genshi_text              | 21.5 ms                                                                | 21.4 ms: 1.01x faster                                        |
| deepcopy                 | 258 us                                                                 | 257 us: 1.01x faster                                         |
| richards                 | 43.4 ms                                                                | 43.2 ms: 1.00x faster                                        |
| hexiom                   | 6.30 ms                                                                | 6.28 ms: 1.00x faster                                        |
| create_gc_cycles         | 2.48 ms                                                                | 2.47 ms: 1.00x faster                                        |
| json_loads               | 29.9 us                                                                | 29.8 us: 1.00x faster                                        |
| docutils                 | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                       |
| sqlglot_v2_optimize      | 53.1 ms                                                                | 52.9 ms: 1.00x faster                                        |
| regex_compile            | 127 ms                                                                 | 126 ms: 1.00x faster                                         |
| sqlalchemy_declarative   | 131 ms                                                                 | 130 ms: 1.00x faster                                         |
| python_startup_no_site   | 8.19 ms                                                                | 8.17 ms: 1.00x faster                                        |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x faster                                         |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                        |
| sympy_integrate          | 19.9 ms                                                                | 19.9 ms: 1.00x slower                                        |
| bench_thread_pool        | 868 us                                                                 | 872 us: 1.00x slower                                         |
| genshi_xml               | 49.1 ms                                                                | 49.3 ms: 1.00x slower                                        |
| comprehensions           | 16.7 us                                                                | 16.8 us: 1.01x slower                                        |
| tomli_loads              | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                       |
| dulwich_log              | 57.9 ms                                                                | 58.4 ms: 1.01x slower                                        |
| sympy_expand             | 451 ms                                                                 | 455 ms: 1.01x slower                                         |
| sympy_sum                | 147 ms                                                                 | 148 ms: 1.01x slower                                         |
| async_tree_memoization   | 316 ms                                                                 | 318 ms: 1.01x slower                                         |
| generators               | 28.5 ms                                                                | 28.7 ms: 1.01x slower                                        |
| logging_format           | 6.11 us                                                                | 6.16 us: 1.01x slower                                        |
| crypto_pyaes             | 75.4 ms                                                                | 76.1 ms: 1.01x slower                                        |
| typing_runtime_protocols | 162 us                                                                 | 164 us: 1.01x slower                                         |
| async_generators         | 391 ms                                                                 | 396 ms: 1.01x slower                                         |
| pathlib                  | 16.8 ms                                                                | 17.0 ms: 1.02x slower                                        |
| html5lib                 | 61.5 ms                                                                | 62.5 ms: 1.02x slower                                        |
| pyflate                  | 439 ms                                                                 | 450 ms: 1.03x slower                                         |
| fannkuch                 | 417 ms                                                                 | 431 ms: 1.03x slower                                         |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (37): k_core, xml_etree_parse, sphinx, async_tree_cpu_io_mixed_tg, telco, xml_etree_iterparse, sqlite_synth, coverage, scimark_monte_carlo, sqlglot_v2_normalize, meteor_contest, mdp, async_tree_memoization_tg, sqlglot_v2_transpile, sympy_str, go, 2to3, bpe_tokeniser, django_template, bench_mp_pool, shortest_path, sqlglot_v2_parse, pylint, deepcopy_reduce, subparsers, async_tree_cpu_io_mixed, async_tree_none_tg, many_optionals, logging_simple, asyncio_websockets, pickle_pure_python, thrift, async_tree_io, async_tree_none, connected_components, spectral_norm, async_tree_io_tg

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x