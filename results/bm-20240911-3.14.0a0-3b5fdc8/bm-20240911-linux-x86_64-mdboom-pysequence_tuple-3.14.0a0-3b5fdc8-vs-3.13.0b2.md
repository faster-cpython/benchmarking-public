# Results vs. 3.13.0b2

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 253 ms: 1.08x faster                                              |
| docutils       | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                            |
| html5lib       | 67.2 ms                                                    | 62.9 ms: 1.07x faster                                             |
| tornado_http   | 94.6 ms                                                    | 89.8 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                      | 1.07x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 313 ms: 1.21x faster                                              |
| async_tree_memoization     | 463 ms                                                     | 393 ms: 1.18x faster                                              |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                              |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                              |
| async_tree_io              | 939 ms                                                     | 866 ms: 1.08x faster                                              |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                              |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                              |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 556 ms: 1.06x faster                                              |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.8 ms: 1.03x faster                                             |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                              |
| nbody          | 88.3 ms                                                    | 87.3 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                      | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                              |
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                             |
| regex_dna      | 221 ms                                                     | 220 ms: 1.01x faster                                              |
| regex_effbot   | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                      | 1.02x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.3 us: 1.06x faster                                             |
| xml_etree_process    | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                             |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                             |
| xml_etree_generate   | 87.4 ms                                                    | 84.2 ms: 1.04x faster                                             |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                              |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                              |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                              |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                            |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                              |
| pickle_list          | 5.11 us                                                    | 5.07 us: 1.01x faster                                             |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                             |
| unpickle_list        | 5.34 us                                                    | 5.37 us: 1.01x slower                                             |
| pickle_dict          | 34.8 us                                                    | 35.1 us: 1.01x slower                                             |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                             |
| python_startup_no_site | 7.11 ms                                                    | 7.00 ms: 1.02x faster                                             |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.6 ms: 1.10x faster                                             |
| genshi_xml      | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                             |
| django_template | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                             |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 258 us: 1.42x faster                                              |
| deepcopy_memo              | 39.7 us                                                    | 29.5 us: 1.35x faster                                             |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                             |
| go                         | 145 ms                                                     | 116 ms: 1.25x faster                                              |
| async_tree_none            | 378 ms                                                     | 313 ms: 1.21x faster                                              |
| async_tree_memoization     | 463 ms                                                     | 393 ms: 1.18x faster                                              |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                              |
| richards                   | 50.9 ms                                                    | 45.1 ms: 1.13x faster                                             |
| richards_super             | 57.4 ms                                                    | 50.9 ms: 1.13x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                              |
| coverage                   | 93.1 ms                                                    | 84.0 ms: 1.11x faster                                             |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                             |
| genshi_text                | 23.7 ms                                                    | 21.6 ms: 1.10x faster                                             |
| scimark_fft                | 392 ms                                                     | 359 ms: 1.09x faster                                              |
| crypto_pyaes               | 77.5 ms                                                    | 71.0 ms: 1.09x faster                                             |
| async_tree_io              | 939 ms                                                     | 866 ms: 1.08x faster                                              |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                              |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.87 ms: 1.08x faster                                             |
| 2to3                       | 274 ms                                                     | 253 ms: 1.08x faster                                              |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                              |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                              |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                              |
| docutils                   | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                            |
| html5lib                   | 67.2 ms                                                    | 62.9 ms: 1.07x faster                                             |
| spectral_norm              | 116 ms                                                     | 109 ms: 1.07x faster                                              |
| pyflate                    | 484 ms                                                     | 454 ms: 1.07x faster                                              |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                             |
| asyncio_tcp                | 508 ms                                                     | 478 ms: 1.06x faster                                              |
| pprint_safe_repr           | 758 ms                                                     | 713 ms: 1.06x faster                                              |
| logging_silent             | 105 ns                                                     | 98.6 ns: 1.06x faster                                             |
| thrift                     | 823 us                                                     | 776 us: 1.06x faster                                              |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                              |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                             |
| json_loads                 | 28.9 us                                                    | 27.3 us: 1.06x faster                                             |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 556 ms: 1.06x faster                                              |
| bench_thread_pool          | 834 us                                                     | 791 us: 1.05x faster                                              |
| sympy_integrate            | 20.5 ms                                                    | 19.4 ms: 1.05x faster                                             |
| tornado_http               | 94.6 ms                                                    | 89.8 ms: 1.05x faster                                             |
| xml_etree_process          | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                             |
| genshi_xml                 | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 52.9 ms: 1.05x faster                                             |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                             |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.80 sec: 1.05x faster                                            |
| sympy_str                  | 282 ms                                                     | 270 ms: 1.05x faster                                              |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                             |
| sympy_expand               | 473 ms                                                     | 454 ms: 1.04x faster                                              |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                             |
| xml_etree_generate         | 87.4 ms                                                    | 84.2 ms: 1.04x faster                                             |
| sqlite_synth               | 2.99 us                                                    | 2.88 us: 1.04x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.69 sec: 1.04x faster                                            |
| dulwich_log                | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                             |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                              |
| deltablue                  | 3.25 ms                                                    | 3.14 ms: 1.04x faster                                             |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                             |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.03x faster                                              |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.9 ms: 1.03x faster                                             |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                              |
| hexiom                     | 6.30 ms                                                    | 6.09 ms: 1.03x faster                                             |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                              |
| logging_simple             | 5.74 us                                                    | 5.57 us: 1.03x faster                                             |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                              |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                            |
| float                      | 78.9 ms                                                    | 76.8 ms: 1.03x faster                                             |
| raytrace                   | 267 ms                                                     | 260 ms: 1.03x faster                                              |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                              |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                              |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                              |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                             |
| gc_traversal               | 3.98 ms                                                    | 3.90 ms: 1.02x faster                                             |
| nqueens                    | 81.4 ms                                                    | 80.0 ms: 1.02x faster                                             |
| tomli_loads                | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                              |
| python_startup_no_site     | 7.11 ms                                                    | 7.00 ms: 1.02x faster                                             |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                              |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                             |
| django_template            | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                             |
| nbody                      | 88.3 ms                                                    | 87.3 ms: 1.01x faster                                             |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                             |
| fannkuch                   | 402 ms                                                     | 399 ms: 1.01x faster                                              |
| pickle_list                | 5.11 us                                                    | 5.07 us: 1.01x faster                                             |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.01x faster                                              |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                             |
| async_generators           | 442 ms                                                     | 440 ms: 1.00x faster                                              |
| unpickle_list              | 5.34 us                                                    | 5.37 us: 1.01x slower                                             |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                             |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                             |
| pickle_dict                | 34.8 us                                                    | 35.1 us: 1.01x slower                                             |
| regex_effbot               | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                             |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                            |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                      |

Benchmark hidden because not significant (4): coroutines, unpickle, telco, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x