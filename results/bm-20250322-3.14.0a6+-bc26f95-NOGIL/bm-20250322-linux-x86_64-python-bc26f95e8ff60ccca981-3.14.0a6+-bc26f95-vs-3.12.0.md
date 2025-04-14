# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.006x slower
- HPT reliability: 98.61%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 296 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 536 ms: 2.21x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 577 ms: 2.00x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 238 ms: 1.89x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                   |
| async_tree_none            | 472 ms                                                 | 283 ms: 1.67x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 352 ms: 1.64x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 459 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                  |
| pidigits       | 187 ms                                                 | 181 ms: 1.03x faster                                                   |
| nbody          | 97.0 ms                                                | 134 ms: 1.39x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                  |
| regex_v8       | 23.1 ms                                                | 21.8 ms: 1.06x faster                                                  |
| regex_compile  | 148 ms                                                 | 149 ms: 1.00x slower                                                   |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.2 ms: 1.12x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.07x faster                                                   |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.02x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                  |
| unpickle             | 15.9 us                                                | 16.6 us: 1.05x slower                                                  |
| pickle               | 11.6 us                                                | 12.3 us: 1.06x slower                                                  |
| xml_etree_generate   | 89.2 ms                                                | 94.4 ms: 1.06x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 66.9 ms: 1.08x slower                                                  |
| pickle_pure_python   | 324 us                                                 | 351 us: 1.08x slower                                                   |
| unpickle_pure_python | 230 us                                                 | 252 us: 1.10x slower                                                   |
| unpickle_list        | 5.29 us                                                | 5.85 us: 1.11x slower                                                  |
| json_loads           | 28.5 us                                                | 33.0 us: 1.16x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.9 ms: 1.24x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 10.9 ms: 1.57x slower                                                  |
| python_startup         | 9.55 ms                                                | 15.5 ms: 1.63x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.60x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 40.1 ms: 1.16x slower                                                  |
| mako            | 11.9 ms                                                | 16.2 ms: 1.36x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 536 ms: 2.21x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 577 ms: 2.00x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 238 ms: 1.89x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 2.17 ms: 1.75x faster                                                  |
| async_tree_none            | 472 ms                                                 | 283 ms: 1.67x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 352 ms: 1.64x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 459 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                                   |
| deepcopy                   | 371 us                                                 | 308 us: 1.21x faster                                                   |
| float                      | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 95.2 ms: 1.12x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 63.1 ms: 1.09x faster                                                  |
| comprehensions             | 21.8 us                                                | 20.1 us: 1.08x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.07x faster                                                   |
| regex_v8                   | 23.1 ms                                                | 21.8 ms: 1.06x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 38.7 us: 1.05x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.20 us: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 448 ms: 1.03x faster                                                   |
| pidigits                   | 187 ms                                                 | 181 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                  |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                  |
| pickle_dict                | 35.5 us                                                | 35.0 us: 1.02x faster                                                  |
| regex_compile              | 148 ms                                                 | 149 ms: 1.00x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.13 us: 1.01x slower                                                  |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                   |
| logging_simple             | 6.46 us                                                | 6.65 us: 1.03x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                   |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.03x slower                                                   |
| logging_format             | 7.23 us                                                | 7.50 us: 1.04x slower                                                  |
| pyflate                    | 482 ms                                                 | 504 ms: 1.04x slower                                                   |
| chaos                      | 67.0 ms                                                | 70.1 ms: 1.05x slower                                                  |
| unpickle                   | 15.9 us                                                | 16.6 us: 1.05x slower                                                  |
| deltablue                  | 3.72 ms                                                | 3.91 ms: 1.05x slower                                                  |
| sympy_str                  | 300 ms                                                 | 315 ms: 1.05x slower                                                   |
| pickle                     | 11.6 us                                                | 12.3 us: 1.06x slower                                                  |
| xml_etree_generate         | 89.2 ms                                                | 94.4 ms: 1.06x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 526 ms: 1.07x slower                                                   |
| raytrace                   | 312 ms                                                 | 335 ms: 1.07x slower                                                   |
| json                       | 5.26 ms                                                | 5.64 ms: 1.07x slower                                                  |
| scimark_sor                | 129 ms                                                 | 138 ms: 1.07x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.08x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 837 ms: 1.08x slower                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 159 ms: 1.08x slower                                                   |
| 2to3                       | 274 ms                                                 | 296 ms: 1.08x slower                                                   |
| xml_etree_process          | 61.7 ms                                                | 66.9 ms: 1.08x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 351 us: 1.08x slower                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.3 ms: 1.09x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.87 sec: 1.09x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 58.9 ns: 1.09x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 252 us: 1.10x slower                                                   |
| logging_silent             | 104 ns                                                 | 115 ns: 1.10x slower                                                   |
| crypto_pyaes               | 81.9 ms                                                | 90.2 ms: 1.10x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.73 sec: 1.10x slower                                                 |
| scimark_fft                | 382 ms                                                 | 422 ms: 1.10x slower                                                   |
| unpickle_list              | 5.29 us                                                | 5.85 us: 1.11x slower                                                  |
| sympy_expand               | 478 ms                                                 | 530 ms: 1.11x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.03 sec: 1.14x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.68 ms: 1.14x slower                                                  |
| django_template            | 34.6 ms                                                | 40.1 ms: 1.16x slower                                                  |
| json_loads                 | 28.5 us                                                | 33.0 us: 1.16x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 87.2 ms: 1.16x slower                                                  |
| meteor_contest             | 112 ms                                                 | 131 ms: 1.16x slower                                                   |
| richards                   | 45.8 ms                                                | 53.4 ms: 1.16x slower                                                  |
| nqueens                    | 83.3 ms                                                | 98.9 ms: 1.19x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.76 ms: 1.21x slower                                                  |
| richards_super             | 51.5 ms                                                | 62.6 ms: 1.22x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 144 ms: 1.22x slower                                                   |
| fannkuch                   | 417 ms                                                 | 511 ms: 1.22x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 12.9 ms: 1.24x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 202 us: 1.28x slower                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.56 ms: 1.30x slower                                                  |
| telco                      | 7.10 ms                                                | 9.31 ms: 1.31x slower                                                  |
| mako                       | 11.9 ms                                                | 16.2 ms: 1.36x slower                                                  |
| nbody                      | 97.0 ms                                                | 134 ms: 1.39x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 10.9 ms: 1.57x slower                                                  |
| python_startup             | 9.55 ms                                                | 15.5 ms: 1.63x slower                                                  |
| coverage                   | 72.7 ms                                                | 121 ms: 1.66x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 91.0 ms: 3.79x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.26 ms: 3.88x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, tomli_loads, docutils
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 98.61% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.33x