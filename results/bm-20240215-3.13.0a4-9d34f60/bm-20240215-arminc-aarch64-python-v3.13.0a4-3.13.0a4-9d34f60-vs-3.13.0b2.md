# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: linux-aarch64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.00x slower
- HPT reliability: 79.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 2.91 sec: 1.07x faster                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (4): 2to3, chameleon, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 791 ms                                                       | 880 ms: 1.11x slower                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.43 sec: 1.12x slower                                       |
| async_tree_memoization     | 645 ms                                                       | 737 ms: 1.14x slower                                         |
| async_tree_none            | 492 ms                                                       | 564 ms: 1.15x slower                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 887 ms: 1.16x slower                                         |
| async_tree_io              | 1.22 sec                                                     | 1.42 sec: 1.16x slower                                       |
| async_tree_none_tg         | 476 ms                                                       | 567 ms: 1.19x slower                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 728 ms: 1.20x slower                                         |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 106 ms: 1.08x faster                                         |
| float          | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                        |
| regex_compile  | 128 ms                                                       | 125 ms: 1.02x faster                                         |
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                         |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 359 us                                                       | 351 us: 1.02x faster                                         |
| xml_etree_process    | 80.8 ms                                                      | 79.1 ms: 1.02x faster                                        |
| pickle_list          | 5.27 us                                                      | 5.22 us: 1.01x faster                                        |
| pickle               | 13.4 us                                                      | 13.5 us: 1.01x slower                                        |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.01x slower                                         |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.02x slower                                         |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (8): unpickle_list, unpickle, xml_etree_generate, pickle_dict, json_loads, tomli_loads, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.1 ms: 1.07x faster                                        |
| python_startup_no_site | 8.60 ms                                                      | 10.5 ms: 1.23x slower                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 40.3 ms: 1.05x faster                                        |
| genshi_text     | 27.4 ms                                                      | 27.1 ms: 1.01x faster                                        |
| genshi_xml      | 60.4 ms                                                      | 59.7 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 193 us                                                       | 133 us: 1.46x faster                                         |
| create_gc_cycles           | 2.33 ms                                                      | 1.96 ms: 1.19x faster                                        |
| gc_traversal               | 5.17 ms                                                      | 4.39 ms: 1.18x faster                                        |
| nbody                      | 114 ms                                                       | 106 ms: 1.08x faster                                         |
| python_startup             | 13.0 ms                                                      | 12.1 ms: 1.07x faster                                        |
| docutils                   | 3.10 sec                                                     | 2.91 sec: 1.07x faster                                       |
| logging_silent             | 133 ns                                                       | 126 ns: 1.06x faster                                         |
| asyncio_tcp                | 584 ms                                                       | 553 ms: 1.06x faster                                         |
| django_template            | 42.3 ms                                                      | 40.3 ms: 1.05x faster                                        |
| deepcopy_memo              | 50.8 us                                                      | 48.5 us: 1.05x faster                                        |
| telco                      | 10.0 ms                                                      | 9.57 ms: 1.05x faster                                        |
| sqlglot_parse              | 1.42 ms                                                      | 1.36 ms: 1.04x faster                                        |
| spectral_norm              | 141 ms                                                       | 135 ms: 1.04x faster                                         |
| crypto_pyaes               | 82.0 ms                                                      | 78.8 ms: 1.04x faster                                        |
| pprint_pformat             | 1.93 sec                                                     | 1.86 sec: 1.04x faster                                       |
| thrift                     | 962 us                                                       | 926 us: 1.04x faster                                         |
| pprint_safe_repr           | 933 ms                                                       | 903 ms: 1.03x faster                                         |
| deepcopy                   | 448 us                                                       | 434 us: 1.03x faster                                         |
| sympy_sum                  | 144 ms                                                       | 139 ms: 1.03x faster                                         |
| sympy_str                  | 265 ms                                                       | 257 ms: 1.03x faster                                         |
| richards                   | 55.9 ms                                                      | 54.2 ms: 1.03x faster                                        |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                        |
| richards_super             | 62.3 ms                                                      | 60.6 ms: 1.03x faster                                        |
| scimark_lu                 | 141 ms                                                       | 138 ms: 1.03x faster                                         |
| generators                 | 37.1 ms                                                      | 36.2 ms: 1.03x faster                                        |
| sqlglot_optimize           | 62.6 ms                                                      | 61.0 ms: 1.03x faster                                        |
| deepcopy_reduce            | 4.04 us                                                      | 3.94 us: 1.03x faster                                        |
| nqueens                    | 98.9 ms                                                      | 96.6 ms: 1.02x faster                                        |
| pickle_pure_python         | 359 us                                                       | 351 us: 1.02x faster                                         |
| regex_compile              | 128 ms                                                       | 125 ms: 1.02x faster                                         |
| sympy_expand               | 457 ms                                                       | 448 ms: 1.02x faster                                         |
| xml_etree_process          | 80.8 ms                                                      | 79.1 ms: 1.02x faster                                        |
| regex_dna                  | 259 ms                                                       | 253 ms: 1.02x faster                                         |
| chaos                      | 68.3 ms                                                      | 67.1 ms: 1.02x faster                                        |
| sqlite_synth               | 3.90 us                                                      | 3.84 us: 1.02x faster                                        |
| regex_effbot               | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                        |
| hexiom                     | 7.08 ms                                                      | 6.98 ms: 1.01x faster                                        |
| genshi_text                | 27.4 ms                                                      | 27.1 ms: 1.01x faster                                        |
| genshi_xml                 | 60.4 ms                                                      | 59.7 ms: 1.01x faster                                        |
| pickle_list                | 5.27 us                                                      | 5.22 us: 1.01x faster                                        |
| logging_format             | 7.82 us                                                      | 7.92 us: 1.01x slower                                        |
| pickle                     | 13.4 us                                                      | 13.5 us: 1.01x slower                                        |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.01x slower                                         |
| dulwich_log                | 58.5 ms                                                      | 59.4 ms: 1.02x slower                                        |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                         |
| float                      | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                        |
| scimark_monte_carlo        | 82.3 ms                                                      | 84.0 ms: 1.02x slower                                        |
| fannkuch                   | 451 ms                                                       | 461 ms: 1.02x slower                                         |
| bench_thread_pool          | 1.26 ms                                                      | 1.30 ms: 1.03x slower                                        |
| coverage                   | 98.4 ms                                                      | 102 ms: 1.03x slower                                         |
| scimark_sor                | 159 ms                                                       | 166 ms: 1.04x slower                                         |
| deltablue                  | 3.88 ms                                                      | 4.03 ms: 1.04x slower                                        |
| pathlib                    | 22.8 ms                                                      | 23.7 ms: 1.04x slower                                        |
| pycparser                  | 1.22 sec                                                     | 1.28 sec: 1.05x slower                                       |
| pyflate                    | 557 ms                                                       | 597 ms: 1.07x slower                                         |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 880 ms: 1.11x slower                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.43 sec: 1.12x slower                                       |
| async_tree_memoization     | 645 ms                                                       | 737 ms: 1.14x slower                                         |
| async_tree_none            | 492 ms                                                       | 564 ms: 1.15x slower                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 887 ms: 1.16x slower                                         |
| async_tree_io              | 1.22 sec                                                     | 1.42 sec: 1.16x slower                                       |
| async_tree_none_tg         | 476 ms                                                       | 567 ms: 1.19x slower                                         |
| mypy2                      | 767 ms                                                       | 915 ms: 1.19x slower                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 728 ms: 1.20x slower                                         |
| python_startup_no_site     | 8.60 ms                                                      | 10.5 ms: 1.23x slower                                        |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (35): sqlglot_normalize, comprehensions, bench_mp_pool, pylint, sympy_integrate, unpickle_list, scimark_fft, raytrace, asyncio_tcp_ssl, unpickle, scimark_sparse_mat_mult, go, xml_etree_generate, chameleon, async_generators, pickle_dict, pidigits, html5lib, mako, 2to3, mdp, json_loads, tomli_loads, asyncio_websockets, json_dumps, coroutines, sqlglot_transpile, logging_simple, aiohttp, json, meteor_contest, flaskblogging, gunicorn, xml_etree_parse, tornado_http
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 79.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x