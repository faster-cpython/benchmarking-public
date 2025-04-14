# Results vs. 3.12.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-x86_64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.048x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 651 ms: 1.62x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 647 ms: 1.61x faster                                                                |
| async_tree_none            | 452 ms                                                       | 288 ms: 1.57x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 351 ms: 1.55x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.7 ms: 1.10x faster                                                               |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                                |
| nbody          | 88.0 ms                                                      | 89.1 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.05 ms: 1.17x faster                                                               |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                                |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 94.6 ms: 1.09x faster                                                               |
| xml_etree_parse      | 144 ms                                                       | 133 ms: 1.08x faster                                                                |
| xml_etree_generate   | 86.1 ms                                                      | 83.0 ms: 1.04x faster                                                               |
| unpickle_pure_python | 210 us                                                       | 204 us: 1.03x faster                                                                |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                              |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                                |
| json_loads           | 24.4 us                                                      | 26.1 us: 1.07x slower                                                               |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                        |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.07 ms: 1.05x slower                                                               |
| python_startup         | 11.6 ms                                                      | 16.2 ms: 1.40x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.8 ms: 1.07x faster                                                               |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 651 ms: 1.62x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 647 ms: 1.61x faster                                                                |
| async_tree_none            | 452 ms                                                       | 288 ms: 1.57x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 351 ms: 1.55x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                                |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                                |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.29x faster                                                               |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                               |
| deepcopy_memo              | 36.8 us                                                      | 29.2 us: 1.26x faster                                                               |
| regex_effbot               | 3.57 ms                                                      | 3.05 ms: 1.17x faster                                                               |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                                |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                               |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.8 ms: 1.12x faster                                                               |
| float                      | 76.6 ms                                                      | 69.7 ms: 1.10x faster                                                               |
| logging_format             | 7.48 us                                                      | 6.83 us: 1.10x faster                                                               |
| crypto_pyaes               | 80.3 ms                                                      | 73.9 ms: 1.09x faster                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 94.6 ms: 1.09x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                               |
| xml_etree_parse            | 144 ms                                                       | 133 ms: 1.08x faster                                                                |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                                |
| raytrace                   | 298 ms                                                       | 278 ms: 1.07x faster                                                                |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.5 ms: 1.07x faster                                                               |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                                |
| spectral_norm              | 91.6 ms                                                      | 85.8 ms: 1.07x faster                                                               |
| django_template            | 38.2 ms                                                      | 35.8 ms: 1.07x faster                                                               |
| logging_simple             | 6.71 us                                                      | 6.32 us: 1.06x faster                                                               |
| chaos                      | 64.0 ms                                                      | 60.6 ms: 1.06x faster                                                               |
| sympy_str                  | 302 ms                                                       | 288 ms: 1.05x faster                                                                |
| mdp                        | 2.57 sec                                                     | 2.46 sec: 1.05x faster                                                              |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 83.0 ms: 1.04x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 778 ms: 1.04x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                               |
| scimark_lu                 | 98.8 ms                                                      | 95.9 ms: 1.03x faster                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                              |
| bench_thread_pool          | 950 us                                                       | 925 us: 1.03x faster                                                                |
| unpickle_pure_python       | 210 us                                                       | 204 us: 1.03x faster                                                                |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                              |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.02x faster                                                                |
| sqlglot_optimize           | 57.5 ms                                                      | 56.3 ms: 1.02x faster                                                               |
| sqlglot_transpile          | 1.78 ms                                                      | 1.74 ms: 1.02x faster                                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.36 ms: 1.02x faster                                                               |
| nqueens                    | 89.9 ms                                                      | 88.6 ms: 1.01x faster                                                               |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.01x faster                                                                |
| sympy_expand               | 484 ms                                                       | 489 ms: 1.01x slower                                                                |
| nbody                      | 88.0 ms                                                      | 89.1 ms: 1.01x slower                                                               |
| dulwich_log                | 65.4 ms                                                      | 66.5 ms: 1.02x slower                                                               |
| logging_silent             | 94.4 ns                                                      | 96.3 ns: 1.02x slower                                                               |
| richards_super             | 51.3 ms                                                      | 52.5 ms: 1.02x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 3.31 ms: 1.02x slower                                                               |
| scimark_fft                | 301 ms                                                       | 309 ms: 1.03x slower                                                                |
| pyflate                    | 439 ms                                                       | 453 ms: 1.03x slower                                                                |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.03x slower                                                                |
| richards                   | 45.7 ms                                                      | 47.3 ms: 1.04x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 6.20 ms: 1.04x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                                |
| python_startup_no_site     | 8.64 ms                                                      | 9.07 ms: 1.05x slower                                                               |
| async_generators           | 390 ms                                                       | 414 ms: 1.06x slower                                                                |
| json                       | 5.12 ms                                                      | 5.47 ms: 1.07x slower                                                               |
| json_loads                 | 24.4 us                                                      | 26.1 us: 1.07x slower                                                               |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 166 us: 1.09x slower                                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.63 ms: 1.10x slower                                                               |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                               |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                                               |
| telco                      | 6.96 ms                                                      | 7.92 ms: 1.14x slower                                                               |
| coverage                   | 66.7 ms                                                      | 78.7 ms: 1.18x slower                                                               |
| python_startup             | 11.6 ms                                                      | 16.2 ms: 1.40x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.80 ms: 1.76x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.31 ms: 1.81x slower                                                               |
| bench_mp_pool              | 4.76 ms                                                      | 1.12 sec: 235.88x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                        |

Benchmark hidden because not significant (8): asyncio_websockets, sqlite_synth, xml_etree_process, 2to3, regex_dna, docutils, scimark_sor, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x