# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 275 ms: 1.04x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.82 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 606 ms: 1.74x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 317 ms: 1.70x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 615 ms: 1.69x faster                                                         |
| async_tree_none            | 452 ms                                                       | 272 ms: 1.66x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 261 ms: 1.65x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 525 ms: 1.33x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 539 ms: 1.29x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 66.4 ms: 1.15x faster                                                        |
| nbody          | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                        |
| pidigits       | 265 ms                                                       | 292 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 2.95 ms: 1.21x faster                                                        |
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                         |
| regex_dna      | 239 ms                                                       | 219 ms: 1.09x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 24.6 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 77.3 ms: 1.11x faster                                                        |
| unpickle             | 14.8 us                                                      | 13.7 us: 1.08x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.00 sec: 1.08x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 54.2 ms: 1.08x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 30.3 us: 1.07x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 199 us: 1.06x faster                                                         |
| unpickle_list        | 4.66 us                                                      | 4.50 us: 1.03x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                         |
| json_loads           | 24.4 us                                                      | 26.6 us: 1.09x slower                                                        |
| pickle               | 10.5 us                                                      | 11.7 us: 1.11x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 162 ms: 1.13x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.13 ms: 1.06x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 32.2 ms: 1.18x faster                                                        |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 606 ms: 1.74x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 317 ms: 1.70x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 615 ms: 1.69x faster                                                         |
| async_tree_none            | 452 ms                                                       | 272 ms: 1.66x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 261 ms: 1.65x faster                                                         |
| comprehensions             | 21.9 us                                                      | 15.3 us: 1.43x faster                                                        |
| deepcopy                   | 368 us                                                       | 258 us: 1.43x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 26.8 us: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 525 ms: 1.33x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 539 ms: 1.29x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 72.4 ms: 1.27x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.8 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.70 us: 1.25x faster                                                        |
| go                         | 150 ms                                                       | 121 ms: 1.24x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 2.95 ms: 1.21x faster                                                        |
| scimark_sor                | 109 ms                                                       | 91.4 ms: 1.19x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 79.6 ns: 1.19x faster                                                        |
| django_template            | 38.2 ms                                                      | 32.2 ms: 1.18x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 58.3 ms: 1.18x faster                                                        |
| raytrace                   | 298 ms                                                       | 253 ms: 1.18x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                        |
| float                      | 76.6 ms                                                      | 66.4 ms: 1.15x faster                                                        |
| chaos                      | 64.0 ms                                                      | 55.8 ms: 1.15x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 139 ms: 1.15x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 86.3 ms: 1.14x faster                                                        |
| logging_simple             | 6.71 us                                                      | 5.92 us: 1.13x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.61 us: 1.13x faster                                                        |
| scimark_fft                | 301 ms                                                       | 266 ms: 1.13x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 77.3 ms: 1.11x faster                                                        |
| pyflate                    | 439 ms                                                       | 395 ms: 1.11x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 20.7 ms: 1.11x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 146 ms: 1.11x faster                                                         |
| richards                   | 45.7 ms                                                      | 41.4 ms: 1.10x faster                                                        |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                         |
| richards_super             | 51.3 ms                                                      | 47.0 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.52 sec: 1.09x faster                                                       |
| regex_dna                  | 239 ms                                                       | 219 ms: 1.09x faster                                                         |
| sympy_str                  | 302 ms                                                       | 278 ms: 1.09x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.3 ms: 1.08x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.1 ms: 1.08x faster                                                        |
| unpickle                   | 14.8 us                                                      | 13.7 us: 1.08x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.00 sec: 1.08x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 54.2 ms: 1.08x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.3 us: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 74.8 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 752 ms: 1.07x faster                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.66 ms: 1.07x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.29 ms: 1.07x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 892 us: 1.06x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 54.3 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 199 us: 1.06x faster                                                         |
| sqlglot_normalize          | 116 ms                                                       | 110 ms: 1.05x faster                                                         |
| nbody                      | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 85.4 ms: 1.05x faster                                                        |
| hexiom                     | 5.96 ms                                                      | 5.68 ms: 1.05x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.09 ms: 1.05x faster                                                        |
| 2to3                       | 285 ms                                                       | 275 ms: 1.04x faster                                                         |
| unpickle_list              | 4.66 us                                                      | 4.50 us: 1.03x faster                                                        |
| sympy_expand               | 484 ms                                                       | 469 ms: 1.03x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.82 sec: 1.02x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.17 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 64.9 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 155 us: 1.02x slower                                                         |
| json                       | 5.12 ms                                                      | 5.29 ms: 1.03x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.6 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.13 ms: 1.06x slower                                                        |
| async_generators           | 390 ms                                                       | 416 ms: 1.07x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.53 ms: 1.08x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.6 us: 1.09x slower                                                        |
| coverage                   | 66.7 ms                                                      | 73.1 ms: 1.10x slower                                                        |
| pidigits                   | 265 ms                                                       | 292 ms: 1.10x slower                                                         |
| pickle                     | 10.5 us                                                      | 11.7 us: 1.11x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 162 ms: 1.13x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.47 ms: 1.57x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.85 ms: 1.79x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 961 ms: 201.84x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (4): pickle_list, unpack_sequence, fannkuch, xml_etree_iterparse
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x