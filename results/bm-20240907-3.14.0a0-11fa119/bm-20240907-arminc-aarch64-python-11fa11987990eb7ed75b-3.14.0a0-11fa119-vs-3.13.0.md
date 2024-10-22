# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.02x faster
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 293 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.05 sec: 1.05x slower                                                  |
| html5lib       | 64.3 ms                                                  | 63.1 ms: 1.02x faster                                                   |
| tornado_http   | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 556 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 733 ms: 1.04x faster                                                    |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.04x faster                                                    |
| float          | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list       | 6.65 us                                                  | 6.28 us: 1.06x faster                                                   |
| unpickle            | 20.2 us                                                  | 19.6 us: 1.03x faster                                                   |
| pickle_dict         | 38.1 us                                                  | 37.5 us: 1.02x faster                                                   |
| pickle_list         | 5.34 us                                                  | 5.27 us: 1.01x faster                                                   |
| xml_etree_parse     | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| pickle_pure_python  | 359 us                                                   | 361 us: 1.01x slower                                                    |
| xml_etree_iterparse | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| json_loads          | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads         | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, json_dumps, pickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.2 ms                                                  | 60.6 ms: 1.01x slower                                                   |
| mako           | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 332 us: 1.36x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 38.0 us: 1.34x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| go                         | 163 ms                                                   | 138 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.45 us: 1.18x faster                                                   |
| async_tree_none            | 493 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 556 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| generators                 | 37.8 ms                                                  | 35.1 ms: 1.08x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.0 ms: 1.07x faster                                                   |
| unpack_sequence            | 57.2 ns                                                  | 54.0 ns: 1.06x faster                                                   |
| unpickle_list              | 6.65 us                                                  | 6.28 us: 1.06x faster                                                   |
| tornado_http               | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| nbody                      | 114 ms                                                   | 109 ms: 1.04x faster                                                    |
| 2to3                       | 306 ms                                                   | 293 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 733 ms: 1.04x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.02 ms: 1.04x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.38 ms: 1.03x faster                                                   |
| unpickle                   | 20.2 us                                                  | 19.6 us: 1.03x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| regex_compile              | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| logging_format             | 7.83 us                                                  | 7.62 us: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.0 ms: 1.02x faster                                                   |
| logging_silent             | 135 ns                                                   | 133 ns: 1.02x faster                                                    |
| html5lib                   | 64.3 ms                                                  | 63.1 ms: 1.02x faster                                                   |
| float                      | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                    |
| pickle_dict                | 38.1 us                                                  | 37.5 us: 1.02x faster                                                   |
| thrift                     | 946 us                                                   | 931 us: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 914 ms: 1.01x faster                                                    |
| pickle_list                | 5.34 us                                                  | 5.27 us: 1.01x faster                                                   |
| richards                   | 53.5 ms                                                  | 52.8 ms: 1.01x faster                                                   |
| richards_super             | 60.3 ms                                                  | 59.5 ms: 1.01x faster                                                   |
| logging_simple             | 7.04 us                                                  | 6.95 us: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                                  |
| xml_etree_parse            | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| scimark_fft                | 447 ms                                                   | 443 ms: 1.01x faster                                                    |
| mdp                        | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                                  |
| pickle_pure_python         | 359 us                                                   | 361 us: 1.01x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 60.6 ms: 1.01x slower                                                   |
| mako                       | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| fannkuch                   | 452 ms                                                   | 456 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| raytrace                   | 298 ms                                                   | 301 ms: 1.01x slower                                                    |
| sqlite_synth               | 3.84 us                                                  | 3.90 us: 1.01x slower                                                   |
| pyflate                    | 556 ms                                                   | 566 ms: 1.02x slower                                                    |
| sympy_expand               | 455 ms                                                   | 464 ms: 1.02x slower                                                    |
| regex_dna                  | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.03x slower                                                  |
| telco                      | 9.73 ms                                                  | 9.99 ms: 1.03x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| json_loads                 | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.05 sec: 1.05x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.30 ms: 1.08x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 4.91 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (33): xml_etree_generate, xml_etree_process, meteor_contest, django_template, sympy_integrate, scimark_sor, sqlglot_normalize, genshi_text, python_startup, chaos, sympy_sum, spectral_norm, pprint_pformat, sqlglot_transpile, json_dumps, nqueens, pidigits, pickle, unpickle_pure_python, sqlglot_optimize, comprehensions, typing_runtime_protocols, hexiom, sympy_str, regex_effbot, asyncio_websockets, crypto_pyaes, python_startup_no_site, asyncio_tcp, coverage, deltablue, json, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: dulwich_log

# HPT report

- Reliability score: 99.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x