# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                               |
| docutils       | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                             |
| html5lib       | 73.5 ms                                                      | 67.8 ms: 1.08x faster                                                              |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 342 ms: 1.36x faster                                                               |
| async_tree_io              | 843 ms                                                       | 647 ms: 1.30x faster                                                               |
| async_tree_io_tg           | 831 ms                                                       | 641 ms: 1.30x faster                                                               |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                               |
| async_tree_memoization     | 453 ms                                                       | 355 ms: 1.28x faster                                                               |
| async_tree_none_tg         | 346 ms                                                       | 283 ms: 1.22x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 513 ms: 1.13x faster                                                               |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                              |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                               |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.0 ms: 1.16x faster                                                              |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                              |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                               |
| regex_dna      | 247 ms                                                       | 243 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.00 sec: 1.23x faster                                                             |
| xml_etree_process    | 61.2 ms                                                      | 55.7 ms: 1.10x faster                                                              |
| unpickle_pure_python | 217 us                                                       | 198 us: 1.10x faster                                                               |
| xml_etree_generate   | 86.5 ms                                                      | 79.1 ms: 1.09x faster                                                              |
| xml_etree_parse      | 150 ms                                                       | 141 ms: 1.07x faster                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 97.3 ms: 1.06x faster                                                              |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.02x slower                                                               |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                              |
| json_loads           | 24.7 us                                                      | 26.5 us: 1.08x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.04 ms: 1.01x slower                                                              |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako           | 10.4 ms                                                      | 9.40 ms: 1.10x faster                                                              |
| genshi_text    | 26.2 ms                                                      | 23.8 ms: 1.10x faster                                                              |
| genshi_xml     | 57.1 ms                                                      | 54.3 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                               |
| async_tree_memoization_tg  | 466 ms                                                       | 342 ms: 1.36x faster                                                               |
| deepcopy_memo              | 38.6 us                                                      | 29.5 us: 1.31x faster                                                              |
| async_tree_io              | 843 ms                                                       | 647 ms: 1.30x faster                                                               |
| async_tree_io_tg           | 831 ms                                                       | 641 ms: 1.30x faster                                                               |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                               |
| async_tree_memoization     | 453 ms                                                       | 355 ms: 1.28x faster                                                               |
| tomli_loads                | 2.46 sec                                                     | 2.00 sec: 1.23x faster                                                             |
| async_tree_none_tg         | 346 ms                                                       | 283 ms: 1.22x faster                                                               |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                              |
| pyflate                    | 503 ms                                                       | 425 ms: 1.18x faster                                                               |
| generators                 | 33.6 ms                                                      | 28.7 ms: 1.17x faster                                                              |
| regex_effbot               | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                                              |
| richards                   | 52.9 ms                                                      | 45.5 ms: 1.16x faster                                                              |
| float                      | 81.3 ms                                                      | 70.0 ms: 1.16x faster                                                              |
| telco                      | 8.79 ms                                                      | 7.59 ms: 1.16x faster                                                              |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                               |
| richards_super             | 59.6 ms                                                      | 51.6 ms: 1.15x faster                                                              |
| spectral_norm              | 97.0 ms                                                      | 84.3 ms: 1.15x faster                                                              |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 513 ms: 1.13x faster                                                               |
| go                         | 162 ms                                                       | 143 ms: 1.13x faster                                                               |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 4.60 sec: 1.11x faster                                                             |
| mako                       | 10.4 ms                                                      | 9.40 ms: 1.10x faster                                                              |
| genshi_text                | 26.2 ms                                                      | 23.8 ms: 1.10x faster                                                              |
| xml_etree_process          | 61.2 ms                                                      | 55.7 ms: 1.10x faster                                                              |
| unpickle_pure_python       | 217 us                                                       | 198 us: 1.10x faster                                                               |
| xml_etree_generate         | 86.5 ms                                                      | 79.1 ms: 1.09x faster                                                              |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                               |
| pprint_pformat             | 1.72 sec                                                     | 1.59 sec: 1.08x faster                                                             |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.0 ms: 1.08x faster                                                              |
| html5lib                   | 73.5 ms                                                      | 67.8 ms: 1.08x faster                                                              |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                               |
| pprint_safe_repr           | 843 ms                                                       | 783 ms: 1.08x faster                                                               |
| connected_components       | 432 ms                                                       | 402 ms: 1.07x faster                                                               |
| pathlib                    | 17.5 ms                                                      | 16.4 ms: 1.07x faster                                                              |
| k_core                     | 2.17 sec                                                     | 2.03 sec: 1.07x faster                                                             |
| xml_etree_parse            | 150 ms                                                       | 141 ms: 1.07x faster                                                               |
| shortest_path              | 460 ms                                                       | 430 ms: 1.07x faster                                                               |
| thrift                     | 901 us                                                       | 851 us: 1.06x faster                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 97.3 ms: 1.06x faster                                                              |
| genshi_xml                 | 57.1 ms                                                      | 54.3 ms: 1.05x faster                                                              |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                               |
| sqlite_synth               | 2.91 us                                                      | 2.79 us: 1.04x faster                                                              |
| json                       | 5.69 ms                                                      | 5.46 ms: 1.04x faster                                                              |
| pycparser                  | 1.24 sec                                                     | 1.20 sec: 1.04x faster                                                             |
| sqlglot_parse              | 1.40 ms                                                      | 1.36 ms: 1.03x faster                                                              |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                              |
| logging_simple             | 6.39 us                                                      | 6.23 us: 1.03x faster                                                              |
| dulwich_log                | 68.2 ms                                                      | 66.6 ms: 1.02x faster                                                              |
| sqlalchemy_declarative     | 148 ms                                                       | 145 ms: 1.02x faster                                                               |
| sqlglot_transpile          | 1.79 ms                                                      | 1.75 ms: 1.02x faster                                                              |
| scimark_lu                 | 98.7 ms                                                      | 96.6 ms: 1.02x faster                                                              |
| logging_format             | 6.94 us                                                      | 6.80 us: 1.02x faster                                                              |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                               |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                               |
| coverage                   | 80.0 ms                                                      | 78.5 ms: 1.02x faster                                                              |
| regex_dna                  | 247 ms                                                       | 243 ms: 1.02x faster                                                               |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                             |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.1 ms: 1.01x faster                                                              |
| sympy_expand               | 509 ms                                                       | 505 ms: 1.01x faster                                                               |
| sympy_str                  | 298 ms                                                       | 296 ms: 1.01x faster                                                               |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                               |
| sympy_sum                  | 155 ms                                                       | 154 ms: 1.00x faster                                                               |
| sympy_integrate            | 23.6 ms                                                      | 23.6 ms: 1.00x slower                                                              |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                               |
| sqlglot_optimize           | 59.3 ms                                                      | 59.7 ms: 1.01x slower                                                              |
| python_startup_no_site     | 8.96 ms                                                      | 9.04 ms: 1.01x slower                                                              |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                              |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                               |
| crypto_pyaes               | 73.3 ms                                                      | 74.5 ms: 1.02x slower                                                              |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.02x slower                                                               |
| mdp                        | 2.54 sec                                                     | 2.58 sec: 1.02x slower                                                             |
| bench_thread_pool          | 942 us                                                       | 961 us: 1.02x slower                                                               |
| chaos                      | 60.2 ms                                                      | 61.7 ms: 1.02x slower                                                              |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.02x slower                                                               |
| create_gc_cycles           | 2.68 ms                                                      | 2.75 ms: 1.03x slower                                                              |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.92 ms: 1.03x slower                                                              |
| fannkuch                   | 363 ms                                                       | 374 ms: 1.03x slower                                                               |
| hexiom                     | 6.55 ms                                                      | 6.80 ms: 1.04x slower                                                              |
| docutils                   | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                             |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                              |
| raytrace                   | 273 ms                                                       | 292 ms: 1.07x slower                                                               |
| nqueens                    | 90.7 ms                                                      | 97.4 ms: 1.07x slower                                                              |
| json_loads                 | 24.7 us                                                      | 26.5 us: 1.08x slower                                                              |
| comprehensions             | 17.0 us                                                      | 18.5 us: 1.09x slower                                                              |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.10x slower                                                              |
| subparsers                 | 17.5 ms                                                      | 23.1 ms: 1.32x slower                                                              |
| gc_traversal               | 4.74 ms                                                      | 6.52 ms: 1.37x slower                                                              |
| bench_mp_pool              | 5.12 ms                                                      | 1.63 sec: 318.42x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                       |

Benchmark hidden because not significant (6): django_template, asyncio_websockets, logging_silent, deltablue, nbody, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x