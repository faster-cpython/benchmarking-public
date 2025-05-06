# Results vs. base

- fork: brandtbucher
- ref: jit_recursive
- machine: linux-x86_64
- commit hash: fe02176
- commit date: 2025-05-05
- overall geometric mean: 1.001x slower
- HPT reliability: 73.32%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7+-b1aa515 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 25.1 ms                                                                | 24.6 ms: 1.02x faster                                                 |
| async_tree_eager_io_tg           | 636 ms                                                                 | 626 ms: 1.02x faster                                                  |
| async_tree_eager_memoization     | 202 ms                                                                 | 200 ms: 1.01x faster                                                  |
| async_generators                 | 425 ms                                                                 | 423 ms: 1.00x faster                                                  |
| async_tree_cpu_io_mixed          | 495 ms                                                                 | 501 ms: 1.01x slower                                                  |
| async_tree_none_tg               | 249 ms                                                                 | 252 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 461 ms                                                                 | 468 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 486 ms                                                                 | 496 ms: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 388 ms                                                                 | 398 ms: 1.03x slower                                                  |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (10): async_tree_eager_io, async_tree_eager_tg, async_tree_eager, async_tree_eager_memoization_tg, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7+-b1aa515 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 191 ms: 1.01x slower                                                  |
| float          | 64.1 ms                                                                | 64.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7+-b1aa515 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.02 ms                                                                | 2.95 ms: 1.02x faster                                                 |
| regex_dna      | 198 ms                                                                 | 196 ms: 1.01x faster                                                  |
| regex_compile  | 127 ms                                                                 | 128 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7+-b1aa515 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads          | 30.2 us                                                                | 29.8 us: 1.01x faster                                                 |
| xml_etree_iterparse | 98.6 ms                                                                | 99.3 ms: 1.01x slower                                                 |
| xml_etree_process   | 55.5 ms                                                                | 56.2 ms: 1.01x slower                                                 |
| xml_etree_generate  | 80.3 ms                                                                | 81.2 ms: 1.01x slower                                                 |
| tomli_loads         | 1.85 sec                                                               | 1.88 sec: 1.01x slower                                                |
| pickle_pure_python  | 317 us                                                                 | 323 us: 1.02x slower                                                  |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7+-b1aa515 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.97 ms                                                                | 6.92 ms: 1.01x faster                                                 |
| python_startup         | 13.2 ms                                                                | 13.1 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7+-b1aa515 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 11.1 ms                                                                | 11.2 ms: 1.00x slower                                                 |
| genshi_xml     | 48.7 ms                                                                | 49.4 ms: 1.01x slower                                                 |
| genshi_text    | 21.2 ms                                                                | 21.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7+-b1aa515 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot                     | 3.02 ms                                                                | 2.95 ms: 1.02x faster                                                 |
| coroutines                       | 25.1 ms                                                                | 24.6 ms: 1.02x faster                                                 |
| scimark_fft                      | 417 ms                                                                 | 409 ms: 1.02x faster                                                  |
| async_tree_eager_io_tg           | 636 ms                                                                 | 626 ms: 1.02x faster                                                  |
| pyflate                          | 446 ms                                                                 | 440 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult          | 6.15 ms                                                                | 6.06 ms: 1.01x faster                                                 |
| json_loads                       | 30.2 us                                                                | 29.8 us: 1.01x faster                                                 |
| json                             | 5.37 ms                                                                | 5.30 ms: 1.01x faster                                                 |
| go                               | 122 ms                                                                 | 121 ms: 1.01x faster                                                  |
| logging_simple                   | 5.74 us                                                                | 5.69 us: 1.01x faster                                                 |
| async_tree_eager_memoization     | 202 ms                                                                 | 200 ms: 1.01x faster                                                  |
| regex_dna                        | 198 ms                                                                 | 196 ms: 1.01x faster                                                  |
| scimark_lu                       | 123 ms                                                                 | 122 ms: 1.01x faster                                                  |
| telco                            | 7.93 ms                                                                | 7.88 ms: 1.01x faster                                                 |
| sqlglot_v2_parse                 | 1.25 ms                                                                | 1.25 ms: 1.01x faster                                                 |
| scimark_sor                      | 123 ms                                                                 | 122 ms: 1.01x faster                                                  |
| python_startup_no_site           | 6.97 ms                                                                | 6.92 ms: 1.01x faster                                                 |
| sqlite_synth                     | 2.81 us                                                                | 2.79 us: 1.01x faster                                                 |
| python_startup                   | 13.2 ms                                                                | 13.1 ms: 1.00x faster                                                 |
| deepcopy                         | 259 us                                                                 | 258 us: 1.00x faster                                                  |
| async_generators                 | 425 ms                                                                 | 423 ms: 1.00x faster                                                  |
| sqlglot_v2_transpile             | 1.57 ms                                                                | 1.57 ms: 1.00x faster                                                 |
| shortest_path                    | 487 ms                                                                 | 486 ms: 1.00x faster                                                  |
| sympy_expand                     | 470 ms                                                                 | 471 ms: 1.00x slower                                                  |
| crypto_pyaes                     | 76.0 ms                                                                | 76.2 ms: 1.00x slower                                                 |
| regex_compile                    | 127 ms                                                                 | 128 ms: 1.00x slower                                                  |
| mako                             | 11.1 ms                                                                | 11.2 ms: 1.00x slower                                                 |
| sympy_integrate                  | 19.3 ms                                                                | 19.4 ms: 1.00x slower                                                 |
| sympy_sum                        | 148 ms                                                                 | 149 ms: 1.00x slower                                                  |
| deltablue                        | 3.04 ms                                                                | 3.05 ms: 1.00x slower                                                 |
| bpe_tokeniser                    | 4.33 sec                                                               | 4.35 sec: 1.00x slower                                                |
| sympy_str                        | 269 ms                                                                 | 270 ms: 1.00x slower                                                  |
| scimark_monte_carlo              | 75.1 ms                                                                | 75.5 ms: 1.00x slower                                                 |
| pidigits                         | 190 ms                                                                 | 191 ms: 1.01x slower                                                  |
| meteor_contest                   | 109 ms                                                                 | 109 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 98.6 ms                                                                | 99.3 ms: 1.01x slower                                                 |
| subparsers                       | 22.9 ms                                                                | 23.1 ms: 1.01x slower                                                 |
| connected_components             | 444 ms                                                                 | 449 ms: 1.01x slower                                                  |
| xml_etree_process                | 55.5 ms                                                                | 56.2 ms: 1.01x slower                                                 |
| float                            | 64.1 ms                                                                | 64.8 ms: 1.01x slower                                                 |
| xml_etree_generate               | 80.3 ms                                                                | 81.2 ms: 1.01x slower                                                 |
| spectral_norm                    | 103 ms                                                                 | 104 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed          | 495 ms                                                                 | 501 ms: 1.01x slower                                                  |
| async_tree_none_tg               | 249 ms                                                                 | 252 ms: 1.01x slower                                                  |
| tomli_loads                      | 1.85 sec                                                               | 1.88 sec: 1.01x slower                                                |
| hexiom                           | 6.56 ms                                                                | 6.65 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 461 ms                                                                 | 468 ms: 1.01x slower                                                  |
| genshi_xml                       | 48.7 ms                                                                | 49.4 ms: 1.01x slower                                                 |
| pickle_pure_python               | 317 us                                                                 | 323 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 486 ms                                                                 | 496 ms: 1.02x slower                                                  |
| generators                       | 30.7 ms                                                                | 31.3 ms: 1.02x slower                                                 |
| nqueens                          | 81.9 ms                                                                | 83.6 ms: 1.02x slower                                                 |
| deepcopy_memo                    | 29.2 us                                                                | 29.8 us: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 388 ms                                                                 | 398 ms: 1.03x slower                                                  |
| gc_traversal                     | 4.94 ms                                                                | 5.08 ms: 1.03x slower                                                 |
| logging_silent                   | 98.6 ns                                                                | 102 ns: 1.03x slower                                                  |
| genshi_text                      | 21.2 ms                                                                | 21.9 ms: 1.03x slower                                                 |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (40): async_tree_eager_io, async_tree_eager_tg, typing_runtime_protocols, pprint_safe_repr, nbody, async_tree_eager, pycparser, async_tree_eager_memoization_tg, async_tree_none, async_tree_memoization_tg, fannkuch, async_tree_memoization, bench_mp_pool, raytrace, mdp, docutils, many_optionals, create_gc_cycles, logging_format, regex_v8, 2to3, deepcopy_reduce, dulwich_log, pylint, async_tree_io_tg, html5lib, bench_thread_pool, chaos, asyncio_websockets, comprehensions, json_dumps, pathlib, async_tree_io, django_template, xml_etree_parse, pprint_pformat, richards, k_core, richards_super, unpickle_pure_python
Ignored benchmarks (2) of results/bm-20250505-3.14.0a7+-b1aa515-JIT/bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7+-b1aa515.json: sqlglot_v2_normalize, sqlglot_v2_optimize

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 73.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x