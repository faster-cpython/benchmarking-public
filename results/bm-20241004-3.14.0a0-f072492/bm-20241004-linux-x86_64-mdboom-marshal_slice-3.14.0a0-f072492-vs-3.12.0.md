# Results vs. 3.12.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: f072492
- commit date: 2024-10-04
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                           |
| docutils       | 2.77 sec                                               | 2.63 sec: 1.05x faster                                         |
| tornado_http   | 103 ms                                                 | 91.1 ms: 1.13x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 310 ms: 1.52x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 398 ms: 1.45x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 524 ms: 1.39x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 891 ms: 1.33x faster                                           |
| async_tree_io              | 1.16 sec                                               | 888 ms: 1.30x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                           |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.5 ms: 1.09x faster                                          |
| nbody          | 97.0 ms                                                | 89.0 ms: 1.09x faster                                          |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                           |
| regex_effbot   | 3.61 ms                                                | 3.54 ms: 1.02x faster                                          |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                           |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.12x faster                                         |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                           |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                          |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                           |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                          |
| pickle_dict          | 35.5 us                                                | 34.2 us: 1.04x faster                                          |
| xml_etree_generate   | 89.2 ms                                                | 86.3 ms: 1.03x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                           |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                           |
| unpickle_list        | 5.29 us                                                | 5.21 us: 1.01x faster                                          |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.38 ms: 1.06x slower                                          |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                          |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                          |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                          |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 310 ms: 1.52x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 398 ms: 1.45x faster                                           |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 524 ms: 1.39x faster                                           |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                          |
| async_tree_io_tg           | 1.18 sec                                               | 891 ms: 1.33x faster                                           |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                          |
| async_tree_io              | 1.16 sec                                               | 888 ms: 1.30x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                          |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                          |
| crypto_pyaes               | 81.9 ms                                                | 69.9 ms: 1.17x faster                                          |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                           |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                           |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                          |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                          |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                           |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                           |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                          |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                          |
| tornado_http               | 103 ms                                                 | 91.1 ms: 1.13x faster                                          |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.12x faster                                         |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                           |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                          |
| float                      | 84.7 ms                                                | 77.5 ms: 1.09x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                           |
| nbody                      | 97.0 ms                                                | 89.0 ms: 1.09x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                          |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                          |
| dulwich_log                | 68.5 ms                                                | 63.9 ms: 1.07x faster                                          |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                          |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                           |
| async_generators           | 463 ms                                                 | 435 ms: 1.06x faster                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                          |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                          |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                           |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                          |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                           |
| nqueens                    | 83.3 ms                                                | 79.2 ms: 1.05x faster                                          |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                         |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                         |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                          |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                           |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                           |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                          |
| json                       | 5.26 ms                                                | 5.03 ms: 1.05x faster                                          |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                           |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                         |
| asyncio_tcp                | 491 ms                                                 | 471 ms: 1.04x faster                                           |
| pickle_dict                | 35.5 us                                                | 34.2 us: 1.04x faster                                          |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                           |
| xml_etree_generate         | 89.2 ms                                                | 86.3 ms: 1.03x faster                                          |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                          |
| gc_traversal               | 3.79 ms                                                | 3.68 ms: 1.03x faster                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                          |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                          |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                          |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                           |
| regex_effbot               | 3.61 ms                                                | 3.54 ms: 1.02x faster                                          |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                          |
| scimark_fft                | 382 ms                                                 | 376 ms: 1.02x faster                                           |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                           |
| unpickle_list              | 5.29 us                                                | 5.21 us: 1.01x faster                                          |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| unpack_sequence            | 54.0 ns                                                | 53.3 ns: 1.01x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                          |
| pyflate                    | 482 ms                                                 | 479 ms: 1.01x faster                                           |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                           |
| bench_thread_pool          | 842 us                                                 | 851 us: 1.01x slower                                           |
| richards                   | 45.8 ms                                                | 46.3 ms: 1.01x slower                                          |
| richards_super             | 51.5 ms                                                | 52.6 ms: 1.02x slower                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.38 ms: 1.06x slower                                          |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                           |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                          |
| telco                      | 7.10 ms                                                | 8.04 ms: 1.13x slower                                          |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                          |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 60.3 ms: 2.51x slower                                          |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                   |

Benchmark hidden because not significant (4): pickle_list, coroutines, typing_runtime_protocols, asyncio_websockets
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-f072492/bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x