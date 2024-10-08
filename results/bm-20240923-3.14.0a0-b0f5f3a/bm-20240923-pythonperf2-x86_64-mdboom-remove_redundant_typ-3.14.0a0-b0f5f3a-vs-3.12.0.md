# Results vs. 3.12.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.03x faster
- HPT reliability: 91.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 398 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 781 ms: 1.35x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 809 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 563 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 78.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 235 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 85.4 ms: 1.01x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 32.7 us: 1.01x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.73 us: 1.01x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.0 us: 1.01x slower                                                       |
| pickle               | 10.5 us                                                      | 10.7 us: 1.01x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.64 us: 1.05x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 224 us: 1.07x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.59 sec: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| django_template | 38.2 ms                                                      | 40.3 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 398 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 781 ms: 1.35x faster                                                        |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.9 ms: 1.30x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 809 ms: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 563 ms: 1.24x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.0 us: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.86 us: 1.18x faster                                                       |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 48.1 ns: 1.10x faster                                                       |
| go                         | 150 ms                                                       | 136 ms: 1.10x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 867 us: 1.10x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.6 ms: 1.09x faster                                                       |
| async_generators           | 390 ms                                                       | 358 ms: 1.09x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.93 us: 1.08x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.37 us: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                        |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.8 ms: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| chaos                      | 64.0 ms                                                      | 62.6 ms: 1.02x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 88.3 ms: 1.02x faster                                                       |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 85.4 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 802 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 32.7 us: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 57.9 ms: 1.01x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                      |
| scimark_fft                | 301 ms                                                       | 304 ms: 1.01x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.1 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 4.73 us: 1.01x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.0 us: 1.01x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.02x slower                                                        |
| float                      | 76.6 ms                                                      | 78.7 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.29 ms: 1.03x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.19 ms: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.04x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.64 us: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.4 ms: 1.05x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.3 ms: 1.06x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 224 us: 1.07x slower                                                        |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.07x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.0 ms: 1.09x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.2 ms: 1.10x slower                                                       |
| pyflate                    | 439 ms                                                       | 489 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.11 ms: 1.16x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.59 sec: 1.20x slower                                                      |
| coverage                   | 66.7 ms                                                      | 80.2 ms: 1.20x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.87 ms: 1.40x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (4): sqlite_synth, pprint_pformat, bench_mp_pool, nbody
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 91.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x