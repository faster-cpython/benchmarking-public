# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-aarch64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                                  |
| html5lib       | 64.3 ms                                                  | 65.6 ms: 1.02x slower                                                   |
| tornado_http   | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 419 ms: 1.18x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 723 ms: 1.06x faster                                                    |
| async_generators           | 496 ms                                                   | 483 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.03x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| float          | 94.4 ms                                                  | 93.3 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 20.2 us                                                  | 19.5 us: 1.03x faster                                                   |
| unpickle_list       | 6.65 us                                                  | 6.54 us: 1.02x faster                                                   |
| pickle_list         | 5.34 us                                                  | 5.26 us: 1.01x faster                                                   |
| xml_etree_parse     | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| xml_etree_iterparse | 147 ms                                                   | 149 ms: 1.01x slower                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_process, xml_etree_generate, json_dumps, pickle_dict, pickle_pure_python, unpickle_pure_python, json_loads, pickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (3): django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 333 us: 1.36x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 38.0 us: 1.34x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 419 ms: 1.18x faster                                                    |
| go                         | 163 ms                                                   | 138 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.50 us: 1.16x faster                                                   |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| tornado_http               | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 723 ms: 1.06x faster                                                    |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| 2to3                       | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.03x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| unpickle                   | 20.2 us                                                  | 19.5 us: 1.03x faster                                                   |
| sympy_sum                  | 143 ms                                                   | 139 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| async_generators           | 496 ms                                                   | 483 ms: 1.03x faster                                                    |
| logging_silent             | 135 ns                                                   | 132 ns: 1.03x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.12 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.03x faster                                                    |
| logging_format             | 7.83 us                                                  | 7.65 us: 1.02x faster                                                   |
| richards_super             | 60.3 ms                                                  | 59.1 ms: 1.02x faster                                                   |
| genshi_text                | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                                   |
| sympy_integrate            | 21.0 ms                                                  | 20.6 ms: 1.02x faster                                                   |
| mdp                        | 3.36 sec                                                 | 3.31 sec: 1.02x faster                                                  |
| unpickle_list              | 6.65 us                                                  | 6.54 us: 1.02x faster                                                   |
| crypto_pyaes               | 82.7 ms                                                  | 81.4 ms: 1.02x faster                                                   |
| richards                   | 53.5 ms                                                  | 52.7 ms: 1.01x faster                                                   |
| thrift                     | 946 us                                                   | 932 us: 1.01x faster                                                    |
| pickle_list                | 5.34 us                                                  | 5.26 us: 1.01x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 914 ms: 1.01x faster                                                    |
| json                       | 5.61 ms                                                  | 5.54 ms: 1.01x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| float                      | 94.4 ms                                                  | 93.3 ms: 1.01x faster                                                   |
| spectral_norm              | 141 ms                                                   | 140 ms: 1.01x faster                                                    |
| scimark_fft                | 447 ms                                                   | 444 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.85 sec: 1.01x faster                                                  |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                  |
| sympy_expand               | 455 ms                                                   | 459 ms: 1.01x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.39 ms: 1.01x slower                                                   |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 194 us: 1.01x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.01x slower                                                    |
| raytrace                   | 298 ms                                                   | 302 ms: 1.02x slower                                                    |
| fannkuch                   | 452 ms                                                   | 459 ms: 1.02x slower                                                    |
| regex_effbot               | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| html5lib                   | 64.3 ms                                                  | 65.6 ms: 1.02x slower                                                   |
| deltablue                  | 3.85 ms                                                  | 3.93 ms: 1.02x slower                                                   |
| regex_dna                  | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 101 ms: 1.02x slower                                                    |
| unpack_sequence            | 57.2 ns                                                  | 58.5 ns: 1.02x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                                  |
| pyflate                    | 556 ms                                                   | 580 ms: 1.04x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| telco                      | 9.73 ms                                                  | 10.3 ms: 1.05x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.28 ms: 1.07x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 5.09 ms: 1.12x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (33): regex_compile, asyncio_tcp, scimark_sor, python_startup, django_template, xml_etree_process, meteor_contest, scimark_sparse_mat_mult, python_startup_no_site, xml_etree_generate, hexiom, scimark_monte_carlo, sympy_str, logging_simple, mako, json_dumps, sqlglot_optimize, pidigits, chaos, asyncio_tcp_ssl, pickle_dict, pickle_pure_python, unpickle_pure_python, sqlglot_transpile, sqlglot_normalize, coverage, json_loads, asyncio_websockets, pickle, comprehensions, sqlite_synth, genshi_xml, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: dulwich_log

# HPT report

- Reliability score: 99.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x