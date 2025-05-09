# Results vs. base

- fork: Fidget-Spinner
- ref: outline
- machine: linux-x86_64
- commit hash: 69dad45
- commit date: 2025-05-08
- overall geometric mean: 1.025x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250506-linux-x86_64-python-3dfed230928de0f64906-3.14.0a7+-3dfed23 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 265 ms: 1.01x slower                                                |
| docutils       | 2.66 sec                                                               | 2.68 sec: 1.01x slower                                              |
| html5lib       | 61.0 ms                                                                | 61.7 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250506-linux-x86_64-python-3dfed230928de0f64906-3.14.0a7+-3dfed23 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg       | 490 ms                                                                 | 484 ms: 1.01x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 462 ms                                                                 | 457 ms: 1.01x faster                                                |
| async_tree_eager_cpu_io_mixed    | 389 ms                                                                 | 386 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed          | 498 ms                                                                 | 494 ms: 1.01x faster                                                |
| async_tree_eager_memoization     | 201 ms                                                                 | 203 ms: 1.01x slower                                                |
| async_generators                 | 422 ms                                                                 | 426 ms: 1.01x slower                                                |
| async_tree_io                    | 599 ms                                                                 | 607 ms: 1.01x slower                                                |
| async_tree_memoization_tg        | 310 ms                                                                 | 315 ms: 1.01x slower                                                |
| async_tree_eager                 | 103 ms                                                                 | 104 ms: 1.02x slower                                                |
| async_tree_eager_io_tg           | 630 ms                                                                 | 642 ms: 1.02x slower                                                |
| async_tree_memoization           | 313 ms                                                                 | 319 ms: 1.02x slower                                                |
| async_tree_eager_io              | 620 ms                                                                 | 632 ms: 1.02x slower                                                |
| async_tree_eager_tg              | 211 ms                                                                 | 216 ms: 1.02x slower                                                |
| async_tree_eager_memoization_tg  | 277 ms                                                                 | 283 ms: 1.02x slower                                                |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (5): coroutines, asyncio_websockets, async_tree_io_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250506-linux-x86_64-python-3dfed230928de0f64906-3.14.0a7+-3dfed23 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 195 ms: 1.04x slower                                                |
| float          | 64.6 ms                                                                | 69.4 ms: 1.07x slower                                               |
| nbody          | 92.2 ms                                                                | 99.3 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250506-linux-x86_64-python-3dfed230928de0f64906-3.14.0a7+-3dfed23 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.04 ms                                                                | 2.95 ms: 1.03x faster                                               |
| regex_dna      | 198 ms                                                                 | 195 ms: 1.01x faster                                                |
| regex_v8       | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                               |
| regex_compile  | 126 ms                                                                 | 130 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250506-linux-x86_64-python-3dfed230928de0f64906-3.14.0a7+-3dfed23 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 29.6 us                                                                | 29.4 us: 1.01x faster                                               |
| xml_etree_iterparse  | 99.1 ms                                                                | 98.3 ms: 1.01x faster                                               |
| json_dumps           | 11.8 ms                                                                | 12.1 ms: 1.02x slower                                               |
| xml_etree_generate   | 81.2 ms                                                                | 83.8 ms: 1.03x slower                                               |
| pickle_pure_python   | 321 us                                                                 | 335 us: 1.04x slower                                                |
| xml_etree_process    | 55.7 ms                                                                | 58.7 ms: 1.05x slower                                               |
| tomli_loads          | 1.90 sec                                                               | 2.06 sec: 1.08x slower                                              |
| unpickle_pure_python | 208 us                                                                 | 234 us: 1.12x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.04x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250506-linux-x86_64-python-3dfed230928de0f64906-3.14.0a7+-3dfed23 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                                | 6.96 ms: 1.00x faster                                               |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250506-linux-x86_64-python-3dfed230928de0f64906-3.14.0a7+-3dfed23 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                | 21.5 ms: 1.01x slower                                               |
| django_template | 32.1 ms                                                                | 32.9 ms: 1.03x slower                                               |
| mako            | 11.2 ms                                                                | 11.7 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250506-linux-x86_64-python-3dfed230928de0f64906-3.14.0a7+-3dfed23 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal                     | 5.09 ms                                                                | 4.73 ms: 1.08x faster                                               |
| regex_effbot                     | 3.04 ms                                                                | 2.95 ms: 1.03x faster                                               |
| regex_dna                        | 198 ms                                                                 | 195 ms: 1.01x faster                                                |
| regex_v8                         | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg       | 490 ms                                                                 | 484 ms: 1.01x faster                                                |
| create_gc_cycles                 | 2.59 ms                                                                | 2.57 ms: 1.01x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 462 ms                                                                 | 457 ms: 1.01x faster                                                |
| async_tree_eager_cpu_io_mixed    | 389 ms                                                                 | 386 ms: 1.01x faster                                                |
| json_loads                       | 29.6 us                                                                | 29.4 us: 1.01x faster                                               |
| xml_etree_iterparse              | 99.1 ms                                                                | 98.3 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed          | 498 ms                                                                 | 494 ms: 1.01x faster                                                |
| python_startup_no_site           | 6.96 ms                                                                | 6.96 ms: 1.00x faster                                               |
| python_startup                   | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                               |
| bench_mp_pool                    | 93.0 ms                                                                | 93.4 ms: 1.00x slower                                               |
| sympy_integrate                  | 19.5 ms                                                                | 19.6 ms: 1.01x slower                                               |
| meteor_contest                   | 110 ms                                                                 | 111 ms: 1.01x slower                                                |
| sympy_sum                        | 148 ms                                                                 | 149 ms: 1.01x slower                                                |
| sqlalchemy_declarative           | 134 ms                                                                 | 135 ms: 1.01x slower                                                |
| scimark_lu                       | 118 ms                                                                 | 119 ms: 1.01x slower                                                |
| docutils                         | 2.66 sec                                                               | 2.68 sec: 1.01x slower                                              |
| async_tree_eager_memoization     | 201 ms                                                                 | 203 ms: 1.01x slower                                                |
| async_generators                 | 422 ms                                                                 | 426 ms: 1.01x slower                                                |
| logging_format                   | 6.35 us                                                                | 6.41 us: 1.01x slower                                               |
| sqlite_synth                     | 2.77 us                                                                | 2.80 us: 1.01x slower                                               |
| html5lib                         | 61.0 ms                                                                | 61.7 ms: 1.01x slower                                               |
| 2to3                             | 262 ms                                                                 | 265 ms: 1.01x slower                                                |
| sympy_str                        | 272 ms                                                                 | 275 ms: 1.01x slower                                                |
| logging_simple                   | 5.67 us                                                                | 5.74 us: 1.01x slower                                               |
| shortest_path                    | 487 ms                                                                 | 493 ms: 1.01x slower                                                |
| async_tree_io                    | 599 ms                                                                 | 607 ms: 1.01x slower                                                |
| deepcopy                         | 256 us                                                                 | 260 us: 1.01x slower                                                |
| genshi_text                      | 21.3 ms                                                                | 21.5 ms: 1.01x slower                                               |
| sqlglot_v2_normalize             | 106 ms                                                                 | 108 ms: 1.01x slower                                                |
| chaos                            | 60.3 ms                                                                | 61.1 ms: 1.01x slower                                               |
| sqlglot_v2_optimize              | 53.5 ms                                                                | 54.2 ms: 1.01x slower                                               |
| sqlalchemy_imperative            | 17.5 ms                                                                | 17.8 ms: 1.01x slower                                               |
| nqueens                          | 82.6 ms                                                                | 83.7 ms: 1.01x slower                                               |
| async_tree_memoization_tg        | 310 ms                                                                 | 315 ms: 1.01x slower                                                |
| sympy_expand                     | 474 ms                                                                 | 481 ms: 1.02x slower                                                |
| async_tree_eager                 | 103 ms                                                                 | 104 ms: 1.02x slower                                                |
| subparsers                       | 22.5 ms                                                                | 22.9 ms: 1.02x slower                                               |
| many_optionals                   | 976 us                                                                 | 994 us: 1.02x slower                                                |
| async_tree_eager_io_tg           | 630 ms                                                                 | 642 ms: 1.02x slower                                                |
| async_tree_memoization           | 313 ms                                                                 | 319 ms: 1.02x slower                                                |
| deepcopy_reduce                  | 2.69 us                                                                | 2.74 us: 1.02x slower                                               |
| scimark_sor                      | 120 ms                                                                 | 122 ms: 1.02x slower                                                |
| async_tree_eager_io              | 620 ms                                                                 | 632 ms: 1.02x slower                                                |
| json_dumps                       | 11.8 ms                                                                | 12.1 ms: 1.02x slower                                               |
| sqlglot_v2_transpile             | 1.57 ms                                                                | 1.61 ms: 1.02x slower                                               |
| async_tree_eager_tg              | 211 ms                                                                 | 216 ms: 1.02x slower                                                |
| async_tree_eager_memoization_tg  | 277 ms                                                                 | 283 ms: 1.02x slower                                                |
| regex_compile                    | 126 ms                                                                 | 130 ms: 1.02x slower                                                |
| django_template                  | 32.1 ms                                                                | 32.9 ms: 1.03x slower                                               |
| typing_runtime_protocols         | 170 us                                                                 | 175 us: 1.03x slower                                                |
| bpe_tokeniser                    | 4.38 sec                                                               | 4.50 sec: 1.03x slower                                              |
| dulwich_log                      | 60.7 ms                                                                | 62.5 ms: 1.03x slower                                               |
| k_core                           | 2.29 sec                                                               | 2.35 sec: 1.03x slower                                              |
| sqlglot_v2_parse                 | 1.25 ms                                                                | 1.29 ms: 1.03x slower                                               |
| xml_etree_generate               | 81.2 ms                                                                | 83.8 ms: 1.03x slower                                               |
| connected_components             | 444 ms                                                                 | 459 ms: 1.03x slower                                                |
| raytrace                         | 272 ms                                                                 | 282 ms: 1.03x slower                                                |
| comprehensions                   | 18.0 us                                                                | 18.7 us: 1.04x slower                                               |
| pidigits                         | 188 ms                                                                 | 195 ms: 1.04x slower                                                |
| mdp                              | 1.24 sec                                                               | 1.29 sec: 1.04x slower                                              |
| pickle_pure_python               | 321 us                                                                 | 335 us: 1.04x slower                                                |
| mako                             | 11.2 ms                                                                | 11.7 ms: 1.04x slower                                               |
| telco                            | 7.82 ms                                                                | 8.21 ms: 1.05x slower                                               |
| deepcopy_memo                    | 29.3 us                                                                | 30.8 us: 1.05x slower                                               |
| xml_etree_process                | 55.7 ms                                                                | 58.7 ms: 1.05x slower                                               |
| crypto_pyaes                     | 75.7 ms                                                                | 80.0 ms: 1.06x slower                                               |
| scimark_monte_carlo              | 67.5 ms                                                                | 71.6 ms: 1.06x slower                                               |
| hexiom                           | 6.61 ms                                                                | 7.08 ms: 1.07x slower                                               |
| float                            | 64.6 ms                                                                | 69.4 ms: 1.07x slower                                               |
| pyflate                          | 430 ms                                                                 | 462 ms: 1.07x slower                                                |
| go                               | 125 ms                                                                 | 135 ms: 1.08x slower                                                |
| nbody                            | 92.2 ms                                                                | 99.3 ms: 1.08x slower                                               |
| fannkuch                         | 404 ms                                                                 | 437 ms: 1.08x slower                                                |
| pprint_pformat                   | 1.56 sec                                                               | 1.69 sec: 1.08x slower                                              |
| tomli_loads                      | 1.90 sec                                                               | 2.06 sec: 1.08x slower                                              |
| pprint_safe_repr                 | 750 ms                                                                 | 820 ms: 1.09x slower                                                |
| richards_super                   | 40.1 ms                                                                | 43.8 ms: 1.09x slower                                               |
| richards                         | 35.0 ms                                                                | 38.5 ms: 1.10x slower                                               |
| scimark_fft                      | 328 ms                                                                 | 362 ms: 1.10x slower                                                |
| unpickle_pure_python             | 208 us                                                                 | 234 us: 1.12x slower                                                |
| scimark_sparse_mat_mult          | 5.07 ms                                                                | 5.79 ms: 1.14x slower                                               |
| deltablue                        | 3.05 ms                                                                | 3.55 ms: 1.16x slower                                               |
| spectral_norm                    | 100 ms                                                                 | 118 ms: 1.18x slower                                                |
| Geometric mean                   | (ref)                                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (16): coroutines, generators, bench_thread_pool, pathlib, asyncio_websockets, coverage, json, logging_silent, xml_etree_parse, genshi_xml, async_tree_io_tg, async_tree_none_tg, pylint, async_tree_none, sphinx, pycparser

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.99x