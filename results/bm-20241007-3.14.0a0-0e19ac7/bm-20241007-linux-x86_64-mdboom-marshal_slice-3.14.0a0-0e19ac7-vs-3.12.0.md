# Results vs. 3.12.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                           |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                         |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 389 ms: 1.49x faster                                           |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.48x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.47x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 915 ms: 1.29x faster                                           |
| async_tree_io              | 1.16 sec                                               | 924 ms: 1.25x faster                                           |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.8 ms: 1.12x faster                                          |
| float          | 84.7 ms                                                | 76.1 ms: 1.11x faster                                          |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                           |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.03x slower                                          |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                           |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                         |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                           |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                           |
| unpickle             | 15.9 us                                                | 15.0 us: 1.05x faster                                          |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                          |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                           |
| pickle_dict          | 35.5 us                                                | 34.9 us: 1.02x faster                                          |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.02x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.01x faster                                           |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                          |
| unpickle_list        | 5.29 us                                                | 5.41 us: 1.02x slower                                          |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                          |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                          |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                          |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                          |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 389 ms: 1.49x faster                                           |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.48x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.47x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                           |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                           |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                           |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 915 ms: 1.29x faster                                           |
| async_tree_io              | 1.16 sec                                               | 924 ms: 1.25x faster                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                          |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.23x faster                                          |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                           |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                          |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                           |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                           |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                          |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.15x faster                                           |
| crypto_pyaes               | 81.9 ms                                                | 71.7 ms: 1.14x faster                                          |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                          |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                          |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                         |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                          |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                           |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                          |
| unpack_sequence            | 54.0 ns                                                | 48.3 ns: 1.12x faster                                          |
| nbody                      | 97.0 ms                                                | 86.8 ms: 1.12x faster                                          |
| float                      | 84.7 ms                                                | 76.1 ms: 1.11x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 703 ms: 1.10x faster                                           |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                          |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                           |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                          |
| dulwich_log                | 68.5 ms                                                | 64.4 ms: 1.06x faster                                          |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                           |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                           |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                           |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                           |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.05x faster                                          |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.82 ms: 1.05x faster                                          |
| scimark_fft                | 382 ms                                                 | 364 ms: 1.05x faster                                           |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.05x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                          |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.05x faster                                         |
| asyncio_tcp                | 491 ms                                                 | 470 ms: 1.04x faster                                           |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                           |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                          |
| json                       | 5.26 ms                                                | 5.07 ms: 1.04x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                          |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                          |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                          |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                           |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                           |
| pyflate                    | 482 ms                                                 | 472 ms: 1.02x faster                                           |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                          |
| pickle_dict                | 35.5 us                                                | 34.9 us: 1.02x faster                                          |
| pickle_list                | 5.08 us                                                | 5.01 us: 1.02x faster                                          |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.01x faster                                           |
| nqueens                    | 83.3 ms                                                | 82.2 ms: 1.01x faster                                          |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                         |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                          |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                           |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                           |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                          |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                           |
| richards_super             | 51.5 ms                                                | 52.1 ms: 1.01x slower                                          |
| bench_thread_pool          | 842 us                                                 | 856 us: 1.02x slower                                           |
| unpickle_list              | 5.29 us                                                | 5.41 us: 1.02x slower                                          |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.03x slower                                          |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                           |
| gc_traversal               | 3.79 ms                                                | 3.95 ms: 1.04x slower                                          |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                          |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                          |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                          |
| coverage                   | 72.7 ms                                                | 84.5 ms: 1.16x slower                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 55.9 ms: 2.33x slower                                          |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                   |

Benchmark hidden because not significant (2): pycparser, richards
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.089x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x