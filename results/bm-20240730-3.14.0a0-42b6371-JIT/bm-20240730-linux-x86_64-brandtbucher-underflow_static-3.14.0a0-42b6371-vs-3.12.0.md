# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 42b6371
- commit date: 2024-07-30
- overall geometric mean: 1.08x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                    |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                  |
| tornado_http   | 103 ms                                                 | 94.0 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                                    |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 400 ms: 1.44x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 913 ms: 1.27x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.2 ms: 1.22x faster                                                   |
| float          | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                   |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                   |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 207 us: 1.11x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                    |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.91 ms: 1.20x faster                                                   |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.8 us: 1.52x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                                    |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 400 ms: 1.44x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                    |
| deepcopy                   | 371 us                                                 | 277 us: 1.34x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 913 ms: 1.27x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 59.6 ms: 1.26x faster                                                   |
| scimark_fft                | 382 ms                                                 | 303 ms: 1.26x faster                                                    |
| nbody                      | 97.0 ms                                                | 79.2 ms: 1.22x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 67.8 ms: 1.21x faster                                                   |
| mako                       | 11.9 ms                                                | 9.91 ms: 1.20x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                   |
| float                      | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.27 ms: 1.18x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                  |
| richards                   | 45.8 ms                                                | 39.3 ms: 1.17x faster                                                   |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                   |
| richards_super             | 51.5 ms                                                | 44.9 ms: 1.15x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                   |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                    |
| fannkuch                   | 417 ms                                                 | 368 ms: 1.13x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.71 us: 1.13x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                   |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 207 us: 1.11x faster                                                    |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                   |
| tornado_http               | 103 ms                                                 | 94.0 ms: 1.09x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                    |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                    |
| chaos                      | 67.0 ms                                                | 62.4 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.55 ms: 1.07x faster                                                   |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                   |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 822 us: 1.02x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                   |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                    |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                   |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                    |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                    |
| async_generators           | 463 ms                                                 | 465 ms: 1.00x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                    |
| nqueens                    | 83.3 ms                                                | 84.1 ms: 1.01x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                    |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.01x slower                                                    |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 507 ms: 1.03x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 57.4 ms: 1.05x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                   |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.78 sec: 1.06x slower                                                  |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                   |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.82 ms: 1.06x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.07x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                  |
| sympy_expand               | 478 ms                                                 | 515 ms: 1.08x slower                                                    |
| generators                 | 31.2 ms                                                | 33.8 ms: 1.08x slower                                                   |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                    |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                   |
| coverage                   | 72.7 ms                                                | 91.2 ms: 1.25x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                            |

Benchmark hidden because not significant (2): bench_mp_pool, scimark_sor
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240730-3.14.0a0-42b6371-JIT/bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x