# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                   |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 468 ms: 1.55x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.9 ms: 1.18x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| nbody          | 97.0 ms                                                | 99.0 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.10 ms: 1.17x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.6 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.05x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.3 us: 1.04x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                   |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.38 us: 1.06x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                  |
| pickle               | 11.6 us                                                | 13.0 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.17 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                  |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 468 ms: 1.55x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                                   |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                  |
| go                         | 139 ms                                                 | 113 ms: 1.24x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.09 ms: 1.20x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                 |
| spectral_norm              | 115 ms                                                 | 96.4 ms: 1.19x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| float                      | 84.7 ms                                                | 71.9 ms: 1.18x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 58.3 ms: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 266 ms: 1.18x faster                                                   |
| async_generators           | 463 ms                                                 | 395 ms: 1.17x faster                                                   |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.10 ms: 1.17x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                   |
| logging_silent             | 104 ns                                                 | 93.7 ns: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                  |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                  |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                   |
| unpickle                   | 15.9 us                                                | 14.4 us: 1.10x faster                                                  |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                                  |
| scimark_fft                | 382 ms                                                 | 352 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                   |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.75 ms: 1.06x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                   |
| unpack_sequence            | 54.0 ns                                                | 50.9 ns: 1.06x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                 |
| richards                   | 45.8 ms                                                | 43.9 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.3 us: 1.04x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                                  |
| richards_super             | 51.5 ms                                                | 49.9 ms: 1.03x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 476 ms: 1.03x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                 |
| nqueens                    | 83.3 ms                                                | 83.6 ms: 1.00x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                  |
| fannkuch                   | 417 ms                                                 | 422 ms: 1.01x slower                                                   |
| json                       | 5.26 ms                                                | 5.37 ms: 1.02x slower                                                  |
| nbody                      | 97.0 ms                                                | 99.0 ms: 1.02x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.6 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 869 us: 1.03x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.38 us: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                  |
| telco                      | 7.10 ms                                                | 7.94 ms: 1.12x slower                                                  |
| pickle                     | 11.6 us                                                | 13.0 us: 1.12x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.17 ms: 1.18x slower                                                  |
| coverage                   | 72.7 ms                                                | 91.6 ms: 1.26x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (3): regex_dna, asyncio_websockets, unpickle_list
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x