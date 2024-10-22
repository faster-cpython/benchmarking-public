# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.02x faster
- HPT reliability: 97.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 302 ms: 1.01x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.13 sec: 1.08x slower                                                  |
| html5lib       | 64.3 ms                                                  | 66.4 ms: 1.03x slower                                                   |
| tornado_http   | 131 ms                                                   | 121 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 533 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 400 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 549 ms: 1.14x faster                                                    |
| async_tree_none            | 493 ms                                                   | 438 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 726 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 706 ms: 1.04x faster                                                    |
| async_generators           | 496 ms                                                   | 482 ms: 1.03x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.08 sec: 1.02x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 28.4 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.11 sec: 1.02x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| float          | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                                  |
| json_loads          | 31.4 us                                                  | 32.8 us: 1.05x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_generate, unpickle_pure_python, pickle_pure_python, xml_etree_process, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 330 us: 1.37x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 37.5 us: 1.36x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 533 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.40 us: 1.20x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 400 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 549 ms: 1.14x faster                                                    |
| async_tree_none            | 493 ms                                                   | 438 ms: 1.13x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.4 ms: 1.10x faster                                                   |
| tornado_http               | 131 ms                                                   | 121 ms: 1.08x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.1 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 726 ms: 1.05x faster                                                    |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 706 ms: 1.04x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.00 ms: 1.04x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.37 ms: 1.03x faster                                                   |
| richards_super             | 60.3 ms                                                  | 58.4 ms: 1.03x faster                                                   |
| richards                   | 53.5 ms                                                  | 51.9 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.03x faster                                                  |
| scimark_sor                | 159 ms                                                   | 154 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| async_generators           | 496 ms                                                   | 482 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.8 ms: 1.02x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.25 ms: 1.02x faster                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.08 sec: 1.02x faster                                                  |
| hexiom                     | 7.13 ms                                                  | 6.98 ms: 1.02x faster                                                   |
| deltablue                  | 3.85 ms                                                  | 3.77 ms: 1.02x faster                                                   |
| go                         | 163 ms                                                   | 159 ms: 1.02x faster                                                    |
| logging_format             | 7.83 us                                                  | 7.69 us: 1.02x faster                                                   |
| chaos                      | 68.8 ms                                                  | 67.7 ms: 1.02x faster                                                   |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| logging_simple             | 7.04 us                                                  | 6.93 us: 1.02x faster                                                   |
| float                      | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                                   |
| 2to3                       | 306 ms                                                   | 302 ms: 1.01x faster                                                    |
| raytrace                   | 298 ms                                                   | 294 ms: 1.01x faster                                                    |
| sqlglot_optimize           | 62.4 ms                                                  | 61.8 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.85 sec: 1.01x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 28.4 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| thrift                     | 946 us                                                   | 957 us: 1.01x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                                  |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 942 ms: 1.02x slower                                                    |
| json                       | 5.61 ms                                                  | 5.72 ms: 1.02x slower                                                   |
| fannkuch                   | 452 ms                                                   | 460 ms: 1.02x slower                                                    |
| sympy_expand               | 455 ms                                                   | 464 ms: 1.02x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.11 sec: 1.02x slower                                                  |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 66.4 ms: 1.03x slower                                                   |
| pyflate                    | 556 ms                                                   | 577 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.04x slower                                                   |
| json_loads                 | 31.4 us                                                  | 32.8 us: 1.05x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 201 us: 1.05x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 4.79 ms: 1.06x slower                                                   |
| telco                      | 9.73 ms                                                  | 10.3 ms: 1.06x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.13 sec: 1.08x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (28): xml_etree_generate, coverage, unpickle_pure_python, sqlglot_normalize, pickle_pure_python, crypto_pyaes, scimark_fft, spectral_norm, meteor_contest, genshi_text, sqlglot_transpile, genshi_xml, pidigits, mako, nqueens, xml_etree_process, sympy_integrate, json_dumps, comprehensions, mdp, python_startup_no_site, asyncio_websockets, xml_etree_parse, regex_effbot, sympy_sum, django_template, asyncio_tcp, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 97.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x