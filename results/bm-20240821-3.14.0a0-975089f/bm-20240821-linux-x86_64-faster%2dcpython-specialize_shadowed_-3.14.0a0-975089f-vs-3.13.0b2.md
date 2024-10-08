# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 975089f
- commit date: 2024-08-21
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 255 ms: 1.08x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                          |
| html5lib       | 67.2 ms                                                    | 66.2 ms: 1.01x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 90.1 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                                            |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 558 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 895 ms: 1.05x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                            |
| nbody          | 88.3 ms                                                    | 86.8 ms: 1.02x faster                                                           |
| float          | 78.9 ms                                                    | 77.7 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.69 ms: 1.01x slower                                                           |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 84.4 ms: 1.04x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.02x faster                                                            |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                            |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.6 ms: 1.05x faster                                                           |
| django_template | 34.8 ms                                                    | 33.6 ms: 1.03x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                           |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 29.6 us: 1.34x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                                            |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                          |
| richards                   | 50.9 ms                                                    | 46.1 ms: 1.10x faster                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                                            |
| richards_super             | 57.4 ms                                                    | 52.0 ms: 1.10x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.78 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 558 ms: 1.09x faster                                                            |
| coverage                   | 93.1 ms                                                    | 85.3 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                           |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                            |
| scimark_fft                | 392 ms                                                     | 364 ms: 1.08x faster                                                            |
| 2to3                       | 274 ms                                                     | 255 ms: 1.08x faster                                                            |
| thrift                     | 823 us                                                     | 766 us: 1.07x faster                                                            |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 72.6 ms: 1.07x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 477 ms: 1.07x faster                                                            |
| bench_thread_pool          | 834 us                                                     | 783 us: 1.06x faster                                                            |
| generators                 | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                                           |
| regex_v8                   | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                          |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.4 ms: 1.06x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 717 ms: 1.06x faster                                                            |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.06x faster                                                            |
| logging_silent             | 105 ns                                                     | 99.3 ns: 1.05x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 90.1 ms: 1.05x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 22.6 ms: 1.05x faster                                                           |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                          |
| async_tree_io_tg           | 936 ms                                                     | 895 ms: 1.05x faster                                                            |
| chaos                      | 61.3 ms                                                    | 58.7 ms: 1.04x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 53.3 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                                          |
| sympy_expand               | 473 ms                                                     | 456 ms: 1.04x faster                                                            |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 84.4 ms: 1.04x faster                                                           |
| telco                      | 8.41 ms                                                    | 8.12 ms: 1.04x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                                           |
| django_template            | 34.8 ms                                                    | 33.6 ms: 1.03x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                           |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| gc_traversal               | 3.98 ms                                                    | 3.86 ms: 1.03x faster                                                           |
| pyflate                    | 484 ms                                                     | 470 ms: 1.03x faster                                                            |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                                            |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| raytrace                   | 267 ms                                                     | 260 ms: 1.03x faster                                                            |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                            |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                            |
| genshi_xml                 | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.8 ms: 1.02x faster                                                           |
| nbody                      | 88.3 ms                                                    | 86.8 ms: 1.02x faster                                                           |
| async_generators           | 442 ms                                                     | 435 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                            |
| float                      | 78.9 ms                                                    | 77.7 ms: 1.02x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.02x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 66.2 ms: 1.01x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.22 ms: 1.01x faster                                                           |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.01x faster                                                          |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                            |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| fannkuch                   | 402 ms                                                     | 404 ms: 1.01x slower                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.69 ms: 1.01x slower                                                           |
| json                       | 5.31 ms                                                    | 5.35 ms: 1.01x slower                                                           |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.02x slower                                                           |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                                            |
| go                         | 145 ms                                                     | 161 ms: 1.11x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (5): async_tree_io, nqueens, comprehensions, coroutines, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x