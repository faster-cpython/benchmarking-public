# Results vs. 3.12.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 8738ae5
- commit date: 2024-10-07
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                           |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                         |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                           |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.32x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 916 ms: 1.29x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                           |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                           |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.9 ms: 1.12x faster                                          |
| float          | 84.7 ms                                                | 76.8 ms: 1.10x faster                                          |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                           |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                          |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                           |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                         |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                           |
| pickle_dict          | 35.5 us                                                | 33.4 us: 1.06x faster                                          |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                           |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                          |
| xml_etree_generate   | 89.2 ms                                                | 86.8 ms: 1.03x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                           |
| pickle_list          | 5.08 us                                                | 4.96 us: 1.03x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                           |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                          |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                          |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                          |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                          |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                          |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                           |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                           |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                           |
| deepcopy_memo              | 40.7 us                                                | 30.5 us: 1.34x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.32x faster                                           |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                          |
| async_tree_io_tg           | 1.18 sec                                               | 916 ms: 1.29x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                           |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                          |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                          |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                           |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                           |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                          |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.15x faster                                           |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                           |
| crypto_pyaes               | 81.9 ms                                                | 71.5 ms: 1.15x faster                                          |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                          |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                          |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                          |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                          |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                           |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                          |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                         |
| nbody                      | 97.0 ms                                                | 86.9 ms: 1.12x faster                                          |
| float                      | 84.7 ms                                                | 76.8 ms: 1.10x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.08x faster                                          |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                          |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                           |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                           |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                           |
| pickle_dict                | 35.5 us                                                | 33.4 us: 1.06x faster                                          |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                           |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                          |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                         |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                           |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                          |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                          |
| gc_traversal               | 3.79 ms                                                | 3.61 ms: 1.05x faster                                          |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                           |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                           |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                         |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                           |
| nqueens                    | 83.3 ms                                                | 79.7 ms: 1.05x faster                                          |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                          |
| asyncio_tcp                | 491 ms                                                 | 472 ms: 1.04x faster                                           |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                           |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 86.8 ms: 1.03x faster                                          |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                          |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                          |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                           |
| pickle_list                | 5.08 us                                                | 4.96 us: 1.03x faster                                          |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                          |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                           |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                           |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                           |
| pyflate                    | 482 ms                                                 | 476 ms: 1.01x faster                                           |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                         |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                          |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                           |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                          |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                          |
| bench_thread_pool          | 842 us                                                 | 853 us: 1.01x slower                                           |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                           |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                          |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                         |
| richards                   | 45.8 ms                                                | 47.4 ms: 1.03x slower                                          |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                           |
| richards_super             | 51.5 ms                                                | 53.5 ms: 1.04x slower                                          |
| unpack_sequence            | 54.0 ns                                                | 57.9 ns: 1.07x slower                                          |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                          |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                          |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                          |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 56.0 ms: 2.33x slower                                          |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                   |

Benchmark hidden because not significant (3): unpickle, sqlite_synth, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-8738ae5/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x