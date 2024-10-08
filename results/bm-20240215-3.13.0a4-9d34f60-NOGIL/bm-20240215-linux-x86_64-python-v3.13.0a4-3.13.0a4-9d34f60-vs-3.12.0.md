# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.06x slower
- HPT reliability: 98.89%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 296 ms: 1.08x slower                                       |
| chameleon      | 7.41 ms                                                | 8.24 ms: 1.11x slower                                      |
| docutils       | 2.77 sec                                               | 3.07 sec: 1.11x slower                                     |
| tornado_http   | 103 ms                                                 | 98.6 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 796 ms: 1.45x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 828 ms: 1.43x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 458 ms: 1.25x faster                                       |
| async_tree_none            | 472 ms                                                 | 377 ms: 1.25x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 476 ms: 1.21x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 377 ms: 1.19x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 612 ms: 1.19x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 646 ms: 1.12x faster                                       |
| Geometric mean             | (ref)                                                  | 1.26x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 84.7 ms                                                | 74.2 ms: 1.14x faster                                      |
| pidigits       | 187 ms                                                 | 194 ms: 1.04x slower                                       |
| nbody          | 97.0 ms                                                | 104 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.60 ms: 1.00x faster                                      |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                      |
| regex_dna      | 212 ms                                                 | 232 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.05x faster                                       |
| tomli_loads          | 2.33 sec                                               | 2.23 sec: 1.04x faster                                     |
| pickle_list          | 5.08 us                                                | 4.88 us: 1.04x faster                                      |
| unpickle_list        | 5.29 us                                                | 5.21 us: 1.02x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 90.5 ms: 1.02x slower                                      |
| pickle_pure_python   | 324 us                                                 | 333 us: 1.03x slower                                       |
| unpickle_pure_python | 230 us                                                 | 237 us: 1.03x slower                                       |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                      |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                      |
| json_loads           | 28.5 us                                                | 32.2 us: 1.13x slower                                      |
| unpickle             | 15.9 us                                                | 18.0 us: 1.13x slower                                      |
| xml_etree_process    | 61.7 ms                                                | 71.1 ms: 1.15x slower                                      |
| pickle_dict          | 35.5 us                                                | 41.2 us: 1.16x slower                                      |
| xml_etree_iterparse  | 107 ms                                                 | 166 ms: 1.55x slower                                       |
| Geometric mean       | (ref)                                                  | 1.08x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 12.0 ms: 1.26x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 10.0 ms: 1.45x slower                                      |
| Geometric mean         | (ref)                                                  | 1.35x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.6 ms                                                | 39.1 ms: 1.13x slower                                      |
| mako            | 11.9 ms                                                | 16.3 ms: 1.37x slower                                      |
| Geometric mean  | (ref)                                                  | 1.24x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| gc_traversal               | 3.79 ms                                                | 2.57 ms: 1.48x faster                                      |
| async_tree_io              | 1.16 sec                                               | 796 ms: 1.45x faster                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.03 ms: 1.44x faster                                      |
| async_tree_io_tg           | 1.18 sec                                               | 828 ms: 1.43x faster                                       |
| typing_runtime_protocols   | 158 us                                                 | 122 us: 1.29x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 458 ms: 1.25x faster                                       |
| async_tree_none            | 472 ms                                                 | 377 ms: 1.25x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 476 ms: 1.21x faster                                       |
| mypy2                      | 830 ms                                                 | 696 ms: 1.19x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 377 ms: 1.19x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 612 ms: 1.19x faster                                       |
| comprehensions             | 21.8 us                                                | 18.5 us: 1.17x faster                                      |
| float                      | 84.7 ms                                                | 74.2 ms: 1.14x faster                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 646 ms: 1.12x faster                                       |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                      |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                       |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.05x faster                                       |
| raytrace                   | 312 ms                                                 | 298 ms: 1.05x faster                                       |
| tomli_loads                | 2.33 sec                                               | 2.23 sec: 1.04x faster                                     |
| pickle_list                | 5.08 us                                                | 4.88 us: 1.04x faster                                      |
| tornado_http               | 103 ms                                                 | 98.6 ms: 1.04x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.4 ms: 1.03x faster                                      |
| pathlib                    | 19.3 ms                                                | 19.0 ms: 1.02x faster                                      |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                       |
| unpickle_list              | 5.29 us                                                | 5.21 us: 1.02x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 74.0 ms: 1.01x faster                                      |
| chaos                      | 67.0 ms                                                | 66.2 ms: 1.01x faster                                      |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                      |
| logging_format             | 7.23 us                                                | 7.18 us: 1.01x faster                                      |
| scimark_fft                | 382 ms                                                 | 380 ms: 1.01x faster                                       |
| regex_effbot               | 3.61 ms                                                | 3.60 ms: 1.00x faster                                      |
| dulwich_log                | 68.5 ms                                                | 69.0 ms: 1.01x slower                                      |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                     |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                       |
| xml_etree_generate         | 89.2 ms                                                | 90.5 ms: 1.02x slower                                      |
| nqueens                    | 83.3 ms                                                | 84.7 ms: 1.02x slower                                      |
| scimark_lu                 | 118 ms                                                 | 121 ms: 1.02x slower                                       |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                       |
| fannkuch                   | 417 ms                                                 | 428 ms: 1.03x slower                                       |
| pickle_pure_python         | 324 us                                                 | 333 us: 1.03x slower                                       |
| meteor_contest             | 112 ms                                                 | 115 ms: 1.03x slower                                       |
| pprint_safe_repr           | 776 ms                                                 | 797 ms: 1.03x slower                                       |
| unpickle_pure_python       | 230 us                                                 | 237 us: 1.03x slower                                       |
| hexiom                     | 6.41 ms                                                | 6.62 ms: 1.03x slower                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.46 us: 1.03x slower                                      |
| asyncio_tcp                | 491 ms                                                 | 508 ms: 1.04x slower                                       |
| pidigits                   | 187 ms                                                 | 194 ms: 1.04x slower                                       |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.25 ms: 1.04x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                     |
| pprint_pformat             | 1.57 sec                                               | 1.64 sec: 1.05x slower                                     |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                       |
| deepcopy                   | 371 us                                                 | 390 us: 1.05x slower                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.78 ms: 1.06x slower                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.44 ms: 1.06x slower                                      |
| nbody                      | 97.0 ms                                                | 104 ms: 1.07x slower                                       |
| richards                   | 45.8 ms                                                | 49.2 ms: 1.07x slower                                      |
| 2to3                       | 274 ms                                                 | 296 ms: 1.08x slower                                       |
| sqlglot_optimize           | 54.8 ms                                                | 59.3 ms: 1.08x slower                                      |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                      |
| richards_super             | 51.5 ms                                                | 56.3 ms: 1.09x slower                                      |
| logging_silent             | 104 ns                                                 | 114 ns: 1.09x slower                                       |
| regex_dna                  | 212 ms                                                 | 232 ms: 1.09x slower                                       |
| aiohttp                    | 1.15 ms                                                | 1.27 ms: 1.10x slower                                      |
| go                         | 139 ms                                                 | 154 ms: 1.10x slower                                       |
| json                       | 5.26 ms                                                | 5.81 ms: 1.10x slower                                      |
| gunicorn                   | 1.24 ms                                                | 1.37 ms: 1.11x slower                                      |
| docutils                   | 2.77 sec                                               | 3.07 sec: 1.11x slower                                     |
| sympy_integrate            | 21.4 ms                                                | 23.8 ms: 1.11x slower                                      |
| chameleon                  | 7.41 ms                                                | 8.24 ms: 1.11x slower                                      |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                      |
| sqlite_synth               | 2.83 us                                                | 3.17 us: 1.12x slower                                      |
| deepcopy_memo              | 40.7 us                                                | 45.6 us: 1.12x slower                                      |
| deltablue                  | 3.72 ms                                                | 4.16 ms: 1.12x slower                                      |
| json_loads                 | 28.5 us                                                | 32.2 us: 1.13x slower                                      |
| django_template            | 34.6 ms                                                | 39.1 ms: 1.13x slower                                      |
| unpickle                   | 15.9 us                                                | 18.0 us: 1.13x slower                                      |
| xml_etree_process          | 61.7 ms                                                | 71.1 ms: 1.15x slower                                      |
| pickle_dict                | 35.5 us                                                | 41.2 us: 1.16x slower                                      |
| sympy_str                  | 300 ms                                                 | 354 ms: 1.18x slower                                       |
| sympy_sum                  | 169 ms                                                 | 211 ms: 1.25x slower                                       |
| python_startup             | 9.55 ms                                                | 12.0 ms: 1.26x slower                                      |
| telco                      | 7.10 ms                                                | 9.09 ms: 1.28x slower                                      |
| sympy_expand               | 478 ms                                                 | 623 ms: 1.30x slower                                       |
| mako                       | 11.9 ms                                                | 16.3 ms: 1.37x slower                                      |
| mdp                        | 2.63 sec                                               | 3.64 sec: 1.38x slower                                     |
| python_startup_no_site     | 6.94 ms                                                | 10.0 ms: 1.45x slower                                      |
| xml_etree_iterparse        | 107 ms                                                 | 166 ms: 1.55x slower                                       |
| bench_thread_pool          | 842 us                                                 | 2.42 ms: 2.88x slower                                      |
| coverage                   | 72.7 ms                                                | 712 ms: 9.80x slower                                       |
| Geometric mean             | (ref)                                                  | 1.06x slower                                               |

Benchmark hidden because not significant (4): logging_simple, generators, async_generators, scimark_sor
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x