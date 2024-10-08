# Results vs. 3.12.0

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 7a595e7
- commit date: 2024-07-14
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                   |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| tornado_http   | 103 ms                                                 | 89.8 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 294 ms: 1.53x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.52x faster                                                   |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 848 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 849 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.1 ms: 1.09x faster                                                  |
| nbody          | 97.0 ms                                                | 91.4 ms: 1.06x faster                                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                  |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                   |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                   |
| json_loads           | 28.5 us                                                | 27.4 us: 1.04x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 158 ms: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                  |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 294 ms: 1.53x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.52x faster                                                   |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                   |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 848 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 849 ms: 1.36x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                  |
| logging_format             | 7.23 us                                                | 6.09 us: 1.19x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                  |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                   |
| tornado_http               | 103 ms                                                 | 89.8 ms: 1.14x faster                                                  |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 72.9 ms: 1.12x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                   |
| float                      | 84.7 ms                                                | 78.1 ms: 1.09x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                  |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 63.7 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.72 ms: 1.07x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                   |
| generators                 | 31.2 ms                                                | 29.3 ms: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 792 us: 1.06x faster                                                   |
| nbody                      | 97.0 ms                                                | 91.4 ms: 1.06x faster                                                  |
| nqueens                    | 83.3 ms                                                | 78.5 ms: 1.06x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                   |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                   |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                   |
| json_loads                 | 28.5 us                                                | 27.4 us: 1.04x faster                                                  |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                  |
| dask                       | 372 ms                                                 | 359 ms: 1.04x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                  |
| scimark_fft                | 382 ms                                                 | 370 ms: 1.03x faster                                                   |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                  |
| pyflate                    | 482 ms                                                 | 467 ms: 1.03x faster                                                   |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.69 ms: 1.03x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                 |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 158 ms: 1.01x faster                                                   |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 492 ms: 1.00x slower                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| go                         | 139 ms                                                 | 140 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                   |
| richards                   | 45.8 ms                                                | 47.2 ms: 1.03x slower                                                  |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                   |
| richards_super             | 51.5 ms                                                | 53.1 ms: 1.03x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                  |
| telco                      | 7.10 ms                                                | 8.34 ms: 1.17x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                  |
| coverage                   | 72.7 ms                                                | 93.1 ms: 1.28x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240714-3.14.0a0-7a595e7/bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x