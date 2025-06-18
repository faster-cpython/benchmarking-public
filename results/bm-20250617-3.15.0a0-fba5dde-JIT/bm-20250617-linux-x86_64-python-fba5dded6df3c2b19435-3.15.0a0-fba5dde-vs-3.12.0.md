# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.025x slower
- HPT reliability: 75.61%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 299 ms: 1.09x slower                                                  |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 662 ms: 1.75x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 691 ms: 1.71x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 348 ms: 1.66x faster                                                  |
| async_tree_none            | 472 ms                                                 | 290 ms: 1.63x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 353 ms: 1.63x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 278 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 586 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 597 ms: 1.22x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.54x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                 |
| nbody          | 97.0 ms                                                | 97.8 ms: 1.01x slower                                                 |
| pidigits       | 187 ms                                                 | 207 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                 |
| regex_dna      | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| regex_compile  | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                |
| unpickle_pure_python | 230 us                                                 | 234 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| pickle_dict          | 35.5 us                                                | 38.0 us: 1.07x slower                                                 |
| xml_etree_process    | 61.7 ms                                                | 68.6 ms: 1.11x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.93 us: 1.12x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 101 ms: 1.13x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.90 us: 1.16x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 378 us: 1.17x slower                                                  |
| json_loads           | 28.5 us                                                | 33.5 us: 1.18x slower                                                 |
| unpickle             | 15.9 us                                                | 18.8 us: 1.19x slower                                                 |
| pickle               | 11.6 us                                                | 14.9 us: 1.28x slower                                                 |
| json_dumps           | 10.4 ms                                                | 13.6 ms: 1.31x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

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
| mako            | 11.9 ms                                                | 13.3 ms: 1.12x slower                                                 |
| django_template | 34.6 ms                                                | 40.9 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.49 sec: 1.77x faster                                                |
| async_tree_io              | 1.16 sec                                               | 662 ms: 1.75x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 691 ms: 1.71x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 348 ms: 1.66x faster                                                  |
| async_tree_none            | 472 ms                                                 | 290 ms: 1.63x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 353 ms: 1.63x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 278 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 586 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 597 ms: 1.22x faster                                                  |
| float                      | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                 |
| richards                   | 45.8 ms                                                | 39.1 ms: 1.17x faster                                                 |
| deepcopy                   | 371 us                                                 | 318 us: 1.17x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 35.1 us: 1.16x faster                                                 |
| richards_super             | 51.5 ms                                                | 45.9 ms: 1.12x faster                                                 |
| scimark_fft                | 382 ms                                                 | 341 ms: 1.12x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| comprehensions             | 21.8 us                                                | 20.0 us: 1.09x faster                                                 |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.44 ms: 1.08x faster                                                 |
| regex_dna                  | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| pathlib                    | 19.3 ms                                                | 18.2 ms: 1.06x faster                                                 |
| async_generators           | 463 ms                                                 | 438 ms: 1.06x faster                                                  |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 65.5 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 73.5 ms: 1.02x faster                                                 |
| regex_compile              | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.00x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 21.6 ms: 1.01x slower                                                 |
| nbody                      | 97.0 ms                                                | 97.8 ms: 1.01x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 496 ms: 1.01x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.39 us: 1.01x slower                                                 |
| unpickle_pure_python       | 230 us                                                 | 234 us: 1.02x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                |
| meteor_contest             | 112 ms                                                 | 116 ms: 1.03x slower                                                  |
| raytrace                   | 312 ms                                                 | 321 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| chaos                      | 67.0 ms                                                | 69.9 ms: 1.04x slower                                                 |
| crypto_pyaes               | 81.9 ms                                                | 85.9 ms: 1.05x slower                                                 |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.06x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                |
| sympy_str                  | 300 ms                                                 | 317 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.38 ms: 1.06x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.40 ms: 1.07x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                 |
| pickle_dict                | 35.5 us                                                | 38.0 us: 1.07x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 3.05 us: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.94 ms: 1.08x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.28 sec: 1.09x slower                                                |
| 2to3                       | 274 ms                                                 | 299 ms: 1.09x slower                                                  |
| pidigits                   | 187 ms                                                 | 207 ms: 1.11x slower                                                  |
| xml_etree_process          | 61.7 ms                                                | 68.6 ms: 1.11x slower                                                 |
| fannkuch                   | 417 ms                                                 | 465 ms: 1.11x slower                                                  |
| mako                       | 11.9 ms                                                | 13.3 ms: 1.12x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.93 us: 1.12x slower                                                 |
| generators                 | 31.2 ms                                                | 35.4 ms: 1.13x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 101 ms: 1.13x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 966 us: 1.15x slower                                                  |
| sympy_expand               | 478 ms                                                 | 552 ms: 1.15x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 136 ms: 1.16x slower                                                  |
| json                       | 5.26 ms                                                | 6.09 ms: 1.16x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.90 us: 1.16x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 378 us: 1.17x slower                                                  |
| json_loads                 | 28.5 us                                                | 33.5 us: 1.18x slower                                                 |
| django_template            | 34.6 ms                                                | 40.9 ms: 1.18x slower                                                 |
| logging_simple             | 6.46 us                                                | 7.66 us: 1.19x slower                                                 |
| logging_format             | 7.23 us                                                | 8.58 us: 1.19x slower                                                 |
| unpickle                   | 15.9 us                                                | 18.8 us: 1.19x slower                                                 |
| coroutines                 | 23.2 ms                                                | 27.6 ms: 1.19x slower                                                 |
| nqueens                    | 83.3 ms                                                | 102 ms: 1.23x slower                                                  |
| pickle                     | 11.6 us                                                | 14.9 us: 1.28x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 205 us: 1.30x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 13.6 ms: 1.31x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 1.03 sec: 1.33x slower                                                |
| pprint_pformat             | 1.57 sec                                               | 2.10 sec: 1.34x slower                                                |
| telco                      | 7.10 ms                                                | 9.58 ms: 1.35x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.19 ms: 1.37x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| coverage                   | 72.7 ms                                                | 103 ms: 1.41x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 76.8 ns: 1.42x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.79x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 105 ms: 4.37x slower                                                  |
| logging_silent             | 104 ns                                                 | 633 ns: 6.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 75.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.15x