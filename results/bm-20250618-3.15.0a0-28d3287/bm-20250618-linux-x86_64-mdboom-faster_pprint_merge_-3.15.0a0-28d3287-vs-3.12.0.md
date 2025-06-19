# Results vs. 3.12.0

- fork: mdboom
- ref: faster_pprint_merge_
- machine: linux-x86_64
- commit hash: 28d3287
- commit date: 2025-06-18
- overall geometric mean: 1.013x slower
- HPT reliability: 90.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 292 ms: 1.07x slower                                                  |
| docutils       | 2.77 sec                                               | 2.85 sec: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 676 ms: 1.75x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 663 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 346 ms: 1.67x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 346 ms: 1.66x faster                                                  |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 277 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 594 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 602 ms: 1.21x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.55x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                 |
| pidigits       | 187 ms                                                 | 205 ms: 1.09x slower                                                  |
| nbody          | 97.0 ms                                                | 106 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.93 ms: 1.23x faster                                                 |
| regex_dna      | 212 ms                                                 | 196 ms: 1.08x faster                                                  |
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.22 sec: 1.05x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 112 ms: 1.05x slower                                                  |
| unpickle_pure_python | 230 us                                                 | 256 us: 1.11x slower                                                  |
| pickle_pure_python   | 324 us                                                 | 374 us: 1.15x slower                                                  |
| json_loads           | 28.5 us                                                | 33.9 us: 1.19x slower                                                 |
| xml_etree_process    | 61.7 ms                                                | 74.3 ms: 1.20x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 108 ms: 1.21x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.39 ms: 1.07x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.6 ms: 1.15x slower                                                 |
| django_template | 34.6 ms                                                | 41.0 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.17x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.47 sec: 1.79x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 676 ms: 1.75x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 663 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 346 ms: 1.67x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 346 ms: 1.66x faster                                                  |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 277 ms: 1.62x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 2.93 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 594 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 602 ms: 1.21x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 34.0 us: 1.20x faster                                                 |
| deepcopy                   | 371 us                                                 | 316 us: 1.18x faster                                                  |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                  |
| comprehensions             | 21.8 us                                                | 19.3 us: 1.13x faster                                                 |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                 |
| regex_dna                  | 212 ms                                                 | 196 ms: 1.08x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 63.6 ms: 1.08x faster                                                 |
| pathlib                    | 19.3 ms                                                | 18.4 ms: 1.05x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.22 sec: 1.05x faster                                                |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                                  |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.9 ms: 1.02x faster                                                 |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 166 ms: 1.02x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.02x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 76.8 ms: 1.02x slower                                                 |
| chaos                      | 67.0 ms                                                | 68.7 ms: 1.03x slower                                                 |
| raytrace                   | 312 ms                                                 | 321 ms: 1.03x slower                                                  |
| sympy_str                  | 300 ms                                                 | 308 ms: 1.03x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.85 sec: 1.03x slower                                                |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                 |
| deltablue                  | 3.72 ms                                                | 3.85 ms: 1.04x slower                                                 |
| meteor_contest             | 112 ms                                                 | 116 ms: 1.04x slower                                                  |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 85.6 ms: 1.05x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 112 ms: 1.05x slower                                                  |
| generators                 | 31.2 ms                                                | 33.0 ms: 1.06x slower                                                 |
| scimark_fft                | 382 ms                                                 | 404 ms: 1.06x slower                                                  |
| 2to3                       | 274 ms                                                 | 292 ms: 1.07x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.39 ms: 1.07x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.26 sec: 1.07x slower                                                |
| pidigits                   | 187 ms                                                 | 205 ms: 1.09x slower                                                  |
| nbody                      | 97.0 ms                                                | 106 ms: 1.10x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.59 ms: 1.11x slower                                                 |
| unpickle_pure_python       | 230 us                                                 | 256 us: 1.11x slower                                                  |
| sympy_expand               | 478 ms                                                 | 535 ms: 1.12x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 133 ms: 1.13x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 3.20 us: 1.13x slower                                                 |
| fannkuch                   | 417 ms                                                 | 478 ms: 1.15x slower                                                  |
| mako                       | 11.9 ms                                                | 13.6 ms: 1.15x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 374 us: 1.15x slower                                                  |
| logging_simple             | 6.46 us                                                | 7.47 us: 1.16x slower                                                 |
| coroutines                 | 23.2 ms                                                | 26.8 ms: 1.16x slower                                                 |
| logging_format             | 7.23 us                                                | 8.41 us: 1.16x slower                                                 |
| json                       | 5.26 ms                                                | 6.12 ms: 1.16x slower                                                 |
| django_template            | 34.6 ms                                                | 41.0 ms: 1.19x slower                                                 |
| nqueens                    | 83.3 ms                                                | 98.9 ms: 1.19x slower                                                 |
| json_loads                 | 28.5 us                                                | 33.9 us: 1.19x slower                                                 |
| richards                   | 45.8 ms                                                | 54.8 ms: 1.20x slower                                                 |
| richards_super             | 51.5 ms                                                | 61.8 ms: 1.20x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 74.3 ms: 1.20x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 108 ms: 1.21x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 198 us: 1.26x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 987 ms: 1.27x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 2.00 sec: 1.28x slower                                                |
| json_dumps                 | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| telco                      | 7.10 ms                                                | 9.42 ms: 1.33x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.14 ms: 1.35x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| coverage                   | 72.7 ms                                                | 102 ms: 1.40x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.79x slower                                                 |
| logging_silent             | 104 ns                                                 | 626 ns: 6.00x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (1): deepcopy_reduce
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250618-3.15.0a0-28d3287/bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 90.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x