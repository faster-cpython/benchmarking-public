# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                            |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                          |
| tornado_http   | 103 ms                                                 | 94.8 ms: 1.08x faster                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.53x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                            |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                            |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 976 ms: 1.21x faster                                            |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.3 ms: 1.18x faster                                           |
| float          | 84.7 ms                                                | 75.6 ms: 1.12x faster                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                            |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                            |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                           |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                          |
| xml_etree_generate   | 89.2 ms                                                | 78.2 ms: 1.14x faster                                           |
| xml_etree_process    | 61.7 ms                                                | 54.8 ms: 1.13x faster                                           |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                            |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                            |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                           |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                            |
| pickle_pure_python   | 324 us                                                 | 311 us: 1.04x faster                                            |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                           |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                           |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                           |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.16x faster                                           |
| django_template | 34.6 ms                                                | 35.8 ms: 1.03x slower                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.53x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                            |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                           |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                            |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                            |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                            |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                            |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                           |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 976 ms: 1.21x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                           |
| crypto_pyaes               | 81.9 ms                                                | 68.6 ms: 1.19x faster                                           |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                           |
| nbody                      | 97.0 ms                                                | 82.3 ms: 1.18x faster                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 64.3 ms: 1.17x faster                                           |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.16x faster                                           |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                           |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                            |
| xml_etree_generate         | 89.2 ms                                                | 78.2 ms: 1.14x faster                                           |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                           |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 54.8 ms: 1.13x faster                                           |
| richards                   | 45.8 ms                                                | 40.8 ms: 1.12x faster                                           |
| float                      | 84.7 ms                                                | 75.6 ms: 1.12x faster                                           |
| pprint_safe_repr           | 776 ms                                                 | 696 ms: 1.12x faster                                            |
| fannkuch                   | 417 ms                                                 | 381 ms: 1.09x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                           |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                            |
| tornado_http               | 103 ms                                                 | 94.8 ms: 1.08x faster                                           |
| richards_super             | 51.5 ms                                                | 47.6 ms: 1.08x faster                                           |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                            |
| logging_silent             | 104 ns                                                 | 97.1 ns: 1.08x faster                                           |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                          |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                            |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                            |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                            |
| json                       | 5.26 ms                                                | 5.00 ms: 1.05x faster                                           |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                            |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                            |
| pickle_pure_python         | 324 us                                                 | 311 us: 1.04x faster                                            |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                          |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.03x faster                                          |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                           |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                            |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                            |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                           |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                           |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                           |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                            |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                           |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.03x slower                                           |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.04x slower                                            |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                           |
| sympy_expand               | 478 ms                                                 | 498 ms: 1.04x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                            |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                            |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                          |
| nqueens                    | 83.3 ms                                                | 87.6 ms: 1.05x slower                                           |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                           |
| telco                      | 7.10 ms                                                | 7.58 ms: 1.07x slower                                           |
| sqlglot_optimize           | 54.8 ms                                                | 59.3 ms: 1.08x slower                                           |
| sympy_integrate            | 21.4 ms                                                | 23.3 ms: 1.09x slower                                           |
| hexiom                     | 6.41 ms                                                | 7.01 ms: 1.09x slower                                           |
| generators                 | 31.2 ms                                                | 35.5 ms: 1.14x slower                                           |
| gc_traversal               | 3.79 ms                                                | 4.37 ms: 1.15x slower                                           |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                           |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 83.8 ms: 3.49x slower                                           |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                    |

Benchmark hidden because not significant (2): sympy_str, spectral_norm
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.16x