# Results vs. 3.13.0

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: linux-aarch64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 301 ms: 1.02x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.08 sec: 1.06x slower                                                  |
| html5lib       | 64.3 ms                                                  | 66.8 ms: 1.04x slower                                                   |
| tornado_http   | 131 ms                                                   | 125 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 407 ms: 1.15x faster                                                    |
| async_tree_none            | 493 ms                                                   | 443 ms: 1.11x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 569 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 734 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 710 ms: 1.04x faster                                                    |
| async_generators           | 496 ms                                                   | 486 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 587 ms: 1.03x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.14 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): coroutines, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| float          | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| regex_dna      | 246 ms                                                   | 258 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| json_loads      | 31.4 us                                                  | 32.6 us: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (7): json_dumps, xml_etree_process, pickle_pure_python, unpickle_pure_python, xml_etree_generate, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 41.7 ms: 1.01x faster                                                   |
| mako            | 13.3 ms                                                  | 13.3 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 328 us: 1.37x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 38.8 us: 1.31x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.37 us: 1.21x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 407 ms: 1.15x faster                                                    |
| async_tree_none            | 493 ms                                                   | 443 ms: 1.11x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 569 ms: 1.10x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.8 ms: 1.09x faster                                                   |
| tornado_http               | 131 ms                                                   | 125 ms: 1.05x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.3 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 734 ms: 1.04x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 710 ms: 1.04x faster                                                    |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.07 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                    |
| richards                   | 53.5 ms                                                  | 52.3 ms: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.02x faster                                                  |
| nbody                      | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| richards_super             | 60.3 ms                                                  | 59.0 ms: 1.02x faster                                                   |
| async_generators           | 496 ms                                                   | 486 ms: 1.02x faster                                                    |
| telco                      | 9.73 ms                                                  | 9.54 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| logging_format             | 7.83 us                                                  | 7.68 us: 1.02x faster                                                   |
| float                      | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.3 ms: 1.02x faster                                                   |
| 2to3                       | 306 ms                                                   | 301 ms: 1.02x faster                                                    |
| chaos                      | 68.8 ms                                                  | 67.7 ms: 1.02x faster                                                   |
| nqueens                    | 98.7 ms                                                  | 97.1 ms: 1.02x faster                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 1.71 ms: 1.01x faster                                                   |
| django_template            | 42.3 ms                                                  | 41.7 ms: 1.01x faster                                                   |
| deltablue                  | 3.85 ms                                                  | 3.80 ms: 1.01x faster                                                   |
| mdp                        | 3.36 sec                                                 | 3.32 sec: 1.01x faster                                                  |
| scimark_fft                | 447 ms                                                   | 442 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                  |
| xml_etree_parse            | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| sqlglot_optimize           | 62.4 ms                                                  | 61.9 ms: 1.01x faster                                                   |
| mako                       | 13.3 ms                                                  | 13.3 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 936 ms: 1.01x slower                                                    |
| sympy_expand               | 455 ms                                                   | 459 ms: 1.01x slower                                                    |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                                  |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                  |
| regex_effbot               | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| dask                       | 350 ms                                                   | 360 ms: 1.03x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 198 us: 1.03x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 587 ms: 1.03x slower                                                    |
| json_loads                 | 31.4 us                                                  | 32.6 us: 1.04x slower                                                   |
| html5lib                   | 64.3 ms                                                  | 66.8 ms: 1.04x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.14 sec: 1.04x slower                                                  |
| regex_dna                  | 246 ms                                                   | 258 ms: 1.05x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.08 sec: 1.06x slower                                                  |
| fannkuch                   | 452 ms                                                   | 478 ms: 1.06x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.31 ms: 1.09x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.08 ms: 1.12x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (34): bench_thread_pool, python_startup, go, json_dumps, crypto_pyaes, xml_etree_process, scimark_sparse_mat_mult, raytrace, thrift, pickle_pure_python, hexiom, unpickle_pure_python, sympy_sum, spectral_norm, xml_etree_generate, regex_compile, scimark_sor, coroutines, pidigits, genshi_text, logging_simple, sympy_integrate, tomli_loads, python_startup_no_site, sqlglot_normalize, asyncio_websockets, coverage, async_tree_io, sympy_str, sqlglot_parse, json, genshi_xml, xml_etree_iterparse, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: dulwich_log

# HPT report

- Reliability score: 99.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x