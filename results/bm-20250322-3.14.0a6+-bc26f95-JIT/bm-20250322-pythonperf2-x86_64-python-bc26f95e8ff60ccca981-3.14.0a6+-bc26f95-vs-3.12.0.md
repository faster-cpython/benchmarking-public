# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.020x faster
- HPT reliability: 83.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 293 ms: 1.03x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.00 sec: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 652 ms: 1.61x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 654 ms: 1.59x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 341 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 281 ms: 1.53x faster                                                         |
| async_tree_none            | 452 ms                                                       | 299 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 66.0 ms: 1.16x faster                                                        |
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 94.5 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 2.98 ms: 1.20x faster                                                        |
| regex_dna      | 239 ms                                                       | 230 ms: 1.04x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                        |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.8 ms: 1.06x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 81.5 ms: 1.06x faster                                                        |
| unpickle             | 14.8 us                                                      | 14.3 us: 1.03x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.8 us: 1.10x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 352 us: 1.11x slower                                                         |
| pickle_dict          | 32.5 us                                                      | 36.4 us: 1.12x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.24 us: 1.13x slower                                                        |
| pickle               | 10.5 us                                                      | 12.1 us: 1.15x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.16 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.2 ms: 1.03x faster                                                        |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 652 ms: 1.61x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 654 ms: 1.59x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 341 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 281 ms: 1.53x faster                                                         |
| async_tree_none            | 452 ms                                                       | 299 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.24x faster                                                        |
| deepcopy                   | 368 us                                                       | 303 us: 1.22x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 2.98 ms: 1.20x faster                                                        |
| float                      | 76.6 ms                                                      | 66.0 ms: 1.16x faster                                                        |
| richards                   | 45.7 ms                                                      | 40.7 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.04 us: 1.11x faster                                                        |
| richards_super             | 51.3 ms                                                      | 46.8 ms: 1.10x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.5 ms: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.0 ms: 1.07x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 150 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 96.8 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 81.5 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| comprehensions             | 21.9 us                                                      | 21.1 us: 1.04x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.20 us: 1.04x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                                         |
| deltablue                  | 3.24 ms                                                      | 3.12 ms: 1.04x faster                                                        |
| regex_dna                  | 239 ms                                                       | 230 ms: 1.04x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 63.2 ms: 1.03x faster                                                        |
| unpickle                   | 14.8 us                                                      | 14.3 us: 1.03x faster                                                        |
| django_template            | 38.2 ms                                                      | 37.2 ms: 1.03x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                        |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.60 us: 1.02x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                                       |
| raytrace                   | 298 ms                                                       | 293 ms: 1.02x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                         |
| sympy_str                  | 302 ms                                                       | 299 ms: 1.01x faster                                                         |
| logging_silent             | 94.4 ns                                                      | 93.6 ns: 1.01x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.56 sec: 1.00x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.79 us: 1.01x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                       |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                         |
| pyflate                    | 439 ms                                                       | 447 ms: 1.02x slower                                                         |
| 2to3                       | 285 ms                                                       | 293 ms: 1.03x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 71.1 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 832 ms: 1.03x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 983 us: 1.03x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 103 ms: 1.04x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.00 sec: 1.05x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                        |
| chaos                      | 64.0 ms                                                      | 67.0 ms: 1.05x slower                                                        |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.05x slower                                                         |
| scimark_fft                | 301 ms                                                       | 316 ms: 1.05x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 95.0 ms: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.31 sec: 1.06x slower                                                       |
| sympy_expand               | 484 ms                                                       | 517 ms: 1.07x slower                                                         |
| nbody                      | 88.0 ms                                                      | 94.5 ms: 1.07x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 87.2 ms: 1.09x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.8 us: 1.10x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 352 us: 1.11x slower                                                         |
| pickle_dict                | 32.5 us                                                      | 36.4 us: 1.12x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 59.5 ns: 1.12x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.24 us: 1.13x slower                                                        |
| async_generators           | 390 ms                                                       | 446 ms: 1.14x slower                                                         |
| pickle                     | 10.5 us                                                      | 12.1 us: 1.15x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.09 ms: 1.16x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.16 us: 1.17x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.97 ms: 1.17x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.2 ms: 1.17x slower                                                        |
| fannkuch                   | 350 ms                                                       | 413 ms: 1.18x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.00 ms: 1.19x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 181 us: 1.19x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.73 ms: 1.72x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.37 ms: 1.83x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.11 sec: 232.19x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, asyncio_tcp_ssl, go
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.020x faster

# HPT report

- Reliability score: 83.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x