# Results vs. 3.12.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                |
| tornado_http   | 103 ms                                                 | 90.4 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 867 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.6 ms: 1.12x faster                                                 |
| nbody          | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.89 ms: 1.08x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                |
| pickle_dict          | 35.5 us                                                | 32.7 us: 1.09x faster                                                 |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.03x faster                                                  |
| unpickle_list        | 5.29 us                                                | 5.15 us: 1.03x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| pickle_list          | 5.08 us                                                | 4.98 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 867 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                  |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                  |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                 |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 72.0 ms: 1.14x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.4 ms: 1.14x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 75.6 ms: 1.12x faster                                                 |
| nbody                      | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                 |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 708 ms: 1.10x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                 |
| unpack_sequence            | 54.0 ns                                                | 49.3 ns: 1.09x faster                                                 |
| pickle_dict                | 35.5 us                                                | 32.7 us: 1.09x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| async_generators           | 463 ms                                                 | 430 ms: 1.08x faster                                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 789 us: 1.07x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                  |
| json                       | 5.26 ms                                                | 4.94 ms: 1.06x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 64.8 ms: 1.06x faster                                                 |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                |
| nqueens                    | 83.3 ms                                                | 79.4 ms: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                 |
| scimark_fft                | 382 ms                                                 | 370 ms: 1.03x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 477 ms: 1.03x faster                                                  |
| unpickle_list              | 5.29 us                                                | 5.15 us: 1.03x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                  |
| pickle_list                | 5.08 us                                                | 4.98 us: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.95 ms: 1.02x faster                                                 |
| pyflate                    | 482 ms                                                 | 473 ms: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                 |
| richards                   | 45.8 ms                                                | 45.4 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.83 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.89 ms: 1.08x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| coverage                   | 72.7 ms                                                | 83.7 ms: 1.15x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                                 |
| telco                      | 7.10 ms                                                | 8.43 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (6): unpickle, pycparser, asyncio_tcp_ssl, bench_mp_pool, richards_super, logging_silent
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.090x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x