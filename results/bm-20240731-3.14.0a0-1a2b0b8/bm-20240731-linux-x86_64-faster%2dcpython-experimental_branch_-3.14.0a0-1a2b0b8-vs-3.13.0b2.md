# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 266 ms: 1.03x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                                          |
| html5lib       | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 90.6 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 865 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                            |
| async_tree_io              | 939 ms                                                     | 906 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.4 ms: 1.03x faster                                                           |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| nbody          | 88.3 ms                                                    | 86.4 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 216 ms: 1.02x faster                                                            |
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 85.2 ms: 1.03x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| pickle_pure_python   | 305 us                                                     | 307 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 50.2 ms: 1.03x faster                                                           |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                           |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 263 us: 1.39x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 30.3 us: 1.31x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                                           |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.71 ms: 1.12x faster                                                           |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.10x faster                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                            |
| coverage                   | 93.1 ms                                                    | 84.6 ms: 1.10x faster                                                           |
| richards                   | 50.9 ms                                                    | 46.5 ms: 1.10x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.65 ms: 1.09x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.09x faster                                                            |
| richards_super             | 57.4 ms                                                    | 52.8 ms: 1.09x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 865 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                            |
| scimark_fft                | 392 ms                                                     | 367 ms: 1.07x faster                                                            |
| generators                 | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 787 us: 1.06x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 116 ms: 1.05x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.19 us: 1.04x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 90.6 ms: 1.04x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 488 ms: 1.04x faster                                                            |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.04x faster                                                            |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| genshi_text                | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                           |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                           |
| telco                      | 8.41 ms                                                    | 8.12 ms: 1.04x faster                                                           |
| thrift                     | 823 us                                                     | 794 us: 1.04x faster                                                            |
| async_tree_io              | 939 ms                                                     | 906 ms: 1.04x faster                                                            |
| docutils                   | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                                          |
| crypto_pyaes               | 77.5 ms                                                    | 74.8 ms: 1.04x faster                                                           |
| dask                       | 369 ms                                                     | 357 ms: 1.03x faster                                                            |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 53.8 ms: 1.03x faster                                                           |
| 2to3                       | 274 ms                                                     | 266 ms: 1.03x faster                                                            |
| float                      | 78.9 ms                                                    | 76.4 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                          |
| chaos                      | 61.3 ms                                                    | 59.5 ms: 1.03x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 50.2 ms: 1.03x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.89 sec: 1.03x faster                                                          |
| sympy_str                  | 282 ms                                                     | 275 ms: 1.03x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 85.2 ms: 1.03x faster                                                           |
| json                       | 5.31 ms                                                    | 5.18 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 740 ms: 1.02x faster                                                            |
| sympy_sum                  | 156 ms                                                     | 152 ms: 1.02x faster                                                            |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.02x faster                                                            |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                            |
| nbody                      | 88.3 ms                                                    | 86.4 ms: 1.02x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                            |
| async_generators           | 442 ms                                                     | 433 ms: 1.02x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                           |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.63 us: 1.02x faster                                                           |
| nqueens                    | 81.4 ms                                                    | 80.0 ms: 1.02x faster                                                           |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                            |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                                            |
| sympy_expand               | 473 ms                                                     | 467 ms: 1.01x faster                                                            |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                                            |
| deltablue                  | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                           |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                            |
| go                         | 145 ms                                                     | 144 ms: 1.00x faster                                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                           |
| pickle_pure_python         | 305 us                                                     | 307 us: 1.01x slower                                                            |
| hexiom                     | 6.30 ms                                                    | 6.33 ms: 1.01x slower                                                           |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                           |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                           |
| pyflate                    | 484 ms                                                     | 490 ms: 1.01x slower                                                            |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                           |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                           |
| fannkuch                   | 402 ms                                                     | 409 ms: 1.02x slower                                                            |
| scimark_sor                | 127 ms                                                     | 134 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                    |

Benchmark hidden because not significant (5): pycparser, regex_v8, scimark_monte_carlo, typing_runtime_protocols, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x