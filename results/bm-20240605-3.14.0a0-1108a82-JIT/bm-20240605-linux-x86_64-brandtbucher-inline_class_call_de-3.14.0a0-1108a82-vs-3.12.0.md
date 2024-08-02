# Results vs. 3.12.0

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 1108a82
- commit date: 2024-06-05
- overall geometric mean: 1.03x faster
- HPT reliability: 97.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                        |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.06x slower                                                      |
| tornado_http   | 103 ms                                                 | 97.2 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 343 ms: 1.31x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 449 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 942 ms: 1.25x faster                                                        |
| async_tree_none            | 472 ms                                                 | 380 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 599 ms: 1.21x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 980 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 638 ms: 1.14x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                       |
| float          | 84.7 ms                                                | 72.7 ms: 1.17x faster                                                       |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.86 ms: 1.07x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                       |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 82.7 ms: 1.08x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                        |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                        |
| pickle_dict          | 35.5 us                                                | 35.1 us: 1.01x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| unpickle_list        | 5.29 us                                                | 5.40 us: 1.02x slower                                                       |
| json_loads           | 28.5 us                                                | 29.4 us: 1.03x slower                                                       |
| pickle               | 11.6 us                                                | 12.2 us: 1.05x slower                                                       |
| pickle_list          | 5.08 us                                                | 5.34 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.63 ms: 1.10x slower                                                       |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                       |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 343 ms: 1.31x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 449 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 942 ms: 1.25x faster                                                        |
| async_tree_none            | 472 ms                                                 | 380 ms: 1.24x faster                                                        |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 67.4 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 599 ms: 1.21x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                      |
| nbody                      | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 980 ms: 1.18x faster                                                        |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                       |
| fannkuch                   | 417 ms                                                 | 355 ms: 1.17x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.33 ms: 1.17x faster                                                       |
| float                      | 84.7 ms                                                | 72.7 ms: 1.17x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 638 ms: 1.14x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.13x faster                                                       |
| logging_format             | 7.23 us                                                | 6.44 us: 1.12x faster                                                       |
| chaos                      | 67.0 ms                                                | 60.3 ms: 1.11x faster                                                       |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 701 ms: 1.11x faster                                                        |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                                        |
| richards                   | 45.8 ms                                                | 42.2 ms: 1.09x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                        |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 82.7 ms: 1.08x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 38.1 us: 1.07x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                        |
| richards_super             | 51.5 ms                                                | 48.5 ms: 1.06x faster                                                       |
| tornado_http               | 103 ms                                                 | 97.2 ms: 1.06x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                        |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                       |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                                       |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                       |
| generators                 | 31.2 ms                                                | 30.6 ms: 1.02x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                      |
| pickle_dict                | 35.5 us                                                | 35.1 us: 1.01x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.76 ms: 1.01x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 3.32 us: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                        |
| async_generators           | 463 ms                                                 | 466 ms: 1.01x slower                                                        |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                        |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.01x slower                                                        |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                       |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                        |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                                        |
| deepcopy                   | 371 us                                                 | 379 us: 1.02x slower                                                        |
| unpickle_list              | 5.29 us                                                | 5.40 us: 1.02x slower                                                       |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                        |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                        |
| scimark_sor                | 129 ms                                                 | 133 ms: 1.03x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.4 us: 1.03x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 57.0 ms: 1.04x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.70 ms: 1.04x slower                                                       |
| pickle                     | 11.6 us                                                | 12.2 us: 1.05x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                       |
| pickle_list                | 5.08 us                                                | 5.34 us: 1.05x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 519 ms: 1.06x slower                                                        |
| nqueens                    | 83.3 ms                                                | 88.1 ms: 1.06x slower                                                       |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.06x slower                                                      |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                        |
| sympy_expand               | 478 ms                                                 | 510 ms: 1.07x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.86 ms: 1.07x slower                                                       |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.07x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                       |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.63 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                        |
| telco                      | 7.10 ms                                                | 8.05 ms: 1.13x slower                                                       |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                       |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (4): bench_mp_pool, dulwich_log, sqlite_synth, deltablue
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.14.0a0-1108a82-JIT/bm-20240605-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-1108a82.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.63% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x