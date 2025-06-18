# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.034x slower
- HPT reliability: 93.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 292 ms: 1.06x slower                                                  |
| docutils       | 2.77 sec                                               | 2.85 sec: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 676 ms: 1.75x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 663 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 347 ms: 1.67x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 346 ms: 1.66x faster                                                  |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 276 ms: 1.63x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 602 ms: 1.21x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.55x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.3 ms: 1.13x faster                                                 |
| pidigits       | 187 ms                                                 | 205 ms: 1.09x slower                                                  |
| nbody          | 97.0 ms                                                | 106 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.93 ms: 1.23x faster                                                 |
| regex_dna      | 212 ms                                                 | 197 ms: 1.08x faster                                                  |
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.22 sec: 1.05x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 112 ms: 1.05x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.68 us: 1.07x slower                                                 |
| pickle_dict          | 35.5 us                                                | 38.2 us: 1.08x slower                                                 |
| unpickle_pure_python | 230 us                                                 | 259 us: 1.13x slower                                                  |
| pickle_pure_python   | 324 us                                                 | 374 us: 1.15x slower                                                  |
| pickle_list          | 5.08 us                                                | 6.06 us: 1.19x slower                                                 |
| json_loads           | 28.5 us                                                | 34.0 us: 1.19x slower                                                 |
| unpickle             | 15.9 us                                                | 19.1 us: 1.20x slower                                                 |
| xml_etree_process    | 61.7 ms                                                | 74.4 ms: 1.21x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 108 ms: 1.21x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| pickle               | 11.6 us                                                | 15.1 us: 1.30x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.40 ms: 1.07x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.6 ms: 1.14x slower                                                 |
| django_template | 34.6 ms                                                | 40.8 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.47 sec: 1.79x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 676 ms: 1.75x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 663 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 347 ms: 1.67x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 346 ms: 1.66x faster                                                  |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 276 ms: 1.63x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 2.93 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 602 ms: 1.21x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 34.1 us: 1.19x faster                                                 |
| deepcopy                   | 371 us                                                 | 315 us: 1.18x faster                                                  |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                  |
| comprehensions             | 21.8 us                                                | 19.3 us: 1.13x faster                                                 |
| float                      | 84.7 ms                                                | 75.3 ms: 1.13x faster                                                 |
| async_generators           | 463 ms                                                 | 413 ms: 1.12x faster                                                  |
| regex_dna                  | 212 ms                                                 | 197 ms: 1.08x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 63.8 ms: 1.07x faster                                                 |
| pathlib                    | 19.3 ms                                                | 18.4 ms: 1.05x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.22 sec: 1.05x faster                                                |
| pyflate                    | 482 ms                                                 | 465 ms: 1.04x faster                                                  |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.9 ms: 1.02x faster                                                 |
| unpack_sequence            | 54.0 ns                                                | 53.0 ns: 1.02x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 166 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.32 us: 1.01x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 488 ms: 1.01x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.02x slower                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 76.4 ms: 1.02x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.02x slower                                                  |
| raytrace                   | 312 ms                                                 | 320 ms: 1.03x slower                                                  |
| sympy_str                  | 300 ms                                                 | 308 ms: 1.03x slower                                                  |
| chaos                      | 67.0 ms                                                | 68.8 ms: 1.03x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.85 sec: 1.03x slower                                                |
| meteor_contest             | 112 ms                                                 | 116 ms: 1.04x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.65 ms: 1.04x slower                                                 |
| deltablue                  | 3.72 ms                                                | 3.86 ms: 1.04x slower                                                 |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                 |
| crypto_pyaes               | 81.9 ms                                                | 85.6 ms: 1.05x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 112 ms: 1.05x slower                                                  |
| scimark_fft                | 382 ms                                                 | 403 ms: 1.05x slower                                                  |
| generators                 | 31.2 ms                                                | 33.0 ms: 1.06x slower                                                 |
| 2to3                       | 274 ms                                                 | 292 ms: 1.06x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.40 ms: 1.07x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.26 sec: 1.07x slower                                                |
| unpickle_list              | 5.29 us                                                | 5.68 us: 1.07x slower                                                 |
| pickle_dict                | 35.5 us                                                | 38.2 us: 1.08x slower                                                 |
| pidigits                   | 187 ms                                                 | 205 ms: 1.09x slower                                                  |
| nbody                      | 97.0 ms                                                | 106 ms: 1.10x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.61 ms: 1.11x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 3.18 us: 1.12x slower                                                 |
| unpickle_pure_python       | 230 us                                                 | 259 us: 1.13x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 133 ms: 1.13x slower                                                  |
| sympy_expand               | 478 ms                                                 | 541 ms: 1.13x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 958 us: 1.14x slower                                                  |
| mako                       | 11.9 ms                                                | 13.6 ms: 1.14x slower                                                 |
| fannkuch                   | 417 ms                                                 | 479 ms: 1.15x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 374 us: 1.15x slower                                                  |
| logging_simple             | 6.46 us                                                | 7.47 us: 1.16x slower                                                 |
| json                       | 5.26 ms                                                | 6.08 ms: 1.16x slower                                                 |
| coroutines                 | 23.2 ms                                                | 26.8 ms: 1.16x slower                                                 |
| logging_format             | 7.23 us                                                | 8.43 us: 1.17x slower                                                 |
| django_template            | 34.6 ms                                                | 40.8 ms: 1.18x slower                                                 |
| nqueens                    | 83.3 ms                                                | 98.2 ms: 1.18x slower                                                 |
| richards                   | 45.8 ms                                                | 54.3 ms: 1.19x slower                                                 |
| pickle_list                | 5.08 us                                                | 6.06 us: 1.19x slower                                                 |
| json_loads                 | 28.5 us                                                | 34.0 us: 1.19x slower                                                 |
| unpickle                   | 15.9 us                                                | 19.1 us: 1.20x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 74.4 ms: 1.21x slower                                                 |
| richards_super             | 51.5 ms                                                | 62.2 ms: 1.21x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 108 ms: 1.21x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 198 us: 1.25x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 993 ms: 1.28x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 2.01 sec: 1.28x slower                                                |
| json_dumps                 | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| pickle                     | 11.6 us                                                | 15.1 us: 1.30x slower                                                 |
| telco                      | 7.10 ms                                                | 9.52 ms: 1.34x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.14 ms: 1.35x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| coverage                   | 72.7 ms                                                | 102 ms: 1.40x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.63 ms: 1.78x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 105 ms: 4.39x slower                                                  |
| logging_silent             | 104 ns                                                 | 623 ns: 5.96x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                          |
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 93.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x