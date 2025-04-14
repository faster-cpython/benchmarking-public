# Results vs. 3.12.0

- fork: python
- ref: v3.13.2
- machine: linux-x86_64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.013x slower
- HPT reliability: 75.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 294 ms: 1.03x slower                                         |
| chameleon      | 7.23 ms                                                      | 7.48 ms: 1.03x slower                                        |
| docutils       | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 840 ms: 1.25x faster                                         |
| async_tree_none_tg         | 431 ms                                                       | 345 ms: 1.25x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 856 ms: 1.22x faster                                         |
| async_tree_none            | 452 ms                                                       | 382 ms: 1.18x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 463 ms: 1.17x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 476 ms: 1.14x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 614 ms: 1.13x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 617 ms: 1.13x faster                                         |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 261 ms: 1.02x faster                                         |
| float          | 76.6 ms                                                      | 80.3 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.26 ms: 1.10x faster                                        |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                         |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                         |
| regex_v8       | 23.6 ms                                                      | 25.4 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 86.6 ms: 1.01x slower                                        |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                         |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                         |
| pickle_pure_python   | 318 us                                                       | 327 us: 1.03x slower                                         |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.1 ms: 1.03x slower                                        |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                         |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                        |
| tomli_loads          | 2.16 sec                                                     | 2.45 sec: 1.14x slower                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.5 ms: 1.07x faster                                        |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 840 ms: 1.25x faster                                         |
| async_tree_none_tg         | 431 ms                                                       | 345 ms: 1.25x faster                                         |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.24x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 856 ms: 1.22x faster                                         |
| async_tree_none            | 452 ms                                                       | 382 ms: 1.18x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 463 ms: 1.17x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 476 ms: 1.14x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 614 ms: 1.13x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 617 ms: 1.13x faster                                         |
| crypto_pyaes               | 80.3 ms                                                      | 72.1 ms: 1.11x faster                                        |
| generators                 | 37.4 ms                                                      | 33.7 ms: 1.11x faster                                        |
| regex_effbot               | 3.57 ms                                                      | 3.26 ms: 1.10x faster                                        |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.08x faster                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.08x faster                                         |
| chaos                      | 64.0 ms                                                      | 59.3 ms: 1.08x faster                                        |
| logging_format             | 7.48 us                                                      | 6.94 us: 1.08x faster                                        |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.08x faster                                        |
| raytrace                   | 298 ms                                                       | 277 ms: 1.07x faster                                         |
| django_template            | 38.2 ms                                                      | 35.5 ms: 1.07x faster                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.0 ms: 1.06x faster                                        |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                         |
| logging_simple             | 6.71 us                                                      | 6.41 us: 1.05x faster                                        |
| bench_thread_pool          | 950 us                                                       | 917 us: 1.04x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.03x faster                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                        |
| docutils                   | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                       |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                         |
| pidigits                   | 265 ms                                                       | 261 ms: 1.02x faster                                         |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.01x faster                                         |
| mdp                        | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                       |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                         |
| gunicorn                   | 1.00 ms                                                      | 994 us: 1.01x faster                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                       |
| pprint_safe_repr           | 807 ms                                                       | 812 ms: 1.01x slower                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                        |
| xml_etree_generate         | 86.1 ms                                                      | 86.6 ms: 1.01x slower                                        |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                         |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                        |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                         |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                       |
| logging_silent             | 94.4 ns                                                      | 96.0 ns: 1.02x slower                                        |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                        |
| pickle_pure_python         | 318 us                                                       | 327 us: 1.03x slower                                         |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                        |
| xml_etree_process          | 58.4 ms                                                      | 60.1 ms: 1.03x slower                                        |
| 2to3                       | 285 ms                                                       | 294 ms: 1.03x slower                                         |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                         |
| chameleon                  | 7.23 ms                                                      | 7.48 ms: 1.03x slower                                        |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                        |
| dulwich_log                | 65.4 ms                                                      | 67.8 ms: 1.04x slower                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.95 ms: 1.04x slower                                        |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.52 us: 1.04x slower                                        |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                         |
| spectral_norm              | 91.6 ms                                                      | 95.6 ms: 1.04x slower                                        |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                         |
| scimark_fft                | 301 ms                                                       | 315 ms: 1.04x slower                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                        |
| sqlite_synth               | 2.77 us                                                      | 2.90 us: 1.05x slower                                        |
| deepcopy_memo              | 36.8 us                                                      | 38.5 us: 1.05x slower                                        |
| float                      | 76.6 ms                                                      | 80.3 ms: 1.05x slower                                        |
| sympy_expand               | 484 ms                                                       | 508 ms: 1.05x slower                                         |
| deepcopy                   | 368 us                                                       | 387 us: 1.05x slower                                         |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                        |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                         |
| hexiom                     | 5.96 ms                                                      | 6.37 ms: 1.07x slower                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                        |
| regex_v8                   | 23.6 ms                                                      | 25.4 ms: 1.07x slower                                        |
| pyflate                    | 439 ms                                                       | 475 ms: 1.08x slower                                         |
| async_generators           | 390 ms                                                       | 427 ms: 1.09x slower                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.68 ms: 1.11x slower                                        |
| scimark_sor                | 109 ms                                                       | 123 ms: 1.13x slower                                         |
| tomli_loads                | 2.16 sec                                                     | 2.45 sec: 1.14x slower                                       |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                         |
| richards                   | 45.7 ms                                                      | 52.3 ms: 1.14x slower                                        |
| richards_super             | 51.3 ms                                                      | 59.3 ms: 1.16x slower                                        |
| telco                      | 6.96 ms                                                      | 8.84 ms: 1.27x slower                                        |
| coverage                   | 66.7 ms                                                      | 84.7 ms: 1.27x slower                                        |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                        |
| gc_traversal               | 3.48 ms                                                      | 4.92 ms: 1.41x slower                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.72 ms: 1.71x slower                                        |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (4): scimark_lu, nqueens, tornado_http, nbody
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 75.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x