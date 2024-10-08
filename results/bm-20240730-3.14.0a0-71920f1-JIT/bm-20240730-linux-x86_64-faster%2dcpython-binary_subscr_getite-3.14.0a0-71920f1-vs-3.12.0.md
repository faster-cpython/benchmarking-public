# Results vs. 3.12.0

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: 71920f1
- commit date: 2024-07-30
- overall geometric mean: 1.08x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.00x faster                                                            |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                          |
| tornado_http   | 103 ms                                                 | 92.2 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                            |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 913 ms: 1.27x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.5 ms: 1.22x faster                                                           |
| float          | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.11x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                           |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 294 us: 1.10x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                            |
| json_loads           | 28.5 us                                                | 28.1 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.93 ms: 1.20x faster                                                           |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                            |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                            |
| deepcopy                   | 371 us                                                 | 279 us: 1.33x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 913 ms: 1.27x faster                                                            |
| scimark_fft                | 382 ms                                                 | 303 ms: 1.26x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 65.8 ms: 1.24x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 60.9 ms: 1.23x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                           |
| nbody                      | 97.0 ms                                                | 79.5 ms: 1.22x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.19 ms: 1.21x faster                                                           |
| logging_format             | 7.23 us                                                | 6.00 us: 1.21x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                           |
| mako                       | 11.9 ms                                                | 9.93 ms: 1.20x faster                                                           |
| float                      | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.19x faster                                                           |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                            |
| chaos                      | 67.0 ms                                                | 57.8 ms: 1.16x faster                                                           |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                            |
| fannkuch                   | 417 ms                                                 | 370 ms: 1.13x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                           |
| regex_compile              | 148 ms                                                 | 133 ms: 1.11x faster                                                            |
| richards                   | 45.8 ms                                                | 41.2 ms: 1.11x faster                                                           |
| tornado_http               | 103 ms                                                 | 92.2 ms: 1.11x faster                                                           |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 294 us: 1.10x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 108 ms: 1.09x faster                                                            |
| richards_super             | 51.5 ms                                                | 47.1 ms: 1.09x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                            |
| pyflate                    | 482 ms                                                 | 449 ms: 1.08x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                                           |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.57 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                           |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                           |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 819 us: 1.03x faster                                                            |
| async_generators           | 463 ms                                                 | 450 ms: 1.03x faster                                                            |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                           |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                            |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| 2to3                       | 274 ms                                                 | 273 ms: 1.00x faster                                                            |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                            |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                          |
| sqlglot_optimize           | 54.8 ms                                                | 55.7 ms: 1.02x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                           |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                          |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                            |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                           |
| nqueens                    | 83.3 ms                                                | 85.8 ms: 1.03x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                           |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                            |
| hexiom                     | 6.41 ms                                                | 6.70 ms: 1.04x slower                                                           |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                            |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                           |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                          |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.05x slower                                                           |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 7.96 ms: 1.12x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                           |
| coverage                   | 72.7 ms                                                | 90.9 ms: 1.25x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): sympy_str, bench_mp_pool, pycparser, json_dumps
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240730-3.14.0a0-71920f1-JIT/bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x