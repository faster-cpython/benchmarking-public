# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d57f8a9
- commit date: 2024-08-02
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                 | 319 ms: 1.16x slower                                  |
| docutils       | 2.77 sec                                               | 3.17 sec: 1.14x slower                                |
| tornado_http   | 103 ms                                                 | 97.6 ms: 1.05x faster                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 408 ms: 1.41x faster                                  |
| async_tree_none            | 472 ms                                                 | 345 ms: 1.37x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 886 ms: 1.33x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 545 ms: 1.33x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 448 ms: 1.29x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 579 ms: 1.25x faster                                  |
| async_tree_io              | 1.16 sec                                               | 940 ms: 1.23x faster                                  |
| Geometric mean             | (ref)                                                  | 1.33x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                  |
| float          | 84.7 ms                                                | 86.2 ms: 1.02x slower                                 |
| nbody          | 97.0 ms                                                | 122 ms: 1.26x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                 |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                  |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                 |
| regex_compile  | 148 ms                                                 | 184 ms: 1.24x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                  |
| xml_etree_iterparse  | 107 ms                                                 | 109 ms: 1.02x slower                                  |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                 |
| xml_etree_generate   | 89.2 ms                                                | 93.7 ms: 1.05x slower                                 |
| xml_etree_process    | 61.7 ms                                                | 65.0 ms: 1.05x slower                                 |
| tomli_loads          | 2.33 sec                                               | 2.57 sec: 1.10x slower                                |
| unpickle_pure_python | 230 us                                                 | 272 us: 1.18x slower                                  |
| pickle_pure_python   | 324 us                                                 | 404 us: 1.25x slower                                  |
| Geometric mean       | (ref)                                                  | 1.07x slower                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.9 ms: 1.17x slower                                 |
| django_template | 34.6 ms                                                | 41.4 ms: 1.20x slower                                 |
| Geometric mean  | (ref)                                                  | 1.18x slower                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 408 ms: 1.41x faster                                  |
| async_tree_none            | 472 ms                                                 | 345 ms: 1.37x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 886 ms: 1.33x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 545 ms: 1.33x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 448 ms: 1.29x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 579 ms: 1.25x faster                                  |
| async_tree_io              | 1.16 sec                                               | 940 ms: 1.23x faster                                  |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                 |
| deepcopy                   | 371 us                                                 | 333 us: 1.11x faster                                  |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                  |
| tornado_http               | 103 ms                                                 | 97.6 ms: 1.05x faster                                 |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                 |
| deepcopy_reduce            | 3.35 us                                                | 3.24 us: 1.03x faster                                 |
| logging_simple             | 6.46 us                                                | 6.33 us: 1.02x faster                                 |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                  |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                  |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                  |
| deepcopy_memo              | 40.7 us                                                | 41.0 us: 1.01x slower                                 |
| dask                       | 372 ms                                                 | 377 ms: 1.01x slower                                  |
| raytrace                   | 312 ms                                                 | 318 ms: 1.02x slower                                  |
| float                      | 84.7 ms                                                | 86.2 ms: 1.02x slower                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                |
| bench_thread_pool          | 842 us                                                 | 862 us: 1.02x slower                                  |
| xml_etree_iterparse        | 107 ms                                                 | 109 ms: 1.02x slower                                  |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                 |
| asyncio_tcp                | 491 ms                                                 | 509 ms: 1.04x slower                                  |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                 |
| xml_etree_generate         | 89.2 ms                                                | 93.7 ms: 1.05x slower                                 |
| xml_etree_process          | 61.7 ms                                                | 65.0 ms: 1.05x slower                                 |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                  |
| sympy_sum                  | 169 ms                                                 | 180 ms: 1.06x slower                                  |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                 |
| deltablue                  | 3.72 ms                                                | 4.04 ms: 1.09x slower                                 |
| meteor_contest             | 112 ms                                                 | 123 ms: 1.09x slower                                  |
| comprehensions             | 21.8 us                                                | 23.8 us: 1.09x slower                                 |
| crypto_pyaes               | 81.9 ms                                                | 90.0 ms: 1.10x slower                                 |
| tomli_loads                | 2.33 sec                                               | 2.57 sec: 1.10x slower                                |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                 |
| sympy_str                  | 300 ms                                                 | 333 ms: 1.11x slower                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 84.4 ms: 1.12x slower                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.71 ms: 1.13x slower                                 |
| mdp                        | 2.63 sec                                               | 2.97 sec: 1.13x slower                                |
| sympy_integrate            | 21.4 ms                                                | 24.3 ms: 1.13x slower                                 |
| scimark_fft                | 382 ms                                                 | 436 ms: 1.14x slower                                  |
| docutils                   | 2.77 sec                                               | 3.17 sec: 1.14x slower                                |
| coverage                   | 72.7 ms                                                | 83.6 ms: 1.15x slower                                 |
| 2to3                       | 274 ms                                                 | 319 ms: 1.16x slower                                  |
| mako                       | 11.9 ms                                                | 13.9 ms: 1.17x slower                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.96 ms: 1.17x slower                                 |
| scimark_lu                 | 118 ms                                                 | 138 ms: 1.17x slower                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.60 ms: 1.18x slower                                 |
| sympy_expand               | 478 ms                                                 | 564 ms: 1.18x slower                                  |
| unpickle_pure_python       | 230 us                                                 | 272 us: 1.18x slower                                  |
| typing_runtime_protocols   | 158 us                                                 | 187 us: 1.19x slower                                  |
| chaos                      | 67.0 ms                                                | 79.5 ms: 1.19x slower                                 |
| pyflate                    | 482 ms                                                 | 574 ms: 1.19x slower                                  |
| fannkuch                   | 417 ms                                                 | 498 ms: 1.19x slower                                  |
| sqlglot_optimize           | 54.8 ms                                                | 65.5 ms: 1.19x slower                                 |
| django_template            | 34.6 ms                                                | 41.4 ms: 1.20x slower                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                 |
| pycparser                  | 1.18 sec                                               | 1.43 sec: 1.21x slower                                |
| scimark_sor                | 129 ms                                                 | 158 ms: 1.22x slower                                  |
| pprint_safe_repr           | 776 ms                                                 | 951 ms: 1.23x slower                                  |
| sqlglot_normalize          | 110 ms                                                 | 136 ms: 1.23x slower                                  |
| telco                      | 7.10 ms                                                | 8.79 ms: 1.24x slower                                 |
| nqueens                    | 83.3 ms                                                | 103 ms: 1.24x slower                                  |
| richards                   | 45.8 ms                                                | 56.9 ms: 1.24x slower                                 |
| regex_compile              | 148 ms                                                 | 184 ms: 1.24x slower                                  |
| richards_super             | 51.5 ms                                                | 64.0 ms: 1.24x slower                                 |
| pickle_pure_python         | 324 us                                                 | 404 us: 1.25x slower                                  |
| spectral_norm              | 115 ms                                                 | 144 ms: 1.25x slower                                  |
| nbody                      | 97.0 ms                                                | 122 ms: 1.26x slower                                  |
| pprint_pformat             | 1.57 sec                                               | 1.98 sec: 1.26x slower                                |
| go                         | 139 ms                                                 | 177 ms: 1.27x slower                                  |
| generators                 | 31.2 ms                                                | 43.4 ms: 1.39x slower                                 |
| logging_silent             | 104 ns                                                 | 146 ns: 1.40x slower                                  |
| hexiom                     | 6.41 ms                                                | 9.64 ms: 1.50x slower                                 |
| Geometric mean             | (ref)                                                  | 1.07x slower                                          |

Benchmark hidden because not significant (5): json_loads, json, bench_mp_pool, coroutines, logging_format
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240802-3.14.0a0-d57f8a9-PYTHON_UOPS/bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 0.99x