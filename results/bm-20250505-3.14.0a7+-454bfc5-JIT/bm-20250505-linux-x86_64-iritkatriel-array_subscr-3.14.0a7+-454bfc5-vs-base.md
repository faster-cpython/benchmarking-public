# Results vs. base

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 454bfc5
- commit date: 2025-05-05
- overall geometric mean: 1.010x slower
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7+-f554237 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization           | 317 ms                                                                 | 313 ms: 1.01x faster                                                |
| async_tree_eager_io_tg           | 634 ms                                                                 | 629 ms: 1.01x faster                                                |
| async_tree_memoization_tg        | 306 ms                                                                 | 308 ms: 1.01x slower                                                |
| async_generators                 | 428 ms                                                                 | 431 ms: 1.01x slower                                                |
| coroutines                       | 25.5 ms                                                                | 25.7 ms: 1.01x slower                                               |
| async_tree_eager                 | 103 ms                                                                 | 104 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg       | 485 ms                                                                 | 493 ms: 1.02x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 450 ms                                                                 | 460 ms: 1.02x slower                                                |
| async_tree_eager_cpu_io_mixed    | 387 ms                                                                 | 396 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed          | 492 ms                                                                 | 503 ms: 1.02x slower                                                |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (9): async_tree_eager_memoization, async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_websockets, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7+-f554237 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                |
| float          | 64.9 ms                                                                | 65.9 ms: 1.02x slower                                               |
| nbody          | 92.5 ms                                                                | 98.1 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7+-f554237 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 127 ms: 1.00x faster                                                |
| regex_effbot   | 3.34 ms                                                                | 3.35 ms: 1.00x slower                                               |
| regex_dna      | 207 ms                                                                 | 208 ms: 1.00x slower                                                |
| regex_v8       | 23.7 ms                                                                | 23.9 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7+-f554237 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse | 99.2 ms                                                                | 98.2 ms: 1.01x faster                                               |
| xml_etree_parse     | 140 ms                                                                 | 141 ms: 1.01x slower                                                |
| json_dumps          | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                               |
| json_loads          | 29.8 us                                                                | 30.2 us: 1.01x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (5): xml_etree_process, unpickle_pure_python, pickle_pure_python, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7+-f554237 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                               |
| python_startup_no_site | 6.94 ms                                                                | 6.94 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7+-f554237 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 49.8 ms                                                                | 49.1 ms: 1.01x faster                                               |
| genshi_text    | 21.2 ms                                                                | 21.1 ms: 1.01x faster                                               |
| mako           | 11.2 ms                                                                | 11.3 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7+-f554237 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo                    | 30.3 us                                                                | 29.1 us: 1.04x faster                                               |
| go                               | 126 ms                                                                 | 123 ms: 1.03x faster                                                |
| generators                       | 30.5 ms                                                                | 29.8 ms: 1.02x faster                                               |
| pprint_safe_repr                 | 750 ms                                                                 | 735 ms: 1.02x faster                                                |
| deepcopy                         | 260 us                                                                 | 255 us: 1.02x faster                                                |
| pprint_pformat                   | 1.55 sec                                                               | 1.53 sec: 1.02x faster                                              |
| genshi_xml                       | 49.8 ms                                                                | 49.1 ms: 1.01x faster                                               |
| async_tree_memoization           | 317 ms                                                                 | 313 ms: 1.01x faster                                                |
| pathlib                          | 17.2 ms                                                                | 17.0 ms: 1.01x faster                                               |
| xml_etree_iterparse              | 99.2 ms                                                                | 98.2 ms: 1.01x faster                                               |
| many_optionals                   | 974 us                                                                 | 964 us: 1.01x faster                                                |
| sqlglot_v2_normalize             | 108 ms                                                                 | 107 ms: 1.01x faster                                                |
| sympy_integrate                  | 19.4 ms                                                                | 19.3 ms: 1.01x faster                                               |
| sympy_expand                     | 473 ms                                                                 | 469 ms: 1.01x faster                                                |
| async_tree_eager_io_tg           | 634 ms                                                                 | 629 ms: 1.01x faster                                                |
| hexiom                           | 6.76 ms                                                                | 6.70 ms: 1.01x faster                                               |
| connected_components             | 449 ms                                                                 | 445 ms: 1.01x faster                                                |
| sympy_str                        | 272 ms                                                                 | 270 ms: 1.01x faster                                                |
| deepcopy_reduce                  | 2.71 us                                                                | 2.69 us: 1.01x faster                                               |
| genshi_text                      | 21.2 ms                                                                | 21.1 ms: 1.01x faster                                               |
| sympy_sum                        | 150 ms                                                                 | 149 ms: 1.01x faster                                                |
| dulwich_log                      | 60.9 ms                                                                | 60.6 ms: 1.00x faster                                               |
| regex_compile                    | 128 ms                                                                 | 127 ms: 1.00x faster                                                |
| python_startup                   | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                               |
| python_startup_no_site           | 6.94 ms                                                                | 6.94 ms: 1.00x slower                                               |
| regex_effbot                     | 3.34 ms                                                                | 3.35 ms: 1.00x slower                                               |
| pidigits                         | 186 ms                                                                 | 187 ms: 1.00x slower                                                |
| shortest_path                    | 487 ms                                                                 | 488 ms: 1.00x slower                                                |
| bench_thread_pool                | 905 us                                                                 | 908 us: 1.00x slower                                                |
| regex_dna                        | 207 ms                                                                 | 208 ms: 1.00x slower                                                |
| async_tree_memoization_tg        | 306 ms                                                                 | 308 ms: 1.01x slower                                                |
| xml_etree_parse                  | 140 ms                                                                 | 141 ms: 1.01x slower                                                |
| regex_v8                         | 23.7 ms                                                                | 23.9 ms: 1.01x slower                                               |
| async_generators                 | 428 ms                                                                 | 431 ms: 1.01x slower                                                |
| json_dumps                       | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                               |
| coroutines                       | 25.5 ms                                                                | 25.7 ms: 1.01x slower                                               |
| async_tree_eager                 | 103 ms                                                                 | 104 ms: 1.01x slower                                                |
| crypto_pyaes                     | 77.1 ms                                                                | 77.9 ms: 1.01x slower                                               |
| json_loads                       | 29.8 us                                                                | 30.2 us: 1.01x slower                                               |
| deltablue                        | 3.03 ms                                                                | 3.07 ms: 1.01x slower                                               |
| meteor_contest                   | 108 ms                                                                 | 110 ms: 1.01x slower                                                |
| float                            | 64.9 ms                                                                | 65.9 ms: 1.02x slower                                               |
| mako                             | 11.2 ms                                                                | 11.3 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg       | 485 ms                                                                 | 493 ms: 1.02x slower                                                |
| logging_silent                   | 98.1 ns                                                                | 99.8 ns: 1.02x slower                                               |
| bpe_tokeniser                    | 4.40 sec                                                               | 4.48 sec: 1.02x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 450 ms                                                                 | 460 ms: 1.02x slower                                                |
| async_tree_eager_cpu_io_mixed    | 387 ms                                                                 | 396 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed          | 492 ms                                                                 | 503 ms: 1.02x slower                                                |
| json                             | 5.26 ms                                                                | 5.39 ms: 1.03x slower                                               |
| chaos                            | 60.0 ms                                                                | 61.6 ms: 1.03x slower                                               |
| raytrace                         | 273 ms                                                                 | 282 ms: 1.03x slower                                                |
| scimark_lu                       | 121 ms                                                                 | 124 ms: 1.03x slower                                                |
| scimark_sor                      | 120 ms                                                                 | 126 ms: 1.05x slower                                                |
| gc_traversal                     | 4.77 ms                                                                | 4.99 ms: 1.05x slower                                               |
| nbody                            | 92.5 ms                                                                | 98.1 ms: 1.06x slower                                               |
| spectral_norm                    | 99.5 ms                                                                | 106 ms: 1.06x slower                                                |
| scimark_monte_carlo              | 68.6 ms                                                                | 76.3 ms: 1.11x slower                                               |
| scimark_fft                      | 327 ms                                                                 | 419 ms: 1.28x slower                                                |
| scimark_sparse_mat_mult          | 4.77 ms                                                                | 6.29 ms: 1.32x slower                                               |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (40): pycparser, logging_simple, async_tree_eager_memoization, async_tree_eager_io, async_tree_eager_memoization_tg, richards_super, pylint, sqlglot_v2_optimize, typing_runtime_protocols, create_gc_cycles, comprehensions, async_tree_eager_tg, sqlglot_v2_parse, xml_etree_process, subparsers, sqlglot_v2_transpile, asyncio_websockets, 2to3, docutils, k_core, sphinx, mdp, django_template, unpickle_pure_python, async_tree_io, bench_mp_pool, nqueens, sqlite_synth, async_tree_io_tg, pyflate, richards, pickle_pure_python, xml_etree_generate, logging_format, tomli_loads, async_tree_none, telco, html5lib, async_tree_none_tg, fannkuch
Ignored benchmarks (3) of results/bm-20250505-3.14.0a7+-f554237-JIT/bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7+-f554237.json: coverage, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 99.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x