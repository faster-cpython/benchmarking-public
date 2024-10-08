# Results vs. 3.13.0b2

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 8738ae5
- commit date: 2024-10-07
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 255 ms: 1.07x faster                                           |
| docutils       | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                         |
| html5lib       | 67.2 ms                                                    | 61.4 ms: 1.09x faster                                          |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                          |
| Geometric mean | (ref)                                                      | 1.07x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.19x faster                                           |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.08x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                           |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                   |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.8 ms: 1.03x faster                                          |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                           |
| nbody          | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                      | 1.02x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                           |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                           |
| regex_effbot   | 3.67 ms                                                    | 3.69 ms: 1.00x slower                                          |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                      | 1.01x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.9 us: 1.07x faster                                          |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                          |
| pickle_dict          | 34.8 us                                                    | 33.4 us: 1.04x faster                                          |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.03x faster                                           |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                           |
| xml_etree_process    | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                          |
| pickle_list          | 5.11 us                                                    | 4.96 us: 1.03x faster                                          |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                         |
| unpickle_list        | 5.34 us                                                    | 5.30 us: 1.01x faster                                          |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                           |
| xml_etree_generate   | 87.4 ms                                                    | 86.8 ms: 1.01x faster                                          |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                          |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                   |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                          |
| python_startup_no_site | 7.11 ms                                                    | 7.01 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.4 ms: 1.06x faster                                          |
| genshi_xml      | 51.6 ms                                                    | 49.6 ms: 1.04x faster                                          |
| django_template | 34.8 ms                                                    | 33.9 ms: 1.03x faster                                          |
| mako            | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                          |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 263 us: 1.40x faster                                           |
| deepcopy_memo              | 39.7 us                                                    | 30.5 us: 1.30x faster                                          |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.23x faster                                          |
| go                         | 145 ms                                                     | 120 ms: 1.20x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.19x faster                                           |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.66 ms: 1.13x faster                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                           |
| gc_traversal               | 3.98 ms                                                    | 3.61 ms: 1.10x faster                                          |
| coverage                   | 93.1 ms                                                    | 84.8 ms: 1.10x faster                                          |
| html5lib                   | 67.2 ms                                                    | 61.4 ms: 1.09x faster                                          |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                          |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                           |
| scimark_fft                | 392 ms                                                     | 360 ms: 1.09x faster                                           |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.09x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.08x faster                                           |
| crypto_pyaes               | 77.5 ms                                                    | 71.5 ms: 1.08x faster                                          |
| asyncio_tcp                | 508 ms                                                     | 472 ms: 1.08x faster                                           |
| richards                   | 50.9 ms                                                    | 47.4 ms: 1.07x faster                                          |
| 2to3                       | 274 ms                                                     | 255 ms: 1.07x faster                                           |
| json_loads                 | 28.9 us                                                    | 26.9 us: 1.07x faster                                          |
| thrift                     | 823 us                                                     | 767 us: 1.07x faster                                           |
| richards_super             | 57.4 ms                                                    | 53.5 ms: 1.07x faster                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                           |
| docutils                   | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                         |
| generators                 | 29.6 ms                                                    | 27.7 ms: 1.07x faster                                          |
| bpe_tokeniser              | 5.02 sec                                                   | 4.71 sec: 1.07x faster                                         |
| sympy_sum                  | 156 ms                                                     | 146 ms: 1.06x faster                                           |
| sqlite_synth               | 2.99 us                                                    | 2.82 us: 1.06x faster                                          |
| genshi_text                | 23.7 ms                                                    | 22.4 ms: 1.06x faster                                          |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                           |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                         |
| pprint_safe_repr           | 758 ms                                                     | 721 ms: 1.05x faster                                           |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                          |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                          |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.77 sec: 1.04x faster                                         |
| genshi_xml                 | 51.6 ms                                                    | 49.6 ms: 1.04x faster                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 53.4 ms: 1.04x faster                                          |
| dulwich_log                | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                          |
| pickle_dict                | 34.8 us                                                    | 33.4 us: 1.04x faster                                          |
| sympy_expand               | 473 ms                                                     | 455 ms: 1.04x faster                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.04x faster                                          |
| json                       | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                          |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.04x faster                                           |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.03x faster                                           |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                           |
| logging_format             | 6.47 us                                                    | 6.26 us: 1.03x faster                                          |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                           |
| xml_etree_process          | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                          |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                           |
| telco                      | 8.41 ms                                                    | 8.16 ms: 1.03x faster                                          |
| pickle_list                | 5.11 us                                                    | 4.96 us: 1.03x faster                                          |
| mdp                        | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                         |
| django_template            | 34.8 ms                                                    | 33.9 ms: 1.03x faster                                          |
| float                      | 78.9 ms                                                    | 76.8 ms: 1.03x faster                                          |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.03x faster                                           |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                         |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                          |
| chaos                      | 61.3 ms                                                    | 59.8 ms: 1.03x faster                                          |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                          |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                           |
| nqueens                    | 81.4 ms                                                    | 79.7 ms: 1.02x faster                                          |
| mako                       | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                          |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                          |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                           |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                           |
| pyflate                    | 484 ms                                                     | 476 ms: 1.02x faster                                           |
| logging_simple             | 5.74 us                                                    | 5.65 us: 1.02x faster                                          |
| async_generators           | 442 ms                                                     | 434 ms: 1.02x faster                                           |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                           |
| nbody                      | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                          |
| tomli_loads                | 2.12 sec                                                   | 2.09 sec: 1.02x faster                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.2 ms: 1.01x faster                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.01 ms: 1.01x faster                                          |
| hexiom                     | 6.30 ms                                                    | 6.22 ms: 1.01x faster                                          |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                          |
| fannkuch                   | 402 ms                                                     | 398 ms: 1.01x faster                                           |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                           |
| unpickle_list              | 5.34 us                                                    | 5.30 us: 1.01x faster                                          |
| raytrace                   | 267 ms                                                     | 265 ms: 1.01x faster                                           |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                           |
| xml_etree_generate         | 87.4 ms                                                    | 86.8 ms: 1.01x faster                                          |
| regex_effbot               | 3.67 ms                                                    | 3.69 ms: 1.00x slower                                          |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                          |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                          |
| bench_thread_pool          | 834 us                                                     | 853 us: 1.02x slower                                           |
| bench_mp_pool              | 23.9 ms                                                    | 56.0 ms: 2.35x slower                                          |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                   |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_io, comprehensions, pickle_pure_python, pylint, deltablue, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-8738ae5/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.00x