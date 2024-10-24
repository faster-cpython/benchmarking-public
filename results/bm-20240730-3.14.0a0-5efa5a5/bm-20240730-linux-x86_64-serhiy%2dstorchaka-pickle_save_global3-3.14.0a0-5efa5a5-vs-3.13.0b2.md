# Results vs. 3.13.0b2

- fork: serhiy-storchaka
- ref: pickle_save_global3
- machine: linux-x86_64
- commit hash: 5efa5a5
- commit date: 2024-07-30
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 263 ms: 1.04x faster                                                             |
| docutils       | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                                           |
| html5lib       | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                            |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                      | 1.04x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.14x faster                                                             |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                             |
| async_tree_memoization     | 463 ms                                                     | 425 ms: 1.09x faster                                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                             |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                                             |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                                             |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                             |
| nbody          | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                             |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                                             |
| regex_effbot   | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                                            |
| regex_v8       | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                                           |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                             |
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.02x faster                                                             |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                             |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                             |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text    | 23.7 ms                                                    | 22.3 ms: 1.06x faster                                                            |
| genshi_xml     | 51.6 ms                                                    | 50.2 ms: 1.03x faster                                                            |
| mako           | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                                             |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.51 ms: 1.17x faster                                                            |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.14x faster                                                             |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                             |
| gc_traversal               | 3.98 ms                                                    | 3.56 ms: 1.12x faster                                                            |
| richards                   | 50.9 ms                                                    | 45.8 ms: 1.11x faster                                                            |
| coverage                   | 93.1 ms                                                    | 84.1 ms: 1.11x faster                                                            |
| richards_super             | 57.4 ms                                                    | 51.8 ms: 1.11x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                             |
| scimark_fft                | 392 ms                                                     | 359 ms: 1.09x faster                                                             |
| async_tree_memoization     | 463 ms                                                     | 425 ms: 1.09x faster                                                             |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                             |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                                             |
| logging_format             | 6.47 us                                                    | 6.01 us: 1.08x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                            |
| spectral_norm              | 116 ms                                                     | 109 ms: 1.07x faster                                                             |
| crypto_pyaes               | 77.5 ms                                                    | 72.9 ms: 1.06x faster                                                            |
| bench_thread_pool          | 834 us                                                     | 786 us: 1.06x faster                                                             |
| genshi_text                | 23.7 ms                                                    | 22.3 ms: 1.06x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.44 us: 1.06x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.05x faster                                                            |
| json                       | 5.31 ms                                                    | 5.04 ms: 1.05x faster                                                            |
| thrift                     | 823 us                                                     | 784 us: 1.05x faster                                                             |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                            |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                             |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                            |
| sympy_str                  | 282 ms                                                     | 270 ms: 1.05x faster                                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 53.1 ms: 1.05x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                                            |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                                             |
| 2to3                       | 274 ms                                                     | 263 ms: 1.04x faster                                                             |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                            |
| generators                 | 29.6 ms                                                    | 28.5 ms: 1.04x faster                                                            |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                            |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                                             |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                                           |
| telco                      | 8.41 ms                                                    | 8.11 ms: 1.04x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.04x faster                                                            |
| docutils                   | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                                           |
| go                         | 145 ms                                                     | 140 ms: 1.04x faster                                                             |
| raytrace                   | 267 ms                                                     | 258 ms: 1.03x faster                                                             |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                             |
| sympy_expand               | 473 ms                                                     | 458 ms: 1.03x faster                                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.2 ms: 1.03x faster                                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                            |
| genshi_xml                 | 51.6 ms                                                    | 50.2 ms: 1.03x faster                                                            |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                            |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                             |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.03x faster                                                           |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                             |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                             |
| xml_etree_parse            | 162 ms                                                     | 158 ms: 1.02x faster                                                             |
| nqueens                    | 81.4 ms                                                    | 79.6 ms: 1.02x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                            |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                             |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                             |
| nbody                      | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 744 ms: 1.02x faster                                                             |
| pyflate                    | 484 ms                                                     | 477 ms: 1.01x faster                                                             |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                            |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                                             |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                             |
| python_startup_no_site     | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                            |
| scimark_sor                | 127 ms                                                     | 127 ms: 1.01x faster                                                             |
| hexiom                     | 6.30 ms                                                    | 6.26 ms: 1.01x faster                                                            |
| deltablue                  | 3.25 ms                                                    | 3.23 ms: 1.01x faster                                                            |
| fannkuch                   | 402 ms                                                     | 403 ms: 1.00x slower                                                             |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                            |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                           |
| comprehensions             | 16.6 us                                                    | 16.9 us: 1.02x slower                                                            |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                                             |
| regex_effbot               | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                                            |
| regex_v8                   | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                     |

Benchmark hidden because not significant (4): float, pylint, async_generators, django_template
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x