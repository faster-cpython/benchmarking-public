# Results vs. 3.13.0b2

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: linux-aarch64
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 361 ms: 1.18x slower                                                    |
| chameleon      | 8.95 ms                                                      | 9.28 ms: 1.04x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.4 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                       | 139 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                        | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 825 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 633 ms: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 801 ms: 1.05x slower                                                    |
| async_tree_none            | 492 ms                                                       | 517 ms: 1.05x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 684 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                            |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 116 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| regex_compile  | 128 ms                                                       | 172 ms: 1.34x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 6.52 us                                                      | 6.41 us: 1.02x faster                                                   |
| pickle_list          | 5.27 us                                                      | 5.21 us: 1.01x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 152 ms: 1.04x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 278 us: 1.11x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 398 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_process, unpickle, pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 14.8 ms: 1.14x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 10.8 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                      | 51.5 ms: 1.22x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 35.3 ms: 1.29x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 83.8 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                    | 22.8 ms                                                      | 21.6 ms: 1.05x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                  |
| richards                   | 55.9 ms                                                      | 54.7 ms: 1.02x faster                                                   |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| unpickle_list              | 6.52 us                                                      | 6.41 us: 1.02x faster                                                   |
| richards_super             | 62.3 ms                                                      | 61.4 ms: 1.02x faster                                                   |
| deepcopy_memo              | 50.8 us                                                      | 50.0 us: 1.02x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.10 ms: 1.01x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.86 us: 1.01x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.21 us: 1.01x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 664 ms: 1.01x slower                                                    |
| coverage                   | 98.4 ms                                                      | 99.6 ms: 1.01x slower                                                   |
| nbody                      | 114 ms                                                       | 116 ms: 1.01x slower                                                    |
| fannkuch                   | 451 ms                                                       | 460 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                  |
| logging_format             | 7.82 us                                                      | 7.99 us: 1.02x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| meteor_contest             | 113 ms                                                       | 117 ms: 1.03x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                                  |
| scimark_fft                | 445 ms                                                       | 461 ms: 1.04x slower                                                    |
| chameleon                  | 8.95 ms                                                      | 9.28 ms: 1.04x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 152 ms: 1.04x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.46 sec: 1.04x slower                                                  |
| create_gc_cycles           | 2.33 ms                                                      | 2.42 ms: 1.04x slower                                                   |
| generators                 | 37.1 ms                                                      | 38.6 ms: 1.04x slower                                                   |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 825 ms: 1.04x slower                                                    |
| async_generators           | 488 ms                                                       | 511 ms: 1.05x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 633 ms: 1.05x slower                                                    |
| dask                       | 370 ms                                                       | 389 ms: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 801 ms: 1.05x slower                                                    |
| async_tree_none            | 492 ms                                                       | 517 ms: 1.05x slower                                                    |
| logging_silent             | 133 ns                                                       | 140 ns: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.91 ms: 1.05x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 617 ms: 1.06x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.06x slower                                                   |
| async_tree_memoization     | 645 ms                                                       | 684 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 208 us: 1.08x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 71.4 ms: 1.08x slower                                                   |
| tornado_http               | 128 ms                                                       | 139 ms: 1.08x slower                                                    |
| flaskblogging              | 4.70 ms                                                      | 5.12 ms: 1.09x slower                                                   |
| raytrace                   | 297 ms                                                       | 324 ms: 1.09x slower                                                    |
| scimark_sor                | 159 ms                                                       | 175 ms: 1.10x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 278 us: 1.11x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 90.7 ms: 1.11x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 398 us: 1.11x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| go                         | 161 ms                                                       | 179 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 144 ms: 1.12x slower                                                    |
| deepcopy                   | 448 us                                                       | 503 us: 1.12x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 70.3 ms: 1.12x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.60 ms: 1.12x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.1 us: 1.13x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 92.8 ms: 1.13x slower                                                   |
| pyflate                    | 557 ms                                                       | 633 ms: 1.14x slower                                                    |
| python_startup             | 13.0 ms                                                      | 14.8 ms: 1.14x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                                  |
| bench_mp_pool              | 7.03 ms                                                      | 8.11 ms: 1.15x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.72 us: 1.17x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.01 ms: 1.17x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.10 sec: 1.18x slower                                                  |
| sympy_expand               | 457 ms                                                       | 541 ms: 1.18x slower                                                    |
| 2to3                       | 305 ms                                                       | 361 ms: 1.18x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.62 ms: 1.19x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.30 sec: 1.19x slower                                                  |
| nqueens                    | 98.9 ms                                                      | 119 ms: 1.20x slower                                                    |
| sympy_str                  | 265 ms                                                       | 323 ms: 1.22x slower                                                    |
| django_template            | 42.3 ms                                                      | 51.5 ms: 1.22x slower                                                   |
| pylint                     | 337 ms                                                       | 413 ms: 1.22x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 71.9 ms: 1.23x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.0 ms: 1.25x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 10.8 ms: 1.26x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 9.07 ms: 1.28x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 184 ms: 1.28x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 35.3 ms: 1.29x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 183 ms: 1.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 88.8 ms: 1.30x slower                                                   |
| regex_compile              | 128 ms                                                       | 172 ms: 1.34x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 83.8 ms: 1.39x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (12): xml_etree_parse, xml_etree_process, unpickle, coroutines, float, pidigits, pickle_dict, json_loads, thrift, json, logging_simple, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x