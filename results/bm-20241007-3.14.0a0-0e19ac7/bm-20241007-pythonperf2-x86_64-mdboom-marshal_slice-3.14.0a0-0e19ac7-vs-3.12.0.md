# Results vs. 3.12.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.04x slower
- HPT reliability: 97.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 279 ms: 1.02x faster                                                 |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                               |
| tornado_http   | 121 ms                                                       | 115 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                 |
| async_tree_none_tg         | 431 ms                                                       | 305 ms: 1.41x faster                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 398 ms: 1.37x faster                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 780 ms: 1.35x faster                                                 |
| async_tree_io              | 1.04 sec                                                     | 806 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                 |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                 |
| float          | 76.6 ms                                                      | 78.8 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                        | 1.01x faster                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                 |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                |
| regex_dna      | 239 ms                                                       | 252 ms: 1.06x slower                                                 |
| regex_v8       | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                        | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 98.5 ms: 1.04x faster                                                |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                 |
| pickle_pure_python   | 318 us                                                       | 310 us: 1.03x faster                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 85.1 ms: 1.01x faster                                                |
| pickle_dict          | 32.5 us                                                      | 32.4 us: 1.00x faster                                                |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                |
| unpickle_list        | 4.66 us                                                      | 4.72 us: 1.01x slower                                                |
| pickle               | 10.5 us                                                      | 10.7 us: 1.02x slower                                                |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                |
| xml_etree_process    | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                 |
| pickle_list          | 4.43 us                                                      | 4.65 us: 1.05x slower                                                |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                |
| tomli_loads          | 2.16 sec                                                     | 2.52 sec: 1.17x slower                                               |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                |
| python_startup         | 11.6 ms                                                      | 13.5 ms: 1.16x slower                                                |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.0 ms: 1.02x slower                                                |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                 |
| async_tree_none_tg         | 431 ms                                                       | 305 ms: 1.41x faster                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 398 ms: 1.37x faster                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 780 ms: 1.35x faster                                                 |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                |
| async_tree_io              | 1.04 sec                                                     | 806 ms: 1.29x faster                                                 |
| deepcopy                   | 368 us                                                       | 285 us: 1.29x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                                 |
| deepcopy_memo              | 36.8 us                                                      | 29.0 us: 1.27x faster                                                |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.26x faster                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                 |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.17x faster                                                |
| go                         | 150 ms                                                       | 133 ms: 1.12x faster                                                 |
| raytrace                   | 298 ms                                                       | 266 ms: 1.12x faster                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 72.3 ms: 1.11x faster                                                |
| async_generators           | 390 ms                                                       | 353 ms: 1.11x faster                                                 |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                                |
| logging_simple             | 6.71 us                                                      | 6.14 us: 1.09x faster                                                |
| logging_format             | 7.48 us                                                      | 6.89 us: 1.09x faster                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.8 ms: 1.08x faster                                                |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                 |
| bench_thread_pool          | 950 us                                                       | 895 us: 1.06x faster                                                 |
| scimark_lu                 | 98.8 ms                                                      | 93.1 ms: 1.06x faster                                                |
| scimark_fft                | 301 ms                                                       | 284 ms: 1.06x faster                                                 |
| tornado_http               | 121 ms                                                       | 115 ms: 1.05x faster                                                 |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 98.5 ms: 1.04x faster                                                |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                 |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                 |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                 |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                               |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                 |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                |
| pickle_pure_python         | 318 us                                                       | 310 us: 1.03x faster                                                 |
| chaos                      | 64.0 ms                                                      | 62.5 ms: 1.02x faster                                                |
| 2to3                       | 285 ms                                                       | 279 ms: 1.02x faster                                                 |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.02x faster                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                               |
| pprint_safe_repr           | 807 ms                                                       | 797 ms: 1.01x faster                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 85.1 ms: 1.01x faster                                                |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                |
| nqueens                    | 89.9 ms                                                      | 89.0 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.17 ms: 1.01x faster                                                |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                               |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.01x faster                                                 |
| pickle_dict                | 32.5 us                                                      | 32.4 us: 1.00x faster                                                |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                               |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                |
| unpickle_list              | 4.66 us                                                      | 4.72 us: 1.01x slower                                                |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                                 |
| json                       | 5.12 ms                                                      | 5.19 ms: 1.01x slower                                                |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.02x slower                                                |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                 |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                |
| dulwich_log                | 65.4 ms                                                      | 66.7 ms: 1.02x slower                                                |
| xml_etree_process          | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                |
| django_template            | 38.2 ms                                                      | 39.0 ms: 1.02x slower                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.02x slower                                                 |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                                |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                 |
| float                      | 76.6 ms                                                      | 78.8 ms: 1.03x slower                                                |
| hexiom                     | 5.96 ms                                                      | 6.16 ms: 1.03x slower                                                |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                 |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.05x slower                                                |
| pickle_list                | 4.43 us                                                      | 4.65 us: 1.05x slower                                                |
| logging_silent             | 94.4 ns                                                      | 99.3 ns: 1.05x slower                                                |
| regex_dna                  | 239 ms                                                       | 252 ms: 1.06x slower                                                 |
| spectral_norm              | 91.6 ms                                                      | 96.8 ms: 1.06x slower                                                |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                |
| richards_super             | 51.3 ms                                                      | 55.8 ms: 1.09x slower                                                |
| richards                   | 45.7 ms                                                      | 50.8 ms: 1.11x slower                                                |
| pyflate                    | 439 ms                                                       | 488 ms: 1.11x slower                                                 |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                 |
| regex_v8                   | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                |
| telco                      | 6.96 ms                                                      | 7.96 ms: 1.14x slower                                                |
| python_startup             | 11.6 ms                                                      | 13.5 ms: 1.16x slower                                                |
| tomli_loads                | 2.16 sec                                                     | 2.52 sec: 1.17x slower                                               |
| coverage                   | 66.7 ms                                                      | 83.6 ms: 1.25x slower                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                                |
| gc_traversal               | 3.48 ms                                                      | 4.53 ms: 1.30x slower                                                |
| bench_mp_pool              | 4.76 ms                                                      | 1.98 sec: 415.02x slower                                             |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                         |

Benchmark hidden because not significant (3): nbody, unpack_sequence, asyncio_websockets
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x