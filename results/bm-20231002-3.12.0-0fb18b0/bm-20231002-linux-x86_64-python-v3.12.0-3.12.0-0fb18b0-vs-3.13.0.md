# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: linux-x86_64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.04x slower                                   |
| chameleon      | 6.85 ms                                                | 7.41 ms: 1.08x slower                                  |
| docutils       | 2.58 sec                                               | 2.77 sec: 1.07x slower                                 |
| tornado_http   | 91.5 ms                                                | 103 ms: 1.12x slower                                   |
| Geometric mean | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 551 ms: 1.01x faster                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                 |
| asyncio_tcp                | 488 ms                                                 | 491 ms: 1.01x slower                                   |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                  |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                   |
| async_tree_memoization_tg  | 465 ms                                                 | 575 ms: 1.24x slower                                   |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 726 ms: 1.26x slower                                   |
| async_tree_memoization     | 442 ms                                                 | 578 ms: 1.31x slower                                   |
| async_tree_none            | 354 ms                                                 | 472 ms: 1.33x slower                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 726 ms: 1.34x slower                                   |
| async_tree_io              | 843 ms                                                 | 1.16 sec: 1.37x slower                                 |
| async_tree_none_tg         | 320 ms                                                 | 450 ms: 1.40x slower                                   |
| async_tree_io_tg           | 825 ms                                                 | 1.18 sec: 1.43x slower                                 |
| Geometric mean             | (ref)                                                  | 1.20x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                   |
| float          | 78.5 ms                                                | 84.7 ms: 1.08x slower                                  |
| nbody          | 85.7 ms                                                | 97.0 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 23.1 ms: 1.09x faster                                  |
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.08x faster                                  |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                   |
| regex_compile  | 131 ms                                                 | 148 ms: 1.13x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_list          | 5.01 us                                                | 5.08 us: 1.02x slower                                  |
| xml_etree_process    | 60.4 ms                                                | 61.7 ms: 1.02x slower                                  |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                   |
| xml_etree_generate   | 87.0 ms                                                | 89.2 ms: 1.03x slower                                  |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.05x slower                                   |
| json_loads           | 27.0 us                                                | 28.5 us: 1.06x slower                                  |
| unpickle_list        | 4.96 us                                                | 5.29 us: 1.07x slower                                  |
| unpickle             | 14.9 us                                                | 15.9 us: 1.07x slower                                  |
| pickle_dict          | 33.2 us                                                | 35.5 us: 1.07x slower                                  |
| unpickle_pure_python | 213 us                                                 | 230 us: 1.08x slower                                   |
| pickle_pure_python   | 300 us                                                 | 324 us: 1.08x slower                                   |
| tomli_loads          | 2.11 sec                                               | 2.33 sec: 1.10x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (2): json_dumps, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 9.55 ms: 1.11x faster                                  |
| python_startup_no_site | 6.99 ms                                                | 6.94 ms: 1.01x faster                                  |
| Geometric mean         | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.6 ms: 1.01x slower                                  |
| mako            | 11.1 ms                                                | 11.9 ms: 1.07x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mypy2                      | 1.07 sec                                               | 830 ms: 1.29x faster                                   |
| telco                      | 8.45 ms                                                | 7.10 ms: 1.19x faster                                  |
| coverage                   | 83.7 ms                                                | 72.7 ms: 1.15x faster                                  |
| python_startup             | 10.6 ms                                                | 9.55 ms: 1.11x faster                                  |
| regex_v8                   | 25.3 ms                                                | 23.1 ms: 1.09x faster                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.48 ms: 1.09x faster                                  |
| regex_effbot               | 3.88 ms                                                | 3.61 ms: 1.08x faster                                  |
| richards_super             | 54.4 ms                                                | 51.5 ms: 1.06x faster                                  |
| richards                   | 48.1 ms                                                | 45.8 ms: 1.05x faster                                  |
| mdp                        | 2.74 sec                                               | 2.63 sec: 1.04x faster                                 |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                   |
| go                         | 142 ms                                                 | 139 ms: 1.01x faster                                   |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                 |
| typing_runtime_protocols   | 159 us                                                 | 158 us: 1.01x faster                                   |
| asyncio_websockets         | 555 ms                                                 | 551 ms: 1.01x faster                                   |
| python_startup_no_site     | 6.99 ms                                                | 6.94 ms: 1.01x faster                                  |
| sqlite_synth               | 2.85 us                                                | 2.83 us: 1.01x faster                                  |
| gc_traversal               | 3.81 ms                                                | 3.79 ms: 1.00x faster                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                 |
| asyncio_tcp                | 488 ms                                                 | 491 ms: 1.01x slower                                   |
| aiohttp                    | 1.14 ms                                                | 1.15 ms: 1.01x slower                                  |
| django_template            | 34.4 ms                                                | 34.6 ms: 1.01x slower                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.06 ms: 1.01x slower                                  |
| gunicorn                   | 1.23 ms                                                | 1.24 ms: 1.01x slower                                  |
| json                       | 5.20 ms                                                | 5.26 ms: 1.01x slower                                  |
| pickle_list                | 5.01 us                                                | 5.08 us: 1.02x slower                                  |
| sqlglot_optimize           | 53.9 ms                                                | 54.8 ms: 1.02x slower                                  |
| xml_etree_process          | 60.4 ms                                                | 61.7 ms: 1.02x slower                                  |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                   |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                   |
| xml_etree_generate         | 87.0 ms                                                | 89.2 ms: 1.03x slower                                  |
| scimark_lu                 | 115 ms                                                 | 118 ms: 1.03x slower                                   |
| sqlglot_normalize          | 107 ms                                                 | 110 ms: 1.03x slower                                   |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                  |
| nqueens                    | 80.6 ms                                                | 83.3 ms: 1.03x slower                                  |
| bench_thread_pool          | 815 us                                                 | 842 us: 1.03x slower                                   |
| 2to3                       | 265 ms                                                 | 274 ms: 1.04x slower                                   |
| sympy_expand               | 462 ms                                                 | 478 ms: 1.04x slower                                   |
| scimark_fft                | 369 ms                                                 | 382 ms: 1.04x slower                                   |
| pprint_pformat             | 1.51 sec                                               | 1.57 sec: 1.04x slower                                 |
| pprint_safe_repr           | 744 ms                                                 | 776 ms: 1.04x slower                                   |
| meteor_contest             | 108 ms                                                 | 112 ms: 1.04x slower                                   |
| xml_etree_iterparse        | 102 ms                                                 | 107 ms: 1.05x slower                                   |
| hexiom                     | 6.13 ms                                                | 6.41 ms: 1.05x slower                                  |
| pyflate                    | 460 ms                                                 | 482 ms: 1.05x slower                                   |
| deepcopy                   | 352 us                                                 | 371 us: 1.05x slower                                   |
| scimark_sor                | 122 ms                                                 | 129 ms: 1.05x slower                                   |
| json_loads                 | 27.0 us                                                | 28.5 us: 1.06x slower                                  |
| deepcopy_reduce            | 3.17 us                                                | 3.35 us: 1.06x slower                                  |
| unpickle_list              | 4.96 us                                                | 5.29 us: 1.07x slower                                  |
| unpickle                   | 14.9 us                                                | 15.9 us: 1.07x slower                                  |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                  |
| deepcopy_memo              | 38.0 us                                                | 40.7 us: 1.07x slower                                  |
| pickle_dict                | 33.2 us                                                | 35.5 us: 1.07x slower                                  |
| docutils                   | 2.58 sec                                               | 2.77 sec: 1.07x slower                                 |
| mako                       | 11.1 ms                                                | 11.9 ms: 1.07x slower                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.08x slower                                  |
| sympy_integrate            | 19.9 ms                                                | 21.4 ms: 1.08x slower                                  |
| unpickle_pure_python       | 213 us                                                 | 230 us: 1.08x slower                                   |
| pickle_pure_python         | 300 us                                                 | 324 us: 1.08x slower                                   |
| float                      | 78.5 ms                                                | 84.7 ms: 1.08x slower                                  |
| chameleon                  | 6.85 ms                                                | 7.41 ms: 1.08x slower                                  |
| generators                 | 28.8 ms                                                | 31.2 ms: 1.08x slower                                  |
| dulwich_log                | 63.0 ms                                                | 68.5 ms: 1.09x slower                                  |
| fannkuch                   | 381 ms                                                 | 417 ms: 1.10x slower                                   |
| sympy_str                  | 274 ms                                                 | 300 ms: 1.10x slower                                   |
| dask                       | 338 ms                                                 | 372 ms: 1.10x slower                                   |
| tomli_loads                | 2.11 sec                                               | 2.33 sec: 1.10x slower                                 |
| tornado_http               | 91.5 ms                                                | 103 ms: 1.12x slower                                   |
| crypto_pyaes               | 73.0 ms                                                | 81.9 ms: 1.12x slower                                  |
| sympy_sum                  | 150 ms                                                 | 169 ms: 1.13x slower                                   |
| nbody                      | 85.7 ms                                                | 97.0 ms: 1.13x slower                                  |
| regex_compile              | 131 ms                                                 | 148 ms: 1.13x slower                                   |
| scimark_monte_carlo        | 66.3 ms                                                | 75.1 ms: 1.13x slower                                  |
| pathlib                    | 17.1 ms                                                | 19.3 ms: 1.13x slower                                  |
| logging_simple             | 5.66 us                                                | 6.46 us: 1.14x slower                                  |
| chaos                      | 58.4 ms                                                | 67.0 ms: 1.15x slower                                  |
| logging_format             | 6.25 us                                                | 7.23 us: 1.16x slower                                  |
| deltablue                  | 3.15 ms                                                | 3.72 ms: 1.18x slower                                  |
| raytrace                   | 262 ms                                                 | 312 ms: 1.19x slower                                   |
| async_tree_memoization_tg  | 465 ms                                                 | 575 ms: 1.24x slower                                   |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 726 ms: 1.26x slower                                   |
| unpack_sequence            | 42.4 ns                                                | 54.0 ns: 1.27x slower                                  |
| async_tree_memoization     | 442 ms                                                 | 578 ms: 1.31x slower                                   |
| comprehensions             | 16.4 us                                                | 21.8 us: 1.33x slower                                  |
| async_tree_none            | 354 ms                                                 | 472 ms: 1.33x slower                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 726 ms: 1.34x slower                                   |
| async_tree_io              | 843 ms                                                 | 1.16 sec: 1.37x slower                                 |
| async_tree_none_tg         | 320 ms                                                 | 450 ms: 1.40x slower                                   |
| async_tree_io_tg           | 825 ms                                                 | 1.18 sec: 1.43x slower                                 |
| Geometric mean             | (ref)                                                  | 1.06x slower                                           |

Benchmark hidden because not significant (4): json_dumps, spectral_norm, bench_mp_pool, pickle
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.04x