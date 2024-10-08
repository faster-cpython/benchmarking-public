# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 975089f
- commit date: 2024-08-21
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.1 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                                            |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.43x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 895 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 558 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 927 ms: 1.25x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.8 ms: 1.12x faster                                                           |
| float          | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                            |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                           |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                           |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                           |
| django_template | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                                            |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                            |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.43x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 895 ms: 1.32x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 558 ms: 1.30x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 927 ms: 1.25x faster                                                            |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                                           |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                                            |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.16x faster                                                           |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                           |
| tornado_http               | 103 ms                                                 | 90.1 ms: 1.14x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 72.6 ms: 1.13x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                          |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                           |
| nbody                      | 97.0 ms                                                | 86.8 ms: 1.12x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                            |
| float                      | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                            |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 783 us: 1.07x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                          |
| async_generators           | 463 ms                                                 | 435 ms: 1.06x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.78 ms: 1.06x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                           |
| logging_silent             | 104 ns                                                 | 99.3 ns: 1.05x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                            |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                            |
| scimark_fft                | 382 ms                                                 | 364 ms: 1.05x faster                                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.05x faster                                                          |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                           |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                            |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                          |
| asyncio_tcp                | 491 ms                                                 | 477 ms: 1.03x faster                                                            |
| django_template            | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                          |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                                            |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.02x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.00x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| richards                   | 45.8 ms                                                | 46.1 ms: 1.01x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 3.86 ms: 1.02x slower                                                           |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                           |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| telco                      | 7.10 ms                                                | 8.12 ms: 1.14x slower                                                           |
| go                         | 139 ms                                                 | 161 ms: 1.16x slower                                                            |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): bench_mp_pool, asyncio_tcp_ssl, json_loads, typing_runtime_protocols
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240821-3.14.0a0-975089f/bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x