Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231218-linux-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-linux-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 281 ms                                                                 | 277 ms: 1.02x faster                                           |
| chameleon      | 7.32 ms                                                                | 7.09 ms: 1.03x faster                                          |
| docutils       | 2.71 sec                                                               | 2.68 sec: 1.01x faster                                         |
| tornado_http   | 98.2 ms                                                                | 97.7 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231218-linux-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-linux-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 592 ms                                                                 | 580 ms: 1.02x faster                                           |
| async_tree_io_tg           | 1.22 sec                                                               | 1.20 sec: 1.02x faster                                         |
| async_tree_io              | 1.21 sec                                                               | 1.19 sec: 1.02x faster                                         |
| async_tree_memoization     | 578 ms                                                                 | 569 ms: 1.01x faster                                           |
| async_tree_none_tg         | 454 ms                                                                 | 448 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed_tg | 736 ms                                                                 | 728 ms: 1.01x faster                                           |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231218-linux-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-linux-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 113 ms                                                                 | 106 ms: 1.06x faster                                           |
| pidigits       | 196 ms                                                                 | 188 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231218-linux-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-linux-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 151 ms                                                                 | 142 ms: 1.06x faster                                           |
| regex_dna      | 216 ms                                                                 | 213 ms: 1.02x faster                                           |
| regex_effbot   | 3.60 ms                                                                | 3.69 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231218-linux-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-linux-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                                | 59.0 ms: 1.04x faster                                          |
| tomli_loads          | 2.32 sec                                                               | 2.25 sec: 1.03x faster                                         |
| xml_etree_generate   | 89.3 ms                                                                | 86.8 ms: 1.03x faster                                          |
| unpickle_list        | 5.28 us                                                                | 5.13 us: 1.03x faster                                          |
| unpickle_pure_python | 233 us                                                                 | 228 us: 1.02x faster                                           |
| unpickle             | 14.9 us                                                                | 14.6 us: 1.02x faster                                          |
| json_dumps           | 10.5 ms                                                                | 10.3 ms: 1.02x faster                                          |
| json_loads           | 27.7 us                                                                | 27.5 us: 1.01x faster                                          |
| pickle_pure_python   | 303 us                                                                 | 301 us: 1.01x faster                                           |
| xml_etree_parse      | 157 ms                                                                 | 158 ms: 1.01x slower                                           |
| pickle               | 11.3 us                                                                | 11.6 us: 1.03x slower                                          |
| pickle_dict          | 34.0 us                                                                | 35.4 us: 1.04x slower                                          |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231218-linux-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-linux-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                          |
| python_startup_no_site | 8.74 ms                                                                | 8.87 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231218-linux-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-linux-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|-----------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 13.5 ms                                                                | 12.7 ms: 1.06x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231218-linux-x86_64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-linux-x86_64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| scimark_fft                | 443 ms                                                                 | 391 ms: 1.14x faster                                           |
| deltablue                  | 4.57 ms                                                                | 4.07 ms: 1.12x faster                                          |
| nbody                      | 113 ms                                                                 | 106 ms: 1.06x faster                                           |
| regex_compile              | 151 ms                                                                 | 142 ms: 1.06x faster                                           |
| pycparser                  | 1.25 sec                                                               | 1.17 sec: 1.06x faster                                         |
| scimark_monte_carlo        | 79.7 ms                                                                | 75.1 ms: 1.06x faster                                          |
| mako                       | 13.5 ms                                                                | 12.7 ms: 1.06x faster                                          |
| logging_format             | 6.81 us                                                                | 6.45 us: 1.06x faster                                          |
| gc_traversal               | 3.97 ms                                                                | 3.77 ms: 1.06x faster                                          |
| raytrace                   | 297 ms                                                                 | 282 ms: 1.05x faster                                           |
| deepcopy_memo              | 40.1 us                                                                | 38.1 us: 1.05x faster                                          |
| richards                   | 48.4 ms                                                                | 46.3 ms: 1.05x faster                                          |
| comprehensions             | 20.7 us                                                                | 19.8 us: 1.04x faster                                          |
| logging_silent             | 108 ns                                                                 | 103 ns: 1.04x faster                                           |
| pidigits                   | 196 ms                                                                 | 188 ms: 1.04x faster                                           |
| richards_super             | 54.8 ms                                                                | 52.7 ms: 1.04x faster                                          |
| deepcopy_reduce            | 3.15 us                                                                | 3.04 us: 1.04x faster                                          |
| xml_etree_process          | 61.2 ms                                                                | 59.0 ms: 1.04x faster                                          |
| generators                 | 29.8 ms                                                                | 28.8 ms: 1.03x faster                                          |
| telco                      | 8.78 ms                                                                | 8.50 ms: 1.03x faster                                          |
| logging_simple             | 6.02 us                                                                | 5.83 us: 1.03x faster                                          |
| chameleon                  | 7.32 ms                                                                | 7.09 ms: 1.03x faster                                          |
| tomli_loads                | 2.32 sec                                                               | 2.25 sec: 1.03x faster                                         |
| xml_etree_generate         | 89.3 ms                                                                | 86.8 ms: 1.03x faster                                          |
| unpickle_list              | 5.28 us                                                                | 5.13 us: 1.03x faster                                          |
| sqlglot_parse              | 1.33 ms                                                                | 1.29 ms: 1.03x faster                                          |
| unpickle_pure_python       | 233 us                                                                 | 228 us: 1.02x faster                                           |
| sqlglot_transpile          | 1.66 ms                                                                | 1.62 ms: 1.02x faster                                          |
| unpickle                   | 14.9 us                                                                | 14.6 us: 1.02x faster                                          |
| mdp                        | 2.67 sec                                                               | 2.61 sec: 1.02x faster                                         |
| sqlglot_optimize           | 57.4 ms                                                                | 56.2 ms: 1.02x faster                                          |
| async_tree_memoization_tg  | 592 ms                                                                 | 580 ms: 1.02x faster                                           |
| typing_runtime_protocols   | 115 us                                                                 | 113 us: 1.02x faster                                           |
| sqlglot_normalize          | 113 ms                                                                 | 111 ms: 1.02x faster                                           |
| meteor_contest             | 112 ms                                                                 | 110 ms: 1.02x faster                                           |
| go                         | 155 ms                                                                 | 152 ms: 1.02x faster                                           |
| 2to3                       | 281 ms                                                                 | 277 ms: 1.02x faster                                           |
| async_tree_io_tg           | 1.22 sec                                                               | 1.20 sec: 1.02x faster                                         |
| dulwich_log                | 69.1 ms                                                                | 68.0 ms: 1.02x faster                                          |
| chaos                      | 71.7 ms                                                                | 70.6 ms: 1.02x faster                                          |
| deepcopy                   | 354 us                                                                 | 349 us: 1.02x faster                                           |
| regex_dna                  | 216 ms                                                                 | 213 ms: 1.02x faster                                           |
| json_dumps                 | 10.5 ms                                                                | 10.3 ms: 1.02x faster                                          |
| async_tree_io              | 1.21 sec                                                               | 1.19 sec: 1.02x faster                                         |
| async_tree_memoization     | 578 ms                                                                 | 569 ms: 1.01x faster                                           |
| pathlib                    | 18.7 ms                                                                | 18.4 ms: 1.01x faster                                          |
| sympy_expand               | 490 ms                                                                 | 483 ms: 1.01x faster                                           |
| async_tree_none_tg         | 454 ms                                                                 | 448 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed_tg | 736 ms                                                                 | 728 ms: 1.01x faster                                           |
| docutils                   | 2.71 sec                                                               | 2.68 sec: 1.01x faster                                         |
| sqlite_synth               | 2.87 us                                                                | 2.85 us: 1.01x faster                                          |
| json_loads                 | 27.7 us                                                                | 27.5 us: 1.01x faster                                          |
| pyflate                    | 508 ms                                                                 | 504 ms: 1.01x faster                                           |
| pickle_pure_python         | 303 us                                                                 | 301 us: 1.01x faster                                           |
| scimark_lu                 | 115 ms                                                                 | 115 ms: 1.01x faster                                           |
| hexiom                     | 8.15 ms                                                                | 8.11 ms: 1.01x faster                                          |
| tornado_http               | 98.2 ms                                                                | 97.7 ms: 1.01x faster                                          |
| asyncio_tcp                | 495 ms                                                                 | 496 ms: 1.00x slower                                           |
| async_generators           | 458 ms                                                                 | 460 ms: 1.00x slower                                           |
| asyncio_tcp_ssl            | 1.80 sec                                                               | 1.81 sec: 1.01x slower                                         |
| pprint_pformat             | 1.67 sec                                                               | 1.68 sec: 1.01x slower                                         |
| xml_etree_parse            | 157 ms                                                                 | 158 ms: 1.01x slower                                           |
| sympy_sum                  | 160 ms                                                                 | 162 ms: 1.01x slower                                           |
| pprint_safe_repr           | 798 ms                                                                 | 807 ms: 1.01x slower                                           |
| python_startup             | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                          |
| python_startup_no_site     | 8.74 ms                                                                | 8.87 ms: 1.02x slower                                          |
| create_gc_cycles           | 1.45 ms                                                                | 1.48 ms: 1.02x slower                                          |
| regex_effbot               | 3.60 ms                                                                | 3.69 ms: 1.02x slower                                          |
| pickle                     | 11.3 us                                                                | 11.6 us: 1.03x slower                                          |
| fannkuch                   | 426 ms                                                                 | 438 ms: 1.03x slower                                           |
| pickle_dict                | 34.0 us                                                                | 35.4 us: 1.04x slower                                          |
| scimark_sor                | 124 ms                                                                 | 131 ms: 1.05x slower                                           |
| unpack_sequence            | 44.3 ns                                                                | 48.5 ns: 1.10x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (20): crypto_pyaes, async_tree_none, async_tree_cpu_io_mixed, xml_etree_iterparse, coroutines, dask, float, coverage, nqueens, asyncio_websockets, pickle_list, bench_thread_pool, regex_v8, json, bench_mp_pool, scimark_sparse_mat_mult, sympy_str, sympy_integrate, spectral_norm, mypy2


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
