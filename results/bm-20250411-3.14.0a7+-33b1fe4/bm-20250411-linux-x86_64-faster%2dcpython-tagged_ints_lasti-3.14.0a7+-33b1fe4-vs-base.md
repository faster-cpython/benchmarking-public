# Results vs. base

- fork: faster-cpython
- ref: tagged_ints_lasti
- machine: linux-x86_64
- commit hash: 33b1fe4
- commit date: 2025-04-11
- overall geometric mean: 1.001x faster
- HPT reliability: 95.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250411-linux-x86_64-python-d87e7f35297d34755026-3.14.0a7+-d87e7f3 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 251 ms: 1.00x faster                                                          |
| docutils       | 2.60 sec                                                               | 2.60 sec: 1.00x slower                                                        |
| html5lib       | 59.4 ms                                                                | 62.0 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250411-linux-x86_64-python-d87e7f35297d34755026-3.14.0a7+-d87e7f3 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg      | 249 ms                                                                 | 247 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed | 482 ms                                                                 | 478 ms: 1.01x faster                                                          |
| async_generators        | 391 ms                                                                 | 393 ms: 1.01x slower                                                          |
| coroutines              | 24.0 ms                                                                | 24.6 ms: 1.02x slower                                                         |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (7): async_tree_io, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250411-linux-x86_64-python-d87e7f35297d34755026-3.14.0a7+-d87e7f3 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 97.1 ms                                                                | 94.6 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250411-linux-x86_64-python-d87e7f35297d34755026-3.14.0a7+-d87e7f3 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                 | 210 ms: 1.00x slower                                                          |
| regex_effbot   | 3.25 ms                                                                | 3.26 ms: 1.00x slower                                                         |
| regex_compile  | 124 ms                                                                 | 125 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250411-linux-x86_64-python-d87e7f35297d34755026-3.14.0a7+-d87e7f3 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_generate   | 85.6 ms                                                                | 84.6 ms: 1.01x faster                                                         |
| xml_etree_process    | 59.3 ms                                                                | 58.6 ms: 1.01x faster                                                         |
| tomli_loads          | 1.94 sec                                                               | 1.93 sec: 1.00x faster                                                        |
| unpickle_pure_python | 218 us                                                                 | 220 us: 1.01x slower                                                          |
| json_loads           | 29.4 us                                                                | 29.8 us: 1.01x slower                                                         |
| json_dumps           | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250411-linux-x86_64-python-d87e7f35297d34755026-3.14.0a7+-d87e7f3 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.21 ms                                                                | 8.19 ms: 1.00x faster                                                         |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250411-linux-x86_64-python-d87e7f35297d34755026-3.14.0a7+-d87e7f3 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 48.9 ms                                                                | 48.5 ms: 1.01x faster                                                         |
| django_template | 31.4 ms                                                                | 32.1 ms: 1.02x slower                                                         |
| mako            | 11.0 ms                                                                | 11.4 ms: 1.03x slower                                                         |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250411-linux-x86_64-python-d87e7f35297d34755026-3.14.0a7+-d87e7f3 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| spectral_norm           | 107 ms                                                                 | 102 ms: 1.05x faster                                                          |
| gc_traversal            | 5.00 ms                                                                | 4.78 ms: 1.05x faster                                                         |
| nbody                   | 97.1 ms                                                                | 94.6 ms: 1.03x faster                                                         |
| scimark_fft             | 357 ms                                                                 | 348 ms: 1.03x faster                                                          |
| chaos                   | 56.9 ms                                                                | 55.7 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult | 4.95 ms                                                                | 4.85 ms: 1.02x faster                                                         |
| pyflate                 | 455 ms                                                                 | 448 ms: 1.01x faster                                                          |
| crypto_pyaes            | 74.2 ms                                                                | 73.2 ms: 1.01x faster                                                         |
| mdp                     | 1.22 sec                                                               | 1.21 sec: 1.01x faster                                                        |
| xml_etree_generate      | 85.6 ms                                                                | 84.6 ms: 1.01x faster                                                         |
| sympy_expand            | 453 ms                                                                 | 448 ms: 1.01x faster                                                          |
| nqueens                 | 81.1 ms                                                                | 80.2 ms: 1.01x faster                                                         |
| logging_silent          | 96.0 ns                                                                | 94.9 ns: 1.01x faster                                                         |
| xml_etree_process       | 59.3 ms                                                                | 58.6 ms: 1.01x faster                                                         |
| async_tree_none_tg      | 249 ms                                                                 | 247 ms: 1.01x faster                                                          |
| dulwich_log             | 60.0 ms                                                                | 59.4 ms: 1.01x faster                                                         |
| genshi_xml              | 48.9 ms                                                                | 48.5 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed | 482 ms                                                                 | 478 ms: 1.01x faster                                                          |
| bpe_tokeniser           | 4.61 sec                                                               | 4.57 sec: 1.01x faster                                                        |
| sympy_integrate         | 19.0 ms                                                                | 18.9 ms: 1.01x faster                                                         |
| comprehensions          | 16.7 us                                                                | 16.6 us: 1.01x faster                                                         |
| deepcopy_reduce         | 2.69 us                                                                | 2.67 us: 1.01x faster                                                         |
| pprint_safe_repr        | 722 ms                                                                 | 717 ms: 1.01x faster                                                          |
| deepcopy                | 252 us                                                                 | 250 us: 1.01x faster                                                          |
| sympy_str               | 266 ms                                                                 | 265 ms: 1.01x faster                                                          |
| sympy_sum               | 148 ms                                                                 | 147 ms: 1.00x faster                                                          |
| tomli_loads             | 1.94 sec                                                               | 1.93 sec: 1.00x faster                                                        |
| sqlglot_v2_optimize     | 52.3 ms                                                                | 52.1 ms: 1.00x faster                                                         |
| python_startup_no_site  | 8.21 ms                                                                | 8.19 ms: 1.00x faster                                                         |
| pprint_pformat          | 1.46 sec                                                               | 1.46 sec: 1.00x faster                                                        |
| fannkuch                | 414 ms                                                                 | 413 ms: 1.00x faster                                                          |
| python_startup          | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                                         |
| create_gc_cycles        | 2.45 ms                                                                | 2.45 ms: 1.00x faster                                                         |
| 2to3                    | 251 ms                                                                 | 251 ms: 1.00x faster                                                          |
| regex_dna               | 210 ms                                                                 | 210 ms: 1.00x slower                                                          |
| bench_thread_pool       | 885 us                                                                 | 887 us: 1.00x slower                                                          |
| richards                | 43.1 ms                                                                | 43.2 ms: 1.00x slower                                                         |
| hexiom                  | 6.25 ms                                                                | 6.27 ms: 1.00x slower                                                         |
| docutils                | 2.60 sec                                                               | 2.60 sec: 1.00x slower                                                        |
| sqlglot_v2_normalize    | 105 ms                                                                 | 105 ms: 1.00x slower                                                          |
| raytrace                | 264 ms                                                                 | 265 ms: 1.00x slower                                                          |
| regex_effbot            | 3.25 ms                                                                | 3.26 ms: 1.00x slower                                                         |
| deepcopy_memo           | 28.3 us                                                                | 28.5 us: 1.01x slower                                                         |
| async_generators        | 391 ms                                                                 | 393 ms: 1.01x slower                                                          |
| regex_compile           | 124 ms                                                                 | 125 ms: 1.01x slower                                                          |
| many_optionals          | 932 us                                                                 | 938 us: 1.01x slower                                                          |
| meteor_contest          | 105 ms                                                                 | 106 ms: 1.01x slower                                                          |
| scimark_lu              | 118 ms                                                                 | 119 ms: 1.01x slower                                                          |
| unpickle_pure_python    | 218 us                                                                 | 220 us: 1.01x slower                                                          |
| json_loads              | 29.4 us                                                                | 29.8 us: 1.01x slower                                                         |
| json_dumps              | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                                         |
| pathlib                 | 16.8 ms                                                                | 17.2 ms: 1.02x slower                                                         |
| django_template         | 31.4 ms                                                                | 32.1 ms: 1.02x slower                                                         |
| coroutines              | 24.0 ms                                                                | 24.6 ms: 1.02x slower                                                         |
| shortest_path           | 489 ms                                                                 | 502 ms: 1.03x slower                                                          |
| connected_components    | 446 ms                                                                 | 459 ms: 1.03x slower                                                          |
| mako                    | 11.0 ms                                                                | 11.4 ms: 1.03x slower                                                         |
| html5lib                | 59.4 ms                                                                | 62.0 ms: 1.04x slower                                                         |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (37): async_tree_io, generators, async_tree_memoization_tg, logging_simple, async_tree_none, bench_mp_pool, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, float, logging_format, async_tree_memoization, pylint, xml_etree_parse, xml_etree_iterparse, sqlite_synth, go, scimark_sor, subparsers, pidigits, scimark_monte_carlo, sqlglot_v2_transpile, pycparser, deltablue, asyncio_websockets, regex_v8, sqlglot_v2_parse, genshi_text, sqlalchemy_declarative, pickle_pure_python, sqlalchemy_imperative, json, async_tree_io_tg, richards_super, coverage, sphinx, telco, k_core

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 95.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x