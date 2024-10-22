# Results vs. 3.13.0

- fork: python
- ref: d27a53fc02a87e76066f
- machine: linux-aarch64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.02x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 302 ms: 1.01x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.16 sec: 1.09x slower                                                  |
| html5lib       | 64.3 ms                                                  | 67.8 ms: 1.05x slower                                                   |
| tornado_http   | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 538 ms: 1.21x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 406 ms: 1.15x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 555 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 438 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 727 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 706 ms: 1.04x faster                                                    |
| async_generators           | 496 ms                                                   | 484 ms: 1.02x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 558 ms: 1.02x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.1 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.19 sec: 1.00x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.12 sec: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                                   |
| regex_compile  | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| regex_dna      | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 254 us                                                   | 251 us: 1.01x faster                                                    |
| xml_etree_parse      | 188 ms                                                   | 185 ms: 1.01x faster                                                    |
| pickle_pure_python   | 359 us                                                   | 365 us: 1.02x slower                                                    |
| json_loads           | 31.4 us                                                  | 33.2 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, tomli_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 328 us: 1.37x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 37.6 us: 1.36x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.34 us: 1.22x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 538 ms: 1.21x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 406 ms: 1.15x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 555 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 438 ms: 1.13x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.8 ms: 1.09x faster                                                   |
| tornado_http               | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 727 ms: 1.05x faster                                                    |
| logging_silent             | 135 ns                                                   | 129 ns: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 80.4 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 706 ms: 1.04x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.01 ms: 1.04x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.03x faster                                                  |
| pathlib                    | 22.4 ms                                                  | 21.7 ms: 1.03x faster                                                   |
| richards_super             | 60.3 ms                                                  | 58.7 ms: 1.03x faster                                                   |
| float                      | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                   |
| chaos                      | 68.8 ms                                                  | 67.0 ms: 1.03x faster                                                   |
| async_generators           | 496 ms                                                   | 484 ms: 1.02x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.44 ms: 1.02x faster                                                   |
| asyncio_tcp                | 568 ms                                                   | 558 ms: 1.02x faster                                                    |
| richards                   | 53.5 ms                                                  | 52.7 ms: 1.02x faster                                                   |
| go                         | 163 ms                                                   | 160 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 254 us                                                   | 251 us: 1.01x faster                                                    |
| raytrace                   | 298 ms                                                   | 294 ms: 1.01x faster                                                    |
| deltablue                  | 3.85 ms                                                  | 3.80 ms: 1.01x faster                                                   |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.01x faster                                                    |
| scimark_sor                | 159 ms                                                   | 157 ms: 1.01x faster                                                    |
| regex_compile              | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| xml_etree_parse            | 188 ms                                                   | 185 ms: 1.01x faster                                                    |
| 2to3                       | 306 ms                                                   | 302 ms: 1.01x faster                                                    |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                  |
| bpe_tokeniser              | 5.90 sec                                                 | 5.86 sec: 1.01x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 28.1 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.19 sec: 1.00x slower                                                  |
| sympy_str                  | 264 ms                                                   | 267 ms: 1.01x slower                                                    |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.01x slower                                                   |
| pickle_pure_python         | 359 us                                                   | 365 us: 1.02x slower                                                    |
| fannkuch                   | 452 ms                                                   | 460 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.94 sec: 1.02x slower                                                  |
| typing_runtime_protocols   | 192 us                                                   | 196 us: 1.02x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 948 ms: 1.02x slower                                                    |
| json                       | 5.61 ms                                                  | 5.76 ms: 1.03x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.12 sec: 1.03x slower                                                  |
| thrift                     | 946 us                                                   | 974 us: 1.03x slower                                                    |
| regex_dna                  | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| dask                       | 350 ms                                                   | 365 ms: 1.04x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 67.8 ms: 1.05x slower                                                   |
| json_loads                 | 31.4 us                                                  | 33.2 us: 1.06x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.16 sec: 1.09x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.34 ms: 1.10x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.06 ms: 1.12x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (32): xml_etree_generate, xml_etree_process, async_tree_io, logging_format, genshi_text, python_startup, crypto_pyaes, django_template, hexiom, spectral_norm, tomli_loads, sqlglot_transpile, coverage, sqlglot_optimize, sympy_sum, sympy_integrate, logging_simple, sqlglot_normalize, pidigits, meteor_contest, asyncio_websockets, mako, sqlglot_parse, python_startup_no_site, sympy_expand, json_dumps, xml_etree_iterparse, telco, regex_effbot, nqueens, genshi_xml, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x