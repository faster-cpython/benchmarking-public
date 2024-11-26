# Results vs. 3.12.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 9f86e46
- commit date: 2024-10-10
- overall geometric mean: 1.079x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.4 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 312 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 404 ms: 1.42x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 919 ms: 1.29x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 937 ms: 1.23x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.8 ms: 1.08x faster                                                           |
| nbody          | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                          |
| json_loads           | 28.5 us                                                | 26.3 us: 1.08x faster                                                           |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.04x faster                                                            |
| pickle_dict          | 35.5 us                                                | 34.2 us: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 87.0 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| unpickle_list        | 5.29 us                                                | 5.19 us: 1.02x faster                                                           |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                           |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 312 ms: 1.44x faster                                                            |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 404 ms: 1.42x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 31.3 us: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                           |
| async_tree_io_tg           | 1.18 sec                                               | 919 ms: 1.29x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 937 ms: 1.23x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                           |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                           |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                            |
| generators                 | 31.2 ms                                                | 26.9 ms: 1.16x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                           |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                            |
| unpack_sequence            | 54.0 ns                                                | 47.0 ns: 1.15x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                            |
| tornado_http               | 103 ms                                                 | 90.4 ms: 1.13x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                                           |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                                           |
| json_loads                 | 28.5 us                                                | 26.3 us: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                           |
| float                      | 84.7 ms                                                | 78.8 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                            |
| json                       | 5.26 ms                                                | 4.93 ms: 1.07x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.06x faster                                                           |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                          |
| pyflate                    | 482 ms                                                 | 457 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                          |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                            |
| nbody                      | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.04x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                                           |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                            |
| pickle_dict                | 35.5 us                                                | 34.2 us: 1.04x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                           |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                            |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                                           |
| asyncio_tcp                | 491 ms                                                 | 477 ms: 1.03x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                            |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                            |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 87.0 ms: 1.02x faster                                                           |
| scimark_fft                | 382 ms                                                 | 373 ms: 1.02x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                           |
| unpickle_list              | 5.29 us                                                | 5.19 us: 1.02x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                            |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                                           |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                          |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                            |
| pickle_list                | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 849 us: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| richards                   | 45.8 ms                                                | 46.8 ms: 1.02x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.9 ms: 1.03x slower                                                           |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                           |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                            |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 3.99 ms: 1.05x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                                           |
| coverage                   | 72.7 ms                                                | 84.1 ms: 1.16x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 56.3 ms: 2.35x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (3): pycparser, regex_effbot, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241010-3.14.0a0-9f86e46/bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.079x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.97x