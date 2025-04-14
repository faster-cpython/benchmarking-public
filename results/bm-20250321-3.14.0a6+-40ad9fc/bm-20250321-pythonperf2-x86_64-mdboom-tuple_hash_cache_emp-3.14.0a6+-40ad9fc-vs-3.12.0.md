# Results vs. 3.12.0

- fork: mdboom
- ref: tuple_hash_cache_emp
- machine: linux-x86_64
- commit hash: 40ad9fc
- commit date: 2025-03-21
- overall geometric mean: 1.026x faster
- HPT reliability: 52.27%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 642 ms: 1.62x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 653 ms: 1.61x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 354 ms: 1.54x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 282 ms: 1.53x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 356 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 521 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 525 ms: 1.32x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.50x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 72.1 ms: 1.06x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 105 ms: 1.20x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.12 ms: 1.15x faster                                                        |
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 24.4 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 97.7 ms: 1.05x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 85.6 ms: 1.01x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.20 sec: 1.02x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 61.5 ms: 1.05x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.2 us: 1.08x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.6 ms: 1.04x faster                                                        |
| mako            | 10.0 ms                                                      | 11.4 ms: 1.14x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.31 sec: 1.96x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 642 ms: 1.62x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 653 ms: 1.61x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 354 ms: 1.54x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 282 ms: 1.53x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 356 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 521 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 525 ms: 1.32x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                        |
| deepcopy                   | 368 us                                                       | 287 us: 1.29x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.7 us: 1.24x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.0 us: 1.22x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.12 ms: 1.15x faster                                                        |
| go                         | 150 ms                                                       | 132 ms: 1.14x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                        |
| float                      | 76.6 ms                                                      | 72.1 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.7 ms: 1.05x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| django_template            | 38.2 ms                                                      | 36.6 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.1 ms: 1.04x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 63.0 ms: 1.04x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.26 us: 1.03x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.59 us: 1.02x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 90.3 ms: 1.01x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 85.6 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.8 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                         |
| chaos                      | 64.0 ms                                                      | 64.2 ms: 1.00x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 99.3 ms: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                         |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.20 sec: 1.02x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 825 ms: 1.02x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 24.4 ms: 1.03x slower                                                        |
| richards_super             | 51.3 ms                                                      | 53.5 ms: 1.04x slower                                                        |
| sympy_expand               | 484 ms                                                       | 507 ms: 1.05x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 84.2 ms: 1.05x slower                                                        |
| scimark_fft                | 301 ms                                                       | 316 ms: 1.05x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.40 ms: 1.05x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 61.5 ms: 1.05x slower                                                        |
| richards                   | 45.7 ms                                                      | 48.3 ms: 1.06x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                                         |
| async_generators           | 390 ms                                                       | 415 ms: 1.06x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                         |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                                        |
| pyflate                    | 439 ms                                                       | 471 ms: 1.07x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 96.7 ms: 1.08x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.2 us: 1.08x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.51 ms: 1.09x slower                                                        |
| fannkuch                   | 350 ms                                                       | 388 ms: 1.11x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.69 ms: 1.12x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                         |
| mako                       | 10.0 ms                                                      | 11.4 ms: 1.14x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.19 ms: 1.18x slower                                                        |
| nbody                      | 88.0 ms                                                      | 105 ms: 1.20x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| coverage                   | 66.7 ms                                                      | 82.4 ms: 1.24x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.87 ms: 1.81x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.61 ms: 1.90x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.65 sec: 346.66x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (4): logging_silent, raytrace, regex_dna, bench_thread_pool
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250321-3.14.0a6+-40ad9fc/bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 52.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x