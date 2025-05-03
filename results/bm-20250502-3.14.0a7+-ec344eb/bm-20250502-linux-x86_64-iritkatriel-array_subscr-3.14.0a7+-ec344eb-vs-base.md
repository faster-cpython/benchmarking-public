# Results vs. base

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: ec344eb
- commit date: 2025-05-02
- overall geometric mean: 1.000x slower
- HPT reliability: 89.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 253 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                       | 26.0 ms                                                                | 25.3 ms: 1.03x faster                                               |
| async_generators                 | 412 ms                                                                 | 405 ms: 1.02x faster                                                |
| async_tree_memoization           | 316 ms                                                                 | 313 ms: 1.01x faster                                                |
| async_tree_eager                 | 103 ms                                                                 | 104 ms: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 467 ms                                                                 | 472 ms: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed    | 391 ms                                                                 | 398 ms: 1.02x slower                                                |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (13): async_tree_eager_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, asyncio_websockets, async_tree_eager_io, async_tree_eager_io_tg, async_tree_io_tg, async_tree_none, async_tree_eager_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 100 ms                                                                 | 98.4 ms: 1.02x faster                                               |
| pidigits       | 187 ms                                                                 | 194 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                 | 204 ms: 1.02x faster                                                |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.00x faster                                                |
| regex_effbot   | 3.20 ms                                                                | 3.32 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 11.9 ms                                                                | 11.7 ms: 1.02x faster                                               |
| json_loads           | 30.0 us                                                                | 29.6 us: 1.01x faster                                               |
| tomli_loads          | 2.01 sec                                                               | 1.99 sec: 1.01x faster                                              |
| unpickle_pure_python | 220 us                                                                 | 219 us: 1.01x faster                                                |
| xml_etree_process    | 59.3 ms                                                                | 59.0 ms: 1.01x faster                                               |
| xml_etree_generate   | 85.4 ms                                                                | 85.2 ms: 1.00x faster                                               |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.92 ms                                                                | 6.91 ms: 1.00x faster                                               |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 49.9 ms                                                                | 49.1 ms: 1.02x faster                                               |
| mako            | 12.0 ms                                                                | 11.8 ms: 1.01x faster                                               |
| genshi_text     | 21.2 ms                                                                | 21.1 ms: 1.01x faster                                               |
| django_template | 31.8 ms                                                                | 31.7 ms: 1.00x faster                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                        | bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| shortest_path                    | 515 ms                                                                 | 486 ms: 1.06x faster                                                |
| pycparser                        | 1.17 sec                                                               | 1.13 sec: 1.04x faster                                              |
| coroutines                       | 26.0 ms                                                                | 25.3 ms: 1.03x faster                                               |
| json_dumps                       | 11.9 ms                                                                | 11.7 ms: 1.02x faster                                               |
| sqlite_synth                     | 2.92 us                                                                | 2.85 us: 1.02x faster                                               |
| regex_dna                        | 208 ms                                                                 | 204 ms: 1.02x faster                                                |
| nbody                            | 100 ms                                                                 | 98.4 ms: 1.02x faster                                               |
| spectral_norm                    | 109 ms                                                                 | 107 ms: 1.02x faster                                                |
| genshi_xml                       | 49.9 ms                                                                | 49.1 ms: 1.02x faster                                               |
| async_generators                 | 412 ms                                                                 | 405 ms: 1.02x faster                                                |
| mako                             | 12.0 ms                                                                | 11.8 ms: 1.01x faster                                               |
| deepcopy_reduce                  | 2.74 us                                                                | 2.70 us: 1.01x faster                                               |
| json_loads                       | 30.0 us                                                                | 29.6 us: 1.01x faster                                               |
| json                             | 5.36 ms                                                                | 5.29 ms: 1.01x faster                                               |
| mdp                              | 1.23 sec                                                               | 1.21 sec: 1.01x faster                                              |
| deltablue                        | 3.42 ms                                                                | 3.38 ms: 1.01x faster                                               |
| connected_components             | 456 ms                                                                 | 451 ms: 1.01x faster                                                |
| deepcopy                         | 262 us                                                                 | 259 us: 1.01x faster                                                |
| sqlglot_v2_transpile             | 1.56 ms                                                                | 1.54 ms: 1.01x faster                                               |
| gc_traversal                     | 4.67 ms                                                                | 4.62 ms: 1.01x faster                                               |
| sqlglot_v2_parse                 | 1.25 ms                                                                | 1.24 ms: 1.01x faster                                               |
| async_tree_memoization           | 316 ms                                                                 | 313 ms: 1.01x faster                                                |
| tomli_loads                      | 2.01 sec                                                               | 1.99 sec: 1.01x faster                                              |
| fannkuch                         | 412 ms                                                                 | 409 ms: 1.01x faster                                                |
| bpe_tokeniser                    | 4.50 sec                                                               | 4.47 sec: 1.01x faster                                              |
| genshi_text                      | 21.2 ms                                                                | 21.1 ms: 1.01x faster                                               |
| richards                         | 43.7 ms                                                                | 43.4 ms: 1.01x faster                                               |
| sqlglot_v2_optimize              | 52.8 ms                                                                | 52.5 ms: 1.01x faster                                               |
| unpickle_pure_python             | 220 us                                                                 | 219 us: 1.01x faster                                                |
| xml_etree_process                | 59.3 ms                                                                | 59.0 ms: 1.01x faster                                               |
| sympy_integrate                  | 19.1 ms                                                                | 19.0 ms: 1.01x faster                                               |
| hexiom                           | 6.40 ms                                                                | 6.37 ms: 1.00x faster                                               |
| django_template                  | 31.8 ms                                                                | 31.7 ms: 1.00x faster                                               |
| richards_super                   | 50.0 ms                                                                | 49.8 ms: 1.00x faster                                               |
| nqueens                          | 81.0 ms                                                                | 80.7 ms: 1.00x faster                                               |
| go                               | 112 ms                                                                 | 111 ms: 1.00x faster                                                |
| dulwich_log                      | 59.5 ms                                                                | 59.3 ms: 1.00x faster                                               |
| sqlglot_v2_normalize             | 106 ms                                                                 | 106 ms: 1.00x faster                                                |
| regex_compile                    | 128 ms                                                                 | 127 ms: 1.00x faster                                                |
| xml_etree_generate               | 85.4 ms                                                                | 85.2 ms: 1.00x faster                                               |
| 2to3                             | 254 ms                                                                 | 253 ms: 1.00x faster                                                |
| bench_thread_pool                | 891 us                                                                 | 889 us: 1.00x faster                                                |
| python_startup_no_site           | 6.92 ms                                                                | 6.91 ms: 1.00x faster                                               |
| python_startup                   | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| raytrace                         | 271 ms                                                                 | 272 ms: 1.00x slower                                                |
| meteor_contest                   | 106 ms                                                                 | 107 ms: 1.00x slower                                                |
| sympy_str                        | 267 ms                                                                 | 268 ms: 1.00x slower                                                |
| pprint_pformat                   | 1.48 sec                                                               | 1.49 sec: 1.00x slower                                              |
| sympy_expand                     | 456 ms                                                                 | 458 ms: 1.00x slower                                                |
| sympy_sum                        | 148 ms                                                                 | 149 ms: 1.01x slower                                                |
| chaos                            | 59.3 ms                                                                | 59.6 ms: 1.01x slower                                               |
| pathlib                          | 16.9 ms                                                                | 17.0 ms: 1.01x slower                                               |
| deepcopy_memo                    | 29.3 us                                                                | 29.5 us: 1.01x slower                                               |
| async_tree_eager                 | 103 ms                                                                 | 104 ms: 1.01x slower                                                |
| many_optionals                   | 949 us                                                                 | 958 us: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 467 ms                                                                 | 472 ms: 1.01x slower                                                |
| pprint_safe_repr                 | 730 ms                                                                 | 738 ms: 1.01x slower                                                |
| logging_format                   | 6.14 us                                                                | 6.22 us: 1.01x slower                                               |
| crypto_pyaes                     | 75.7 ms                                                                | 76.8 ms: 1.01x slower                                               |
| logging_simple                   | 5.52 us                                                                | 5.61 us: 1.02x slower                                               |
| async_tree_eager_cpu_io_mixed    | 391 ms                                                                 | 398 ms: 1.02x slower                                                |
| subparsers                       | 22.5 ms                                                                | 23.0 ms: 1.02x slower                                               |
| pyflate                          | 427 ms                                                                 | 440 ms: 1.03x slower                                                |
| regex_effbot                     | 3.20 ms                                                                | 3.32 ms: 1.04x slower                                               |
| pidigits                         | 187 ms                                                                 | 194 ms: 1.04x slower                                                |
| scimark_fft                      | 379 ms                                                                 | 397 ms: 1.05x slower                                                |
| logging_silent                   | 97.6 ns                                                                | 103 ns: 1.06x slower                                                |
| scimark_monte_carlo              | 67.9 ms                                                                | 72.9 ms: 1.07x slower                                               |
| scimark_sparse_mat_mult          | 5.06 ms                                                                | 5.90 ms: 1.16x slower                                               |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (31): async_tree_eager_memoization, sphinx, html5lib, k_core, async_tree_memoization_tg, scimark_sor, async_tree_none_tg, async_tree_io, regex_v8, typing_runtime_protocols, telco, float, pickle_pure_python, xml_etree_iterparse, asyncio_websockets, create_gc_cycles, docutils, async_tree_eager_io, pylint, bench_mp_pool, async_tree_eager_io_tg, xml_etree_parse, scimark_lu, async_tree_io_tg, async_tree_none, comprehensions, generators, async_tree_eager_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg
Ignored benchmarks (3) of results/bm-20250502-3.14.0a7+-49ea8a0/bm-20250502-linux-x86_64-python-49ea8a0b2d5d65122e5e-3.14.0a7+-49ea8a0.json: coverage, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 89.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x