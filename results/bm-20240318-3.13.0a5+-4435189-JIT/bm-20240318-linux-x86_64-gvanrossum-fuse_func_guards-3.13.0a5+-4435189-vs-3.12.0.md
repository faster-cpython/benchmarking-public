# Results vs. 3.12.0

- fork: gvanrossum
- ref: fuse_func_guards
- machine: linux-x86_64
- commit hash: 4435189
- commit date: 2024-03-18
- overall geometric mean: 1.01x slower
- HPT reliability: 81.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                                   |
| chameleon      | 7.41 ms                                                | 6.98 ms: 1.06x faster                                                  |
| tornado_http   | 103 ms                                                 | 99.0 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 445 ms: 1.06x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 457 ms: 1.02x slower                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 584 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 739 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                 |
| async_tree_io              | 1.16 sec                                               | 1.21 sec: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.3 ms: 1.06x faster                                                  |
| nbody          | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                  |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                  |
| regex_dna      | 212 ms                                                 | 224 ms: 1.05x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                   |
| pickle_dict          | 35.5 us                                                | 33.7 us: 1.06x faster                                                  |
| unpickle_list        | 5.29 us                                                | 5.07 us: 1.04x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                  |
| unpickle             | 15.9 us                                                | 15.5 us: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.02x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 87.9 ms: 1.01x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 160 ms: 1.01x slower                                                   |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 109 ms: 1.02x slower                                                   |
| unpickle_pure_python | 230 us                                                 | 239 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| python_startup_no_site | 6.94 ms                                                | 11.2 ms: 1.61x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 112 us: 1.41x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.5 us: 1.25x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                 |
| logging_format             | 7.23 us                                                | 6.50 us: 1.11x faster                                                  |
| scimark_fft                | 382 ms                                                 | 346 ms: 1.10x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.89 us: 1.10x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.08 us: 1.09x faster                                                  |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 75.9 ms: 1.08x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.45 ms: 1.08x faster                                                  |
| raytrace                   | 312 ms                                                 | 293 ms: 1.07x faster                                                   |
| deepcopy                   | 371 us                                                 | 348 us: 1.07x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 70.7 ms: 1.06x faster                                                  |
| chameleon                  | 7.41 ms                                                | 6.98 ms: 1.06x faster                                                  |
| async_tree_none            | 472 ms                                                 | 445 ms: 1.06x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                   |
| pickle_dict                | 35.5 us                                                | 33.7 us: 1.06x faster                                                  |
| float                      | 84.7 ms                                                | 80.3 ms: 1.06x faster                                                  |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                  |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                   |
| sympy_str                  | 300 ms                                                 | 287 ms: 1.04x faster                                                   |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 39.0 us: 1.04x faster                                                  |
| chaos                      | 67.0 ms                                                | 64.2 ms: 1.04x faster                                                  |
| unpickle_list              | 5.29 us                                                | 5.07 us: 1.04x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 162 ms: 1.04x faster                                                   |
| nbody                      | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                  |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                   |
| tornado_http               | 103 ms                                                 | 99.0 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                  |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 758 ms: 1.02x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.5 us: 1.02x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.96 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                   |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                                   |
| pickle_list                | 5.08 us                                                | 5.01 us: 1.02x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.01x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 87.9 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                  |
| pathlib                    | 19.3 ms                                                | 19.1 ms: 1.01x faster                                                  |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 21.2 ms: 1.01x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 160 ms: 1.01x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                 |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                   |
| async_generators           | 463 ms                                                 | 468 ms: 1.01x slower                                                   |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                   |
| richards                   | 45.8 ms                                                | 46.5 ms: 1.01x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 855 us: 1.02x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                  |
| dulwich_log                | 68.5 ms                                                | 69.7 ms: 1.02x slower                                                  |
| async_tree_none_tg         | 450 ms                                                 | 457 ms: 1.02x slower                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 584 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 739 ms: 1.02x slower                                                   |
| sympy_expand               | 478 ms                                                 | 487 ms: 1.02x slower                                                   |
| richards_super             | 51.5 ms                                                | 52.6 ms: 1.02x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 109 ms: 1.02x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.51 ms: 1.02x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                   |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 3.92 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                                 |
| unpickle_pure_python       | 230 us                                                 | 239 us: 1.04x slower                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                 |
| aiohttp                    | 1.15 ms                                                | 1.20 ms: 1.04x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                                  |
| gunicorn                   | 1.24 ms                                                | 1.30 ms: 1.05x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                  |
| async_tree_io              | 1.16 sec                                               | 1.21 sec: 1.05x slower                                                 |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.05x slower                                                   |
| nqueens                    | 83.3 ms                                                | 90.2 ms: 1.08x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.04 ms: 1.10x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 26.4 ms: 1.10x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 132 ms: 1.12x slower                                                   |
| go                         | 139 ms                                                 | 158 ms: 1.13x slower                                                   |
| telco                      | 7.10 ms                                                | 8.44 ms: 1.19x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| coverage                   | 72.7 ms                                                | 98.6 ms: 1.36x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 86.8 ns: 1.61x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 11.2 ms: 1.61x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (9): async_tree_memoization, pickle, pyflate, django_template, sqlite_synth, docutils, async_tree_cpu_io_mixed, dask, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240318-3.13.0a5+-4435189-JIT/bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 81.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.17x