# Results vs. base

- fork: brandtbucher
- ref: jit_guard_dict_tuple
- machine: linux-x86_64
- commit hash: 99d6288
- commit date: 2025-04-01
- overall geometric mean: 1.001x faster
- HPT reliability: 54.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                 | 258 ms: 1.00x slower                                                         |
| html5lib       | 61.9 ms                                                                | 61.0 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization | 313 ms                                                                 | 311 ms: 1.01x faster                                                         |
| coroutines             | 23.5 ms                                                                | 23.6 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, asyncio_websockets, async_generators, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 86.4 ms                                                                | 84.0 ms: 1.03x faster                                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                 | 205 ms: 1.08x faster                                                         |
| regex_effbot   | 3.35 ms                                                                | 3.15 ms: 1.06x faster                                                        |
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads         | 29.6 us                                                                | 29.7 us: 1.00x slower                                                        |
| pickle_pure_python | 317 us                                                                 | 320 us: 1.01x slower                                                         |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (7): xml_etree_process, xml_etree_iterparse, tomli_loads, xml_etree_generate, xml_etree_parse, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                                        |
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 32.6 ms                                                                | 31.8 ms: 1.03x faster                                                        |
| genshi_xml      | 49.9 ms                                                                | 49.3 ms: 1.01x faster                                                        |
| genshi_text     | 21.2 ms                                                                | 21.4 ms: 1.01x slower                                                        |
| mako            | 10.9 ms                                                                | 10.9 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna                | 221 ms                                                                 | 205 ms: 1.08x faster                                                         |
| regex_effbot             | 3.35 ms                                                                | 3.15 ms: 1.06x faster                                                        |
| pycparser                | 1.17 sec                                                               | 1.12 sec: 1.05x faster                                                       |
| nbody                    | 86.4 ms                                                                | 84.0 ms: 1.03x faster                                                        |
| django_template          | 32.6 ms                                                                | 31.8 ms: 1.03x faster                                                        |
| typing_runtime_protocols | 173 us                                                                 | 169 us: 1.03x faster                                                         |
| nqueens                  | 84.7 ms                                                                | 82.8 ms: 1.02x faster                                                        |
| telco                    | 8.02 ms                                                                | 7.86 ms: 1.02x faster                                                        |
| html5lib                 | 61.9 ms                                                                | 61.0 ms: 1.02x faster                                                        |
| genshi_xml               | 49.9 ms                                                                | 49.3 ms: 1.01x faster                                                        |
| spectral_norm            | 100 ms                                                                 | 99.1 ms: 1.01x faster                                                        |
| sqlite_synth             | 2.75 us                                                                | 2.72 us: 1.01x faster                                                        |
| sqlglot_v2_parse         | 1.25 ms                                                                | 1.24 ms: 1.01x faster                                                        |
| sqlglot_v2_transpile     | 1.58 ms                                                                | 1.56 ms: 1.01x faster                                                        |
| async_tree_memoization   | 313 ms                                                                 | 311 ms: 1.01x faster                                                         |
| crypto_pyaes             | 74.4 ms                                                                | 74.0 ms: 1.01x faster                                                        |
| sqlalchemy_declarative   | 133 ms                                                                 | 133 ms: 1.00x faster                                                         |
| create_gc_cycles         | 2.50 ms                                                                | 2.49 ms: 1.00x faster                                                        |
| bench_thread_pool        | 890 us                                                                 | 887 us: 1.00x faster                                                         |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| python_startup_no_site   | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                                        |
| json_loads               | 29.6 us                                                                | 29.7 us: 1.00x slower                                                        |
| sqlglot_v2_optimize      | 54.0 ms                                                                | 54.1 ms: 1.00x slower                                                        |
| python_startup           | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                                        |
| sympy_expand             | 469 ms                                                                 | 471 ms: 1.00x slower                                                         |
| 2to3                     | 257 ms                                                                 | 258 ms: 1.00x slower                                                         |
| mdp                      | 1.22 sec                                                               | 1.22 sec: 1.00x slower                                                       |
| pathlib                  | 16.6 ms                                                                | 16.6 ms: 1.00x slower                                                        |
| coroutines               | 23.5 ms                                                                | 23.6 ms: 1.00x slower                                                        |
| sympy_integrate          | 19.6 ms                                                                | 19.7 ms: 1.01x slower                                                        |
| comprehensions           | 18.2 us                                                                | 18.3 us: 1.01x slower                                                        |
| generators               | 29.5 ms                                                                | 29.7 ms: 1.01x slower                                                        |
| connected_components     | 451 ms                                                                 | 454 ms: 1.01x slower                                                         |
| dulwich_log              | 60.2 ms                                                                | 60.6 ms: 1.01x slower                                                        |
| raytrace                 | 259 ms                                                                 | 260 ms: 1.01x slower                                                         |
| genshi_text              | 21.2 ms                                                                | 21.4 ms: 1.01x slower                                                        |
| bench_mp_pool            | 82.7 ms                                                                | 83.4 ms: 1.01x slower                                                        |
| mako                     | 10.9 ms                                                                | 10.9 ms: 1.01x slower                                                        |
| pickle_pure_python       | 317 us                                                                 | 320 us: 1.01x slower                                                         |
| deepcopy                 | 252 us                                                                 | 254 us: 1.01x slower                                                         |
| coverage                 | 85.1 ms                                                                | 86.0 ms: 1.01x slower                                                        |
| regex_compile            | 126 ms                                                                 | 127 ms: 1.01x slower                                                         |
| go                       | 123 ms                                                                 | 125 ms: 1.01x slower                                                         |
| logging_simple           | 5.57 us                                                                | 5.65 us: 1.02x slower                                                        |
| deepcopy_reduce          | 2.64 us                                                                | 2.68 us: 1.02x slower                                                        |
| scimark_sor              | 117 ms                                                                 | 119 ms: 1.02x slower                                                         |
| deepcopy_memo            | 28.6 us                                                                | 29.2 us: 1.02x slower                                                        |
| logging_format           | 6.15 us                                                                | 6.30 us: 1.02x slower                                                        |
| deltablue                | 3.03 ms                                                                | 3.11 ms: 1.02x slower                                                        |
| pyflate                  | 429 ms                                                                 | 442 ms: 1.03x slower                                                         |
| gc_traversal             | 4.82 ms                                                                | 4.99 ms: 1.03x slower                                                        |
| logging_silent           | 95.9 ns                                                                | 100 ns: 1.05x slower                                                         |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (43): sphinx, scimark_monte_carlo, async_tree_io_tg, async_tree_cpu_io_mixed_tg, k_core, richards_super, fannkuch, sqlalchemy_imperative, pylint, scimark_lu, many_optionals, async_tree_cpu_io_mixed, xml_etree_process, pprint_pformat, scimark_sparse_mat_mult, sympy_str, regex_v8, async_tree_none, async_tree_io, richards, shortest_path, asyncio_websockets, async_generators, subparsers, bpe_tokeniser, xml_etree_iterparse, tomli_loads, pprint_safe_repr, xml_etree_generate, scimark_fft, xml_etree_parse, float, json, sympy_sum, sqlglot_v2_normalize, json_dumps, chaos, docutils, hexiom, meteor_contest, unpickle_pure_python, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 54.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x