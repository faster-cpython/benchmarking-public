# Results vs. 3.12.0

- fork: faster-cpython
- ref: fix_gc_counting
- machine: linux-x86_64
- commit hash: d0672a4
- commit date: 2024-03-21
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 268 ms: 1.02x faster                                                        |
| chameleon      | 7.41 ms                                                | 6.95 ms: 1.07x faster                                                       |
| docutils       | 2.77 sec                                               | 2.74 sec: 1.01x faster                                                      |
| tornado_http   | 103 ms                                                 | 94.8 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 442 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 917 ms: 1.29x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                        |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 917 ms: 1.26x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 461 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 590 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 606 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.5 ms: 1.08x faster                                                       |
| nbody          | 97.0 ms                                                | 89.9 ms: 1.08x faster                                                       |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                        |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                        |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle             | 15.9 us                                                | 14.6 us: 1.09x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                        |
| tomli_loads          | 2.33 sec                                               | 2.19 sec: 1.06x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                       |
| unpickle_list        | 5.29 us                                                | 5.24 us: 1.01x faster                                                       |
| pickle_dict          | 35.5 us                                                | 35.3 us: 1.01x faster                                                       |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                       |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.02x slower                                                        |
| pickle_list          | 5.08 us                                                | 5.36 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (2): json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                       |
| python_startup_no_site | 6.94 ms                                                | 8.83 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                       |
| django_template | 34.6 ms                                                | 34.0 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 113 us: 1.40x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 442 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 917 ms: 1.29x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                        |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 917 ms: 1.26x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 461 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 590 ms: 1.23x faster                                                        |
| unpack_sequence            | 54.0 ns                                                | 44.2 ns: 1.22x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 606 ms: 1.20x faster                                                        |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                       |
| mypy2                      | 830 ms                                                 | 738 ms: 1.12x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 72.9 ms: 1.12x faster                                                       |
| logging_format             | 7.23 us                                                | 6.49 us: 1.11x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.84 us: 1.11x faster                                                       |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                        |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.09x faster                                                       |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.08x faster                                                       |
| tornado_http               | 103 ms                                                 | 94.8 ms: 1.08x faster                                                       |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 69.6 ms: 1.08x faster                                                       |
| float                      | 84.7 ms                                                | 78.5 ms: 1.08x faster                                                       |
| nbody                      | 97.0 ms                                                | 89.9 ms: 1.08x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 38.1 us: 1.07x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                       |
| chameleon                  | 7.41 ms                                                | 6.95 ms: 1.07x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.19 sec: 1.06x faster                                                      |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 3.16 us: 1.06x faster                                                       |
| async_generators           | 463 ms                                                 | 440 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.81 ms: 1.05x faster                                                       |
| pathlib                    | 19.3 ms                                                | 18.4 ms: 1.05x faster                                                       |
| deepcopy                   | 371 us                                                 | 353 us: 1.05x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                        |
| logging_silent             | 104 ns                                                 | 99.8 ns: 1.05x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 741 ms: 1.05x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                                       |
| generators                 | 31.2 ms                                                | 30.1 ms: 1.04x faster                                                       |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                        |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                       |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.44 ms: 1.02x faster                                                       |
| 2to3                       | 274 ms                                                 | 268 ms: 1.02x faster                                                        |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                        |
| nqueens                    | 83.3 ms                                                | 81.8 ms: 1.02x faster                                                       |
| django_template            | 34.6 ms                                                | 34.0 ms: 1.02x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                        |
| hexiom                     | 6.41 ms                                                | 6.34 ms: 1.01x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.9 ms: 1.01x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.74 sec: 1.01x faster                                                      |
| unpickle_list              | 5.29 us                                                | 5.24 us: 1.01x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                       |
| pickle_dict                | 35.5 us                                                | 35.3 us: 1.01x faster                                                       |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                       |
| richards                   | 45.8 ms                                                | 46.1 ms: 1.01x slower                                                       |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                       |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                        |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                        |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                       |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.02x slower                                                        |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                        |
| aiohttp                    | 1.15 ms                                                | 1.17 ms: 1.02x slower                                                       |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                                       |
| gunicorn                   | 1.24 ms                                                | 1.27 ms: 1.02x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 503 ms: 1.03x slower                                                        |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                      |
| richards_super             | 51.5 ms                                                | 53.1 ms: 1.03x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                      |
| pickle_list                | 5.08 us                                                | 5.36 us: 1.05x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                       |
| telco                      | 7.10 ms                                                | 8.41 ms: 1.18x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 8.83 ms: 1.27x slower                                                       |
| coverage                   | 72.7 ms                                                | 96.1 ms: 1.32x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (8): dask, spectral_norm, sqlglot_optimize, pyflate, regex_effbot, json_dumps, coroutines, xml_etree_iterparse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240321-3.13.0a5+-d0672a4/bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 0.95x