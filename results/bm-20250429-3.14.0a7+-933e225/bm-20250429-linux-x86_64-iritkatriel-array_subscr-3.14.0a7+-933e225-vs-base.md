# Results vs. base

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 933e225
- commit date: 2025-04-29
- overall geometric mean: 1.001x slower
- HPT reliability: 80.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 253 ms: 1.00x faster                                                |
| docutils       | 2.62 sec                                                               | 2.61 sec: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                       | 24.6 ms                                                                | 23.8 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg       | 493 ms                                                                 | 479 ms: 1.03x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 468 ms                                                                 | 454 ms: 1.03x faster                                                |
| async_tree_eager_cpu_io_mixed    | 389 ms                                                                 | 379 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed          | 497 ms                                                                 | 488 ms: 1.02x faster                                                |
| async_tree_memoization_tg        | 309 ms                                                                 | 305 ms: 1.01x faster                                                |
| async_tree_none_tg               | 252 ms                                                                 | 249 ms: 1.01x faster                                                |
| async_generators                 | 399 ms                                                                 | 397 ms: 1.00x faster                                                |
| async_tree_eager                 | 101 ms                                                                 | 102 ms: 1.01x slower                                                |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (10): async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, asyncio_websockets, async_tree_eager_io_tg, async_tree_memoization, async_tree_eager_io, async_tree_none, async_tree_eager_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.2 ms                                                                | 95.1 ms: 1.02x faster                                               |
| pidigits       | 191 ms                                                                 | 194 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                 | 204 ms: 1.03x faster                                                |
| regex_effbot   | 3.22 ms                                                                | 3.18 ms: 1.01x faster                                               |
| regex_v8       | 23.4 ms                                                                | 23.3 ms: 1.01x faster                                               |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process    | 59.5 ms                                                                | 59.0 ms: 1.01x faster                                               |
| xml_etree_generate   | 84.8 ms                                                                | 84.2 ms: 1.01x faster                                               |
| xml_etree_parse      | 142 ms                                                                 | 141 ms: 1.01x faster                                                |
| unpickle_pure_python | 217 us                                                                 | 216 us: 1.01x faster                                                |
| json_loads           | 29.8 us                                                                | 30.0 us: 1.00x slower                                               |
| pickle_pure_python   | 315 us                                                                 | 317 us: 1.01x slower                                                |
| tomli_loads          | 1.95 sec                                                               | 1.96 sec: 1.01x slower                                              |
| json_dumps           | 11.5 ms                                                                | 11.7 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                               |
| python_startup_no_site | 8.21 ms                                                                | 8.20 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                               |
| genshi_xml     | 48.7 ms                                                                | 49.2 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                        | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal                     | 5.06 ms                                                                | 4.64 ms: 1.09x faster                                               |
| coroutines                       | 24.6 ms                                                                | 23.8 ms: 1.04x faster                                               |
| generators                       | 30.3 ms                                                                | 29.3 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed_tg       | 493 ms                                                                 | 479 ms: 1.03x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 468 ms                                                                 | 454 ms: 1.03x faster                                                |
| regex_dna                        | 210 ms                                                                 | 204 ms: 1.03x faster                                                |
| async_tree_eager_cpu_io_mixed    | 389 ms                                                                 | 379 ms: 1.03x faster                                                |
| nbody                            | 97.2 ms                                                                | 95.1 ms: 1.02x faster                                               |
| typing_runtime_protocols         | 172 us                                                                 | 168 us: 1.02x faster                                                |
| fannkuch                         | 420 ms                                                                 | 412 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed          | 497 ms                                                                 | 488 ms: 1.02x faster                                                |
| crypto_pyaes                     | 73.7 ms                                                                | 72.4 ms: 1.02x faster                                               |
| dulwich_log                      | 59.3 ms                                                                | 58.6 ms: 1.01x faster                                               |
| async_tree_memoization_tg        | 309 ms                                                                 | 305 ms: 1.01x faster                                                |
| regex_effbot                     | 3.22 ms                                                                | 3.18 ms: 1.01x faster                                               |
| async_tree_none_tg               | 252 ms                                                                 | 249 ms: 1.01x faster                                                |
| hexiom                           | 6.20 ms                                                                | 6.14 ms: 1.01x faster                                               |
| bpe_tokeniser                    | 4.47 sec                                                               | 4.42 sec: 1.01x faster                                              |
| create_gc_cycles                 | 2.48 ms                                                                | 2.46 ms: 1.01x faster                                               |
| xml_etree_process                | 59.5 ms                                                                | 59.0 ms: 1.01x faster                                               |
| shortest_path                    | 508 ms                                                                 | 503 ms: 1.01x faster                                                |
| sqlite_synth                     | 2.83 us                                                                | 2.81 us: 1.01x faster                                               |
| xml_etree_generate               | 84.8 ms                                                                | 84.2 ms: 1.01x faster                                               |
| xml_etree_parse                  | 142 ms                                                                 | 141 ms: 1.01x faster                                                |
| regex_v8                         | 23.4 ms                                                                | 23.3 ms: 1.01x faster                                               |
| unpickle_pure_python             | 217 us                                                                 | 216 us: 1.01x faster                                                |
| regex_compile                    | 126 ms                                                                 | 125 ms: 1.01x faster                                                |
| docutils                         | 2.62 sec                                                               | 2.61 sec: 1.01x faster                                              |
| 2to3                             | 254 ms                                                                 | 253 ms: 1.00x faster                                                |
| async_generators                 | 399 ms                                                                 | 397 ms: 1.00x faster                                                |
| nqueens                          | 80.9 ms                                                                | 80.6 ms: 1.00x faster                                               |
| many_optionals                   | 935 us                                                                 | 932 us: 1.00x faster                                                |
| sqlalchemy_declarative           | 132 ms                                                                 | 131 ms: 1.00x faster                                                |
| python_startup                   | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                               |
| python_startup_no_site           | 8.21 ms                                                                | 8.20 ms: 1.00x faster                                               |
| bench_thread_pool                | 884 us                                                                 | 886 us: 1.00x slower                                                |
| sympy_str                        | 264 ms                                                                 | 265 ms: 1.00x slower                                                |
| raytrace                         | 262 ms                                                                 | 263 ms: 1.00x slower                                                |
| sympy_expand                     | 449 ms                                                                 | 450 ms: 1.00x slower                                                |
| json_loads                       | 29.8 us                                                                | 30.0 us: 1.00x slower                                               |
| sympy_sum                        | 147 ms                                                                 | 147 ms: 1.01x slower                                                |
| pickle_pure_python               | 315 us                                                                 | 317 us: 1.01x slower                                                |
| sympy_integrate                  | 18.8 ms                                                                | 19.0 ms: 1.01x slower                                               |
| async_tree_eager                 | 101 ms                                                                 | 102 ms: 1.01x slower                                                |
| tomli_loads                      | 1.95 sec                                                               | 1.96 sec: 1.01x slower                                              |
| mako                             | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                               |
| deepcopy                         | 254 us                                                                 | 257 us: 1.01x slower                                                |
| genshi_xml                       | 48.7 ms                                                                | 49.2 ms: 1.01x slower                                               |
| richards                         | 42.7 ms                                                                | 43.2 ms: 1.01x slower                                               |
| sqlglot_v2_transpile             | 1.52 ms                                                                | 1.54 ms: 1.01x slower                                               |
| json_dumps                       | 11.5 ms                                                                | 11.7 ms: 1.01x slower                                               |
| sqlglot_v2_parse                 | 1.21 ms                                                                | 1.23 ms: 1.01x slower                                               |
| deltablue                        | 3.36 ms                                                                | 3.40 ms: 1.01x slower                                               |
| json                             | 5.32 ms                                                                | 5.40 ms: 1.02x slower                                               |
| pprint_safe_repr                 | 710 ms                                                                 | 721 ms: 1.02x slower                                                |
| subparsers                       | 20.6 ms                                                                | 20.9 ms: 1.02x slower                                               |
| logging_simple                   | 5.49 us                                                                | 5.57 us: 1.02x slower                                               |
| logging_silent                   | 96.4 ns                                                                | 97.9 ns: 1.02x slower                                               |
| pprint_pformat                   | 1.45 sec                                                               | 1.47 sec: 1.02x slower                                              |
| deepcopy_memo                    | 28.1 us                                                                | 28.6 us: 1.02x slower                                               |
| richards_super                   | 49.0 ms                                                                | 49.9 ms: 1.02x slower                                               |
| pidigits                         | 191 ms                                                                 | 194 ms: 1.02x slower                                                |
| scimark_lu                       | 120 ms                                                                 | 123 ms: 1.02x slower                                                |
| go                               | 111 ms                                                                 | 114 ms: 1.03x slower                                                |
| logging_format                   | 6.03 us                                                                | 6.23 us: 1.03x slower                                               |
| scimark_sor                      | 117 ms                                                                 | 122 ms: 1.04x slower                                                |
| scimark_monte_carlo              | 67.5 ms                                                                | 72.6 ms: 1.08x slower                                               |
| scimark_fft                      | 354 ms                                                                 | 386 ms: 1.09x slower                                                |
| scimark_sparse_mat_mult          | 5.01 ms                                                                | 5.63 ms: 1.12x slower                                               |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (34): async_tree_eager_memoization_tg, meteor_contest, coverage, float, connected_components, async_tree_eager_tg, async_tree_io_tg, deepcopy_reduce, comprehensions, genshi_text, pylint, chaos, sphinx, asyncio_websockets, mdp, xml_etree_iterparse, k_core, async_tree_eager_io_tg, sqlalchemy_imperative, pyflate, sqlglot_v2_optimize, bench_mp_pool, async_tree_memoization, spectral_norm, pathlib, sqlglot_v2_normalize, telco, django_template, html5lib, pycparser, async_tree_eager_io, async_tree_none, async_tree_eager_memoization, async_tree_io

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 80.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x