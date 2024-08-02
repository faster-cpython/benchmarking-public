# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: c3cb6dd
- commit date: 2024-05-22
- overall geometric mean: 1.04x faster
- HPT reliability: 99.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 275 ms: 1.00x slower                                                  |
| chameleon      | 7.41 ms                                                | 7.14 ms: 1.04x faster                                                 |
| docutils       | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                |
| tornado_http   | 103 ms                                                 | 96.7 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 442 ms: 1.30x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 459 ms: 1.26x faster                                                  |
| async_tree_none            | 472 ms                                                 | 377 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 946 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 934 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 613 ms: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.3 ms: 1.22x faster                                                 |
| float          | 84.7 ms                                                | 72.2 ms: 1.17x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                 |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                 |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.06x faster                                                  |
| unpickle             | 15.9 us                                                | 15.0 us: 1.05x faster                                                 |
| unpickle_list        | 5.29 us                                                | 5.10 us: 1.04x faster                                                 |
| pickle_dict          | 35.5 us                                                | 34.8 us: 1.02x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 227 us: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.10 us: 1.00x slower                                                 |
| pickle               | 11.6 us                                                | 12.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.58 ms: 1.09x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                 |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 442 ms: 1.30x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 459 ms: 1.26x faster                                                  |
| async_tree_none            | 472 ms                                                 | 377 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 946 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 934 ms: 1.24x faster                                                  |
| nbody                      | 97.0 ms                                                | 79.3 ms: 1.22x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 68.2 ms: 1.20x faster                                                 |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 63.1 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 613 ms: 1.18x faster                                                  |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                 |
| float                      | 84.7 ms                                                | 72.2 ms: 1.17x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                |
| fannkuch                   | 417 ms                                                 | 363 ms: 1.15x faster                                                  |
| richards                   | 45.8 ms                                                | 40.2 ms: 1.14x faster                                                 |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.12x faster                                                 |
| logging_format             | 7.23 us                                                | 6.47 us: 1.12x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 703 ms: 1.10x faster                                                  |
| richards_super             | 51.5 ms                                                | 46.8 ms: 1.10x faster                                                 |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                  |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                  |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 37.5 us: 1.09x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.08x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.08x faster                                                 |
| tornado_http               | 103 ms                                                 | 96.7 ms: 1.06x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.06x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| chameleon                  | 7.41 ms                                                | 7.14 ms: 1.04x faster                                                 |
| unpickle_list              | 5.29 us                                                | 5.10 us: 1.04x faster                                                 |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                |
| pickle_dict                | 35.5 us                                                | 34.8 us: 1.02x faster                                                 |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 3.29 us: 1.02x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 227 us: 1.02x faster                                                  |
| deepcopy                   | 371 us                                                 | 366 us: 1.01x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                 |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                                  |
| 2to3                       | 274 ms                                                 | 275 ms: 1.00x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.10 us: 1.00x slower                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.01x slower                                                 |
| deltablue                  | 3.72 ms                                                | 3.77 ms: 1.02x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                 |
| async_generators           | 463 ms                                                 | 471 ms: 1.02x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.8 ms: 1.02x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 859 us: 1.02x slower                                                  |
| nqueens                    | 83.3 ms                                                | 85.1 ms: 1.02x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                  |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.03x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.2 ms: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                  |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                 |
| logging_silent             | 104 ns                                                 | 109 ns: 1.05x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                |
| mdp                        | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                |
| sympy_expand               | 478 ms                                                 | 503 ms: 1.05x slower                                                  |
| pickle                     | 11.6 us                                                | 12.2 us: 1.05x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 519 ms: 1.06x slower                                                  |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.06x slower                                                  |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.07x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.58 ms: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                 |
| telco                      | 7.10 ms                                                | 8.13 ms: 1.14x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                 |
| coverage                   | 72.7 ms                                                | 93.3 ms: 1.28x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (3): bench_mp_pool, json_loads, dask
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240522-3.14.0a0-c3cb6dd-JIT/bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.22% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x