# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.02x faster
- HPT reliability: 99.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 287 ms: 1.01x faster                                                        |
| docutils       | 2.81 sec                                                     | 3.00 sec: 1.07x slower                                                      |
| html5lib       | 71.9 ms                                                      | 74.1 ms: 1.03x slower                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 379 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                        |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 535 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 769 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 799 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 386 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 81.0 ms: 1.01x faster                                                       |
| nbody          | 88.0 ms                                                      | 90.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| regex_dna      | 244 ms                                                       | 254 ms: 1.04x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.28 sec: 1.06x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 59.5 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.5 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 57.3 ms                                                      | 54.0 ms: 1.06x faster                                                       |
| genshi_text    | 26.6 ms                                                      | 25.4 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 286 us: 1.39x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.9 us: 1.32x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 379 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                       |
| generators                 | 33.5 ms                                                      | 28.7 ms: 1.17x faster                                                       |
| scimark_sor                | 126 ms                                                       | 108 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                        |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| telco                      | 8.58 ms                                                      | 7.98 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 535 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 769 ms: 1.06x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.0 ms: 1.06x faster                                                       |
| async_tree_io              | 847 ms                                                       | 799 ms: 1.06x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.28 sec: 1.06x faster                                                      |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                        |
| raytrace                   | 289 ms                                                       | 276 ms: 1.05x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 25.4 ms: 1.05x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 93.5 ms: 1.05x faster                                                       |
| richards_super             | 59.8 ms                                                      | 57.2 ms: 1.05x faster                                                       |
| scimark_fft                | 314 ms                                                       | 302 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.90 sec: 1.04x faster                                                      |
| bench_thread_pool          | 901 us                                                       | 870 us: 1.04x faster                                                        |
| richards                   | 52.7 ms                                                      | 51.2 ms: 1.03x faster                                                       |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.3 ms: 1.02x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 59.5 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                       |
| pycparser                  | 1.26 sec                                                     | 1.24 sec: 1.02x faster                                                      |
| 2to3                       | 291 ms                                                       | 287 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.23 ms: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| float                      | 81.9 ms                                                      | 81.0 ms: 1.01x faster                                                       |
| hexiom                     | 6.33 ms                                                      | 6.27 ms: 1.01x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                       |
| chaos                      | 61.7 ms                                                      | 61.1 ms: 1.01x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| logging_format             | 7.07 us                                                      | 7.02 us: 1.01x faster                                                       |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.01x faster                                                        |
| thrift                     | 877 us                                                       | 871 us: 1.01x faster                                                        |
| sqlglot_normalize          | 118 ms                                                       | 118 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.01x faster                                                        |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| sympy_expand               | 505 ms                                                       | 507 ms: 1.00x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 386 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.47 us: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.5 us: 1.01x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.45 ms: 1.01x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 89.4 ms: 1.01x slower                                                       |
| fannkuch                   | 365 ms                                                       | 370 ms: 1.01x slower                                                        |
| go                         | 160 ms                                                       | 163 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| nbody                      | 88.0 ms                                                      | 90.6 ms: 1.03x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 74.1 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 812 ms                                                       | 837 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.2 ms: 1.03x slower                                                       |
| json                       | 5.22 ms                                                      | 5.42 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.71 sec: 1.04x slower                                                      |
| regex_dna                  | 244 ms                                                       | 254 ms: 1.04x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.5 us: 1.06x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.00 sec: 1.07x slower                                                      |
| coverage                   | 81.1 ms                                                      | 87.3 ms: 1.08x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.74 ms: 1.15x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.04 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (16): django_template, crypto_pyaes, mako, asyncio_tcp_ssl, typing_runtime_protocols, pidigits, sympy_integrate, pyflate, sympy_str, sympy_sum, async_generators, logging_silent, pylint, xml_etree_generate, bench_mp_pool, dask
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x