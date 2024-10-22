# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: 3d7e23f
- commit date: 2024-08-05
- overall geometric mean: 1.02x faster
- HPT reliability: 88.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 263 ms: 1.01x faster                                                            |
| docutils       | 2.58 sec                                               | 2.74 sec: 1.06x slower                                                          |
| html5lib       | 64.5 ms                                                | 66.0 ms: 1.02x slower                                                           |
| tornado_http   | 91.5 ms                                                | 89.7 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.19x faster                                                            |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 526 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 558 ms: 1.03x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 485 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                                            |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 866 ms: 1.05x slower                                                            |
| async_tree_io              | 843 ms                                                 | 899 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.8 ms: 1.01x faster                                                           |
| nbody          | 85.7 ms                                                | 86.2 ms: 1.01x slower                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.87 ms: 1.00x faster                                                           |
| regex_v8       | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                           |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.03 sec: 1.04x faster                                                          |
| xml_etree_generate   | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 59.4 ms: 1.02x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                            |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.00x slower                                                            |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.02x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.02x slower                                                            |
| json_loads           | 27.0 us                                                | 27.8 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                           |
| mako           | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| genshi_xml     | 50.3 ms                                                | 52.5 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 28.6 us: 1.33x faster                                                           |
| go                         | 142 ms                                                 | 117 ms: 1.21x faster                                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.19x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.71 us: 1.17x faster                                                           |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                            |
| pathlib                    | 17.1 ms                                                | 15.7 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                            |
| richards_super             | 54.4 ms                                                | 51.6 ms: 1.05x faster                                                           |
| richards                   | 48.1 ms                                                | 45.9 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.81 ms: 1.04x faster                                                           |
| logging_silent             | 102 ns                                                 | 98.0 ns: 1.04x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 2.03 sec: 1.04x faster                                                          |
| telco                      | 8.45 ms                                                | 8.12 ms: 1.04x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 785 us: 1.04x faster                                                            |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                          |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 526 ms: 1.03x faster                                                            |
| scimark_fft                | 369 ms                                                 | 358 ms: 1.03x faster                                                            |
| logging_simple             | 5.66 us                                                | 5.51 us: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 558 ms: 1.03x faster                                                            |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                            |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| tornado_http               | 91.5 ms                                                | 89.7 ms: 1.02x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                          |
| thrift                     | 796 us                                                 | 781 us: 1.02x faster                                                            |
| logging_format             | 6.25 us                                                | 6.14 us: 1.02x faster                                                           |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                           |
| raytrace                   | 262 ms                                                 | 257 ms: 1.02x faster                                                            |
| xml_etree_generate         | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                           |
| xml_etree_process          | 60.4 ms                                                | 59.4 ms: 1.02x faster                                                           |
| nqueens                    | 80.6 ms                                                | 79.3 ms: 1.02x faster                                                           |
| sqlglot_optimize           | 53.9 ms                                                | 53.1 ms: 1.02x faster                                                           |
| gc_traversal               | 3.81 ms                                                | 3.75 ms: 1.01x faster                                                           |
| sympy_expand               | 462 ms                                                 | 456 ms: 1.01x faster                                                            |
| chaos                      | 58.4 ms                                                | 57.7 ms: 1.01x faster                                                           |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                            |
| sympy_str                  | 274 ms                                                 | 271 ms: 1.01x faster                                                            |
| crypto_pyaes               | 73.0 ms                                                | 72.2 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 744 ms                                                 | 737 ms: 1.01x faster                                                            |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                            |
| 2to3                       | 265 ms                                                 | 263 ms: 1.01x faster                                                            |
| float                      | 78.5 ms                                                | 77.8 ms: 1.01x faster                                                           |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.01x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 485 ms: 1.01x faster                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| regex_effbot               | 3.88 ms                                                | 3.87 ms: 1.00x faster                                                           |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x slower                                                            |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.00x slower                                                            |
| nbody                      | 85.7 ms                                                | 86.2 ms: 1.01x slower                                                           |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| genshi_text                | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 66.8 ms: 1.01x slower                                                           |
| hexiom                     | 6.13 ms                                                | 6.18 ms: 1.01x slower                                                           |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                            |
| deltablue                  | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                           |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| regex_v8                   | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.78 sec: 1.02x slower                                                          |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                                            |
| html5lib                   | 64.5 ms                                                | 66.0 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 159 us                                                 | 163 us: 1.02x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.02x slower                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.02x slower                                                            |
| json_loads                 | 27.0 us                                                | 27.8 us: 1.03x slower                                                           |
| pyflate                    | 460 ms                                                 | 473 ms: 1.03x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                           |
| genshi_xml                 | 50.3 ms                                                | 52.5 ms: 1.04x slower                                                           |
| regex_dna                  | 220 ms                                                 | 229 ms: 1.04x slower                                                            |
| dask                       | 338 ms                                                 | 353 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 866 ms: 1.05x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.74 sec: 1.06x slower                                                          |
| async_tree_io              | 843 ms                                                 | 899 ms: 1.07x slower                                                            |
| fannkuch                   | 381 ms                                                 | 408 ms: 1.07x slower                                                            |
| coverage                   | 83.7 ms                                                | 90.3 ms: 1.08x slower                                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (8): json, django_template, bench_mp_pool, sqlglot_parse, xml_etree_parse, sympy_sum, regex_compile, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 88.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x