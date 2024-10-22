# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: linux-aarch64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.00x slower
- HPT reliability: 66.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 9.02 ms                                                  | 8.86 ms: 1.02x faster                                        |
| html5lib       | 64.3 ms                                                  | 65.9 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                         |
| asyncio_websockets         | 656 ms                                                   | 664 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                       |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 731 ms: 1.13x slower                                         |
| async_tree_none            | 493 ms                                                   | 573 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 893 ms: 1.17x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 737 ms: 1.18x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 890 ms: 1.21x slower                                         |
| async_tree_none_tg         | 467 ms                                                   | 577 ms: 1.24x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.43 sec: 1.31x slower                                       |
| Geometric mean             | (ref)                                                    | 1.13x slower                                                 |

Benchmark hidden because not significant (1): asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 103 ms: 1.10x faster                                         |
| float          | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                    | 1.04x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                        |
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                         |
| regex_effbot   | 4.87 ms                                                  | 4.94 ms: 1.01x slower                                        |
| regex_dna      | 246 ms                                                   | 251 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_list       | 6.65 us                                                  | 6.25 us: 1.06x faster                                        |
| json_dumps          | 13.4 ms                                                  | 12.8 ms: 1.05x faster                                        |
| unpickle            | 20.2 us                                                  | 19.3 us: 1.04x faster                                        |
| pickle_pure_python  | 359 us                                                   | 349 us: 1.03x faster                                         |
| pickle_list         | 5.34 us                                                  | 5.26 us: 1.02x faster                                        |
| pickle              | 13.5 us                                                  | 13.3 us: 1.02x faster                                        |
| xml_etree_iterparse | 147 ms                                                   | 149 ms: 1.01x slower                                         |
| json_loads          | 31.4 us                                                  | 32.2 us: 1.02x slower                                        |
| tomli_loads         | 2.53 sec                                                 | 2.59 sec: 1.03x slower                                       |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (5): pickle_dict, xml_etree_process, unpickle_pure_python, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 12.2 ms: 1.09x faster                                        |
| python_startup_no_site | 8.75 ms                                                  | 10.5 ms: 1.20x slower                                        |
| Geometric mean         | (ref)                                                    | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 40.5 ms: 1.04x faster                                        |
| mako            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                        |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 192 us                                                   | 133 us: 1.44x faster                                         |
| mypy2                      | 1.18 sec                                                 | 917 ms: 1.29x faster                                         |
| nbody                      | 114 ms                                                   | 103 ms: 1.10x faster                                         |
| python_startup             | 13.3 ms                                                  | 12.2 ms: 1.09x faster                                        |
| create_gc_cycles           | 2.12 ms                                                  | 1.99 ms: 1.07x faster                                        |
| unpickle_list              | 6.65 us                                                  | 6.25 us: 1.06x faster                                        |
| deepcopy_memo              | 51.0 us                                                  | 48.2 us: 1.06x faster                                        |
| generators                 | 37.8 ms                                                  | 35.9 ms: 1.05x faster                                        |
| json_dumps                 | 13.4 ms                                                  | 12.8 ms: 1.05x faster                                        |
| deepcopy                   | 451 us                                                   | 431 us: 1.05x faster                                         |
| django_template            | 42.3 ms                                                  | 40.5 ms: 1.04x faster                                        |
| crypto_pyaes               | 82.7 ms                                                  | 79.2 ms: 1.04x faster                                        |
| unpickle                   | 20.2 us                                                  | 19.3 us: 1.04x faster                                        |
| spectral_norm              | 141 ms                                                   | 135 ms: 1.04x faster                                         |
| bench_mp_pool              | 7.30 ms                                                  | 7.02 ms: 1.04x faster                                        |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                         |
| regex_v8                   | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                        |
| richards                   | 53.5 ms                                                  | 51.8 ms: 1.03x faster                                        |
| mako                       | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                        |
| hexiom                     | 7.13 ms                                                  | 6.92 ms: 1.03x faster                                        |
| pickle_pure_python         | 359 us                                                   | 349 us: 1.03x faster                                         |
| deepcopy_reduce            | 4.07 us                                                  | 3.95 us: 1.03x faster                                        |
| sympy_sum                  | 143 ms                                                   | 140 ms: 1.03x faster                                         |
| nqueens                    | 98.7 ms                                                  | 96.0 ms: 1.03x faster                                        |
| sympy_integrate            | 21.0 ms                                                  | 20.4 ms: 1.03x faster                                        |
| pprint_safe_repr           | 926 ms                                                   | 903 ms: 1.03x faster                                         |
| comprehensions             | 20.4 us                                                  | 19.9 us: 1.02x faster                                        |
| sqlglot_normalize          | 128 ms                                                   | 126 ms: 1.02x faster                                         |
| pprint_pformat             | 1.90 sec                                                 | 1.86 sec: 1.02x faster                                       |
| richards_super             | 60.3 ms                                                  | 59.1 ms: 1.02x faster                                        |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.1 ms: 1.02x faster                                        |
| regex_compile              | 128 ms                                                   | 126 ms: 1.02x faster                                         |
| sqlglot_optimize           | 62.4 ms                                                  | 61.2 ms: 1.02x faster                                        |
| chaos                      | 68.8 ms                                                  | 67.6 ms: 1.02x faster                                        |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                         |
| gc_traversal               | 4.53 ms                                                  | 4.45 ms: 1.02x faster                                        |
| thrift                     | 946 us                                                   | 929 us: 1.02x faster                                         |
| chameleon                  | 9.02 ms                                                  | 8.86 ms: 1.02x faster                                        |
| scimark_lu                 | 139 ms                                                   | 137 ms: 1.02x faster                                         |
| pickle_list                | 5.34 us                                                  | 5.26 us: 1.02x faster                                        |
| pickle                     | 13.5 us                                                  | 13.3 us: 1.02x faster                                        |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.02x faster                                         |
| float                      | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                        |
| sympy_str                  | 264 ms                                                   | 260 ms: 1.01x faster                                         |
| mdp                        | 3.36 sec                                                 | 3.32 sec: 1.01x faster                                       |
| bench_thread_pool          | 1.28 ms                                                  | 1.29 ms: 1.01x slower                                        |
| pycparser                  | 1.26 sec                                                 | 1.28 sec: 1.01x slower                                       |
| asyncio_websockets         | 656 ms                                                   | 664 ms: 1.01x slower                                         |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.01x slower                                         |
| regex_effbot               | 4.87 ms                                                  | 4.94 ms: 1.01x slower                                        |
| fannkuch                   | 452 ms                                                   | 459 ms: 1.02x slower                                         |
| json                       | 5.61 ms                                                  | 5.71 ms: 1.02x slower                                        |
| regex_dna                  | 246 ms                                                   | 251 ms: 1.02x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                       |
| logging_simple             | 7.04 us                                                  | 7.18 us: 1.02x slower                                        |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                        |
| json_loads                 | 31.4 us                                                  | 32.2 us: 1.02x slower                                        |
| html5lib                   | 64.3 ms                                                  | 65.9 ms: 1.02x slower                                        |
| tomli_loads                | 2.53 sec                                                 | 2.59 sec: 1.03x slower                                       |
| coverage                   | 98.5 ms                                                  | 102 ms: 1.03x slower                                         |
| scimark_sor                | 159 ms                                                   | 165 ms: 1.04x slower                                         |
| deltablue                  | 3.85 ms                                                  | 4.00 ms: 1.04x slower                                        |
| telco                      | 9.73 ms                                                  | 10.2 ms: 1.05x slower                                        |
| pyflate                    | 556 ms                                                   | 591 ms: 1.06x slower                                         |
| pathlib                    | 22.4 ms                                                  | 24.2 ms: 1.08x slower                                        |
| dask                       | 350 ms                                                   | 383 ms: 1.09x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 731 ms: 1.13x slower                                         |
| async_tree_none            | 493 ms                                                   | 573 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 893 ms: 1.17x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 737 ms: 1.18x slower                                         |
| python_startup_no_site     | 8.75 ms                                                  | 10.5 ms: 1.20x slower                                        |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 890 ms: 1.21x slower                                         |
| async_tree_none_tg         | 467 ms                                                   | 577 ms: 1.24x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.43 sec: 1.31x slower                                       |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (25): pylint, asyncio_tcp, pickle_dict, aiohttp, scimark_sparse_mat_mult, go, sympy_expand, raytrace, sqlglot_parse, logging_format, pidigits, genshi_text, 2to3, docutils, xml_etree_process, genshi_xml, unpickle_pure_python, sqlite_synth, sqlglot_transpile, xml_etree_parse, meteor_contest, gunicorn, flaskblogging, tornado_http, xml_etree_generate
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, unpack_sequence
Ignored benchmarks (1) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169.json: dulwich_log

# HPT report

- Reliability score: 66.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x