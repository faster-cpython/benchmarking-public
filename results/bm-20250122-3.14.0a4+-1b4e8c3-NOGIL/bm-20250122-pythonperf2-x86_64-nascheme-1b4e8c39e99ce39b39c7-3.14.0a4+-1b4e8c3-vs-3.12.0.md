# Results vs. 3.12.0

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: linux-x86_64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.080x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 342 ms: 1.20x slower                                                           |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                         |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 585 ms: 1.80x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 250 ms: 1.72x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 617 ms: 1.69x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 322 ms: 1.68x faster                                                           |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 488 ms: 1.43x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 533 ms: 1.31x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 248 ms: 1.07x faster                                                           |
| float          | 76.6 ms                                                      | 75.2 ms: 1.02x faster                                                          |
| nbody          | 88.0 ms                                                      | 134 ms: 1.52x slower                                                           |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.12 ms: 1.14x faster                                                          |
| regex_dna      | 239 ms                                                       | 245 ms: 1.02x slower                                                           |
| regex_compile  | 144 ms                                                       | 157 ms: 1.09x slower                                                           |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.44 sec: 1.13x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 237 us: 1.13x slower                                                           |
| json_loads           | 24.4 us                                                      | 28.2 us: 1.16x slower                                                          |
| pickle_pure_python   | 318 us                                                       | 388 us: 1.22x slower                                                           |
| json_dumps           | 10.2 ms                                                      | 13.6 ms: 1.33x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.19x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.0 ms: 1.39x slower                                                          |
| python_startup         | 11.6 ms                                                      | 18.9 ms: 1.62x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.50x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 46.7 ms: 1.22x slower                                                          |
| mako            | 10.0 ms                                                      | 18.0 ms: 1.80x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.48x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 585 ms: 1.80x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 250 ms: 1.72x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 617 ms: 1.69x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 322 ms: 1.68x faster                                                           |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 488 ms: 1.43x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 533 ms: 1.31x faster                                                           |
| generators                 | 37.4 ms                                                      | 31.5 ms: 1.19x faster                                                          |
| pathlib                    | 18.9 ms                                                      | 16.4 ms: 1.15x faster                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.12 ms: 1.14x faster                                                          |
| deepcopy                   | 368 us                                                       | 337 us: 1.09x faster                                                           |
| pidigits                   | 265 ms                                                       | 248 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.77 us                                                      | 2.63 us: 1.06x faster                                                          |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.04x faster                                                          |
| asyncio_websockets         | 387 ms                                                       | 378 ms: 1.02x faster                                                           |
| float                      | 76.6 ms                                                      | 75.2 ms: 1.02x faster                                                          |
| comprehensions             | 21.9 us                                                      | 21.7 us: 1.01x faster                                                          |
| go                         | 150 ms                                                       | 149 ms: 1.01x faster                                                           |
| deepcopy_memo              | 36.8 us                                                      | 37.4 us: 1.02x slower                                                          |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.02x slower                                                           |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.04x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 69.3 ms: 1.06x slower                                                          |
| mdp                        | 2.57 sec                                                     | 2.74 sec: 1.07x slower                                                         |
| logging_format             | 7.48 us                                                      | 8.05 us: 1.08x slower                                                          |
| logging_simple             | 6.71 us                                                      | 7.27 us: 1.08x slower                                                          |
| sympy_sum                  | 162 ms                                                       | 176 ms: 1.08x slower                                                           |
| deepcopy_reduce            | 3.37 us                                                      | 3.66 us: 1.09x slower                                                          |
| regex_compile              | 144 ms                                                       | 157 ms: 1.09x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                          |
| json                       | 5.12 ms                                                      | 5.62 ms: 1.10x slower                                                          |
| logging_silent             | 94.4 ns                                                      | 104 ns: 1.10x slower                                                           |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.10x slower                                                           |
| sqlalchemy_declarative     | 159 ms                                                       | 175 ms: 1.10x slower                                                           |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.9 ms: 1.11x slower                                                          |
| chaos                      | 64.0 ms                                                      | 71.5 ms: 1.12x slower                                                          |
| sympy_str                  | 302 ms                                                       | 340 ms: 1.13x slower                                                           |
| scimark_sor                | 109 ms                                                       | 123 ms: 1.13x slower                                                           |
| pprint_safe_repr           | 807 ms                                                       | 910 ms: 1.13x slower                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.44 sec: 1.13x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 237 us: 1.13x slower                                                           |
| sympy_integrate            | 23.9 ms                                                      | 27.1 ms: 1.13x slower                                                          |
| sqlglot_normalize          | 116 ms                                                       | 131 ms: 1.14x slower                                                           |
| pprint_pformat             | 1.65 sec                                                     | 1.88 sec: 1.14x slower                                                         |
| pyflate                    | 439 ms                                                       | 499 ms: 1.14x slower                                                           |
| crypto_pyaes               | 80.3 ms                                                      | 92.4 ms: 1.15x slower                                                          |
| json_loads                 | 24.4 us                                                      | 28.2 us: 1.16x slower                                                          |
| raytrace                   | 298 ms                                                       | 348 ms: 1.17x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 2.07 ms: 1.17x slower                                                          |
| sqlglot_optimize           | 57.5 ms                                                      | 67.4 ms: 1.17x slower                                                          |
| sympy_expand               | 484 ms                                                       | 568 ms: 1.17x slower                                                           |
| scimark_fft                | 301 ms                                                       | 354 ms: 1.18x slower                                                           |
| 2to3                       | 285 ms                                                       | 342 ms: 1.20x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.65 ms: 1.20x slower                                                          |
| async_generators           | 390 ms                                                       | 470 ms: 1.20x slower                                                           |
| pickle_pure_python         | 318 us                                                       | 388 us: 1.22x slower                                                           |
| meteor_contest             | 128 ms                                                       | 156 ms: 1.22x slower                                                           |
| django_template            | 38.2 ms                                                      | 46.7 ms: 1.22x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 7.31 ms: 1.23x slower                                                          |
| scimark_lu                 | 98.8 ms                                                      | 123 ms: 1.24x slower                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 87.8 ms: 1.27x slower                                                          |
| richards                   | 45.7 ms                                                      | 58.8 ms: 1.28x slower                                                          |
| nqueens                    | 89.9 ms                                                      | 116 ms: 1.29x slower                                                           |
| richards_super             | 51.3 ms                                                      | 66.9 ms: 1.30x slower                                                          |
| telco                      | 6.96 ms                                                      | 9.10 ms: 1.31x slower                                                          |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.59 ms: 1.33x slower                                                          |
| json_dumps                 | 10.2 ms                                                      | 13.6 ms: 1.33x slower                                                          |
| gc_traversal               | 3.48 ms                                                      | 4.64 ms: 1.33x slower                                                          |
| fannkuch                   | 350 ms                                                       | 479 ms: 1.37x slower                                                           |
| python_startup_no_site     | 8.64 ms                                                      | 12.0 ms: 1.39x slower                                                          |
| deltablue                  | 3.24 ms                                                      | 4.57 ms: 1.41x slower                                                          |
| typing_runtime_protocols   | 152 us                                                       | 223 us: 1.47x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 2.40 ms: 1.51x slower                                                          |
| nbody                      | 88.0 ms                                                      | 134 ms: 1.52x slower                                                           |
| coverage                   | 66.7 ms                                                      | 102 ms: 1.53x slower                                                           |
| bench_thread_pool          | 950 us                                                       | 1.46 ms: 1.53x slower                                                          |
| python_startup             | 11.6 ms                                                      | 18.9 ms: 1.62x slower                                                          |
| mako                       | 10.0 ms                                                      | 18.0 ms: 1.80x slower                                                          |
| bench_mp_pool              | 4.76 ms                                                      | 49.7 ms: 10.44x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.12x slower                                                                   |
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
Ignored benchmarks (12) of results/bm-20250122-3.14.0a4+-1b4e8c3-NOGIL/bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.080x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.26x