# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0
- machine: linux-aarch64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.00x faster
- HPT reliability: 76.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 2.91 sec: 1.07x faster                                   |
| html5lib       | 66.1 ms                                                      | 64.3 ms: 1.03x faster                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                             |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.09 sec: 1.17x faster                                   |
| async_tree_io              | 1.22 sec                                                     | 1.11 sec: 1.11x faster                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 736 ms: 1.04x faster                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 764 ms: 1.04x faster                                     |
| async_tree_memoization     | 645 ms                                                       | 626 ms: 1.03x faster                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 649 ms: 1.07x slower                                     |
| Geometric mean             | (ref)                                                        | 1.04x faster                                             |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 91.4 ms                                                      | 94.4 ms: 1.03x slower                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                     |
| regex_effbot   | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                    |
| regex_v8       | 31.1 ms                                                      | 31.5 ms: 1.01x slower                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.4 us: 1.02x faster                                    |
| tomli_loads          | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                   |
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                     |
| pickle_list          | 5.27 us                                                      | 5.34 us: 1.01x slower                                    |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                    |
| unpickle             | 19.8 us                                                      | 20.2 us: 1.02x slower                                    |
| unpickle_list        | 6.52 us                                                      | 6.65 us: 1.02x slower                                    |
| Geometric mean       | (ref)                                                        | 1.00x slower                                             |

Benchmark hidden because not significant (7): xml_etree_parse, xml_etree_process, xml_etree_generate, xml_etree_iterparse, pickle_pure_python, pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                    |
| python_startup         | 13.0 ms                                                      | 13.3 ms: 1.02x slower                                    |
| Geometric mean         | (ref)                                                        | 1.02x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.7 ms: 1.01x slower                                    |
| mako           | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                             |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.09 sec: 1.17x faster                                   |
| gc_traversal               | 5.17 ms                                                      | 4.53 ms: 1.14x faster                                    |
| async_tree_io              | 1.22 sec                                                     | 1.11 sec: 1.11x faster                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.12 ms: 1.10x faster                                    |
| docutils                   | 3.10 sec                                                     | 2.91 sec: 1.07x faster                                   |
| dask                       | 370 ms                                                       | 350 ms: 1.06x faster                                     |
| regex_dna                  | 259 ms                                                       | 246 ms: 1.05x faster                                     |
| richards                   | 55.9 ms                                                      | 53.5 ms: 1.04x faster                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 736 ms: 1.04x faster                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 764 ms: 1.04x faster                                     |
| richards_super             | 62.3 ms                                                      | 60.3 ms: 1.03x faster                                    |
| async_tree_memoization     | 645 ms                                                       | 626 ms: 1.03x faster                                     |
| telco                      | 10.0 ms                                                      | 9.73 ms: 1.03x faster                                    |
| asyncio_tcp                | 584 ms                                                       | 568 ms: 1.03x faster                                     |
| html5lib                   | 66.1 ms                                                      | 64.3 ms: 1.03x faster                                    |
| coroutines                 | 29.0 ms                                                      | 28.2 ms: 1.03x faster                                    |
| logging_simple             | 7.21 us                                                      | 7.04 us: 1.02x faster                                    |
| regex_effbot               | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                    |
| json_loads                 | 32.1 us                                                      | 31.4 us: 1.02x faster                                    |
| flaskblogging              | 4.70 ms                                                      | 4.60 ms: 1.02x faster                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.90 sec: 1.02x faster                                   |
| tomli_loads                | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                   |
| thrift                     | 962 us                                                       | 946 us: 1.02x faster                                     |
| pathlib                    | 22.8 ms                                                      | 22.4 ms: 1.02x faster                                    |
| sqlite_synth               | 3.90 us                                                      | 3.84 us: 1.02x faster                                    |
| scimark_lu                 | 141 ms                                                       | 139 ms: 1.01x faster                                     |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.18 sec: 1.01x faster                                   |
| pprint_safe_repr           | 933 ms                                                       | 926 ms: 1.01x faster                                     |
| deepcopy_reduce            | 4.04 us                                                      | 4.07 us: 1.01x slower                                    |
| genshi_text                | 27.4 ms                                                      | 27.7 ms: 1.01x slower                                    |
| mdp                        | 3.33 sec                                                     | 3.36 sec: 1.01x slower                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.90 sec: 1.01x slower                                   |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                     |
| pickle_list                | 5.27 us                                                      | 5.34 us: 1.01x slower                                    |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                    |
| logging_silent             | 133 ns                                                       | 135 ns: 1.01x slower                                     |
| regex_v8                   | 31.1 ms                                                      | 31.5 ms: 1.01x slower                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.28 ms: 1.02x slower                                    |
| async_generators           | 488 ms                                                       | 496 ms: 1.02x slower                                     |
| python_startup_no_site     | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                    |
| generators                 | 37.1 ms                                                      | 37.8 ms: 1.02x slower                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.8 ms: 1.02x slower                                    |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                    |
| unpickle                   | 19.8 us                                                      | 20.2 us: 1.02x slower                                    |
| unpickle_list              | 6.52 us                                                      | 6.65 us: 1.02x slower                                    |
| python_startup             | 13.0 ms                                                      | 13.3 ms: 1.02x slower                                    |
| float                      | 91.4 ms                                                      | 94.4 ms: 1.03x slower                                    |
| pycparser                  | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.30 ms: 1.04x slower                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 649 ms: 1.07x slower                                     |
| mypy2                      | 767 ms                                                       | 1.18 sec: 1.54x slower                                   |
| Geometric mean             | (ref)                                                        | 1.00x faster                                             |

Benchmark hidden because not significant (50): sqlglot_parse, xml_etree_parse, async_tree_none_tg, xml_etree_process, typing_runtime_protocols, sqlglot_normalize, deltablue, sympy_str, comprehensions, sympy_expand, json, sqlglot_optimize, xml_etree_generate, genshi_xml, scimark_sor, nqueens, asyncio_websockets, pyflate, django_template, sympy_sum, spectral_norm, pidigits, xml_etree_iterparse, nbody, meteor_contest, logging_format, fannkuch, coverage, pickle_pure_python, async_tree_none, 2to3, regex_compile, raytrace, scimark_sparse_mat_mult, scimark_fft, deepcopy_memo, sympy_integrate, deepcopy, pickle, chameleon, chaos, hexiom, crypto_pyaes, aiohttp, go, sqlglot_transpile, gunicorn, pickle_dict, pylint, tornado_http
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: dulwich_log
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 76.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x