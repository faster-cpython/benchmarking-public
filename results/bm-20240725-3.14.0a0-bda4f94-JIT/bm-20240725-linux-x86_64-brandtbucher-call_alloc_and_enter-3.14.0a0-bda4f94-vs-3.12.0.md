# Results vs. 3.12.0

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: bda4f94
- commit date: 2024-07-25
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                        |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.04x slower                                                      |
| tornado_http   | 103 ms                                                 | 92.3 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                        |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 525 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 864 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 898 ms: 1.29x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.9 ms: 1.21x faster                                                       |
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                       |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                        |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                       |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                        |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 525 ms: 1.38x faster                                                        |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 864 ms: 1.37x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 898 ms: 1.29x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 60.7 ms: 1.24x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 66.3 ms: 1.23x faster                                                       |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                        |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                       |
| nbody                      | 97.0 ms                                                | 79.9 ms: 1.21x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                      |
| mako                       | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                       |
| logging_format             | 7.23 us                                                | 6.09 us: 1.19x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.29 ms: 1.18x faster                                                       |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                       |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| richards                   | 45.8 ms                                                | 40.5 ms: 1.13x faster                                                       |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                       |
| pyflate                    | 482 ms                                                 | 433 ms: 1.11x faster                                                        |
| tornado_http               | 103 ms                                                 | 92.3 ms: 1.11x faster                                                       |
| fannkuch                   | 417 ms                                                 | 377 ms: 1.11x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                       |
| richards_super             | 51.5 ms                                                | 46.9 ms: 1.10x faster                                                       |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.51 ms: 1.06x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.03x faster                                                       |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                       |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 824 us: 1.02x faster                                                        |
| sympy_str                  | 300 ms                                                 | 294 ms: 1.02x faster                                                        |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                        |
| dask                       | 372 ms                                                 | 366 ms: 1.02x faster                                                        |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| asyncio_tcp                | 491 ms                                                 | 486 ms: 1.01x faster                                                        |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.53 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 55.9 ms: 1.02x slower                                                       |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                        |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                       |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                      |
| nqueens                    | 83.3 ms                                                | 86.0 ms: 1.03x slower                                                       |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 22.2 ms: 1.03x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                       |
| sympy_expand               | 478 ms                                                 | 499 ms: 1.04x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.04x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.08x slower                                                        |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                                        |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                       |
| coverage                   | 72.7 ms                                                | 91.6 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (3): sympy_sum, bench_mp_pool, json_dumps
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240725-3.14.0a0-bda4f94-JIT/bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x