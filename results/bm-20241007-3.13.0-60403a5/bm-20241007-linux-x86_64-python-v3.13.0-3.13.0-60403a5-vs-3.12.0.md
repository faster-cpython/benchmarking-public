# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.04x faster                                   |
| chameleon      | 7.41 ms                                                | 6.85 ms: 1.08x faster                                  |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                 |
| tornado_http   | 103 ms                                                 | 91.5 ms: 1.12x faster                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 825 ms: 1.43x faster                                   |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                   |
| async_tree_io              | 1.16 sec                                               | 843 ms: 1.37x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                   |
| async_tree_none            | 472 ms                                                 | 354 ms: 1.33x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 442 ms: 1.31x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 465 ms: 1.24x faster                                   |
| Geometric mean             | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.7 ms: 1.13x faster                                  |
| float          | 84.7 ms                                                | 78.5 ms: 1.08x faster                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                   |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                   |
| regex_effbot   | 3.61 ms                                                | 3.88 ms: 1.08x slower                                  |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                 |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                   |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                   |
| pickle_dict          | 35.5 us                                                | 33.2 us: 1.07x faster                                  |
| unpickle             | 15.9 us                                                | 14.9 us: 1.07x faster                                  |
| unpickle_list        | 5.29 us                                                | 4.96 us: 1.07x faster                                  |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                  |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                   |
| xml_etree_generate   | 89.2 ms                                                | 87.0 ms: 1.03x faster                                  |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                   |
| xml_etree_process    | 61.7 ms                                                | 60.4 ms: 1.02x faster                                  |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.02x faster                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): pickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.99 ms: 1.01x slower                                  |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                  |
| django_template | 34.6 ms                                                | 34.4 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 825 ms: 1.43x faster                                   |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                   |
| async_tree_io              | 1.16 sec                                               | 843 ms: 1.37x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                   |
| async_tree_none            | 472 ms                                                 | 354 ms: 1.33x faster                                   |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 442 ms: 1.31x faster                                   |
| unpack_sequence            | 54.0 ns                                                | 42.4 ns: 1.27x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 465 ms: 1.24x faster                                   |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                   |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                  |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                  |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                  |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                  |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 66.3 ms: 1.13x faster                                  |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                   |
| nbody                      | 97.0 ms                                                | 85.7 ms: 1.13x faster                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                  |
| tornado_http               | 103 ms                                                 | 91.5 ms: 1.12x faster                                  |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                 |
| dask                       | 372 ms                                                 | 338 ms: 1.10x faster                                   |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.10x faster                                   |
| fannkuch                   | 417 ms                                                 | 381 ms: 1.10x faster                                   |
| dulwich_log                | 68.5 ms                                                | 63.0 ms: 1.09x faster                                  |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.08x faster                                  |
| chameleon                  | 7.41 ms                                                | 6.85 ms: 1.08x faster                                  |
| float                      | 84.7 ms                                                | 78.5 ms: 1.08x faster                                  |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                   |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                   |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.08x faster                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                  |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                 |
| pickle_dict                | 35.5 us                                                | 33.2 us: 1.07x faster                                  |
| deepcopy_memo              | 40.7 us                                                | 38.0 us: 1.07x faster                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                  |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                   |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.07x faster                                  |
| unpickle_list              | 5.29 us                                                | 4.96 us: 1.07x faster                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.17 us: 1.06x faster                                  |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                  |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.05x faster                                   |
| deepcopy                   | 371 us                                                 | 352 us: 1.05x faster                                   |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                   |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                  |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                   |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                   |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                 |
| scimark_fft                | 382 ms                                                 | 369 ms: 1.04x faster                                   |
| sympy_expand               | 478 ms                                                 | 462 ms: 1.04x faster                                   |
| 2to3                       | 274 ms                                                 | 265 ms: 1.04x faster                                   |
| bench_thread_pool          | 842 us                                                 | 815 us: 1.03x faster                                   |
| nqueens                    | 83.3 ms                                                | 80.6 ms: 1.03x faster                                  |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                  |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                   |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                   |
| xml_etree_generate         | 89.2 ms                                                | 87.0 ms: 1.03x faster                                  |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                   |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                   |
| xml_etree_process          | 61.7 ms                                                | 60.4 ms: 1.02x faster                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                  |
| pickle_list                | 5.08 us                                                | 5.01 us: 1.02x faster                                  |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                  |
| gunicorn                   | 1.24 ms                                                | 1.23 ms: 1.01x faster                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.03 ms: 1.01x faster                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                   |
| django_template            | 34.6 ms                                                | 34.4 ms: 1.01x faster                                  |
| aiohttp                    | 1.15 ms                                                | 1.14 ms: 1.01x faster                                  |
| asyncio_tcp                | 491 ms                                                 | 488 ms: 1.01x faster                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                 |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.00x slower                                  |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.99 ms: 1.01x slower                                  |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                   |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                   |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                 |
| go                         | 139 ms                                                 | 142 ms: 1.01x slower                                   |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                   |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                 |
| richards                   | 45.8 ms                                                | 48.1 ms: 1.05x slower                                  |
| richards_super             | 51.5 ms                                                | 54.4 ms: 1.06x slower                                  |
| regex_effbot               | 3.61 ms                                                | 3.88 ms: 1.08x slower                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.61 ms: 1.09x slower                                  |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                  |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                  |
| coverage                   | 72.7 ms                                                | 83.7 ms: 1.15x slower                                  |
| telco                      | 7.10 ms                                                | 8.45 ms: 1.19x slower                                  |
| mypy2                      | 830 ms                                                 | 1.07 sec: 1.29x slower                                 |
| Geometric mean             | (ref)                                                  | 1.06x faster                                           |

Benchmark hidden because not significant (4): pickle, bench_mp_pool, spectral_norm, json_dumps
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.97x