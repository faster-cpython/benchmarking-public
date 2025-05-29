# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 273 ms: 1.04x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.79 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 608 ms: 1.73x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 316 ms: 1.71x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 613 ms: 1.70x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 323 ms: 1.68x faster                                                         |
| async_tree_none            | 452 ms                                                       | 270 ms: 1.67x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 262 ms: 1.64x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 517 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 532 ms: 1.31x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 65.3 ms: 1.17x faster                                                        |
| nbody          | 88.0 ms                                                      | 82.2 ms: 1.07x faster                                                        |
| pidigits       | 265 ms                                                       | 291 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.02 ms: 1.18x faster                                                        |
| regex_compile  | 144 ms                                                       | 130 ms: 1.11x faster                                                         |
| regex_dna      | 239 ms                                                       | 226 ms: 1.06x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 76.9 ms: 1.12x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 53.8 ms: 1.09x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.00 sec: 1.08x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 198 us: 1.06x faster                                                         |
| pickle_pure_python   | 318 us                                                       | 304 us: 1.05x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                         |
| json_loads           | 24.4 us                                                      | 26.1 us: 1.07x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 163 ms: 1.13x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 33.2 ms: 1.15x faster                                                        |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 608 ms: 1.73x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 316 ms: 1.71x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 613 ms: 1.70x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 323 ms: 1.68x faster                                                         |
| async_tree_none            | 452 ms                                                       | 270 ms: 1.67x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 262 ms: 1.64x faster                                                         |
| comprehensions             | 21.9 us                                                      | 14.9 us: 1.47x faster                                                        |
| deepcopy                   | 368 us                                                       | 258 us: 1.43x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 26.1 us: 1.41x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 517 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 532 ms: 1.31x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 70.9 ms: 1.29x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.62 us: 1.29x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 54.4 ms: 1.27x faster                                                        |
| go                         | 150 ms                                                       | 120 ms: 1.25x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                        |
| scimark_sor                | 109 ms                                                       | 90.9 ms: 1.20x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.02 ms: 1.18x faster                                                        |
| raytrace                   | 298 ms                                                       | 252 ms: 1.18x faster                                                         |
| float                      | 76.6 ms                                                      | 65.3 ms: 1.17x faster                                                        |
| chaos                      | 64.0 ms                                                      | 54.8 ms: 1.17x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 138 ms: 1.16x faster                                                         |
| django_template            | 38.2 ms                                                      | 33.2 ms: 1.15x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.56 us: 1.14x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 87.2 ms: 1.13x faster                                                        |
| scimark_fft                | 301 ms                                                       | 267 ms: 1.13x faster                                                         |
| logging_simple             | 6.71 us                                                      | 5.95 us: 1.13x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.4 ms: 1.13x faster                                                        |
| richards                   | 45.7 ms                                                      | 40.8 ms: 1.12x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 84.3 ns: 1.12x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 76.9 ms: 1.12x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 146 ms: 1.11x faster                                                         |
| pyflate                    | 439 ms                                                       | 395 ms: 1.11x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 72.5 ms: 1.11x faster                                                        |
| regex_compile              | 144 ms                                                       | 130 ms: 1.11x faster                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.24 ms: 1.11x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.0 ms: 1.10x faster                                                        |
| richards_super             | 51.3 ms                                                      | 46.7 ms: 1.10x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.62 ms: 1.10x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 53.8 ms: 1.09x faster                                                        |
| sympy_str                  | 302 ms                                                       | 278 ms: 1.09x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 22.1 ms: 1.08x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.00 sec: 1.08x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 883 us: 1.08x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 754 ms: 1.07x faster                                                         |
| nbody                      | 88.0 ms                                                      | 82.2 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.55 sec: 1.07x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 84.5 ms: 1.06x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.04 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 198 us: 1.06x faster                                                         |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.06x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 304 us: 1.05x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 55.0 ms: 1.05x faster                                                        |
| 2to3                       | 285 ms                                                       | 273 ms: 1.04x faster                                                         |
| sqlglot_normalize          | 116 ms                                                       | 111 ms: 1.04x faster                                                         |
| hexiom                     | 5.96 ms                                                      | 5.72 ms: 1.04x faster                                                        |
| sympy_expand               | 484 ms                                                       | 471 ms: 1.03x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.79 sec: 1.03x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 64.3 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.17 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                         |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                         |
| fannkuch                   | 350 ms                                                       | 356 ms: 1.02x slower                                                         |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 159 us: 1.05x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                        |
| async_generators           | 390 ms                                                       | 411 ms: 1.05x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.35 ms: 1.06x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.1 us: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| pidigits                   | 265 ms                                                       | 291 ms: 1.10x slower                                                         |
| coverage                   | 66.7 ms                                                      | 74.2 ms: 1.11x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 163 ms: 1.13x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.66 ms: 1.63x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.81 ms: 1.76x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.22 sec: 256.93x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): pycparser, sqlite_synth
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.098x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x