# Results vs. base

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                              | 353 ms: 1.15x slower                                                                                                            |
| chameleon      | 8.94 ms                                                                                                             | 10.0 ms: 1.12x slower                                                                                                           |
| docutils       | 3.09 sec                                                                                                            | 3.50 sec: 1.13x slower                                                                                                          |
| html5lib       | 66.1 ms                                                                                                             | 72.1 ms: 1.09x slower                                                                                                           |
| tornado_http   | 126 ms                                                                                                              | 134 ms: 1.07x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                               | 1.11x slower                                                                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.28 sec                                                                                                            | 1.24 sec: 1.03x faster                                                                                                          |
| async_tree_none_tg         | 474 ms                                                                                                              | 491 ms: 1.04x slower                                                                                                            |
| async_tree_io              | 1.21 sec                                                                                                            | 1.26 sec: 1.04x slower                                                                                                          |
| async_tree_memoization_tg  | 604 ms                                                                                                              | 629 ms: 1.04x slower                                                                                                            |
| async_tree_cpu_io_mixed_tg | 761 ms                                                                                                              | 793 ms: 1.04x slower                                                                                                            |
| async_tree_cpu_io_mixed    | 792 ms                                                                                                              | 828 ms: 1.05x slower                                                                                                            |
| async_tree_none            | 490 ms                                                                                                              | 519 ms: 1.06x slower                                                                                                            |
| async_tree_memoization     | 645 ms                                                                                                              | 684 ms: 1.06x slower                                                                                                            |
| Geometric mean             | (ref)                                                                                                               | 1.04x slower                                                                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| float          | 91.9 ms                                                                                                             | 113 ms: 1.22x slower                                                                                                            |
| nbody          | 113 ms                                                                                                              | 141 ms: 1.25x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                               | 1.16x slower                                                                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                                                              | 166 ms: 1.28x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                               | 1.07x slower                                                                                                                    |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| pickle               | 13.6 us                                                                                                             | 13.4 us: 1.01x faster                                                                                                           |
| json_loads           | 32.0 us                                                                                                             | 32.2 us: 1.01x slower                                                                                                           |
| json_dumps           | 13.5 ms                                                                                                             | 13.7 ms: 1.01x slower                                                                                                           |
| unpickle             | 19.6 us                                                                                                             | 19.9 us: 1.01x slower                                                                                                           |
| unpickle_list        | 6.47 us                                                                                                             | 6.62 us: 1.02x slower                                                                                                           |
| xml_etree_generate   | 117 ms                                                                                                              | 124 ms: 1.06x slower                                                                                                            |
| xml_etree_process    | 81.7 ms                                                                                                             | 87.0 ms: 1.07x slower                                                                                                           |
| xml_etree_iterparse  | 148 ms                                                                                                              | 162 ms: 1.09x slower                                                                                                            |
| pickle_pure_python   | 368 us                                                                                                              | 448 us: 1.22x slower                                                                                                            |
| tomli_loads          | 2.54 sec                                                                                                            | 3.11 sec: 1.23x slower                                                                                                          |
| unpickle_pure_python | 253 us                                                                                                              | 348 us: 1.37x slower                                                                                                            |
| Geometric mean       | (ref)                                                                                                               | 1.07x slower                                                                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| django_template | 42.7 ms                                                                                                             | 48.9 ms: 1.15x slower                                                                                                           |
| mako            | 13.5 ms                                                                                                             | 16.4 ms: 1.22x slower                                                                                                           |
| genshi_xml      | 62.1 ms                                                                                                             | 76.1 ms: 1.23x slower                                                                                                           |
| genshi_text     | 27.6 ms                                                                                                             | 36.2 ms: 1.31x slower                                                                                                           |
| Geometric mean  | (ref)                                                                                                               | 1.22x slower                                                                                                                    |

All benchmarks:
===============

| Benchmark                  | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.28 sec                                                                                                            | 1.24 sec: 1.03x faster                                                                                                          |
| pickle                     | 13.6 us                                                                                                             | 13.4 us: 1.01x faster                                                                                                           |
| json_loads                 | 32.0 us                                                                                                             | 32.2 us: 1.01x slower                                                                                                           |
| json_dumps                 | 13.5 ms                                                                                                             | 13.7 ms: 1.01x slower                                                                                                           |
| unpickle                   | 19.6 us                                                                                                             | 19.9 us: 1.01x slower                                                                                                           |
| asyncio_tcp                | 586 ms                                                                                                              | 596 ms: 1.02x slower                                                                                                            |
| sqlite_synth               | 3.91 us                                                                                                             | 3.99 us: 1.02x slower                                                                                                           |
| unpickle_list              | 6.47 us                                                                                                             | 6.62 us: 1.02x slower                                                                                                           |
| coverage                   | 98.0 ms                                                                                                             | 101 ms: 1.03x slower                                                                                                            |
| flaskblogging              | 4.87 ms                                                                                                             | 5.03 ms: 1.03x slower                                                                                                           |
| create_gc_cycles           | 2.34 ms                                                                                                             | 2.41 ms: 1.03x slower                                                                                                           |
| logging_format             | 7.75 us                                                                                                             | 8.02 us: 1.03x slower                                                                                                           |
| json                       | 5.64 ms                                                                                                             | 5.84 ms: 1.04x slower                                                                                                           |
| pathlib                    | 22.6 ms                                                                                                             | 23.4 ms: 1.04x slower                                                                                                           |
| async_tree_none_tg         | 474 ms                                                                                                              | 491 ms: 1.04x slower                                                                                                            |
| logging_simple             | 7.06 us                                                                                                             | 7.32 us: 1.04x slower                                                                                                           |
| coroutines                 | 29.2 ms                                                                                                             | 30.4 ms: 1.04x slower                                                                                                           |
| async_tree_io              | 1.21 sec                                                                                                            | 1.26 sec: 1.04x slower                                                                                                          |
| async_tree_memoization_tg  | 604 ms                                                                                                              | 629 ms: 1.04x slower                                                                                                            |
| async_tree_cpu_io_mixed_tg | 761 ms                                                                                                              | 793 ms: 1.04x slower                                                                                                            |
| dask                       | 373 ms                                                                                                              | 389 ms: 1.04x slower                                                                                                            |
| async_tree_cpu_io_mixed    | 792 ms                                                                                                              | 828 ms: 1.05x slower                                                                                                            |
| aiohttp                    | 1.22 ms                                                                                                             | 1.28 ms: 1.05x slower                                                                                                           |
| bench_thread_pool          | 1.28 ms                                                                                                             | 1.34 ms: 1.05x slower                                                                                                           |
| async_tree_none            | 490 ms                                                                                                              | 519 ms: 1.06x slower                                                                                                            |
| xml_etree_generate         | 117 ms                                                                                                              | 124 ms: 1.06x slower                                                                                                            |
| async_tree_memoization     | 645 ms                                                                                                              | 684 ms: 1.06x slower                                                                                                            |
| xml_etree_process          | 81.7 ms                                                                                                             | 87.0 ms: 1.07x slower                                                                                                           |
| tornado_http               | 126 ms                                                                                                              | 134 ms: 1.07x slower                                                                                                            |
| mdp                        | 3.31 sec                                                                                                            | 3.56 sec: 1.08x slower                                                                                                          |
| generators                 | 37.4 ms                                                                                                             | 40.2 ms: 1.08x slower                                                                                                           |
| dulwich_log                | 61.0 ms                                                                                                             | 65.9 ms: 1.08x slower                                                                                                           |
| xml_etree_iterparse        | 148 ms                                                                                                              | 162 ms: 1.09x slower                                                                                                            |
| gunicorn                   | 1.24 ms                                                                                                             | 1.35 ms: 1.09x slower                                                                                                           |
| html5lib                   | 66.1 ms                                                                                                             | 72.1 ms: 1.09x slower                                                                                                           |
| telco                      | 9.86 ms                                                                                                             | 10.8 ms: 1.10x slower                                                                                                           |
| async_generators           | 486 ms                                                                                                              | 538 ms: 1.11x slower                                                                                                            |
| bench_mp_pool              | 7.22 ms                                                                                                             | 8.06 ms: 1.12x slower                                                                                                           |
| chameleon                  | 8.94 ms                                                                                                             | 10.0 ms: 1.12x slower                                                                                                           |
| pycparser                  | 1.21 sec                                                                                                            | 1.36 sec: 1.12x slower                                                                                                          |
| sympy_expand               | 462 ms                                                                                                              | 521 ms: 1.13x slower                                                                                                            |
| docutils                   | 3.09 sec                                                                                                            | 3.50 sec: 1.13x slower                                                                                                          |
| raytrace                   | 299 ms                                                                                                              | 340 ms: 1.14x slower                                                                                                            |
| mypy2                      | 759 ms                                                                                                              | 866 ms: 1.14x slower                                                                                                            |
| django_template            | 42.7 ms                                                                                                             | 48.9 ms: 1.15x slower                                                                                                           |
| typing_runtime_protocols   | 192 us                                                                                                              | 222 us: 1.15x slower                                                                                                            |
| 2to3                       | 306 ms                                                                                                              | 353 ms: 1.15x slower                                                                                                            |
| pylint                     | 338 ms                                                                                                              | 393 ms: 1.16x slower                                                                                                            |
| sympy_str                  | 268 ms                                                                                                              | 314 ms: 1.17x slower                                                                                                            |
| sqlglot_optimize           | 62.0 ms                                                                                                             | 72.7 ms: 1.17x slower                                                                                                           |
| meteor_contest             | 113 ms                                                                                                              | 133 ms: 1.18x slower                                                                                                            |
| sqlglot_normalize          | 127 ms                                                                                                              | 150 ms: 1.18x slower                                                                                                            |
| richards_super             | 62.2 ms                                                                                                             | 73.6 ms: 1.18x slower                                                                                                           |
| deepcopy_reduce            | 4.00 us                                                                                                             | 4.78 us: 1.19x slower                                                                                                           |
| richards                   | 55.4 ms                                                                                                             | 66.4 ms: 1.20x slower                                                                                                           |
| deepcopy                   | 448 us                                                                                                              | 539 us: 1.20x slower                                                                                                            |
| sympy_sum                  | 143 ms                                                                                                              | 173 ms: 1.21x slower                                                                                                            |
| scimark_sparse_mat_mult    | 6.66 ms                                                                                                             | 8.05 ms: 1.21x slower                                                                                                           |
| sqlglot_parse              | 1.40 ms                                                                                                             | 1.70 ms: 1.22x slower                                                                                                           |
| pickle_pure_python         | 368 us                                                                                                              | 448 us: 1.22x slower                                                                                                            |
| scimark_fft                | 446 ms                                                                                                              | 543 ms: 1.22x slower                                                                                                            |
| mako                       | 13.5 ms                                                                                                             | 16.4 ms: 1.22x slower                                                                                                           |
| go                         | 161 ms                                                                                                              | 196 ms: 1.22x slower                                                                                                            |
| float                      | 91.9 ms                                                                                                             | 113 ms: 1.22x slower                                                                                                            |
| fannkuch                   | 447 ms                                                                                                              | 547 ms: 1.23x slower                                                                                                            |
| genshi_xml                 | 62.1 ms                                                                                                             | 76.1 ms: 1.23x slower                                                                                                           |
| tomli_loads                | 2.54 sec                                                                                                            | 3.11 sec: 1.23x slower                                                                                                          |
| sqlglot_transpile          | 1.75 ms                                                                                                             | 2.15 ms: 1.23x slower                                                                                                           |
| scimark_sor                | 161 ms                                                                                                              | 199 ms: 1.23x slower                                                                                                            |
| pprint_safe_repr           | 943 ms                                                                                                              | 1.16 sec: 1.23x slower                                                                                                          |
| pprint_pformat             | 1.93 sec                                                                                                            | 2.38 sec: 1.23x slower                                                                                                          |
| sympy_integrate            | 21.0 ms                                                                                                             | 26.0 ms: 1.23x slower                                                                                                           |
| crypto_pyaes               | 81.6 ms                                                                                                             | 101 ms: 1.24x slower                                                                                                            |
| nbody                      | 113 ms                                                                                                              | 141 ms: 1.25x slower                                                                                                            |
| chaos                      | 67.8 ms                                                                                                             | 85.2 ms: 1.26x slower                                                                                                           |
| pyflate                    | 554 ms                                                                                                              | 706 ms: 1.28x slower                                                                                                            |
| regex_compile              | 129 ms                                                                                                              | 166 ms: 1.28x slower                                                                                                            |
| nqueens                    | 99.7 ms                                                                                                             | 128 ms: 1.29x slower                                                                                                            |
| spectral_norm              | 141 ms                                                                                                              | 183 ms: 1.30x slower                                                                                                            |
| genshi_text                | 27.6 ms                                                                                                             | 36.2 ms: 1.31x slower                                                                                                           |
| deltablue                  | 3.85 ms                                                                                                             | 5.13 ms: 1.33x slower                                                                                                           |
| unpickle_pure_python       | 253 us                                                                                                              | 348 us: 1.37x slower                                                                                                            |
| logging_silent             | 132 ns                                                                                                              | 188 ns: 1.42x slower                                                                                                            |
| scimark_monte_carlo        | 81.6 ms                                                                                                             | 116 ms: 1.42x slower                                                                                                            |
| deepcopy_memo              | 50.1 us                                                                                                             | 72.0 us: 1.44x slower                                                                                                           |
| comprehensions             | 20.1 us                                                                                                             | 29.6 us: 1.47x slower                                                                                                           |
| hexiom                     | 7.06 ms                                                                                                             | 10.5 ms: 1.49x slower                                                                                                           |
| scimark_lu                 | 141 ms                                                                                                              | 211 ms: 1.50x slower                                                                                                            |
| Geometric mean             | (ref)                                                                                                               | 1.13x slower                                                                                                                    |

Benchmark hidden because not significant (13): xml_etree_parse, pickle_dict, regex_effbot, regex_dna, asyncio_websockets, python_startup, thrift, asyncio_tcp_ssl, pickle_list, python_startup_no_site, pidigits, gc_traversal, regex_v8

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.01x