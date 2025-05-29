# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.142x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 251 ms: 1.09x faster                                                   |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 605 ms: 1.95x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 303 ms: 1.90x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 305 ms: 1.89x faster                                                   |
| async_tree_none            | 472 ms                                                 | 252 ms: 1.87x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 243 ms: 1.85x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.79x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                  |
| nbody          | 97.0 ms                                                | 90.8 ms: 1.07x faster                                                  |
| pidigits       | 187 ms                                                 | 202 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.04 ms: 1.19x faster                                                  |
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| regex_dna      | 212 ms                                                 | 186 ms: 1.14x faster                                                   |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                 |
| unpickle_list        | 5.29 us                                                | 4.52 us: 1.17x faster                                                  |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                   |
| pickle_dict          | 35.5 us                                                | 33.9 us: 1.05x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                  |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.34 us: 1.05x slower                                                  |
| pickle               | 11.6 us                                                | 13.5 us: 1.17x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.2 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.11 ms: 1.17x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 30.8 ms: 1.12x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 605 ms: 1.95x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 303 ms: 1.90x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 305 ms: 1.89x faster                                                   |
| async_tree_none            | 472 ms                                                 | 252 ms: 1.87x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 243 ms: 1.85x faster                                                   |
| deepcopy                   | 371 us                                                 | 244 us: 1.52x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                  |
| spectral_norm              | 115 ms                                                 | 85.8 ms: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.58 us: 1.30x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.0 ms: 1.29x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 3.95 ms: 1.28x faster                                                  |
| scimark_fft                | 382 ms                                                 | 300 ms: 1.27x faster                                                   |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.04 ms: 1.22x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 61.6 ms: 1.22x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                 |
| float                      | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                  |
| raytrace                   | 312 ms                                                 | 258 ms: 1.21x faster                                                   |
| async_generators           | 463 ms                                                 | 385 ms: 1.20x faster                                                   |
| chaos                      | 67.0 ms                                                | 55.7 ms: 1.20x faster                                                  |
| scimark_sor                | 129 ms                                                 | 108 ms: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 57.4 ms: 1.19x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.04 ms: 1.19x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                  |
| unpickle_list              | 5.29 us                                                | 4.52 us: 1.17x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 145 ms: 1.17x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.1 ms: 1.16x faster                                                  |
| pyflate                    | 482 ms                                                 | 415 ms: 1.16x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                   |
| logging_silent             | 104 ns                                                 | 90.4 ns: 1.16x faster                                                  |
| sympy_str                  | 300 ms                                                 | 262 ms: 1.15x faster                                                   |
| regex_dna                  | 212 ms                                                 | 186 ms: 1.14x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 104 ms: 1.14x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                  |
| django_template            | 34.6 ms                                                | 30.8 ms: 1.12x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 74.3 ms: 1.10x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.4 us: 1.10x faster                                                  |
| richards                   | 45.8 ms                                                | 41.7 ms: 1.10x faster                                                  |
| 2to3                       | 274 ms                                                 | 251 ms: 1.09x faster                                                   |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.7 ms: 1.08x faster                                                  |
| sympy_expand               | 478 ms                                                 | 445 ms: 1.08x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.00 ms: 1.07x faster                                                  |
| nbody                      | 97.0 ms                                                | 90.8 ms: 1.07x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.67 us: 1.06x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                   |
| nqueens                    | 83.3 ms                                                | 79.4 ms: 1.05x faster                                                  |
| pickle_dict                | 35.5 us                                                | 33.9 us: 1.05x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.2 ms: 1.05x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 469 ms: 1.05x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 755 ms: 1.03x faster                                                   |
| typing_runtime_protocols   | 158 us                                                 | 154 us: 1.03x faster                                                   |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                   |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.34 us: 1.05x slower                                                  |
| telco                      | 7.10 ms                                                | 7.47 ms: 1.05x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 57.0 ns: 1.06x slower                                                  |
| pidigits                   | 187 ms                                                 | 202 ms: 1.08x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.92 sec: 1.11x slower                                                 |
| coverage                   | 72.7 ms                                                | 80.8 ms: 1.11x slower                                                  |
| pickle                     | 11.6 us                                                | 13.5 us: 1.17x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.11 ms: 1.17x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 12.2 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.86 ms: 1.28x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.55 ms: 1.73x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (4): xml_etree_parse, asyncio_websockets, json, mako
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.142x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x