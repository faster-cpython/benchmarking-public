# Results vs. 3.12.0

- fork: mdboom
- ref: mimalloc
- machine: linux-x86_64
- commit hash: f46688b
- commit date: 2024-08-29
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 251 ms: 1.09x faster                                      |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                    |
| tornado_http   | 103 ms                                                 | 86.9 ms: 1.18x faster                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 407 ms: 1.41x faster                                      |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 534 ms: 1.36x faster                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                      |
| async_tree_io_tg           | 1.18 sec                                               | 948 ms: 1.25x faster                                      |
| async_tree_io              | 1.16 sec                                               | 1.00 sec: 1.16x faster                                    |
| Geometric mean             | (ref)                                                  | 1.34x faster                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.7 ms: 1.12x faster                                     |
| nbody          | 97.0 ms                                                | 89.7 ms: 1.08x faster                                     |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                      |
| regex_effbot   | 3.61 ms                                                | 3.34 ms: 1.08x faster                                     |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                      |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                    |
| pickle_pure_python   | 324 us                                                 | 296 us: 1.09x faster                                      |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 84.7 ms: 1.05x faster                                     |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                     |
| xml_etree_parse      | 159 ms                                                 | 153 ms: 1.04x faster                                      |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                      |
| json_loads           | 28.5 us                                                | 27.5 us: 1.04x faster                                     |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                     |
| Geometric mean       | (ref)                                                  | 1.06x faster                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                     |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                     |
| Geometric mean         | (ref)                                                  | 1.05x slower                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.4 ms: 1.15x faster                                     |
| django_template | 34.6 ms                                                | 33.2 ms: 1.04x faster                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                      |
| deepcopy                   | 371 us                                                 | 253 us: 1.46x faster                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 407 ms: 1.41x faster                                      |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 534 ms: 1.36x faster                                      |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.61 us: 1.28x faster                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                      |
| pathlib                    | 19.3 ms                                                | 15.2 ms: 1.27x faster                                     |
| async_tree_io_tg           | 1.18 sec                                               | 948 ms: 1.25x faster                                      |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                      |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                      |
| tornado_http               | 103 ms                                                 | 86.9 ms: 1.18x faster                                     |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                     |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 69.9 ms: 1.17x faster                                     |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                     |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                    |
| async_tree_io              | 1.16 sec                                               | 1.00 sec: 1.16x faster                                    |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                     |
| mako                       | 11.9 ms                                                | 10.4 ms: 1.15x faster                                     |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.15x faster                                     |
| sympy_str                  | 300 ms                                                 | 263 ms: 1.14x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 66.1 ms: 1.14x faster                                     |
| float                      | 84.7 ms                                                | 75.7 ms: 1.12x faster                                     |
| pprint_safe_repr           | 776 ms                                                 | 697 ms: 1.11x faster                                      |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                     |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                     |
| pickle_pure_python         | 324 us                                                 | 296 us: 1.09x faster                                      |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                      |
| scimark_fft                | 382 ms                                                 | 350 ms: 1.09x faster                                      |
| pycparser                  | 1.18 sec                                               | 1.08 sec: 1.09x faster                                    |
| 2to3                       | 274 ms                                                 | 251 ms: 1.09x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                    |
| regex_effbot               | 3.61 ms                                                | 3.34 ms: 1.08x faster                                     |
| nbody                      | 97.0 ms                                                | 89.7 ms: 1.08x faster                                     |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.08x faster                                     |
| nqueens                    | 83.3 ms                                                | 77.9 ms: 1.07x faster                                     |
| sympy_expand               | 478 ms                                                 | 447 ms: 1.07x faster                                      |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.07x faster                                      |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                      |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.06x faster                                      |
| logging_silent             | 104 ns                                                 | 98.5 ns: 1.06x faster                                     |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                      |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                      |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                     |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                      |
| sqlglot_optimize           | 54.8 ms                                                | 52.1 ms: 1.05x faster                                     |
| xml_etree_generate         | 89.2 ms                                                | 84.7 ms: 1.05x faster                                     |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                     |
| gc_traversal               | 3.79 ms                                                | 3.62 ms: 1.05x faster                                     |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.84 ms: 1.04x faster                                     |
| django_template            | 34.6 ms                                                | 33.2 ms: 1.04x faster                                     |
| xml_etree_parse            | 159 ms                                                 | 153 ms: 1.04x faster                                      |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                      |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                    |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.04x faster                                     |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                     |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                     |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                      |
| asyncio_websockets         | 551 ms                                                 | 542 ms: 1.02x faster                                      |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                      |
| typing_runtime_protocols   | 158 us                                                 | 157 us: 1.01x faster                                      |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                     |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                     |
| asyncio_tcp                | 491 ms                                                 | 496 ms: 1.01x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                    |
| richards                   | 45.8 ms                                                | 47.0 ms: 1.02x slower                                     |
| richards_super             | 51.5 ms                                                | 53.5 ms: 1.04x slower                                     |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                     |
| telco                      | 7.10 ms                                                | 8.47 ms: 1.19x slower                                     |
| coverage                   | 72.7 ms                                                | 89.3 ms: 1.23x slower                                     |
| bench_thread_pool          | 842 us                                                 | 1.24 ms: 1.48x slower                                     |
| Geometric mean             | (ref)                                                  | 1.09x faster                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240829-3.14.0a0-f46688b/bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.07x