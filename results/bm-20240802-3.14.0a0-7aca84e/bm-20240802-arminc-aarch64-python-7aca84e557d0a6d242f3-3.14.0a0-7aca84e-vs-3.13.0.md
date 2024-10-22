# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.02x faster
- HPT reliability: 98.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.91 sec                                                 | 3.12 sec: 1.07x slower                                                  |
| html5lib       | 64.3 ms                                                  | 66.6 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 531 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 397 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 434 ms: 1.14x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 552 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 728 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 702 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.12 sec: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| float          | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.6 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| regex_dna      | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 254 us                                                   | 251 us: 1.01x faster                                                    |
| json_loads           | 31.4 us                                                  | 33.0 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (7): xml_etree_generate, pickle_pure_python, xml_etree_parse, json_dumps, tomli_loads, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.75 ms                                                  | 8.90 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 330 us: 1.37x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 38.1 us: 1.34x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 531 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.38 us: 1.20x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 397 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 434 ms: 1.14x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 552 ms: 1.13x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.3 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 728 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 702 ms: 1.05x faster                                                    |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.33 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| richards                   | 53.5 ms                                                  | 51.9 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.6 ms: 1.03x faster                                                   |
| richards_super             | 60.3 ms                                                  | 58.5 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.5 ms: 1.03x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.11 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                    |
| go                         | 163 ms                                                   | 159 ms: 1.02x faster                                                    |
| scimark_sor                | 159 ms                                                   | 156 ms: 1.02x faster                                                    |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                    |
| float                      | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 440 ms: 1.02x faster                                                    |
| chaos                      | 68.8 ms                                                  | 67.8 ms: 1.02x faster                                                   |
| unpickle_pure_python       | 254 us                                                   | 251 us: 1.01x faster                                                    |
| spectral_norm              | 141 ms                                                   | 139 ms: 1.01x faster                                                    |
| sqlglot_optimize           | 62.4 ms                                                  | 61.5 ms: 1.01x faster                                                   |
| hexiom                     | 7.13 ms                                                  | 7.04 ms: 1.01x faster                                                   |
| raytrace                   | 298 ms                                                   | 294 ms: 1.01x faster                                                    |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                  |
| regex_compile              | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| logging_simple             | 7.04 us                                                  | 6.97 us: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                  |
| mako                       | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| sympy_expand               | 455 ms                                                   | 460 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                                  |
| telco                      | 9.73 ms                                                  | 9.86 ms: 1.01x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 146 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 941 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.75 ms                                                  | 8.90 ms: 1.02x slower                                                   |
| sympy_str                  | 264 ms                                                   | 269 ms: 1.02x slower                                                    |
| json                       | 5.61 ms                                                  | 5.74 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.12 sec: 1.03x slower                                                  |
| typing_runtime_protocols   | 192 us                                                   | 197 us: 1.03x slower                                                    |
| dask                       | 350 ms                                                   | 362 ms: 1.03x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.03x slower                                                   |
| fannkuch                   | 452 ms                                                   | 467 ms: 1.03x slower                                                    |
| thrift                     | 946 us                                                   | 979 us: 1.04x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 66.6 ms: 1.04x slower                                                   |
| regex_dna                  | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| pyflate                    | 556 ms                                                   | 582 ms: 1.05x slower                                                    |
| json_loads                 | 31.4 us                                                  | 33.0 us: 1.05x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.12 sec: 1.07x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 4.98 ms: 1.10x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.37 ms: 1.11x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (29): tornado_http, xml_etree_generate, logging_format, django_template, deltablue, meteor_contest, async_tree_io, nqueens, crypto_pyaes, pickle_pure_python, sqlglot_transpile, coverage, 2to3, pidigits, xml_etree_parse, json_dumps, tomli_loads, sympy_integrate, asyncio_websockets, sqlglot_normalize, python_startup, xml_etree_process, genshi_text, regex_effbot, comprehensions, asyncio_tcp, genshi_xml, xml_etree_iterparse, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x