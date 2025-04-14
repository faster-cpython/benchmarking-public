# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 266 ms: 1.03x faster                                         |
| chameleon      | 7.41 ms                                                | 6.88 ms: 1.08x faster                                        |
| tornado_http   | 103 ms                                                 | 91.0 ms: 1.13x faster                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 895 ms: 1.32x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 341 ms: 1.32x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 440 ms: 1.31x faster                                         |
| async_tree_io              | 1.16 sec                                               | 893 ms: 1.29x faster                                         |
| async_tree_none            | 472 ms                                                 | 367 ms: 1.29x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 451 ms: 1.28x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 572 ms: 1.27x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 594 ms: 1.22x faster                                         |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.6 ms: 1.13x faster                                        |
| float          | 84.7 ms                                                | 76.7 ms: 1.11x faster                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.13x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.85 ms: 1.07x slower                                        |
| regex_dna      | 212 ms                                                 | 237 ms: 1.12x slower                                         |
| regex_v8       | 23.1 ms                                                | 26.3 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                  | 1.05x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                       |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                         |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                         |
| json_loads           | 28.5 us                                                | 27.0 us: 1.05x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 60.6 ms: 1.02x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 88.0 ms: 1.01x faster                                        |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.00x faster                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.99 ms: 1.01x slower                                        |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.08x faster                                        |
| django_template | 34.6 ms                                                | 33.6 ms: 1.03x faster                                        |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.3 us: 1.33x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 895 ms: 1.32x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 341 ms: 1.32x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 440 ms: 1.31x faster                                         |
| async_tree_io              | 1.16 sec                                               | 893 ms: 1.29x faster                                         |
| async_tree_none            | 472 ms                                                 | 367 ms: 1.29x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 451 ms: 1.28x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 572 ms: 1.27x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 594 ms: 1.22x faster                                         |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                        |
| mypy2                      | 830 ms                                                 | 714 ms: 1.16x faster                                         |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                        |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                        |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                        |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                        |
| nbody                      | 97.0 ms                                                | 85.6 ms: 1.13x faster                                        |
| tornado_http               | 103 ms                                                 | 91.0 ms: 1.13x faster                                        |
| regex_compile              | 148 ms                                                 | 132 ms: 1.13x faster                                         |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                        |
| float                      | 84.7 ms                                                | 76.7 ms: 1.11x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                        |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                       |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                        |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                         |
| dulwich_log                | 68.5 ms                                                | 63.2 ms: 1.08x faster                                        |
| chameleon                  | 7.41 ms                                                | 6.88 ms: 1.08x faster                                        |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.08x faster                                        |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.02 ms: 1.07x faster                                        |
| deepcopy_memo              | 40.7 us                                                | 38.5 us: 1.06x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 3.16 us: 1.06x faster                                        |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                         |
| async_generators           | 463 ms                                                 | 439 ms: 1.06x faster                                         |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.05x faster                                        |
| coroutines                 | 23.2 ms                                                | 22.0 ms: 1.05x faster                                        |
| logging_silent             | 104 ns                                                 | 99.5 ns: 1.05x faster                                        |
| deepcopy                   | 371 us                                                 | 354 us: 1.05x faster                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                       |
| json                       | 5.26 ms                                                | 5.04 ms: 1.04x faster                                        |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                         |
| bench_thread_pool          | 842 us                                                 | 812 us: 1.04x faster                                         |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                         |
| 2to3                       | 274 ms                                                 | 266 ms: 1.03x faster                                         |
| django_template            | 34.6 ms                                                | 33.6 ms: 1.03x faster                                        |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                         |
| dask                       | 372 ms                                                 | 361 ms: 1.03x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                         |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                         |
| nqueens                    | 83.3 ms                                                | 81.4 ms: 1.02x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 60.6 ms: 1.02x faster                                        |
| gc_traversal               | 3.79 ms                                                | 3.73 ms: 1.02x faster                                        |
| sqlglot_optimize           | 54.8 ms                                                | 54.0 ms: 1.02x faster                                        |
| fannkuch                   | 417 ms                                                 | 411 ms: 1.01x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 88.0 ms: 1.01x faster                                        |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                         |
| pyflate                    | 482 ms                                                 | 477 ms: 1.01x faster                                         |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.00x faster                                        |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                         |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                       |
| python_startup_no_site     | 6.94 ms                                                | 6.99 ms: 1.01x slower                                        |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                       |
| go                         | 139 ms                                                 | 142 ms: 1.01x slower                                         |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                         |
| richards                   | 45.8 ms                                                | 47.5 ms: 1.04x slower                                        |
| richards_super             | 51.5 ms                                                | 54.0 ms: 1.05x slower                                        |
| regex_effbot               | 3.61 ms                                                | 3.85 ms: 1.07x slower                                        |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                        |
| regex_dna                  | 212 ms                                                 | 237 ms: 1.12x slower                                         |
| regex_v8                   | 23.1 ms                                                | 26.3 ms: 1.14x slower                                        |
| coverage                   | 72.7 ms                                                | 83.9 ms: 1.15x slower                                        |
| telco                      | 7.10 ms                                                | 8.23 ms: 1.16x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                        |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                 |

Benchmark hidden because not significant (5): scimark_sparse_mat_mult, spectral_norm, docutils, bench_mp_pool, pycparser
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.062x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x