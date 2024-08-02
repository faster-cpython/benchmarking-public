# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 283 ms: 1.03x faster                                                                  |
| html5lib       | 74.7 ms                                                          | 71.7 ms: 1.04x faster                                                                 |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 758 ms: 1.19x faster                                                                  |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.14x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 788 ms: 1.11x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 331 ms: 1.10x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 537 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 76.8 ms: 1.04x faster                                                                 |
| nbody          | 87.8 ms                                                          | 85.7 ms: 1.02x faster                                                                 |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 238 ms: 1.05x faster                                                                  |
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                                                  |
| regex_v8       | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.16 sec: 1.11x faster                                                                |
| unpickle_pure_python | 224 us                                                           | 205 us: 1.09x faster                                                                  |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                                  |
| xml_etree_process    | 59.7 ms                                                          | 58.8 ms: 1.02x faster                                                                 |
| xml_etree_generate   | 85.7 ms                                                          | 84.4 ms: 1.02x faster                                                                 |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                                  |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| json_loads           | 25.0 us                                                          | 25.7 us: 1.03x slower                                                                 |
| pickle_pure_python   | 307 us                                                           | 319 us: 1.04x slower                                                                  |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 55.0 ms: 1.06x faster                                                                 |
| mako           | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 292 us: 1.29x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 30.5 us: 1.22x faster                                                                 |
| generators                 | 33.5 ms                                                          | 28.1 ms: 1.19x faster                                                                 |
| async_tree_io_tg           | 900 ms                                                           | 758 ms: 1.19x faster                                                                  |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                                  |
| deepcopy_reduce            | 3.39 us                                                          | 2.97 us: 1.14x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.14x faster                                                                  |
| richards_super             | 61.2 ms                                                          | 54.7 ms: 1.12x faster                                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.16 sec: 1.11x faster                                                                |
| async_tree_io              | 873 ms                                                           | 788 ms: 1.11x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 331 ms: 1.10x faster                                                                  |
| richards                   | 53.4 ms                                                          | 48.4 ms: 1.10x faster                                                                 |
| unpickle_pure_python       | 224 us                                                           | 205 us: 1.09x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 537 ms: 1.07x faster                                                                  |
| pathlib                    | 17.1 ms                                                          | 16.1 ms: 1.07x faster                                                                 |
| bench_thread_pool          | 908 us                                                           | 853 us: 1.07x faster                                                                  |
| coverage                   | 83.5 ms                                                          | 78.7 ms: 1.06x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                                  |
| genshi_xml                 | 58.1 ms                                                          | 55.0 ms: 1.06x faster                                                                 |
| telco                      | 8.40 ms                                                          | 7.97 ms: 1.05x faster                                                                 |
| pyflate                    | 482 ms                                                           | 458 ms: 1.05x faster                                                                  |
| bpe_tokeniser              | 5.14 sec                                                         | 4.89 sec: 1.05x faster                                                                |
| regex_dna                  | 249 ms                                                           | 238 ms: 1.05x faster                                                                  |
| go                         | 165 ms                                                           | 158 ms: 1.05x faster                                                                  |
| logging_format             | 7.11 us                                                          | 6.80 us: 1.05x faster                                                                 |
| gc_traversal               | 4.69 ms                                                          | 4.49 ms: 1.04x faster                                                                 |
| float                      | 80.2 ms                                                          | 76.8 ms: 1.04x faster                                                                 |
| html5lib                   | 74.7 ms                                                          | 71.7 ms: 1.04x faster                                                                 |
| dask                       | 391 ms                                                           | 376 ms: 1.04x faster                                                                  |
| logging_simple             | 6.40 us                                                          | 6.18 us: 1.04x faster                                                                 |
| regex_compile              | 144 ms                                                           | 139 ms: 1.04x faster                                                                  |
| async_generators           | 363 ms                                                           | 351 ms: 1.03x faster                                                                  |
| 2to3                       | 291 ms                                                           | 283 ms: 1.03x faster                                                                  |
| create_gc_cycles           | 2.00 ms                                                          | 1.94 ms: 1.03x faster                                                                 |
| regex_v8                   | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                                                 |
| coroutines                 | 22.0 ms                                                          | 21.4 ms: 1.03x faster                                                                 |
| scimark_lu                 | 97.5 ms                                                          | 95.0 ms: 1.03x faster                                                                 |
| nbody                      | 87.8 ms                                                          | 85.7 ms: 1.02x faster                                                                 |
| hexiom                     | 6.35 ms                                                          | 6.22 ms: 1.02x faster                                                                 |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                                  |
| xml_etree_process          | 59.7 ms                                                          | 58.8 ms: 1.02x faster                                                                 |
| xml_etree_generate         | 85.7 ms                                                          | 84.4 ms: 1.02x faster                                                                 |
| sympy_sum                  | 155 ms                                                           | 153 ms: 1.01x faster                                                                  |
| xml_etree_parse            | 144 ms                                                           | 142 ms: 1.01x faster                                                                  |
| sympy_str                  | 295 ms                                                           | 291 ms: 1.01x faster                                                                  |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                                  |
| sympy_expand               | 501 ms                                                           | 496 ms: 1.01x faster                                                                  |
| sqlglot_optimize           | 59.5 ms                                                          | 59.0 ms: 1.01x faster                                                                 |
| logging_silent             | 96.3 ns                                                          | 95.6 ns: 1.01x faster                                                                 |
| spectral_norm              | 97.3 ms                                                          | 96.7 ms: 1.01x faster                                                                 |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                                  |
| asyncio_tcp                | 378 ms                                                           | 376 ms: 1.01x faster                                                                  |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                                  |
| pprint_pformat             | 1.66 sec                                                         | 1.67 sec: 1.00x slower                                                                |
| sqlglot_transpile          | 1.76 ms                                                          | 1.77 ms: 1.01x slower                                                                 |
| sympy_integrate            | 23.2 ms                                                          | 23.4 ms: 1.01x slower                                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.1 ms: 1.01x slower                                                                 |
| mako                       | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                                 |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| crypto_pyaes               | 73.6 ms                                                          | 74.7 ms: 1.01x slower                                                                 |
| json                       | 5.35 ms                                                          | 5.45 ms: 1.02x slower                                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                                 |
| comprehensions             | 17.0 us                                                          | 17.4 us: 1.02x slower                                                                 |
| raytrace                   | 260 ms                                                           | 267 ms: 1.02x slower                                                                  |
| json_loads                 | 25.0 us                                                          | 25.7 us: 1.03x slower                                                                 |
| pycparser                  | 1.22 sec                                                         | 1.26 sec: 1.03x slower                                                                |
| chaos                      | 59.6 ms                                                          | 61.4 ms: 1.03x slower                                                                 |
| nqueens                    | 88.4 ms                                                          | 91.1 ms: 1.03x slower                                                                 |
| regex_effbot               | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                                 |
| fannkuch                   | 353 ms                                                           | 365 ms: 1.03x slower                                                                  |
| pickle_pure_python         | 307 us                                                           | 319 us: 1.04x slower                                                                  |
| mdp                        | 2.46 sec                                                         | 2.58 sec: 1.05x slower                                                                |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.49 ms: 1.05x slower                                                                 |
| typing_runtime_protocols   | 171 us                                                           | 180 us: 1.06x slower                                                                  |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                          |

Benchmark hidden because not significant (12): bench_mp_pool, scimark_fft, genshi_text, sqlglot_parse, thrift, docutils, asyncio_tcp_ssl, pprint_safe_repr, deltablue, django_template, scimark_sor, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x