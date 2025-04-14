# Results vs. base

- fork: brandtbucher
- ref: jit_guard_float_int_
- machine: linux-x86_64
- commit hash: 602f0e9
- commit date: 2025-03-27
- overall geometric mean: 1.005x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 261 ms: 1.01x faster                                                         |
| docutils       | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 480 ms                                                                 | 473 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 487 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_none, async_tree_io, asyncio_websockets, async_generators, coroutines, async_tree_io_tg, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 63.8 ms                                                                | 63.4 ms: 1.01x faster                                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.23 ms: 1.09x faster                                                        |
| regex_dna      | 228 ms                                                                 | 219 ms: 1.04x faster                                                         |
| regex_v8       | 24.0 ms                                                                | 23.0 ms: 1.04x faster                                                        |
| regex_compile  | 128 ms                                                                 | 126 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads           | 29.9 us                                                                | 29.7 us: 1.01x faster                                                        |
| xml_etree_generate   | 79.3 ms                                                                | 79.0 ms: 1.00x faster                                                        |
| pickle_pure_python   | 321 us                                                                 | 325 us: 1.01x slower                                                         |
| unpickle_pure_python | 210 us                                                                 | 218 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (5): xml_etree_process, json_dumps, tomli_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.19 ms: 1.00x faster                                                        |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot               | 3.51 ms                                                                | 3.23 ms: 1.09x faster                                                        |
| gc_traversal               | 5.05 ms                                                                | 4.76 ms: 1.06x faster                                                        |
| pycparser                  | 1.19 sec                                                               | 1.13 sec: 1.05x faster                                                       |
| regex_dna                  | 228 ms                                                                 | 219 ms: 1.04x faster                                                         |
| regex_v8                   | 24.0 ms                                                                | 23.0 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.66 ms                                                                | 4.48 ms: 1.04x faster                                                        |
| logging_silent             | 99.4 ns                                                                | 96.2 ns: 1.03x faster                                                        |
| typing_runtime_protocols   | 169 us                                                                 | 166 us: 1.02x faster                                                         |
| coverage                   | 85.1 ms                                                                | 83.7 ms: 1.02x faster                                                        |
| pathlib                    | 16.8 ms                                                                | 16.5 ms: 1.02x faster                                                        |
| scimark_sor                | 121 ms                                                                 | 119 ms: 1.02x faster                                                         |
| generators                 | 28.6 ms                                                                | 28.1 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 480 ms                                                                 | 473 ms: 1.01x faster                                                         |
| regex_compile              | 128 ms                                                                 | 126 ms: 1.01x faster                                                         |
| mdp                        | 1.25 sec                                                               | 1.23 sec: 1.01x faster                                                       |
| connected_components       | 456 ms                                                                 | 450 ms: 1.01x faster                                                         |
| subparsers                 | 21.0 ms                                                                | 20.7 ms: 1.01x faster                                                        |
| chaos                      | 59.1 ms                                                                | 58.4 ms: 1.01x faster                                                        |
| scimark_fft                | 314 ms                                                                 | 310 ms: 1.01x faster                                                         |
| shortest_path              | 492 ms                                                                 | 487 ms: 1.01x faster                                                         |
| bench_mp_pool              | 83.8 ms                                                                | 83.0 ms: 1.01x faster                                                        |
| docutils                   | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                       |
| create_gc_cycles           | 2.49 ms                                                                | 2.47 ms: 1.01x faster                                                        |
| logging_format             | 6.16 us                                                                | 6.11 us: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                                 | 107 ms: 1.01x faster                                                         |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.28 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 487 ms: 1.01x faster                                                         |
| float                      | 63.8 ms                                                                | 63.4 ms: 1.01x faster                                                        |
| 2to3                       | 263 ms                                                                 | 261 ms: 1.01x faster                                                         |
| json_loads                 | 29.9 us                                                                | 29.7 us: 1.01x faster                                                        |
| sympy_expand               | 474 ms                                                                 | 472 ms: 1.01x faster                                                         |
| bpe_tokeniser              | 4.54 sec                                                               | 4.52 sec: 1.01x faster                                                       |
| sqlalchemy_imperative      | 17.2 ms                                                                | 17.1 ms: 1.01x faster                                                        |
| dulwich_log                | 60.6 ms                                                                | 60.2 ms: 1.01x faster                                                        |
| sympy_integrate            | 19.9 ms                                                                | 19.8 ms: 1.00x faster                                                        |
| python_startup_no_site     | 8.22 ms                                                                | 8.19 ms: 1.00x faster                                                        |
| raytrace                   | 267 ms                                                                 | 266 ms: 1.00x faster                                                         |
| sympy_str                  | 274 ms                                                                 | 273 ms: 1.00x faster                                                         |
| bench_thread_pool          | 884 us                                                                 | 880 us: 1.00x faster                                                         |
| sqlglot_v2_normalize       | 108 ms                                                                 | 108 ms: 1.00x faster                                                         |
| xml_etree_generate         | 79.3 ms                                                                | 79.0 ms: 1.00x faster                                                        |
| sqlalchemy_declarative     | 132 ms                                                                 | 131 ms: 1.00x faster                                                         |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| sqlglot_v2_transpile       | 1.60 ms                                                                | 1.61 ms: 1.01x slower                                                        |
| crypto_pyaes               | 75.3 ms                                                                | 75.9 ms: 1.01x slower                                                        |
| json                       | 5.29 ms                                                                | 5.34 ms: 1.01x slower                                                        |
| comprehensions             | 18.5 us                                                                | 18.7 us: 1.01x slower                                                        |
| scimark_monte_carlo        | 66.9 ms                                                                | 67.5 ms: 1.01x slower                                                        |
| logging_simple             | 5.49 us                                                                | 5.55 us: 1.01x slower                                                        |
| deepcopy                   | 257 us                                                                 | 260 us: 1.01x slower                                                         |
| pickle_pure_python         | 321 us                                                                 | 325 us: 1.01x slower                                                         |
| deltablue                  | 3.03 ms                                                                | 3.07 ms: 1.01x slower                                                        |
| scimark_lu                 | 115 ms                                                                 | 117 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.57 sec                                                               | 1.60 sec: 1.02x slower                                                       |
| pyflate                    | 433 ms                                                                 | 441 ms: 1.02x slower                                                         |
| telco                      | 7.87 ms                                                                | 8.02 ms: 1.02x slower                                                        |
| spectral_norm              | 92.3 ms                                                                | 94.6 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                                 | 218 us: 1.04x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (36): pylint, sphinx, k_core, deepcopy_reduce, async_tree_memoization_tg, xml_etree_process, go, html5lib, sqlite_synth, json_dumps, genshi_text, many_optionals, richards, tomli_loads, async_tree_none, sympy_sum, hexiom, async_tree_io, genshi_xml, django_template, asyncio_websockets, async_generators, sqlglot_v2_optimize, coroutines, mako, async_tree_io_tg, async_tree_memoization, richards_super, fannkuch, xml_etree_parse, nqueens, async_tree_none_tg, xml_etree_iterparse, pprint_safe_repr, deepcopy_memo, nbody

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x