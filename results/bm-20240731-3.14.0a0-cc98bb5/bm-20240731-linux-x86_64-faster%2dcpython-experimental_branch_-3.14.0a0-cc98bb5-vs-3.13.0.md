# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.02x faster
- HPT reliability: 98.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 261 ms: 1.01x faster                                                            |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                          |
| html5lib       | 64.5 ms                                                | 65.0 ms: 1.01x slower                                                           |
| tornado_http   | 91.5 ms                                                | 90.0 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                                            |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 526 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 559 ms: 1.03x faster                                                            |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| asyncio_tcp                | 488 ms                                                 | 491 ms: 1.01x slower                                                            |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 865 ms: 1.05x slower                                                            |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 75.9 ms: 1.03x faster                                                           |
| nbody          | 85.7 ms                                                | 84.5 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                           |
| regex_compile  | 131 ms                                                 | 131 ms: 1.00x faster                                                            |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                           |
| xml_etree_generate  | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                           |
| xml_etree_parse     | 156 ms                                                 | 153 ms: 1.02x faster                                                            |
| tomli_loads         | 2.11 sec                                               | 2.09 sec: 1.01x faster                                                          |
| pickle_pure_python  | 300 us                                                 | 301 us: 1.00x slower                                                            |
| json_dumps          | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| xml_etree_iterparse | 102 ms                                                 | 104 ms: 1.02x slower                                                            |
| json_loads          | 27.0 us                                                | 28.0 us: 1.04x slower                                                           |
| Geometric mean      | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                | 22.4 ms: 1.02x faster                                                           |
| genshi_xml     | 50.3 ms                                                | 49.5 ms: 1.02x faster                                                           |
| mako           | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 262 us: 1.35x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 29.7 us: 1.28x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.71 us: 1.17x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                                            |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                            |
| pathlib                    | 17.1 ms                                                | 15.6 ms: 1.09x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                          |
| richards_super             | 54.4 ms                                                | 50.6 ms: 1.08x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                            |
| richards                   | 48.1 ms                                                | 45.1 ms: 1.07x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.05x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.79 ms: 1.05x faster                                                           |
| logging_simple             | 5.66 us                                                | 5.42 us: 1.05x faster                                                           |
| telco                      | 8.45 ms                                                | 8.10 ms: 1.04x faster                                                           |
| gc_traversal               | 3.81 ms                                                | 3.65 ms: 1.04x faster                                                           |
| go                         | 142 ms                                                 | 136 ms: 1.04x faster                                                            |
| logging_format             | 6.25 us                                                | 6.03 us: 1.04x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 788 us: 1.03x faster                                                            |
| float                      | 78.5 ms                                                | 75.9 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 526 ms: 1.03x faster                                                            |
| regex_effbot               | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                           |
| scimark_fft                | 369 ms                                                 | 359 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 559 ms: 1.03x faster                                                            |
| genshi_text                | 22.9 ms                                                | 22.4 ms: 1.02x faster                                                           |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                           |
| logging_silent             | 102 ns                                                 | 100.0 ns: 1.02x faster                                                          |
| json                       | 5.20 ms                                                | 5.10 ms: 1.02x faster                                                           |
| raytrace                   | 262 ms                                                 | 257 ms: 1.02x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                           |
| xml_etree_generate         | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                           |
| genshi_xml                 | 50.3 ms                                                | 49.5 ms: 1.02x faster                                                           |
| tornado_http               | 91.5 ms                                                | 90.0 ms: 1.02x faster                                                           |
| xml_etree_parse            | 156 ms                                                 | 153 ms: 1.02x faster                                                            |
| thrift                     | 796 us                                                 | 784 us: 1.02x faster                                                            |
| nqueens                    | 80.6 ms                                                | 79.4 ms: 1.02x faster                                                           |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.02x faster                                                            |
| nbody                      | 85.7 ms                                                | 84.5 ms: 1.02x faster                                                           |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                            |
| 2to3                       | 265 ms                                                 | 261 ms: 1.01x faster                                                            |
| tomli_loads                | 2.11 sec                                               | 2.09 sec: 1.01x faster                                                          |
| sqlglot_optimize           | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.25 ms: 1.01x faster                                                           |
| deltablue                  | 3.15 ms                                                | 3.12 ms: 1.01x faster                                                           |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 72.3 ms: 1.01x faster                                                           |
| chaos                      | 58.4 ms                                                | 57.9 ms: 1.01x faster                                                           |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                            |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                                            |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| regex_compile              | 131 ms                                                 | 131 ms: 1.00x faster                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| pickle_pure_python         | 300 us                                                 | 301 us: 1.00x slower                                                            |
| pprint_safe_repr           | 744 ms                                                 | 748 ms: 1.01x slower                                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| asyncio_tcp                | 488 ms                                                 | 491 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 66.3 ms                                                | 66.7 ms: 1.01x slower                                                           |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                           |
| html5lib                   | 64.5 ms                                                | 65.0 ms: 1.01x slower                                                           |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.53 sec: 1.01x slower                                                          |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                           |
| coverage                   | 83.7 ms                                                | 84.6 ms: 1.01x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.02x slower                                                            |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                            |
| pyflate                    | 460 ms                                                 | 469 ms: 1.02x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.28 ms: 1.02x slower                                                           |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.04x slower                                                            |
| json_loads                 | 27.0 us                                                | 28.0 us: 1.04x slower                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.87 sec: 1.04x slower                                                          |
| dask                       | 338 ms                                                 | 353 ms: 1.04x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 865 ms: 1.05x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                          |
| fannkuch                   | 381 ms                                                 | 403 ms: 1.06x slower                                                            |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (9): sympy_str, sympy_expand, django_template, regex_v8, unpickle_pure_python, bench_mp_pool, meteor_contest, coroutines, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x