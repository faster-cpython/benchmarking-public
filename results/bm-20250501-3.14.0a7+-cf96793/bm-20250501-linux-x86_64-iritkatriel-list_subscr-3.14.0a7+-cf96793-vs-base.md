# Results vs. base

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: cf96793
- commit date: 2025-05-01
- overall geometric mean: 1.005x slower
- HPT reliability: 88.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250501-linux-x86_64-python-3831752689f4a43c2674-3.14.0a7+-3831752 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 255 ms: 1.01x slower                                               |
| docutils       | 2.62 sec                                                               | 2.61 sec: 1.00x faster                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250501-linux-x86_64-python-3831752689f4a43c2674-3.14.0a7+-3831752 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager                 | 104 ms                                                                 | 102 ms: 1.01x faster                                               |
| async_tree_memoization           | 316 ms                                                                 | 313 ms: 1.01x faster                                               |
| async_tree_memoization_tg        | 310 ms                                                                 | 307 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg       | 491 ms                                                                 | 494 ms: 1.01x slower                                               |
| async_tree_eager_io_tg           | 612 ms                                                                 | 617 ms: 1.01x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 462 ms                                                                 | 466 ms: 1.01x slower                                               |
| async_generators                 | 406 ms                                                                 | 409 ms: 1.01x slower                                               |
| coroutines                       | 25.0 ms                                                                | 26.3 ms: 1.05x slower                                              |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (11): async_tree_eager_memoization, async_tree_none_tg, async_tree_none, async_tree_eager_memoization_tg, async_tree_io_tg, asyncio_websockets, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_io, async_tree_eager_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250501-linux-x86_64-python-3831752689f4a43c2674-3.14.0a7+-3831752 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                               |
| nbody          | 95.8 ms                                                                | 97.7 ms: 1.02x slower                                              |
| float          | 69.1 ms                                                                | 72.0 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250501-linux-x86_64-python-3831752689f4a43c2674-3.14.0a7+-3831752 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 211 ms                                                                 | 208 ms: 1.01x faster                                               |
| regex_effbot   | 3.37 ms                                                                | 3.34 ms: 1.01x faster                                              |
| regex_compile  | 127 ms                                                                 | 128 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250501-linux-x86_64-python-3831752689f4a43c2674-3.14.0a7+-3831752 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 147 ms                                                                 | 142 ms: 1.03x faster                                               |
| xml_etree_process    | 59.8 ms                                                                | 59.3 ms: 1.01x faster                                              |
| xml_etree_iterparse  | 101 ms                                                                 | 100 ms: 1.01x faster                                               |
| xml_etree_generate   | 85.4 ms                                                                | 85.0 ms: 1.00x faster                                              |
| json_loads           | 30.3 us                                                                | 30.5 us: 1.01x slower                                              |
| unpickle_pure_python | 217 us                                                                 | 219 us: 1.01x slower                                               |
| json_dumps           | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                              |
| tomli_loads          | 1.99 sec                                                               | 2.08 sec: 1.04x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250501-linux-x86_64-python-3831752689f4a43c2674-3.14.0a7+-3831752 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                              |
| python_startup_no_site | 6.92 ms                                                                | 6.94 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250501-linux-x86_64-python-3831752689f4a43c2674-3.14.0a7+-3831752 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 49.4 ms                                                                | 49.2 ms: 1.01x faster                                              |
| mako            | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                              |
| django_template | 32.1 ms                                                                | 32.5 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20250501-linux-x86_64-python-3831752689f4a43c2674-3.14.0a7+-3831752 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| gc_traversal                     | 4.99 ms                                                                | 4.79 ms: 1.04x faster                                              |
| xml_etree_parse                  | 147 ms                                                                 | 142 ms: 1.03x faster                                               |
| subparsers                       | 21.1 ms                                                                | 20.8 ms: 1.01x faster                                              |
| logging_silent                   | 95.0 ns                                                                | 93.6 ns: 1.01x faster                                              |
| typing_runtime_protocols         | 167 us                                                                 | 165 us: 1.01x faster                                               |
| async_tree_eager                 | 104 ms                                                                 | 102 ms: 1.01x faster                                               |
| deepcopy                         | 258 us                                                                 | 255 us: 1.01x faster                                               |
| regex_dna                        | 211 ms                                                                 | 208 ms: 1.01x faster                                               |
| async_tree_memoization           | 316 ms                                                                 | 313 ms: 1.01x faster                                               |
| regex_effbot                     | 3.37 ms                                                                | 3.34 ms: 1.01x faster                                              |
| chaos                            | 59.9 ms                                                                | 59.3 ms: 1.01x faster                                              |
| async_tree_memoization_tg        | 310 ms                                                                 | 307 ms: 1.01x faster                                               |
| xml_etree_process                | 59.8 ms                                                                | 59.3 ms: 1.01x faster                                              |
| json                             | 5.51 ms                                                                | 5.45 ms: 1.01x faster                                              |
| sqlalchemy_imperative            | 17.4 ms                                                                | 17.2 ms: 1.01x faster                                              |
| pprint_safe_repr                 | 732 ms                                                                 | 727 ms: 1.01x faster                                               |
| xml_etree_iterparse              | 101 ms                                                                 | 100 ms: 1.01x faster                                               |
| sqlglot_v2_normalize             | 107 ms                                                                 | 107 ms: 1.01x faster                                               |
| genshi_xml                       | 49.4 ms                                                                | 49.2 ms: 1.01x faster                                              |
| meteor_contest                   | 108 ms                                                                 | 107 ms: 1.01x faster                                               |
| mdp                              | 1.24 sec                                                               | 1.24 sec: 1.00x faster                                             |
| pprint_pformat                   | 1.49 sec                                                               | 1.49 sec: 1.00x faster                                             |
| docutils                         | 2.62 sec                                                               | 2.61 sec: 1.00x faster                                             |
| xml_etree_generate               | 85.4 ms                                                                | 85.0 ms: 1.00x faster                                              |
| create_gc_cycles                 | 2.49 ms                                                                | 2.48 ms: 1.00x faster                                              |
| sqlalchemy_declarative           | 133 ms                                                                 | 132 ms: 1.00x faster                                               |
| nqueens                          | 81.9 ms                                                                | 81.8 ms: 1.00x faster                                              |
| many_optionals                   | 932 us                                                                 | 931 us: 1.00x faster                                               |
| pidigits                         | 187 ms                                                                 | 187 ms: 1.00x faster                                               |
| python_startup                   | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                              |
| python_startup_no_site           | 6.92 ms                                                                | 6.94 ms: 1.00x slower                                              |
| bench_thread_pool                | 888 us                                                                 | 892 us: 1.00x slower                                               |
| regex_compile                    | 127 ms                                                                 | 128 ms: 1.00x slower                                               |
| json_loads                       | 30.3 us                                                                | 30.5 us: 1.01x slower                                              |
| generators                       | 29.5 ms                                                                | 29.7 ms: 1.01x slower                                              |
| mako                             | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                              |
| dulwich_log                      | 59.4 ms                                                                | 59.8 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg       | 491 ms                                                                 | 494 ms: 1.01x slower                                               |
| coverage                         | 92.5 ms                                                                | 93.2 ms: 1.01x slower                                              |
| async_tree_eager_io_tg           | 612 ms                                                                 | 617 ms: 1.01x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 462 ms                                                                 | 466 ms: 1.01x slower                                               |
| async_generators                 | 406 ms                                                                 | 409 ms: 1.01x slower                                               |
| unpickle_pure_python             | 217 us                                                                 | 219 us: 1.01x slower                                               |
| scimark_sor                      | 120 ms                                                                 | 122 ms: 1.01x slower                                               |
| json_dumps                       | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                              |
| 2to3                             | 253 ms                                                                 | 255 ms: 1.01x slower                                               |
| scimark_monte_carlo              | 67.5 ms                                                                | 68.2 ms: 1.01x slower                                              |
| deltablue                        | 3.32 ms                                                                | 3.36 ms: 1.01x slower                                              |
| go                               | 111 ms                                                                 | 113 ms: 1.01x slower                                               |
| bpe_tokeniser                    | 4.51 sec                                                               | 4.56 sec: 1.01x slower                                             |
| richards                         | 42.8 ms                                                                | 43.3 ms: 1.01x slower                                              |
| comprehensions                   | 17.0 us                                                                | 17.2 us: 1.01x slower                                              |
| django_template                  | 32.1 ms                                                                | 32.5 ms: 1.01x slower                                              |
| pathlib                          | 17.0 ms                                                                | 17.2 ms: 1.01x slower                                              |
| sqlglot_v2_transpile             | 1.53 ms                                                                | 1.55 ms: 1.02x slower                                              |
| deepcopy_memo                    | 29.1 us                                                                | 29.6 us: 1.02x slower                                              |
| nbody                            | 95.8 ms                                                                | 97.7 ms: 1.02x slower                                              |
| crypto_pyaes                     | 75.4 ms                                                                | 77.1 ms: 1.02x slower                                              |
| logging_simple                   | 5.50 us                                                                | 5.63 us: 1.02x slower                                              |
| hexiom                           | 6.23 ms                                                                | 6.37 ms: 1.02x slower                                              |
| sqlglot_v2_parse                 | 1.22 ms                                                                | 1.24 ms: 1.02x slower                                              |
| logging_format                   | 6.10 us                                                                | 6.28 us: 1.03x slower                                              |
| fannkuch                         | 409 ms                                                                 | 424 ms: 1.04x slower                                               |
| float                            | 69.1 ms                                                                | 72.0 ms: 1.04x slower                                              |
| tomli_loads                      | 1.99 sec                                                               | 2.08 sec: 1.04x slower                                             |
| scimark_fft                      | 363 ms                                                                 | 378 ms: 1.04x slower                                               |
| spectral_norm                    | 106 ms                                                                 | 110 ms: 1.05x slower                                               |
| coroutines                       | 25.0 ms                                                                | 26.3 ms: 1.05x slower                                              |
| pyflate                          | 429 ms                                                                 | 453 ms: 1.06x slower                                               |
| scimark_sparse_mat_mult          | 4.89 ms                                                                | 5.37 ms: 1.10x slower                                              |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (33): async_tree_eager_memoization, async_tree_none_tg, scimark_lu, sqlite_synth, telco, async_tree_none, async_tree_eager_memoization_tg, raytrace, async_tree_io_tg, html5lib, asyncio_websockets, k_core, sphinx, sympy_integrate, deepcopy_reduce, async_tree_eager_cpu_io_mixed, sympy_expand, bench_mp_pool, async_tree_cpu_io_mixed, sqlglot_v2_optimize, sympy_str, sympy_sum, pycparser, shortest_path, genshi_text, async_tree_io, async_tree_eager_tg, richards_super, connected_components, async_tree_eager_io, regex_v8, pickle_pure_python, pylint

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 88.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x