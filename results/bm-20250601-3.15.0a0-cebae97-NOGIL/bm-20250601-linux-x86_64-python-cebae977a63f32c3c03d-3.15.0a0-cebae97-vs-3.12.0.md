# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.154x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 340 ms: 1.24x slower                                                  |
| docutils       | 2.77 sec                                               | 3.15 sec: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 601 ms: 1.97x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 637 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 261 ms: 1.72x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 339 ms: 1.70x faster                                                  |
| async_tree_none            | 472 ms                                                 | 300 ms: 1.57x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 377 ms: 1.53x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 580 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 621 ms: 1.17x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.57x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.4 ms: 1.05x faster                                                 |
| pidigits       | 187 ms                                                 | 199 ms: 1.06x slower                                                  |
| nbody          | 97.0 ms                                                | 151 ms: 1.55x slower                                                  |
| Geometric mean | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                 |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                 |
| regex_compile  | 148 ms                                                 | 172 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| pickle_dict          | 35.5 us                                                | 36.0 us: 1.01x slower                                                 |
| xml_etree_parse      | 159 ms                                                 | 165 ms: 1.03x slower                                                  |
| tomli_loads          | 2.33 sec                                               | 2.60 sec: 1.12x slower                                                |
| pickle_list          | 5.08 us                                                | 5.77 us: 1.13x slower                                                 |
| unpickle_list        | 5.29 us                                                | 6.36 us: 1.20x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 418 us: 1.29x slower                                                  |
| pickle               | 11.6 us                                                | 15.1 us: 1.30x slower                                                 |
| json_loads           | 28.5 us                                                | 37.4 us: 1.31x slower                                                 |
| unpickle_pure_python | 230 us                                                 | 304 us: 1.32x slower                                                  |
| unpickle             | 15.9 us                                                | 22.0 us: 1.39x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 124 ms: 1.39x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 86.8 ms: 1.41x slower                                                 |
| json_dumps           | 10.4 ms                                                | 15.2 ms: 1.47x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.23x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 10.00 ms: 1.44x slower                                                |
| python_startup         | 9.55 ms                                                | 17.1 ms: 1.79x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.61x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 52.6 ms: 1.52x slower                                                 |
| mako            | 11.9 ms                                                | 19.0 ms: 1.60x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.56x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 601 ms: 1.97x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 637 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 261 ms: 1.72x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 339 ms: 1.70x faster                                                  |
| async_tree_none            | 472 ms                                                 | 300 ms: 1.57x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 377 ms: 1.53x faster                                                  |
| mdp                        | 2.63 sec                                               | 1.73 sec: 1.52x faster                                                |
| gc_traversal               | 3.79 ms                                                | 2.74 ms: 1.39x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 580 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 621 ms: 1.17x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                 |
| float                      | 84.7 ms                                                | 80.4 ms: 1.05x faster                                                 |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                  |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| pickle_dict                | 35.5 us                                                | 36.0 us: 1.01x slower                                                 |
| pathlib                    | 19.3 ms                                                | 19.7 ms: 1.02x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 165 ms: 1.03x slower                                                  |
| comprehensions             | 21.8 us                                                | 22.6 us: 1.04x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 72.7 ms: 1.06x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 57.3 ns: 1.06x slower                                                 |
| pidigits                   | 187 ms                                                 | 199 ms: 1.06x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.30 sec: 1.10x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 545 ms: 1.11x slower                                                  |
| tomli_loads                | 2.33 sec                                               | 2.60 sec: 1.12x slower                                                |
| generators                 | 31.2 ms                                                | 35.0 ms: 1.12x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 3.21 us: 1.13x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.77 us: 1.13x slower                                                 |
| docutils                   | 2.77 sec                                               | 3.15 sec: 1.14x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.04 sec: 1.14x slower                                                |
| pyflate                    | 482 ms                                                 | 552 ms: 1.14x slower                                                  |
| regex_compile              | 148 ms                                                 | 172 ms: 1.16x slower                                                  |
| spectral_norm              | 115 ms                                                 | 134 ms: 1.16x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 25.0 ms: 1.17x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 198 ms: 1.17x slower                                                  |
| scimark_sor                | 129 ms                                                 | 155 ms: 1.20x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                | 4.02 us: 1.20x slower                                                 |
| unpickle_list              | 5.29 us                                                | 6.36 us: 1.20x slower                                                 |
| meteor_contest             | 112 ms                                                 | 135 ms: 1.20x slower                                                  |
| deltablue                  | 3.72 ms                                                | 4.54 ms: 1.22x slower                                                 |
| sympy_str                  | 300 ms                                                 | 366 ms: 1.22x slower                                                  |
| chaos                      | 67.0 ms                                                | 82.0 ms: 1.22x slower                                                 |
| 2to3                       | 274 ms                                                 | 340 ms: 1.24x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.95 ms: 1.24x slower                                                 |
| raytrace                   | 312 ms                                                 | 388 ms: 1.24x slower                                                  |
| scimark_fft                | 382 ms                                                 | 477 ms: 1.25x slower                                                  |
| json                       | 5.26 ms                                                | 6.62 ms: 1.26x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.88 ms: 1.27x slower                                                 |
| coroutines                 | 23.2 ms                                                | 29.5 ms: 1.27x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 418 us: 1.29x slower                                                  |
| pickle                     | 11.6 us                                                | 15.1 us: 1.30x slower                                                 |
| sympy_expand               | 478 ms                                                 | 624 ms: 1.31x slower                                                  |
| json_loads                 | 28.5 us                                                | 37.4 us: 1.31x slower                                                 |
| unpickle_pure_python       | 230 us                                                 | 304 us: 1.32x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 101 ms: 1.35x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.89 ms: 1.36x slower                                                 |
| crypto_pyaes               | 81.9 ms                                                | 112 ms: 1.37x slower                                                  |
| unpickle                   | 15.9 us                                                | 22.0 us: 1.39x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 124 ms: 1.39x slower                                                  |
| fannkuch                   | 417 ms                                                 | 581 ms: 1.39x slower                                                  |
| logging_simple             | 6.46 us                                                | 9.07 us: 1.40x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 86.8 ms: 1.41x slower                                                 |
| logging_format             | 7.23 us                                                | 10.2 us: 1.41x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 167 ms: 1.41x slower                                                  |
| nqueens                    | 83.3 ms                                                | 118 ms: 1.42x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 10.00 ms: 1.44x slower                                                |
| richards                   | 45.8 ms                                                | 67.0 ms: 1.46x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 15.2 ms: 1.47x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 235 us: 1.49x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 1.17 sec: 1.51x slower                                                |
| django_template            | 34.6 ms                                                | 52.6 ms: 1.52x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 2.41 sec: 1.54x slower                                                |
| richards_super             | 51.5 ms                                                | 79.7 ms: 1.55x slower                                                 |
| nbody                      | 97.0 ms                                                | 151 ms: 1.55x slower                                                  |
| mako                       | 11.9 ms                                                | 19.0 ms: 1.60x slower                                                 |
| telco                      | 7.10 ms                                                | 11.8 ms: 1.66x slower                                                 |
| python_startup             | 9.55 ms                                                | 17.1 ms: 1.79x slower                                                 |
| coverage                   | 72.7 ms                                                | 133 ms: 1.83x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.51 ms: 4.17x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 112 ms: 4.67x slower                                                  |
| logging_silent             | 104 ns                                                 | 720 ns: 6.89x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x slower                                                          |

Benchmark hidden because not significant (4): deepcopy, go, asyncio_websockets, deepcopy_memo
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.154x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.37x