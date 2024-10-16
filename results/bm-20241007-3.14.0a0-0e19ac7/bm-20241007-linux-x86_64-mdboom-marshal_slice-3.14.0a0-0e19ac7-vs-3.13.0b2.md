# Results vs. 3.13.0b2

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 253 ms: 1.08x faster                                           |
| docutils       | 2.83 sec                                                   | 2.62 sec: 1.08x faster                                         |
| html5lib       | 67.2 ms                                                    | 61.4 ms: 1.10x faster                                          |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                          |
| Geometric mean | (ref)                                                      | 1.08x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 389 ms: 1.19x faster                                           |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 400 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.09x faster                                           |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                   |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.1 ms: 1.04x faster                                          |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                           |
| nbody          | 88.3 ms                                                    | 86.8 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                      | 1.03x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 127 ms: 1.07x faster                                           |
| regex_dna      | 221 ms                                                     | 220 ms: 1.00x faster                                           |
| regex_v8       | 25.1 ms                                                    | 25.2 ms: 1.00x slower                                          |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                      | 1.02x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.1 us: 1.07x faster                                          |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                          |
| xml_etree_process    | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                          |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                           |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                           |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.03x faster                                         |
| pickle_list          | 5.11 us                                                    | 5.01 us: 1.02x faster                                          |
| xml_etree_generate   | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                          |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                           |
| unpickle             | 15.1 us                                                    | 15.0 us: 1.01x faster                                          |
| pickle_dict          | 34.8 us                                                    | 34.9 us: 1.00x slower                                          |
| pickle               | 11.5 us                                                    | 11.5 us: 1.00x slower                                          |
| unpickle_list        | 5.34 us                                                    | 5.41 us: 1.01x slower                                          |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                   |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                          |
| python_startup_no_site | 7.11 ms                                                    | 7.01 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.9 ms: 1.08x faster                                          |
| genshi_xml      | 51.6 ms                                                    | 49.3 ms: 1.05x faster                                          |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                          |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.02x slower                                          |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                           |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                          |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.24x faster                                          |
| go                         | 145 ms                                                     | 119 ms: 1.22x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 389 ms: 1.19x faster                                           |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 400 ms: 1.11x faster                                           |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                         |
| richards                   | 50.9 ms                                                    | 46.0 ms: 1.11x faster                                          |
| coverage                   | 93.1 ms                                                    | 84.5 ms: 1.10x faster                                          |
| richards_super             | 57.4 ms                                                    | 52.1 ms: 1.10x faster                                          |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                           |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                          |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                           |
| html5lib                   | 67.2 ms                                                    | 61.4 ms: 1.10x faster                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.09x faster                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.82 ms: 1.09x faster                                          |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.09x faster                                           |
| genshi_text                | 23.7 ms                                                    | 21.9 ms: 1.08x faster                                          |
| 2to3                       | 274 ms                                                     | 253 ms: 1.08x faster                                           |
| asyncio_tcp                | 508 ms                                                     | 470 ms: 1.08x faster                                           |
| crypto_pyaes               | 77.5 ms                                                    | 71.7 ms: 1.08x faster                                          |
| pprint_safe_repr           | 758 ms                                                     | 703 ms: 1.08x faster                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                         |
| docutils                   | 2.83 sec                                                   | 2.62 sec: 1.08x faster                                         |
| scimark_fft                | 392 ms                                                     | 364 ms: 1.08x faster                                           |
| regex_compile              | 137 ms                                                     | 127 ms: 1.07x faster                                           |
| thrift                     | 823 us                                                     | 767 us: 1.07x faster                                           |
| generators                 | 29.6 ms                                                    | 27.7 ms: 1.07x faster                                          |
| sqlite_synth               | 2.99 us                                                    | 2.80 us: 1.07x faster                                          |
| json_loads                 | 28.9 us                                                    | 27.1 us: 1.07x faster                                          |
| sympy_sum                  | 156 ms                                                     | 146 ms: 1.06x faster                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.73 sec: 1.06x faster                                         |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                           |
| logging_format             | 6.47 us                                                    | 6.15 us: 1.05x faster                                          |
| telco                      | 8.41 ms                                                    | 8.01 ms: 1.05x faster                                          |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                          |
| sympy_expand               | 473 ms                                                     | 450 ms: 1.05x faster                                           |
| genshi_xml                 | 51.6 ms                                                    | 49.3 ms: 1.05x faster                                          |
| json                       | 5.31 ms                                                    | 5.07 ms: 1.05x faster                                          |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 53.3 ms: 1.04x faster                                          |
| dulwich_log                | 67.2 ms                                                    | 64.4 ms: 1.04x faster                                          |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.77 sec: 1.04x faster                                         |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.04x faster                                          |
| float                      | 78.9 ms                                                    | 76.1 ms: 1.04x faster                                          |
| xml_etree_process          | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.04x faster                                          |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.03x faster                                           |
| logging_simple             | 5.74 us                                                    | 5.55 us: 1.03x faster                                          |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                          |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                           |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                           |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                           |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                           |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                           |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.03x faster                                         |
| chaos                      | 61.3 ms                                                    | 59.8 ms: 1.03x faster                                          |
| pyflate                    | 484 ms                                                     | 472 ms: 1.03x faster                                           |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.8 ms: 1.02x faster                                          |
| async_generators           | 442 ms                                                     | 433 ms: 1.02x faster                                           |
| pickle_list                | 5.11 us                                                    | 5.01 us: 1.02x faster                                          |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                          |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                          |
| nbody                      | 88.3 ms                                                    | 86.8 ms: 1.02x faster                                          |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.79 ms: 1.02x faster                                          |
| xml_etree_generate         | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                          |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.01 ms: 1.01x faster                                          |
| hexiom                     | 6.30 ms                                                    | 6.24 ms: 1.01x faster                                          |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                           |
| fannkuch                   | 402 ms                                                     | 399 ms: 1.01x faster                                           |
| gc_traversal               | 3.98 ms                                                    | 3.95 ms: 1.01x faster                                          |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                           |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                          |
| unpickle                   | 15.1 us                                                    | 15.0 us: 1.01x faster                                          |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.00x faster                                           |
| pickle_dict                | 34.8 us                                                    | 34.9 us: 1.00x slower                                          |
| regex_v8                   | 25.1 ms                                                    | 25.2 ms: 1.00x slower                                          |
| pickle                     | 11.5 us                                                    | 11.5 us: 1.00x slower                                          |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                          |
| nqueens                    | 81.4 ms                                                    | 82.2 ms: 1.01x slower                                          |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                         |
| unpickle_list              | 5.34 us                                                    | 5.41 us: 1.01x slower                                          |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.02x slower                                          |
| bench_thread_pool          | 834 us                                                     | 856 us: 1.03x slower                                           |
| bench_mp_pool              | 23.9 ms                                                    | 55.9 ms: 2.34x slower                                          |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                   |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_io, pylint, pickle_pure_python, deltablue
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x