# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b9e10d1
- commit date: 2024-08-19
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                  |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.02x faster                                |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 423 ms: 1.36x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 535 ms: 1.36x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 890 ms: 1.33x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                  |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                  |
| Geometric mean             | (ref)                                                  | 1.38x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.9 ms: 1.12x faster                                 |
| float          | 84.7 ms                                                | 78.6 ms: 1.08x faster                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                  |
| regex_effbot   | 3.61 ms                                                | 3.59 ms: 1.01x faster                                 |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                  |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                  |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                  |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                 |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                 |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                  |
| xml_etree_parse      | 159 ms                                                 | 158 ms: 1.01x faster                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                 |
| django_template | 34.6 ms                                                | 34.0 ms: 1.02x faster                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                  |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 423 ms: 1.36x faster                                  |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 535 ms: 1.36x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 890 ms: 1.33x faster                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                  |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                 |
| raytrace                   | 312 ms                                                 | 255 ms: 1.22x faster                                  |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                 |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                 |
| logging_simple             | 6.46 us                                                | 5.42 us: 1.19x faster                                 |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                 |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                  |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                 |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                 |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                 |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                |
| nbody                      | 97.0 ms                                                | 86.9 ms: 1.12x faster                                 |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                 |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                 |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.10x faster                                  |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                  |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                 |
| float                      | 84.7 ms                                                | 78.6 ms: 1.08x faster                                 |
| bench_thread_pool          | 842 us                                                 | 784 us: 1.07x faster                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                 |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                  |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                 |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                 |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                  |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                 |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                 |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                  |
| scimark_fft                | 382 ms                                                 | 365 ms: 1.05x faster                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                |
| nqueens                    | 83.3 ms                                                | 79.9 ms: 1.04x faster                                 |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                  |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                  |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                  |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                 |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.02x faster                                |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                 |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                  |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                 |
| django_template            | 34.6 ms                                                | 34.0 ms: 1.02x faster                                 |
| asyncio_tcp                | 491 ms                                                 | 483 ms: 1.02x faster                                  |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                  |
| pyflate                    | 482 ms                                                 | 477 ms: 1.01x faster                                  |
| xml_etree_parse            | 159 ms                                                 | 158 ms: 1.01x faster                                  |
| regex_effbot               | 3.61 ms                                                | 3.59 ms: 1.01x faster                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                  |
| fannkuch                   | 417 ms                                                 | 420 ms: 1.01x slower                                  |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                  |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                 |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                 |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                  |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                  |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                 |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.07x slower                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                 |
| telco                      | 7.10 ms                                                | 8.05 ms: 1.13x slower                                 |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                          |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, richards, spectral_norm, bench_mp_pool, richards_super, json_loads
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240819-3.14.0a0-b9e10d1/bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x