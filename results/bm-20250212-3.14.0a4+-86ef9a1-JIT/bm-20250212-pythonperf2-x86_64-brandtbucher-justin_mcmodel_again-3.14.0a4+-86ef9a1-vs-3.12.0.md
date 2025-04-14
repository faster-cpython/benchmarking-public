# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.039x faster
- HPT reliability: 99.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                               |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 641 ms: 1.64x faster                                                               |
| async_tree_io              | 1.04 sec                                                     | 647 ms: 1.61x faster                                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 342 ms: 1.58x faster                                                               |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                               |
| async_tree_memoization     | 544 ms                                                       | 355 ms: 1.53x faster                                                               |
| async_tree_none_tg         | 431 ms                                                       | 283 ms: 1.52x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 513 ms: 1.36x faster                                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                               |
| Geometric mean             | (ref)                                                        | 1.51x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.0 ms: 1.09x faster                                                              |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                               |
| nbody          | 88.0 ms                                                      | 89.9 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                              |
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                               |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                               |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.14x slower                                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.1 ms: 1.09x faster                                                              |
| tomli_loads          | 2.16 sec                                                     | 2.00 sec: 1.08x faster                                                             |
| unpickle_pure_python | 210 us                                                       | 198 us: 1.06x faster                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 97.3 ms: 1.06x faster                                                              |
| xml_etree_process    | 58.4 ms                                                      | 55.7 ms: 1.05x faster                                                              |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                               |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                               |
| json_loads           | 24.4 us                                                      | 26.5 us: 1.09x slower                                                              |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                              |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.40 ms: 1.06x faster                                                              |
| django_template | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                                              |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 641 ms: 1.64x faster                                                               |
| async_tree_io              | 1.04 sec                                                     | 647 ms: 1.61x faster                                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 342 ms: 1.58x faster                                                               |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                               |
| async_tree_memoization     | 544 ms                                                       | 355 ms: 1.53x faster                                                               |
| async_tree_none_tg         | 431 ms                                                       | 283 ms: 1.52x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 513 ms: 1.36x faster                                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                               |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                               |
| generators                 | 37.4 ms                                                      | 28.7 ms: 1.30x faster                                                              |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                                              |
| comprehensions             | 21.9 us                                                      | 18.5 us: 1.18x faster                                                              |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.16x faster                                                              |
| pathlib                    | 18.9 ms                                                      | 16.4 ms: 1.15x faster                                                              |
| regex_effbot               | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                              |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.0 ms: 1.13x faster                                                              |
| logging_format             | 7.48 us                                                      | 6.80 us: 1.10x faster                                                              |
| sqlalchemy_declarative     | 159 ms                                                       | 145 ms: 1.10x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                              |
| float                      | 76.6 ms                                                      | 70.0 ms: 1.09x faster                                                              |
| xml_etree_generate         | 86.1 ms                                                      | 79.1 ms: 1.09x faster                                                              |
| spectral_norm              | 91.6 ms                                                      | 84.3 ms: 1.09x faster                                                              |
| tomli_loads                | 2.16 sec                                                     | 2.00 sec: 1.08x faster                                                             |
| crypto_pyaes               | 80.3 ms                                                      | 74.5 ms: 1.08x faster                                                              |
| logging_simple             | 6.71 us                                                      | 6.23 us: 1.08x faster                                                              |
| mako                       | 10.0 ms                                                      | 9.40 ms: 1.06x faster                                                              |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                               |
| unpickle_pure_python       | 210 us                                                       | 198 us: 1.06x faster                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 97.3 ms: 1.06x faster                                                              |
| django_template            | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                                              |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                               |
| xml_etree_process          | 58.4 ms                                                      | 55.7 ms: 1.05x faster                                                              |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.59 sec: 1.04x faster                                                             |
| go                         | 150 ms                                                       | 143 ms: 1.04x faster                                                               |
| chaos                      | 64.0 ms                                                      | 61.7 ms: 1.04x faster                                                              |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.1 ms: 1.04x faster                                                              |
| pycparser                  | 1.23 sec                                                     | 1.20 sec: 1.03x faster                                                             |
| pyflate                    | 439 ms                                                       | 425 ms: 1.03x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 783 ms: 1.03x faster                                                               |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                               |
| scimark_lu                 | 98.8 ms                                                      | 96.6 ms: 1.02x faster                                                              |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                               |
| raytrace                   | 298 ms                                                       | 292 ms: 1.02x faster                                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.36 ms: 1.01x faster                                                              |
| sqlglot_transpile          | 1.78 ms                                                      | 1.75 ms: 1.01x faster                                                              |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                              |
| richards_super             | 51.3 ms                                                      | 51.6 ms: 1.01x slower                                                              |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.01x slower                                                             |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                               |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                               |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                               |
| dulwich_log                | 65.4 ms                                                      | 66.6 ms: 1.02x slower                                                              |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                               |
| nbody                      | 88.0 ms                                                      | 89.9 ms: 1.02x slower                                                              |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                             |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                               |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.03x slower                                                               |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                                              |
| sqlglot_optimize           | 57.5 ms                                                      | 59.7 ms: 1.04x slower                                                              |
| sympy_expand               | 484 ms                                                       | 505 ms: 1.04x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                              |
| deltablue                  | 3.24 ms                                                      | 3.42 ms: 1.06x slower                                                              |
| json                       | 5.12 ms                                                      | 5.46 ms: 1.07x slower                                                              |
| fannkuch                   | 350 ms                                                       | 374 ms: 1.07x slower                                                               |
| nqueens                    | 89.9 ms                                                      | 97.4 ms: 1.08x slower                                                              |
| json_loads                 | 24.4 us                                                      | 26.5 us: 1.09x slower                                                              |
| telco                      | 6.96 ms                                                      | 7.59 ms: 1.09x slower                                                              |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                               |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.14x slower                                                              |
| hexiom                     | 5.96 ms                                                      | 6.80 ms: 1.14x slower                                                              |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                              |
| async_generators           | 390 ms                                                       | 448 ms: 1.15x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.92 ms: 1.17x slower                                                              |
| coverage                   | 66.7 ms                                                      | 78.5 ms: 1.18x slower                                                              |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                              |
| create_gc_cycles           | 1.59 ms                                                      | 2.75 ms: 1.73x slower                                                              |
| gc_traversal               | 3.48 ms                                                      | 6.52 ms: 1.87x slower                                                              |
| bench_mp_pool              | 4.76 ms                                                      | 1.63 sec: 342.38x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                       |

Benchmark hidden because not significant (4): richards, asyncio_websockets, sqlite_synth, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.35% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x