# Results vs. 3.12.0

- fork: brandtbucher
- ref: revert_90a1b28
- machine: linux-x86_64
- commit hash: 0f9d2fe
- commit date: 2024-03-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                                   |
| chameleon      | 7.41 ms                                                | 6.95 ms: 1.07x faster                                                  |
| tornado_http   | 103 ms                                                 | 95.0 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 435 ms: 1.32x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 898 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 343 ms: 1.31x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 442 ms: 1.31x faster                                                   |
| async_tree_none            | 472 ms                                                 | 368 ms: 1.28x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 918 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 609 ms: 1.19x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.7 ms: 1.10x faster                                                  |
| nbody          | 97.0 ms                                                | 90.2 ms: 1.08x faster                                                  |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                  |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.17 sec: 1.08x faster                                                 |
| unpickle             | 15.9 us                                                | 14.9 us: 1.06x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.3 us: 1.04x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                   |
| unpickle_list        | 5.29 us                                                | 5.16 us: 1.02x faster                                                  |
| pickle_list          | 5.08 us                                                | 4.97 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                  |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.89 ms: 1.01x faster                                                  |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                  |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 112 us: 1.41x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 435 ms: 1.32x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 898 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 343 ms: 1.31x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 442 ms: 1.31x faster                                                   |
| async_tree_none            | 472 ms                                                 | 368 ms: 1.28x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 918 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 609 ms: 1.19x faster                                                   |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                  |
| mypy2                      | 830 ms                                                 | 735 ms: 1.13x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.4 ms: 1.12x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                                  |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                   |
| logging_format             | 7.23 us                                                | 6.54 us: 1.11x faster                                                  |
| float                      | 84.7 ms                                                | 76.7 ms: 1.10x faster                                                  |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                   |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.95 us: 1.09x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                   |
| tornado_http               | 103 ms                                                 | 95.0 ms: 1.08x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.17 sec: 1.08x faster                                                 |
| nbody                      | 97.0 ms                                                | 90.2 ms: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                  |
| chameleon                  | 7.41 ms                                                | 6.95 ms: 1.07x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.06x faster                                                  |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.06x faster                                                   |
| fannkuch                   | 417 ms                                                 | 394 ms: 1.06x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 3.17 us: 1.06x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 38.5 us: 1.06x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                                  |
| deepcopy                   | 371 us                                                 | 352 us: 1.05x faster                                                   |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                  |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                   |
| pathlib                    | 19.3 ms                                                | 18.4 ms: 1.05x faster                                                  |
| scimark_fft                | 382 ms                                                 | 366 ms: 1.04x faster                                                   |
| pyflate                    | 482 ms                                                 | 463 ms: 1.04x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 445 ms: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.3 ms: 1.04x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.3 us: 1.04x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                   |
| sympy_expand               | 478 ms                                                 | 462 ms: 1.03x faster                                                   |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                   |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                   |
| unpickle_list              | 5.29 us                                                | 5.16 us: 1.02x faster                                                  |
| pickle_list                | 5.08 us                                                | 4.97 us: 1.02x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.5 ms: 1.02x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                   |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                  |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.89 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 54.7 ms: 1.00x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                  |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 54.5 ns: 1.01x slower                                                  |
| richards                   | 45.8 ms                                                | 46.3 ms: 1.01x slower                                                  |
| richards_super             | 51.5 ms                                                | 52.2 ms: 1.01x slower                                                  |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                   |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                  |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 498 ms: 1.01x slower                                                   |
| aiohttp                    | 1.15 ms                                                | 1.17 ms: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                 |
| gunicorn                   | 1.24 ms                                                | 1.28 ms: 1.03x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 569 ms: 1.03x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.93 us: 1.03x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.00 ms: 1.06x slower                                                  |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.67 ms: 1.13x slower                                                  |
| telco                      | 7.10 ms                                                | 8.45 ms: 1.19x slower                                                  |
| coverage                   | 72.7 ms                                                | 95.5 ms: 1.31x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (4): dask, docutils, pycparser, xml_etree_parse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240327-3.13.0a5+-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: 0.95x