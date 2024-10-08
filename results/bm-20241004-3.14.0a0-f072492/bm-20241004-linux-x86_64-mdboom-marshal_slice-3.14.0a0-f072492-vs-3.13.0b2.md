# Results vs. 3.13.0b2

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: f072492
- commit date: 2024-10-04
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 257 ms: 1.06x faster                                           |
| docutils       | 2.83 sec                                                   | 2.63 sec: 1.07x faster                                         |
| html5lib       | 67.2 ms                                                    | 62.3 ms: 1.08x faster                                          |
| tornado_http   | 94.6 ms                                                    | 91.1 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                      | 1.06x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 310 ms: 1.22x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 398 ms: 1.16x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 383 ms: 1.16x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 524 ms: 1.12x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                           |
| async_tree_io              | 939 ms                                                     | 888 ms: 1.06x faster                                           |
| async_tree_io_tg           | 936 ms                                                     | 891 ms: 1.05x faster                                           |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                           |
| float          | 78.9 ms                                                    | 77.5 ms: 1.02x faster                                          |
| nbody          | 88.3 ms                                                    | 89.0 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                      | 1.01x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                           |
| regex_effbot   | 3.67 ms                                                    | 3.54 ms: 1.04x faster                                          |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.9 us: 1.08x faster                                          |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                          |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                           |
| xml_etree_process    | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                          |
| unpickle_list        | 5.34 us                                                    | 5.21 us: 1.02x faster                                          |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                           |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                         |
| xml_etree_generate   | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                          |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                           |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                          |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.00x faster                                          |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                   |

Benchmark hidden because not significant (3): pickle_dict, unpickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                          |
| python_startup_no_site | 7.11 ms                                                    | 7.38 ms: 1.04x slower                                          |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                          |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                          |
| genshi_xml      | 51.6 ms                                                    | 50.1 ms: 1.03x faster                                          |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                           |
| deepcopy_memo              | 39.7 us                                                    | 29.5 us: 1.35x faster                                          |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                          |
| async_tree_none            | 378 ms                                                     | 310 ms: 1.22x faster                                           |
| go                         | 145 ms                                                     | 119 ms: 1.21x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 398 ms: 1.16x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 383 ms: 1.16x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 524 ms: 1.12x faster                                           |
| crypto_pyaes               | 77.5 ms                                                    | 69.9 ms: 1.11x faster                                          |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                         |
| richards                   | 50.9 ms                                                    | 46.3 ms: 1.10x faster                                          |
| coverage                   | 93.1 ms                                                    | 85.2 ms: 1.09x faster                                          |
| richards_super             | 57.4 ms                                                    | 52.6 ms: 1.09x faster                                          |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                          |
| html5lib                   | 67.2 ms                                                    | 62.3 ms: 1.08x faster                                          |
| gc_traversal               | 3.98 ms                                                    | 3.68 ms: 1.08x faster                                          |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                           |
| asyncio_tcp                | 508 ms                                                     | 471 ms: 1.08x faster                                           |
| json_loads                 | 28.9 us                                                    | 26.9 us: 1.08x faster                                          |
| docutils                   | 2.83 sec                                                   | 2.63 sec: 1.07x faster                                         |
| thrift                     | 823 us                                                     | 767 us: 1.07x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.92 ms: 1.07x faster                                          |
| sqlite_synth               | 2.99 us                                                    | 2.80 us: 1.07x faster                                          |
| pprint_safe_repr           | 758 ms                                                     | 712 ms: 1.07x faster                                           |
| 2to3                       | 274 ms                                                     | 257 ms: 1.06x faster                                           |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.75 sec: 1.06x faster                                         |
| async_tree_io              | 939 ms                                                     | 888 ms: 1.06x faster                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                         |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.06x faster                                           |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.06x faster                                           |
| json                       | 5.31 ms                                                    | 5.03 ms: 1.05x faster                                          |
| generators                 | 29.6 ms                                                    | 28.1 ms: 1.05x faster                                          |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.05x faster                                           |
| genshi_text                | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                          |
| dulwich_log                | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                          |
| async_tree_io_tg           | 936 ms                                                     | 891 ms: 1.05x faster                                           |
| telco                      | 8.41 ms                                                    | 8.04 ms: 1.05x faster                                          |
| sqlglot_normalize          | 110 ms                                                     | 105 ms: 1.05x faster                                           |
| scimark_fft                | 392 ms                                                     | 376 ms: 1.05x faster                                           |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 53.2 ms: 1.04x faster                                          |
| typing_runtime_protocols   | 165 us                                                     | 158 us: 1.04x faster                                           |
| logging_format             | 6.47 us                                                    | 6.22 us: 1.04x faster                                          |
| tornado_http               | 94.6 ms                                                    | 91.1 ms: 1.04x faster                                          |
| sympy_expand               | 473 ms                                                     | 455 ms: 1.04x faster                                           |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                           |
| chaos                      | 61.3 ms                                                    | 59.1 ms: 1.04x faster                                          |
| regex_effbot               | 3.67 ms                                                    | 3.54 ms: 1.04x faster                                          |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                           |
| xml_etree_process          | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                          |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                          |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                         |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                          |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                         |
| sympy_integrate            | 20.5 ms                                                    | 19.9 ms: 1.03x faster                                          |
| logging_simple             | 5.74 us                                                    | 5.58 us: 1.03x faster                                          |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                          |
| genshi_xml                 | 51.6 ms                                                    | 50.1 ms: 1.03x faster                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                          |
| nqueens                    | 81.4 ms                                                    | 79.2 ms: 1.03x faster                                          |
| asyncio_websockets         | 567 ms                                                     | 552 ms: 1.03x faster                                           |
| unpickle_list              | 5.34 us                                                    | 5.21 us: 1.02x faster                                          |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                           |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                         |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                           |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                           |
| float                      | 78.9 ms                                                    | 77.5 ms: 1.02x faster                                          |
| fannkuch                   | 402 ms                                                     | 396 ms: 1.02x faster                                           |
| async_generators           | 442 ms                                                     | 435 ms: 1.02x faster                                           |
| xml_etree_generate         | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                          |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                           |
| pyflate                    | 484 ms                                                     | 479 ms: 1.01x faster                                           |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                          |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                           |
| pickle_list                | 5.11 us                                                    | 5.08 us: 1.00x faster                                          |
| hexiom                     | 6.30 ms                                                    | 6.27 ms: 1.00x faster                                          |
| nbody                      | 88.3 ms                                                    | 89.0 ms: 1.01x slower                                          |
| deltablue                  | 3.25 ms                                                    | 3.28 ms: 1.01x slower                                          |
| bench_thread_pool          | 834 us                                                     | 851 us: 1.02x slower                                           |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                           |
| python_startup             | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.38 ms: 1.04x slower                                          |
| bench_mp_pool              | 23.9 ms                                                    | 60.3 ms: 2.52x slower                                          |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                   |

Benchmark hidden because not significant (10): pickle_dict, pylint, unpickle, scimark_monte_carlo, regex_v8, coroutines, comprehensions, pickle_pure_python, mako, raytrace
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-f072492/bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.01x