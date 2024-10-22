# Results vs. 3.13.0

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-aarch64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 89.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 302 ms: 1.01x faster                                                     |
| docutils       | 2.91 sec                                                 | 3.08 sec: 1.06x slower                                                   |
| html5lib       | 64.3 ms                                                  | 66.6 ms: 1.03x slower                                                    |
| tornado_http   | 131 ms                                                   | 126 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                     |
| async_tree_none_tg         | 467 ms                                                   | 406 ms: 1.15x faster                                                     |
| async_tree_memoization     | 626 ms                                                   | 550 ms: 1.14x faster                                                     |
| async_tree_none            | 493 ms                                                   | 439 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 724 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 705 ms: 1.04x faster                                                     |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                     |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (5): async_tree_io, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 112 ms: 1.02x faster                                                     |
| float          | 94.4 ms                                                  | 93.0 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                                    |
| regex_dna      | 246 ms                                                   | 250 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                                   |
| json_loads          | 31.4 us                                                  | 32.3 us: 1.03x slower                                                    |
| xml_etree_iterparse | 147 ms                                                   | 152 ms: 1.03x slower                                                     |
| xml_etree_parse     | 188 ms                                                   | 196 ms: 1.04x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_generate, unpickle_pure_python, json_dumps, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 331 us: 1.36x faster                                                     |
| deepcopy_memo              | 51.0 us                                                  | 38.5 us: 1.33x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 4.07 us                                                  | 3.51 us: 1.16x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 406 ms: 1.15x faster                                                     |
| async_tree_memoization     | 626 ms                                                   | 550 ms: 1.14x faster                                                     |
| async_tree_none            | 493 ms                                                   | 439 ms: 1.12x faster                                                     |
| pathlib                    | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 724 ms: 1.05x faster                                                     |
| tornado_http               | 131 ms                                                   | 126 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 705 ms: 1.04x faster                                                     |
| bench_mp_pool              | 7.30 ms                                                  | 7.01 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.41 ms: 1.03x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                     |
| nbody                      | 114 ms                                                   | 112 ms: 1.02x faster                                                     |
| richards_super             | 60.3 ms                                                  | 59.0 ms: 1.02x faster                                                    |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                     |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.4 ms: 1.02x faster                                                    |
| mdp                        | 3.36 sec                                                 | 3.31 sec: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.01x faster                                                     |
| float                      | 94.4 ms                                                  | 93.0 ms: 1.01x faster                                                    |
| hexiom                     | 7.13 ms                                                  | 7.04 ms: 1.01x faster                                                    |
| richards                   | 53.5 ms                                                  | 52.8 ms: 1.01x faster                                                    |
| 2to3                       | 306 ms                                                   | 302 ms: 1.01x faster                                                     |
| crypto_pyaes               | 82.7 ms                                                  | 81.6 ms: 1.01x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                    |
| chaos                      | 68.8 ms                                                  | 68.0 ms: 1.01x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                                    |
| logging_silent             | 135 ns                                                   | 134 ns: 1.01x faster                                                     |
| bpe_tokeniser              | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 931 ms: 1.01x slower                                                     |
| tomli_loads                | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                                   |
| sympy_str                  | 264 ms                                                   | 266 ms: 1.01x slower                                                     |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                                    |
| json                       | 5.61 ms                                                  | 5.69 ms: 1.01x slower                                                    |
| regex_dna                  | 246 ms                                                   | 250 ms: 1.01x slower                                                     |
| coverage                   | 98.5 ms                                                  | 100.0 ms: 1.01x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.40 ms: 1.02x slower                                                    |
| thrift                     | 946 us                                                   | 964 us: 1.02x slower                                                     |
| fannkuch                   | 452 ms                                                   | 461 ms: 1.02x slower                                                     |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                                    |
| telco                      | 9.73 ms                                                  | 9.94 ms: 1.02x slower                                                    |
| json_loads                 | 31.4 us                                                  | 32.3 us: 1.03x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 152 ms: 1.03x slower                                                     |
| html5lib                   | 64.3 ms                                                  | 66.6 ms: 1.03x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 103 ms: 1.04x slower                                                     |
| typing_runtime_protocols   | 192 us                                                   | 200 us: 1.04x slower                                                     |
| xml_etree_parse            | 188 ms                                                   | 196 ms: 1.04x slower                                                     |
| docutils                   | 2.91 sec                                                 | 3.08 sec: 1.06x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.30 ms: 1.08x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 4.93 ms: 1.09x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (36): pylint, async_tree_io, xml_etree_generate, asyncio_tcp, meteor_contest, go, unpickle_pure_python, sqlglot_transpile, logging_format, json_dumps, spectral_norm, asyncio_tcp_ssl, raytrace, xml_etree_process, deltablue, sympy_integrate, regex_effbot, pickle_pure_python, generators, pidigits, scimark_sor, python_startup_no_site, mako, pprint_pformat, genshi_xml, logging_simple, pyflate, genshi_text, sympy_expand, regex_compile, asyncio_websockets, sqlglot_normalize, django_template, async_tree_io_tg, sqlglot_optimize, sympy_sum
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240717-3.14.0a0-85453d0/bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json: dulwich_log

# HPT report

- Reliability score: 89.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x