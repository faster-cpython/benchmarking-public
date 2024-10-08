# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 261 ms: 1.05x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                                          |
| html5lib       | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 90.0 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.15x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 526 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 559 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 865 ms: 1.08x faster                                                            |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 84.5 ms: 1.05x faster                                                           |
| float          | 78.9 ms                                                    | 75.9 ms: 1.04x faster                                                           |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                      | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.05x faster                                                            |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.05x faster                                                            |
| json_loads           | 28.9 us                                                    | 28.0 us: 1.03x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 85.5 ms: 1.02x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                                          |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.4 ms: 1.06x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 49.5 ms: 1.04x faster                                                           |
| django_template | 34.8 ms                                                    | 34.3 ms: 1.01x faster                                                           |
| mako            | 11.2 ms                                                    | 11.2 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.23x faster                                                           |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.15x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                            |
| richards_super             | 57.4 ms                                                    | 50.6 ms: 1.13x faster                                                           |
| richards                   | 50.9 ms                                                    | 45.1 ms: 1.13x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 526 ms: 1.12x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 15.6 ms: 1.11x faster                                                           |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.79 ms: 1.10x faster                                                           |
| coverage                   | 93.1 ms                                                    | 84.6 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 559 ms: 1.09x faster                                                            |
| scimark_fft                | 392 ms                                                     | 359 ms: 1.09x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.65 ms: 1.09x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 865 ms: 1.08x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                           |
| crypto_pyaes               | 77.5 ms                                                    | 72.3 ms: 1.07x faster                                                           |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.06x faster                                                            |
| go                         | 145 ms                                                     | 136 ms: 1.06x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.42 us: 1.06x faster                                                           |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 788 us: 1.06x faster                                                            |
| genshi_text                | 23.7 ms                                                    | 22.4 ms: 1.06x faster                                                           |
| scimark_sor                | 127 ms                                                     | 121 ms: 1.06x faster                                                            |
| xml_etree_parse            | 162 ms                                                     | 153 ms: 1.05x faster                                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.25 ms: 1.05x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 90.0 ms: 1.05x faster                                                           |
| generators                 | 29.6 ms                                                    | 28.2 ms: 1.05x faster                                                           |
| thrift                     | 823 us                                                     | 784 us: 1.05x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                           |
| 2to3                       | 274 ms                                                     | 261 ms: 1.05x faster                                                            |
| regex_compile              | 137 ms                                                     | 131 ms: 1.05x faster                                                            |
| logging_silent             | 105 ns                                                     | 100.0 ns: 1.05x faster                                                          |
| dask                       | 369 ms                                                     | 353 ms: 1.05x faster                                                            |
| nbody                      | 88.3 ms                                                    | 84.5 ms: 1.05x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 49.5 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                           |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 53.3 ms: 1.04x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.12 ms: 1.04x faster                                                           |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                           |
| telco                      | 8.41 ms                                                    | 8.10 ms: 1.04x faster                                                           |
| float                      | 78.9 ms                                                    | 75.9 ms: 1.04x faster                                                           |
| raytrace                   | 267 ms                                                     | 257 ms: 1.04x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.7 ms: 1.04x faster                                                           |
| sympy_str                  | 282 ms                                                     | 272 ms: 1.04x faster                                                            |
| docutils                   | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                                          |
| asyncio_tcp                | 508 ms                                                     | 491 ms: 1.03x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                           |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| pyflate                    | 484 ms                                                     | 469 ms: 1.03x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.87 sec: 1.03x faster                                                          |
| async_generators           | 442 ms                                                     | 429 ms: 1.03x faster                                                            |
| sympy_expand               | 473 ms                                                     | 460 ms: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| sympy_sum                  | 156 ms                                                     | 152 ms: 1.03x faster                                                            |
| nqueens                    | 81.4 ms                                                    | 79.4 ms: 1.03x faster                                                           |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.02x faster                                                            |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 85.5 ms: 1.02x faster                                                           |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                           |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.02x faster                                                          |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                                          |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                                          |
| django_template            | 34.8 ms                                                    | 34.3 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 748 ms: 1.01x faster                                                            |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                           |
| mako                       | 11.2 ms                                                    | 11.2 ms: 1.01x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.28 ms: 1.00x faster                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| regex_dna                  | 221 ms                                                     | 226 ms: 1.02x slower                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (5): pylint, comprehensions, typing_runtime_protocols, fannkuch, regex_v8
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.01x