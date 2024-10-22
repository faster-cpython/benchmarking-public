# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-aarch64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.01x faster
- HPT reliability: 95.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 2.91 sec                                                 | 3.17 sec: 1.09x slower                                                            |
| html5lib       | 64.3 ms                                                  | 66.1 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                    | 1.03x slower                                                                      |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                              |
| async_tree_none_tg         | 467 ms                                                   | 402 ms: 1.16x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 558 ms: 1.12x faster                                                              |
| async_tree_none            | 493 ms                                                   | 443 ms: 1.11x faster                                                              |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 736 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 710 ms: 1.04x faster                                                              |
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                                              |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                            |
| asyncio_tcp                | 568 ms                                                   | 585 ms: 1.03x slower                                                              |
| async_tree_io_tg           | 1.09 sec                                                 | 1.14 sec: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 92.2 ms: 1.02x faster                                                             |
| nbody          | 114 ms                                                   | 112 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.9 ms: 1.02x faster                                                             |
| regex_effbot   | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                             |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 254 us                                                   | 249 us: 1.02x faster                                                              |
| tomli_loads          | 2.53 sec                                                 | 2.48 sec: 1.02x faster                                                            |
| xml_etree_parse      | 188 ms                                                   | 186 ms: 1.01x faster                                                              |
| json_loads           | 31.4 us                                                  | 32.7 us: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, pickle_pure_python, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                             |
| genshi_text    | 27.7 ms                                                  | 28.0 ms: 1.01x slower                                                             |
| genshi_xml     | 60.2 ms                                                  | 62.2 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 329 us: 1.37x faster                                                              |
| deepcopy_memo              | 51.0 us                                                  | 38.6 us: 1.32x faster                                                             |
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                              |
| deepcopy_reduce            | 4.07 us                                                  | 3.44 us: 1.18x faster                                                             |
| async_tree_none_tg         | 467 ms                                                   | 402 ms: 1.16x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 558 ms: 1.12x faster                                                              |
| async_tree_none            | 493 ms                                                   | 443 ms: 1.11x faster                                                              |
| generators                 | 37.8 ms                                                  | 34.9 ms: 1.08x faster                                                             |
| logging_silent             | 135 ns                                                   | 129 ns: 1.05x faster                                                              |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 736 ms: 1.04x faster                                                              |
| pathlib                    | 22.4 ms                                                  | 21.6 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 710 ms: 1.04x faster                                                              |
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                                              |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                             |
| bench_mp_pool              | 7.30 ms                                                  | 7.07 ms: 1.03x faster                                                             |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                              |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                            |
| go                         | 163 ms                                                   | 158 ms: 1.03x faster                                                              |
| richards                   | 53.5 ms                                                  | 52.2 ms: 1.03x faster                                                             |
| logging_format             | 7.83 us                                                  | 7.63 us: 1.03x faster                                                             |
| float                      | 94.4 ms                                                  | 92.2 ms: 1.02x faster                                                             |
| richards_super             | 60.3 ms                                                  | 58.9 ms: 1.02x faster                                                             |
| unpickle_pure_python       | 254 us                                                   | 249 us: 1.02x faster                                                              |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                             |
| regex_v8                   | 31.5 ms                                                  | 30.9 ms: 1.02x faster                                                             |
| tomli_loads                | 2.53 sec                                                 | 2.48 sec: 1.02x faster                                                            |
| nbody                      | 114 ms                                                   | 112 ms: 1.02x faster                                                              |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.48 ms: 1.02x faster                                                             |
| logging_simple             | 7.04 us                                                  | 6.95 us: 1.01x faster                                                             |
| scimark_fft                | 447 ms                                                   | 442 ms: 1.01x faster                                                              |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                            |
| bpe_tokeniser              | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                            |
| xml_etree_parse            | 188 ms                                                   | 186 ms: 1.01x faster                                                              |
| mako                       | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                             |
| sympy_expand               | 455 ms                                                   | 460 ms: 1.01x slower                                                              |
| genshi_text                | 27.7 ms                                                  | 28.0 ms: 1.01x slower                                                             |
| hexiom                     | 7.13 ms                                                  | 7.22 ms: 1.01x slower                                                             |
| pyflate                    | 556 ms                                                   | 563 ms: 1.01x slower                                                              |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.01x slower                                                             |
| sympy_integrate            | 21.0 ms                                                  | 21.3 ms: 1.02x slower                                                             |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.02x slower                                                              |
| pprint_pformat             | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                                            |
| thrift                     | 946 us                                                   | 962 us: 1.02x slower                                                              |
| regex_effbot               | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                             |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                            |
| pprint_safe_repr           | 926 ms                                                   | 946 ms: 1.02x slower                                                              |
| nqueens                    | 98.7 ms                                                  | 101 ms: 1.02x slower                                                              |
| html5lib                   | 64.3 ms                                                  | 66.1 ms: 1.03x slower                                                             |
| typing_runtime_protocols   | 192 us                                                   | 197 us: 1.03x slower                                                              |
| asyncio_tcp                | 568 ms                                                   | 585 ms: 1.03x slower                                                              |
| fannkuch                   | 452 ms                                                   | 466 ms: 1.03x slower                                                              |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                                              |
| genshi_xml                 | 60.2 ms                                                  | 62.2 ms: 1.03x slower                                                             |
| dask                       | 350 ms                                                   | 364 ms: 1.04x slower                                                              |
| json_loads                 | 31.4 us                                                  | 32.7 us: 1.04x slower                                                             |
| async_tree_io_tg           | 1.09 sec                                                 | 1.14 sec: 1.04x slower                                                            |
| docutils                   | 2.91 sec                                                 | 3.17 sec: 1.09x slower                                                            |
| create_gc_cycles           | 2.12 ms                                                  | 2.32 ms: 1.09x slower                                                             |
| gc_traversal               | 4.53 ms                                                  | 5.04 ms: 1.11x slower                                                             |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (31): async_tree_io, scimark_sor, sqlglot_transpile, scimark_monte_carlo, tornado_http, sqlglot_normalize, meteor_contest, chaos, json_dumps, coverage, 2to3, raytrace, regex_compile, deltablue, xml_etree_process, django_template, sqlglot_optimize, pidigits, python_startup_no_site, asyncio_websockets, telco, pickle_pure_python, crypto_pyaes, spectral_norm, coroutines, json, xml_etree_iterparse, xml_etree_generate, sympy_sum, sqlglot_parse, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 95.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x