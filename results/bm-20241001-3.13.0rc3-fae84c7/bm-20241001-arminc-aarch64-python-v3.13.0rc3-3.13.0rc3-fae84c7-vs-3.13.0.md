# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-aarch64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.00x faster
- HPT reliability: 88.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 303 ms: 1.01x faster                                           |
| html5lib       | 64.3 ms                                                  | 64.7 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (3): chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 726 ms: 1.01x faster                                           |
| async_tree_memoization_tg  | 649 ms                                                   | 643 ms: 1.01x faster                                           |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                           |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_io_tg, async_tree_none, async_generators, async_tree_none_tg, asyncio_tcp, async_tree_cpu_io_mixed, async_tree_io, asyncio_tcp_ssl, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 93.7 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                          |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_list    | 5.34 us                                                  | 5.36 us: 1.00x slower                                          |
| json_dumps     | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                          |
| unpickle_list  | 6.65 us                                                  | 6.92 us: 1.04x slower                                          |
| Geometric mean | (ref)                                                    | 1.01x slower                                                   |

Benchmark hidden because not significant (11): xml_etree_generate, unpickle, json_loads, xml_etree_iterparse, pickle_dict, xml_etree_process, tomli_loads, pickle, unpickle_pure_python, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 41.5 ms: 1.02x faster                                          |
| mako            | 13.3 ms                                                  | 13.3 ms: 1.00x faster                                          |
| genshi_xml      | 60.2 ms                                                  | 61.2 ms: 1.02x slower                                          |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| unpack_sequence            | 57.2 ns                                                  | 51.9 ns: 1.10x faster                                          |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                          |
| logging_format             | 7.83 us                                                  | 7.67 us: 1.02x faster                                          |
| django_template            | 42.3 ms                                                  | 41.5 ms: 1.02x faster                                          |
| json                       | 5.61 ms                                                  | 5.53 ms: 1.02x faster                                          |
| flaskblogging              | 4.60 ms                                                  | 4.54 ms: 1.01x faster                                          |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 726 ms: 1.01x faster                                           |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.7 ms: 1.01x faster                                          |
| logging_silent             | 135 ns                                                   | 134 ns: 1.01x faster                                           |
| hexiom                     | 7.13 ms                                                  | 7.04 ms: 1.01x faster                                          |
| async_tree_memoization_tg  | 649 ms                                                   | 643 ms: 1.01x faster                                           |
| 2to3                       | 306 ms                                                   | 303 ms: 1.01x faster                                           |
| float                      | 94.4 ms                                                  | 93.7 ms: 1.01x faster                                          |
| bench_thread_pool          | 1.28 ms                                                  | 1.27 ms: 1.01x faster                                          |
| bpe_tokeniser              | 5.90 sec                                                 | 5.86 sec: 1.01x faster                                         |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.54 ms: 1.01x faster                                          |
| mako                       | 13.3 ms                                                  | 13.3 ms: 1.00x faster                                          |
| pickle_list                | 5.34 us                                                  | 5.36 us: 1.00x slower                                          |
| html5lib                   | 64.3 ms                                                  | 64.7 ms: 1.01x slower                                          |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                           |
| pyflate                    | 556 ms                                                   | 561 ms: 1.01x slower                                           |
| pathlib                    | 22.4 ms                                                  | 22.8 ms: 1.02x slower                                          |
| deepcopy                   | 451 us                                                   | 459 us: 1.02x slower                                           |
| genshi_xml                 | 60.2 ms                                                  | 61.2 ms: 1.02x slower                                          |
| deepcopy_reduce            | 4.07 us                                                  | 4.14 us: 1.02x slower                                          |
| sqlite_synth               | 3.84 us                                                  | 3.92 us: 1.02x slower                                          |
| json_dumps                 | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                          |
| regex_dna                  | 246 ms                                                   | 252 ms: 1.02x slower                                           |
| unpickle_list              | 6.65 us                                                  | 6.92 us: 1.04x slower                                          |
| Geometric mean             | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (73): aiohttp, gunicorn, async_tree_memoization, sympy_sum, xml_etree_generate, unpickle, crypto_pyaes, async_tree_io_tg, async_tree_none, deltablue, async_generators, python_startup, async_tree_none_tg, docutils, sqlglot_normalize, raytrace, chaos, sqlglot_transpile, pylint, coverage, telco, pycparser, asyncio_tcp, async_tree_cpu_io_mixed, json_loads, mypy2, meteor_contest, mdp, logging_simple, xml_etree_iterparse, tornado_http, nbody, scimark_sor, generators, regex_compile, sqlglot_parse, scimark_fft, python_startup_no_site, pickle_dict, nqueens, async_tree_io, dask, pidigits, pprint_pformat, fannkuch, sympy_integrate, richards, xml_etree_process, thrift, comprehensions, tomli_loads, pprint_safe_repr, sympy_str, scimark_lu, spectral_norm, asyncio_tcp_ssl, chameleon, go, bench_mp_pool, pickle, regex_effbot, gc_traversal, unpickle_pure_python, coroutines, sympy_expand, typing_runtime_protocols, sqlglot_optimize, genshi_text, pickle_pure_python, create_gc_cycles, richards_super, deepcopy_memo, xml_etree_parse

# HPT report

- Reliability score: 88.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x