# Results vs. base

- fork: brandtbucher
- ref: trace_load_attr_prop
- machine: linux-x86_64
- commit hash: 9b7a6a6
- commit date: 2025-02-07
- overall geometric mean: 1.001x slower
- HPT reliability: 68.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                 | 259 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization    | 327 ms                                                                 | 329 ms: 1.01x slower                                                         |
| async_tree_memoization_tg | 317 ms                                                                 | 320 ms: 1.01x slower                                                         |
| async_tree_none_tg        | 257 ms                                                                 | 260 ms: 1.01x slower                                                         |
| coroutines                | 22.8 ms                                                                | 23.5 ms: 1.03x slower                                                        |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (7): async_generators, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 93.9 ms                                                                | 96.5 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                         |
| regex_dna      | 208 ms                                                                 | 212 ms: 1.02x slower                                                         |
| regex_effbot   | 3.17 ms                                                                | 3.24 ms: 1.02x slower                                                        |
| regex_v8       | 23.7 ms                                                                | 24.4 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps          | 11.9 ms                                                                | 11.6 ms: 1.02x faster                                                        |
| xml_etree_iterparse | 95.5 ms                                                                | 96.1 ms: 1.01x slower                                                        |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (7): xml_etree_generate, xml_etree_process, tomli_loads, xml_etree_parse, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.07 ms                                                                | 7.07 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 32.6 ms                                                                | 32.1 ms: 1.02x faster                                                        |
| mako            | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                        |
| genshi_text     | 21.8 ms                                                                | 22.2 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| richards_super            | 51.4 ms                                                                | 49.8 ms: 1.03x faster                                                        |
| go                        | 122 ms                                                                 | 118 ms: 1.03x faster                                                         |
| richards                  | 45.0 ms                                                                | 43.8 ms: 1.03x faster                                                        |
| thrift                    | 775 us                                                                 | 756 us: 1.03x faster                                                         |
| spectral_norm             | 96.1 ms                                                                | 93.9 ms: 1.02x faster                                                        |
| json_dumps                | 11.9 ms                                                                | 11.6 ms: 1.02x faster                                                        |
| logging_silent            | 109 ns                                                                 | 107 ns: 1.02x faster                                                         |
| sqlalchemy_imperative     | 17.0 ms                                                                | 16.7 ms: 1.02x faster                                                        |
| django_template           | 32.6 ms                                                                | 32.1 ms: 1.02x faster                                                        |
| logging_simple            | 5.63 us                                                                | 5.54 us: 1.02x faster                                                        |
| deepcopy                  | 262 us                                                                 | 259 us: 1.01x faster                                                         |
| many_optionals            | 956 us                                                                 | 945 us: 1.01x faster                                                         |
| sympy_str                 | 276 ms                                                                 | 273 ms: 1.01x faster                                                         |
| deepcopy_memo             | 30.8 us                                                                | 30.4 us: 1.01x faster                                                        |
| logging_format            | 6.23 us                                                                | 6.16 us: 1.01x faster                                                        |
| sqlite_synth              | 2.75 us                                                                | 2.72 us: 1.01x faster                                                        |
| subparsers                | 20.6 ms                                                                | 20.4 ms: 1.01x faster                                                        |
| sympy_expand              | 472 ms                                                                 | 467 ms: 1.01x faster                                                         |
| regex_compile             | 126 ms                                                                 | 125 ms: 1.01x faster                                                         |
| deltablue                 | 3.28 ms                                                                | 3.26 ms: 1.01x faster                                                        |
| sqlalchemy_declarative    | 132 ms                                                                 | 131 ms: 1.01x faster                                                         |
| mdp                       | 2.56 sec                                                               | 2.55 sec: 1.00x faster                                                       |
| raytrace                  | 274 ms                                                                 | 273 ms: 1.00x faster                                                         |
| pathlib                   | 15.9 ms                                                                | 15.9 ms: 1.00x faster                                                        |
| 2to3                      | 260 ms                                                                 | 259 ms: 1.00x faster                                                         |
| bench_thread_pool         | 889 us                                                                 | 886 us: 1.00x faster                                                         |
| pidigits                  | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| python_startup_no_site    | 7.07 ms                                                                | 7.07 ms: 1.00x slower                                                        |
| create_gc_cycles          | 2.46 ms                                                                | 2.46 ms: 1.00x slower                                                        |
| mako                      | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                        |
| connected_components      | 439 ms                                                                 | 442 ms: 1.01x slower                                                         |
| async_tree_memoization    | 327 ms                                                                 | 329 ms: 1.01x slower                                                         |
| xml_etree_iterparse       | 95.5 ms                                                                | 96.1 ms: 1.01x slower                                                        |
| shortest_path             | 482 ms                                                                 | 485 ms: 1.01x slower                                                         |
| scimark_fft               | 310 ms                                                                 | 313 ms: 1.01x slower                                                         |
| sqlglot_transpile         | 1.59 ms                                                                | 1.61 ms: 1.01x slower                                                        |
| chaos                     | 58.5 ms                                                                | 59.1 ms: 1.01x slower                                                        |
| deepcopy_reduce           | 2.66 us                                                                | 2.69 us: 1.01x slower                                                        |
| async_tree_memoization_tg | 317 ms                                                                 | 320 ms: 1.01x slower                                                         |
| scimark_lu                | 114 ms                                                                 | 115 ms: 1.01x slower                                                         |
| hexiom                    | 6.62 ms                                                                | 6.70 ms: 1.01x slower                                                        |
| async_tree_none_tg        | 257 ms                                                                 | 260 ms: 1.01x slower                                                         |
| comprehensions            | 17.1 us                                                                | 17.3 us: 1.01x slower                                                        |
| telco                     | 7.60 ms                                                                | 7.71 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult   | 4.47 ms                                                                | 4.53 ms: 1.01x slower                                                        |
| json                      | 5.19 ms                                                                | 5.27 ms: 1.02x slower                                                        |
| regex_dna                 | 208 ms                                                                 | 212 ms: 1.02x slower                                                         |
| genshi_text               | 21.8 ms                                                                | 22.2 ms: 1.02x slower                                                        |
| regex_effbot              | 3.17 ms                                                                | 3.24 ms: 1.02x slower                                                        |
| coverage                  | 89.6 ms                                                                | 91.3 ms: 1.02x slower                                                        |
| generators                | 28.1 ms                                                                | 28.7 ms: 1.02x slower                                                        |
| scimark_monte_carlo       | 65.5 ms                                                                | 67.0 ms: 1.02x slower                                                        |
| coroutines                | 22.8 ms                                                                | 23.5 ms: 1.03x slower                                                        |
| nbody                     | 93.9 ms                                                                | 96.5 ms: 1.03x slower                                                        |
| regex_v8                  | 23.7 ms                                                                | 24.4 ms: 1.03x slower                                                        |
| pprint_pformat            | 1.53 sec                                                               | 1.58 sec: 1.03x slower                                                       |
| gc_traversal              | 4.58 ms                                                                | 4.76 ms: 1.04x slower                                                        |
| pyflate                   | 436 ms                                                                 | 462 ms: 1.06x slower                                                         |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (37): pylint, bench_mp_pool, docutils, html5lib, float, async_generators, k_core, dulwich_log, scimark_sor, sympy_integrate, fannkuch, sqlglot_normalize, sphinx, sqlglot_optimize, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, xml_etree_generate, sympy_sum, async_tree_io, async_tree_none, typing_runtime_protocols, crypto_pyaes, sqlglot_parse, meteor_contest, xml_etree_process, bpe_tokeniser, genshi_xml, tomli_loads, xml_etree_parse, unpickle_pure_python, pycparser, async_tree_io_tg, json_loads, pprint_safe_repr, nqueens, pickle_pure_python

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 68.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x