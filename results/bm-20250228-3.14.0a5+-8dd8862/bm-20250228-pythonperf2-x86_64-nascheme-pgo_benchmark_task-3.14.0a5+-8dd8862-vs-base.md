# Results vs. base

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-x86_64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.020x faster
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                       | 289 ms: 1.01x slower                                                         |
| html5lib       | 68.6 ms                                                                      | 69.3 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 343 ms                                                                       | 321 ms: 1.07x faster                                                         |
| async_tree_memoization_tg  | 331 ms                                                                       | 312 ms: 1.06x faster                                                         |
| coroutines                 | 21.2 ms                                                                      | 20.0 ms: 1.06x faster                                                        |
| async_tree_none            | 282 ms                                                                       | 266 ms: 1.06x faster                                                         |
| async_tree_none_tg         | 272 ms                                                                       | 259 ms: 1.05x faster                                                         |
| async_tree_io_tg           | 639 ms                                                                       | 611 ms: 1.05x faster                                                         |
| async_tree_io              | 636 ms                                                                       | 609 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg | 500 ms                                                                       | 482 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed    | 510 ms                                                                       | 494 ms: 1.03x faster                                                         |
| async_generators           | 410 ms                                                                       | 402 ms: 1.02x faster                                                         |
| Geometric mean             | (ref)                                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 94.2 ms                                                                      | 91.2 ms: 1.03x faster                                                        |
| pidigits       | 254 ms                                                                       | 261 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.11 ms                                                                      | 2.52 ms: 1.23x faster                                                        |
| regex_dna      | 236 ms                                                                       | 192 ms: 1.23x faster                                                         |
| regex_v8       | 25.2 ms                                                                      | 24.3 ms: 1.04x faster                                                        |
| regex_compile  | 137 ms                                                                       | 138 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|---------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse     | 136 ms                                                                       | 124 ms: 1.09x faster                                                         |
| json_loads          | 25.9 us                                                                      | 24.8 us: 1.05x faster                                                        |
| xml_etree_iterparse | 95.3 ms                                                                      | 91.8 ms: 1.04x faster                                                        |
| json_dumps          | 11.5 ms                                                                      | 11.1 ms: 1.03x faster                                                        |
| xml_etree_generate  | 82.8 ms                                                                      | 80.6 ms: 1.03x faster                                                        |
| pickle_pure_python  | 333 us                                                                       | 325 us: 1.03x faster                                                         |
| xml_etree_process   | 58.6 ms                                                                      | 57.1 ms: 1.03x faster                                                        |
| tomli_loads         | 2.12 sec                                                                     | 2.18 sec: 1.03x slower                                                       |
| Geometric mean      | (ref)                                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 16.3 ms                                                                      | 16.4 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 25.0 ms                                                                      | 24.2 ms: 1.03x faster                                                        |
| django_template | 36.4 ms                                                                      | 37.2 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250226-pythonperf2-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot               | 3.11 ms                                                                      | 2.52 ms: 1.23x faster                                                        |
| regex_dna                  | 236 ms                                                                       | 192 ms: 1.23x faster                                                         |
| gc_traversal               | 6.53 ms                                                                      | 5.46 ms: 1.20x faster                                                        |
| meteor_contest             | 125 ms                                                                       | 114 ms: 1.10x faster                                                         |
| scimark_monte_carlo        | 61.9 ms                                                                      | 56.5 ms: 1.10x faster                                                        |
| xml_etree_parse            | 136 ms                                                                       | 124 ms: 1.09x faster                                                         |
| scimark_fft                | 309 ms                                                                       | 284 ms: 1.09x faster                                                         |
| telco                      | 8.23 ms                                                                      | 7.59 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult    | 4.68 ms                                                                      | 4.38 ms: 1.07x faster                                                        |
| async_tree_memoization     | 343 ms                                                                       | 321 ms: 1.07x faster                                                         |
| async_tree_memoization_tg  | 331 ms                                                                       | 312 ms: 1.06x faster                                                         |
| coroutines                 | 21.2 ms                                                                      | 20.0 ms: 1.06x faster                                                        |
| async_tree_none            | 282 ms                                                                       | 266 ms: 1.06x faster                                                         |
| async_tree_none_tg         | 272 ms                                                                       | 259 ms: 1.05x faster                                                         |
| json_loads                 | 25.9 us                                                                      | 24.8 us: 1.05x faster                                                        |
| async_tree_io_tg           | 639 ms                                                                       | 611 ms: 1.05x faster                                                         |
| deepcopy_memo              | 30.2 us                                                                      | 28.9 us: 1.05x faster                                                        |
| fannkuch                   | 361 ms                                                                       | 346 ms: 1.04x faster                                                         |
| async_tree_io              | 636 ms                                                                       | 609 ms: 1.04x faster                                                         |
| deepcopy_reduce            | 2.98 us                                                                      | 2.86 us: 1.04x faster                                                        |
| deepcopy                   | 287 us                                                                       | 276 us: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg | 500 ms                                                                       | 482 ms: 1.04x faster                                                         |
| xml_etree_iterparse        | 95.3 ms                                                                      | 91.8 ms: 1.04x faster                                                        |
| regex_v8                   | 25.2 ms                                                                      | 24.3 ms: 1.04x faster                                                        |
| generators                 | 29.2 ms                                                                      | 28.1 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 784 ms                                                                       | 757 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed    | 510 ms                                                                       | 494 ms: 1.03x faster                                                         |
| genshi_text                | 25.0 ms                                                                      | 24.2 ms: 1.03x faster                                                        |
| nbody                      | 94.2 ms                                                                      | 91.2 ms: 1.03x faster                                                        |
| json_dumps                 | 11.5 ms                                                                      | 11.1 ms: 1.03x faster                                                        |
| nqueens                    | 91.0 ms                                                                      | 88.2 ms: 1.03x faster                                                        |
| spectral_norm              | 86.4 ms                                                                      | 83.8 ms: 1.03x faster                                                        |
| raytrace                   | 282 ms                                                                       | 273 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.59 sec                                                                     | 1.54 sec: 1.03x faster                                                       |
| xml_etree_generate         | 82.8 ms                                                                      | 80.6 ms: 1.03x faster                                                        |
| richards                   | 47.5 ms                                                                      | 46.3 ms: 1.03x faster                                                        |
| pickle_pure_python         | 333 us                                                                       | 325 us: 1.03x faster                                                         |
| xml_etree_process          | 58.6 ms                                                                      | 57.1 ms: 1.03x faster                                                        |
| mdp                        | 2.49 sec                                                                     | 2.43 sec: 1.02x faster                                                       |
| go                         | 132 ms                                                                       | 129 ms: 1.02x faster                                                         |
| async_generators           | 410 ms                                                                       | 402 ms: 1.02x faster                                                         |
| bpe_tokeniser              | 4.64 sec                                                                     | 4.55 sec: 1.02x faster                                                       |
| scimark_lu                 | 96.0 ms                                                                      | 94.6 ms: 1.02x faster                                                        |
| comprehensions             | 17.1 us                                                                      | 16.8 us: 1.01x faster                                                        |
| shortest_path              | 448 ms                                                                       | 442 ms: 1.01x faster                                                         |
| pathlib                    | 16.8 ms                                                                      | 16.6 ms: 1.01x faster                                                        |
| pyflate                    | 435 ms                                                                       | 431 ms: 1.01x faster                                                         |
| logging_silent             | 98.4 ns                                                                      | 97.7 ns: 1.01x faster                                                        |
| chaos                      | 60.8 ms                                                                      | 60.5 ms: 1.01x faster                                                        |
| connected_components       | 420 ms                                                                       | 418 ms: 1.01x faster                                                         |
| many_optionals             | 1.02 ms                                                                      | 1.02 ms: 1.00x faster                                                        |
| hexiom                     | 6.05 ms                                                                      | 6.03 ms: 1.00x faster                                                        |
| python_startup             | 16.3 ms                                                                      | 16.4 ms: 1.01x slower                                                        |
| sqlalchemy_imperative      | 18.2 ms                                                                      | 18.3 ms: 1.01x slower                                                        |
| sqlalchemy_declarative     | 145 ms                                                                       | 146 ms: 1.01x slower                                                         |
| subparsers                 | 22.9 ms                                                                      | 23.1 ms: 1.01x slower                                                        |
| regex_compile              | 137 ms                                                                       | 138 ms: 1.01x slower                                                         |
| 2to3                       | 286 ms                                                                       | 289 ms: 1.01x slower                                                         |
| html5lib                   | 68.6 ms                                                                      | 69.3 ms: 1.01x slower                                                        |
| scimark_sor                | 108 ms                                                                       | 109 ms: 1.01x slower                                                         |
| dulwich_log                | 68.2 ms                                                                      | 69.2 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.78 us                                                                      | 2.82 us: 1.01x slower                                                        |
| sqlglot_optimize           | 57.8 ms                                                                      | 58.9 ms: 1.02x slower                                                        |
| django_template            | 36.4 ms                                                                      | 37.2 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                                      | 1.40 ms: 1.02x slower                                                        |
| sympy_integrate            | 23.2 ms                                                                      | 23.7 ms: 1.02x slower                                                        |
| sympy_expand               | 496 ms                                                                       | 507 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                                      | 1.80 ms: 1.02x slower                                                        |
| crypto_pyaes               | 75.8 ms                                                                      | 77.6 ms: 1.02x slower                                                        |
| logging_format             | 7.22 us                                                                      | 7.40 us: 1.02x slower                                                        |
| pidigits                   | 254 ms                                                                       | 261 ms: 1.03x slower                                                         |
| tomli_loads                | 2.12 sec                                                                     | 2.18 sec: 1.03x slower                                                       |
| sqlglot_normalize          | 117 ms                                                                       | 121 ms: 1.03x slower                                                         |
| sympy_str                  | 290 ms                                                                       | 299 ms: 1.03x slower                                                         |
| sympy_sum                  | 152 ms                                                                       | 157 ms: 1.03x slower                                                         |
| bench_thread_pool          | 960 us                                                                       | 1.00 ms: 1.04x slower                                                        |
| coverage                   | 79.8 ms                                                                      | 83.3 ms: 1.04x slower                                                        |
| json                       | 5.29 ms                                                                      | 5.65 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (18): bench_mp_pool, richards_super, thrift, docutils, sphinx, typing_runtime_protocols, asyncio_websockets, mako, python_startup_no_site, float, create_gc_cycles, genshi_xml, unpickle_pure_python, pycparser, deltablue, logging_simple, pylint, k_core

- Geometric mean (including insignificant results): 1.020x faster

# HPT report

- Reliability score: 99.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x