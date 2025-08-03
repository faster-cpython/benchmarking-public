# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 406dc71
- commit date: 2025-08-03
- overall geometric mean: 1.138x slower
- HPT reliability: 98.84%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 325 ms: 1.14x slower                                        |
| docutils       | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                      |
| Geometric mean | (ref)                                                        | 1.12x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 671 ms: 1.57x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 667 ms: 1.56x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 354 ms: 1.53x faster                                        |
| async_tree_memoization     | 544 ms                                                       | 362 ms: 1.50x faster                                        |
| async_tree_none_tg         | 431 ms                                                       | 290 ms: 1.48x faster                                        |
| async_tree_none            | 452 ms                                                       | 306 ms: 1.47x faster                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 527 ms: 1.32x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 531 ms: 1.31x faster                                        |
| Geometric mean             | (ref)                                                        | 1.47x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 257 ms: 1.03x faster                                        |
| float          | 76.6 ms                                                      | 107 ms: 1.39x slower                                        |
| nbody          | 88.0 ms                                                      | 184 ms: 2.10x slower                                        |
| Geometric mean | (ref)                                                        | 1.41x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                        |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                       |
| regex_effbot   | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                       |
| regex_compile  | 144 ms                                                       | 159 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                       |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                        |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                       |
| xml_etree_generate   | 86.1 ms                                                      | 109 ms: 1.27x slower                                        |
| pickle_pure_python   | 318 us                                                       | 410 us: 1.29x slower                                        |
| xml_etree_process    | 58.4 ms                                                      | 76.1 ms: 1.30x slower                                       |
| tomli_loads          | 2.16 sec                                                     | 3.08 sec: 1.43x slower                                      |
| unpickle_pure_python | 210 us                                                       | 388 us: 1.85x slower                                        |
| Geometric mean       | (ref)                                                        | 1.24x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                       |
| mako            | 10.0 ms                                                      | 16.9 ms: 1.69x slower                                       |
| Geometric mean  | (ref)                                                        | 1.25x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.46 sec: 1.76x faster                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 671 ms: 1.57x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 667 ms: 1.56x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 354 ms: 1.53x faster                                        |
| async_tree_memoization     | 544 ms                                                       | 362 ms: 1.50x faster                                        |
| async_tree_none_tg         | 431 ms                                                       | 290 ms: 1.48x faster                                        |
| async_tree_none            | 452 ms                                                       | 306 ms: 1.47x faster                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.6 us: 1.33x faster                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 527 ms: 1.32x faster                                        |
| deepcopy                   | 368 us                                                       | 279 us: 1.32x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 531 ms: 1.31x faster                                        |
| generators                 | 37.4 ms                                                      | 29.9 ms: 1.25x faster                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                       |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                       |
| logging_format             | 7.48 us                                                      | 6.69 us: 1.12x faster                                       |
| logging_simple             | 6.71 us                                                      | 6.10 us: 1.10x faster                                       |
| django_template            | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                       |
| dulwich_log                | 65.4 ms                                                      | 60.9 ms: 1.07x faster                                       |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                        |
| scimark_lu                 | 98.8 ms                                                      | 92.5 ms: 1.07x faster                                       |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.06x faster                                        |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                       |
| pidigits                   | 265 ms                                                       | 257 ms: 1.03x faster                                        |
| logging_silent             | 94.4 ns                                                      | 91.7 ns: 1.03x faster                                       |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                        |
| chaos                      | 64.0 ms                                                      | 63.4 ms: 1.01x faster                                       |
| sympy_sum                  | 162 ms                                                       | 161 ms: 1.01x faster                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                       |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                       |
| regex_effbot               | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                       |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                       |
| json                       | 5.12 ms                                                      | 5.33 ms: 1.04x slower                                       |
| sympy_str                  | 302 ms                                                       | 315 ms: 1.04x slower                                        |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                        |
| sqlite_synth               | 2.77 us                                                      | 3.01 us: 1.09x slower                                       |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                       |
| docutils                   | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                      |
| regex_compile              | 144 ms                                                       | 159 ms: 1.10x slower                                        |
| 2to3                       | 285 ms                                                       | 325 ms: 1.14x slower                                        |
| sympy_expand               | 484 ms                                                       | 552 ms: 1.14x slower                                        |
| raytrace                   | 298 ms                                                       | 341 ms: 1.14x slower                                        |
| nqueens                    | 89.9 ms                                                      | 103 ms: 1.15x slower                                        |
| richards_super             | 51.3 ms                                                      | 59.7 ms: 1.16x slower                                       |
| richards                   | 45.7 ms                                                      | 53.3 ms: 1.16x slower                                       |
| coverage                   | 66.7 ms                                                      | 77.8 ms: 1.17x slower                                       |
| async_generators           | 390 ms                                                       | 456 ms: 1.17x slower                                        |
| pycparser                  | 1.23 sec                                                     | 1.52 sec: 1.23x slower                                      |
| meteor_contest             | 128 ms                                                       | 160 ms: 1.25x slower                                        |
| xml_etree_generate         | 86.1 ms                                                      | 109 ms: 1.27x slower                                        |
| pickle_pure_python         | 318 us                                                       | 410 us: 1.29x slower                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 88.9 ms: 1.29x slower                                       |
| xml_etree_process          | 58.4 ms                                                      | 76.1 ms: 1.30x slower                                       |
| crypto_pyaes               | 80.3 ms                                                      | 105 ms: 1.31x slower                                        |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                       |
| typing_runtime_protocols   | 152 us                                                       | 201 us: 1.32x slower                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.26 sec: 1.36x slower                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.11 sec: 1.38x slower                                      |
| float                      | 76.6 ms                                                      | 107 ms: 1.39x slower                                        |
| comprehensions             | 21.9 us                                                      | 30.6 us: 1.40x slower                                       |
| tomli_loads                | 2.16 sec                                                     | 3.08 sec: 1.43x slower                                      |
| pyflate                    | 439 ms                                                       | 632 ms: 1.44x slower                                        |
| go                         | 150 ms                                                       | 224 ms: 1.49x slower                                        |
| scimark_fft                | 301 ms                                                       | 462 ms: 1.53x slower                                        |
| mako                       | 10.0 ms                                                      | 16.9 ms: 1.69x slower                                       |
| fannkuch                   | 350 ms                                                       | 607 ms: 1.74x slower                                        |
| hexiom                     | 5.96 ms                                                      | 10.6 ms: 1.78x slower                                       |
| spectral_norm              | 91.6 ms                                                      | 168 ms: 1.83x slower                                        |
| deltablue                  | 3.24 ms                                                      | 5.97 ms: 1.84x slower                                       |
| unpickle_pure_python       | 210 us                                                       | 388 us: 1.85x slower                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.94 ms: 1.85x slower                                       |
| gc_traversal               | 3.48 ms                                                      | 6.77 ms: 1.95x slower                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 8.35 ms: 1.99x slower                                       |
| nbody                      | 88.0 ms                                                      | 184 ms: 2.10x slower                                        |
| telco                      | 6.96 ms                                                      | 159 ms: 22.88x slower                                       |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250803-3.15.0a0-406dc71-PYTHON_UOPS/bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.138x slower

# HPT report

- Reliability score: 98.84% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x