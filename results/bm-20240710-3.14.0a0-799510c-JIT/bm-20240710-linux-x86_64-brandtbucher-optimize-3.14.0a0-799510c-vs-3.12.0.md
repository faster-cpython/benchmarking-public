# Results vs. 3.12.0

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 799510c
- commit date: 2024-07-10
- overall geometric mean: 1.02x faster
- HPT reliability: 98.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                            |
| docutils       | 2.77 sec                                               | 6.74 sec: 2.43x slower                                          |
| tornado_http   | 103 ms                                                 | 97.9 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                  | 1.32x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 382 ms: 1.50x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                            |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 863 ms: 1.37x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.32x faster                                            |
| async_tree_io              | 1.16 sec                                               | 896 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                            |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 77.4 ms: 1.25x faster                                           |
| float          | 84.7 ms                                                | 70.9 ms: 1.20x faster                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                  | 1.15x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                            |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                            |
| regex_effbot   | 3.61 ms                                                | 3.88 ms: 1.08x slower                                           |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                            |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                           |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                           |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.04x faster                                            |
| json_loads           | 28.5 us                                                | 27.4 us: 1.04x faster                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.87 ms: 1.21x faster                                           |
| django_template | 34.6 ms                                                | 40.3 ms: 1.16x slower                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 382 ms: 1.50x faster                                            |
| deepcopy_memo              | 40.7 us                                                | 27.2 us: 1.50x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                            |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                            |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 863 ms: 1.37x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.32x faster                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.32x faster                                           |
| async_tree_io              | 1.16 sec                                               | 896 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                           |
| nbody                      | 97.0 ms                                                | 77.4 ms: 1.25x faster                                           |
| crypto_pyaes               | 81.9 ms                                                | 66.6 ms: 1.23x faster                                           |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                            |
| mako                       | 11.9 ms                                                | 9.87 ms: 1.21x faster                                           |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                           |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                          |
| chaos                      | 67.0 ms                                                | 56.0 ms: 1.20x faster                                           |
| float                      | 84.7 ms                                                | 70.9 ms: 1.20x faster                                           |
| richards                   | 45.8 ms                                                | 38.5 ms: 1.19x faster                                           |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                           |
| spectral_norm              | 115 ms                                                 | 98.0 ms: 1.17x faster                                           |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                           |
| richards_super             | 51.5 ms                                                | 44.6 ms: 1.16x faster                                           |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                            |
| fannkuch                   | 417 ms                                                 | 377 ms: 1.11x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                           |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.67 ms: 1.08x faster                                           |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                            |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                            |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                           |
| tornado_http               | 103 ms                                                 | 97.9 ms: 1.05x faster                                           |
| dulwich_log                | 68.5 ms                                                | 65.4 ms: 1.05x faster                                           |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.04x faster                                            |
| pyflate                    | 482 ms                                                 | 463 ms: 1.04x faster                                            |
| json_loads                 | 28.5 us                                                | 27.4 us: 1.04x faster                                           |
| json                       | 5.26 ms                                                | 5.08 ms: 1.04x faster                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                           |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                            |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                            |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                          |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                            |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                            |
| gc_traversal               | 3.79 ms                                                | 3.80 ms: 1.00x slower                                           |
| go                         | 139 ms                                                 | 140 ms: 1.00x slower                                            |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                            |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                            |
| bench_thread_pool          | 842 us                                                 | 853 us: 1.01x slower                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                          |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                           |
| scimark_lu                 | 118 ms                                                 | 121 ms: 1.02x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                           |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                          |
| dask                       | 372 ms                                                 | 383 ms: 1.03x slower                                            |
| sympy_expand               | 478 ms                                                 | 493 ms: 1.03x slower                                            |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                            |
| asyncio_tcp                | 491 ms                                                 | 516 ms: 1.05x slower                                            |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                            |
| regex_effbot               | 3.61 ms                                                | 3.88 ms: 1.08x slower                                           |
| sqlglot_optimize           | 54.8 ms                                                | 60.0 ms: 1.10x slower                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                           |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                           |
| async_generators           | 463 ms                                                 | 514 ms: 1.11x slower                                            |
| telco                      | 7.10 ms                                                | 7.90 ms: 1.11x slower                                           |
| nqueens                    | 83.3 ms                                                | 94.1 ms: 1.13x slower                                           |
| django_template            | 34.6 ms                                                | 40.3 ms: 1.16x slower                                           |
| sympy_integrate            | 21.4 ms                                                | 25.3 ms: 1.18x slower                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                           |
| coroutines                 | 23.2 ms                                                | 27.5 ms: 1.19x slower                                           |
| coverage                   | 72.7 ms                                                | 93.3 ms: 1.28x slower                                           |
| generators                 | 31.2 ms                                                | 47.6 ms: 1.52x slower                                           |
| docutils                   | 2.77 sec                                               | 6.74 sec: 2.43x slower                                          |
| raytrace                   | 312 ms                                                 | 4.85 sec: 15.53x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (2): json_dumps, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240710-3.14.0a0-799510c-JIT/bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x