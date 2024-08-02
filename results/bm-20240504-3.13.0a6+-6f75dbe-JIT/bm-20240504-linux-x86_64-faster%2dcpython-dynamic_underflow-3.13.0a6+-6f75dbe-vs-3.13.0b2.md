# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: dynamic_underflow
- machine: linux-x86_64
- commit hash: 6f75dbe
- commit date: 2024-05-04
- overall geometric mean: 1.01x slower
- HPT reliability: 92.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 285 ms: 1.04x slower                                                          |
| chameleon      | 7.22 ms                                                    | 7.31 ms: 1.01x slower                                                         |
| html5lib       | 67.2 ms                                                    | 70.6 ms: 1.05x slower                                                         |
| tornado_http   | 94.6 ms                                                    | 105 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                      | 1.05x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 611 ms                                                     | 639 ms: 1.05x slower                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 615 ms: 1.05x slower                                                          |
| async_tree_none_tg         | 336 ms                                                     | 354 ms: 1.05x slower                                                          |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                                  |

Benchmark hidden because not significant (5): async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                         |
| float          | 78.9 ms                                                    | 73.2 ms: 1.08x faster                                                         |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.71 ms: 1.01x slower                                                         |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                                          |
| regex_compile  | 137 ms                                                     | 143 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                          |
| tomli_loads          | 2.12 sec                                                   | 2.02 sec: 1.05x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                         |
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                         |
| xml_etree_process    | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                                         |
| unpickle_pure_python | 218 us                                                     | 209 us: 1.05x faster                                                          |
| xml_etree_generate   | 87.4 ms                                                    | 83.9 ms: 1.04x faster                                                         |
| pickle_list          | 5.11 us                                                    | 4.92 us: 1.04x faster                                                         |
| pickle_pure_python   | 305 us                                                     | 299 us: 1.02x faster                                                          |
| unpickle_list        | 5.34 us                                                    | 5.26 us: 1.02x faster                                                         |
| pickle_dict          | 34.8 us                                                    | 35.0 us: 1.01x slower                                                         |
| unpickle             | 15.1 us                                                    | 15.5 us: 1.03x slower                                                         |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                         |
| python_startup_no_site | 7.11 ms                                                    | 7.65 ms: 1.08x slower                                                         |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.66 ms: 1.16x faster                                                         |
| genshi_text     | 23.7 ms                                                    | 23.5 ms: 1.01x faster                                                         |
| django_template | 34.8 ms                                                    | 36.7 ms: 1.06x slower                                                         |
| genshi_xml      | 51.6 ms                                                    | 62.7 ms: 1.22x slower                                                         |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_fft                | 392 ms                                                     | 322 ms: 1.22x faster                                                          |
| mako                       | 11.2 ms                                                    | 9.66 ms: 1.16x faster                                                         |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.6 ms: 1.12x faster                                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.71 ms: 1.12x faster                                                         |
| richards_super             | 57.4 ms                                                    | 51.5 ms: 1.11x faster                                                         |
| crypto_pyaes               | 77.5 ms                                                    | 69.7 ms: 1.11x faster                                                         |
| richards                   | 50.9 ms                                                    | 45.9 ms: 1.11x faster                                                         |
| nbody                      | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                         |
| fannkuch                   | 402 ms                                                     | 371 ms: 1.08x faster                                                          |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.08x faster                                                          |
| pyflate                    | 484 ms                                                     | 447 ms: 1.08x faster                                                          |
| float                      | 78.9 ms                                                    | 73.2 ms: 1.08x faster                                                         |
| mdp                        | 2.79 sec                                                   | 2.59 sec: 1.07x faster                                                        |
| logging_silent             | 105 ns                                                     | 98.0 ns: 1.07x faster                                                         |
| chaos                      | 61.3 ms                                                    | 57.5 ms: 1.07x faster                                                         |
| coverage                   | 93.1 ms                                                    | 87.4 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                     | 101 ms: 1.06x faster                                                          |
| tomli_loads                | 2.12 sec                                                   | 2.02 sec: 1.05x faster                                                        |
| sqlite_synth               | 2.99 us                                                    | 2.84 us: 1.05x faster                                                         |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                         |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                         |
| xml_etree_process          | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                                         |
| unpickle_pure_python       | 218 us                                                     | 209 us: 1.05x faster                                                          |
| deepcopy_memo              | 39.7 us                                                    | 38.1 us: 1.04x faster                                                         |
| xml_etree_generate         | 87.4 ms                                                    | 83.9 ms: 1.04x faster                                                         |
| json                       | 5.31 ms                                                    | 5.11 ms: 1.04x faster                                                         |
| pickle_list                | 5.11 us                                                    | 4.92 us: 1.04x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 3.24 us: 1.03x faster                                                         |
| gc_traversal               | 3.98 ms                                                    | 3.86 ms: 1.03x faster                                                         |
| telco                      | 8.41 ms                                                    | 8.18 ms: 1.03x faster                                                         |
| thrift                     | 823 us                                                     | 802 us: 1.03x faster                                                          |
| pickle_pure_python         | 305 us                                                     | 299 us: 1.02x faster                                                          |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                          |
| unpickle_list              | 5.34 us                                                    | 5.26 us: 1.02x faster                                                         |
| pidigits                   | 191 ms                                                     | 189 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 758 ms                                                     | 751 ms: 1.01x faster                                                          |
| genshi_text                | 23.7 ms                                                    | 23.5 ms: 1.01x faster                                                         |
| pickle_dict                | 34.8 us                                                    | 35.0 us: 1.01x slower                                                         |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                          |
| regex_effbot               | 3.67 ms                                                    | 3.71 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                        |
| chameleon                  | 7.22 ms                                                    | 7.31 ms: 1.01x slower                                                         |
| logging_format             | 6.47 us                                                    | 6.58 us: 1.02x slower                                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.85 ms: 1.02x slower                                                         |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                        |
| raytrace                   | 267 ms                                                     | 273 ms: 1.02x slower                                                          |
| generators                 | 29.6 ms                                                    | 30.3 ms: 1.02x slower                                                         |
| unpickle                   | 15.1 us                                                    | 15.5 us: 1.03x slower                                                         |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                                          |
| pathlib                    | 17.3 ms                                                    | 17.8 ms: 1.03x slower                                                         |
| logging_simple             | 5.74 us                                                    | 5.92 us: 1.03x slower                                                         |
| python_startup             | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                         |
| dask                       | 369 ms                                                     | 383 ms: 1.04x slower                                                          |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.04x slower                                                         |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                         |
| nqueens                    | 81.4 ms                                                    | 84.7 ms: 1.04x slower                                                         |
| 2to3                       | 274 ms                                                     | 285 ms: 1.04x slower                                                          |
| asyncio_tcp                | 508 ms                                                     | 530 ms: 1.04x slower                                                          |
| regex_compile              | 137 ms                                                     | 143 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 639 ms: 1.05x slower                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 615 ms: 1.05x slower                                                          |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 58.2 ms: 1.05x slower                                                         |
| html5lib                   | 67.2 ms                                                    | 70.6 ms: 1.05x slower                                                         |
| async_tree_none_tg         | 336 ms                                                     | 354 ms: 1.05x slower                                                          |
| hexiom                     | 6.30 ms                                                    | 6.64 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 165 us                                                     | 174 us: 1.06x slower                                                          |
| django_template            | 34.8 ms                                                    | 36.7 ms: 1.06x slower                                                         |
| djangocms                  | 31.5 us                                                    | 33.3 us: 1.06x slower                                                         |
| bench_thread_pool          | 834 us                                                     | 882 us: 1.06x slower                                                          |
| coroutines                 | 23.2 ms                                                    | 24.5 ms: 1.06x slower                                                         |
| scimark_lu                 | 122 ms                                                     | 129 ms: 1.06x slower                                                          |
| flaskblogging              | 9.01 ms                                                    | 9.55 ms: 1.06x slower                                                         |
| python_startup_no_site     | 7.11 ms                                                    | 7.65 ms: 1.08x slower                                                         |
| sqlglot_normalize          | 110 ms                                                     | 119 ms: 1.08x slower                                                          |
| tornado_http               | 94.6 ms                                                    | 105 ms: 1.11x slower                                                          |
| dulwich_log                | 67.2 ms                                                    | 74.4 ms: 1.11x slower                                                         |
| aiohttp                    | 1.18 ms                                                    | 1.31 ms: 1.11x slower                                                         |
| scimark_sor                | 127 ms                                                     | 142 ms: 1.11x slower                                                          |
| gunicorn                   | 1.28 ms                                                    | 1.43 ms: 1.12x slower                                                         |
| sympy_expand               | 473 ms                                                     | 528 ms: 1.12x slower                                                          |
| sympy_str                  | 282 ms                                                     | 317 ms: 1.12x slower                                                          |
| sympy_integrate            | 20.5 ms                                                    | 23.6 ms: 1.15x slower                                                         |
| sympy_sum                  | 156 ms                                                     | 184 ms: 1.18x slower                                                          |
| genshi_xml                 | 51.6 ms                                                    | 62.7 ms: 1.22x slower                                                         |
| mypy2                      | 742 ms                                                     | 926 ms: 1.25x slower                                                          |
| pylint                     | 317 ms                                                     | 409 ms: 1.29x slower                                                          |
| deltablue                  | 3.25 ms                                                    | 4.21 ms: 1.29x slower                                                         |
| Geometric mean             | (ref)                                                      | 1.01x slower                                                                  |

Benchmark hidden because not significant (12): async_tree_none, async_tree_io, pprint_pformat, sqlglot_parse, deepcopy, comprehensions, asyncio_websockets, regex_v8, bench_mp_pool, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, docutils

# HPT report

- Reliability score: 92.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x