# Results vs. 3.12.0

- fork: gvanrossum
- ref: func_version_cache
- machine: linux-x86_64
- commit hash: 0fd96be
- commit date: 2024-03-19
- overall geometric mean: 1.00x slower
- HPT reliability: 73.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                     |
| chameleon      | 7.41 ms                                                | 6.93 ms: 1.07x faster                                                    |
| docutils       | 2.77 sec                                               | 2.75 sec: 1.01x faster                                                   |
| tornado_http   | 103 ms                                                 | 99.1 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 450 ms: 1.05x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 460 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 743 ms: 1.02x slower                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 592 ms: 1.03x slower                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                   |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.06x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 92.6 ms: 1.05x faster                                                    |
| float          | 84.7 ms                                                | 81.4 ms: 1.04x faster                                                    |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                    |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                     |
| pickle_dict          | 35.5 us                                                | 33.5 us: 1.06x faster                                                    |
| unpickle_list        | 5.29 us                                                | 5.05 us: 1.05x faster                                                    |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                    |
| pickle_list          | 5.08 us                                                | 4.93 us: 1.03x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 88.0 ms: 1.01x faster                                                    |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                    |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                    |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 109 ms: 1.02x slower                                                     |
| unpickle_pure_python | 230 us                                                 | 237 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.5 ms: 1.21x slower                                                    |
| python_startup_no_site | 6.94 ms                                                | 10.1 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.33x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 111 us: 1.42x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.9 us: 1.22x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                   |
| logging_format             | 7.23 us                                                | 6.48 us: 1.12x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.84 us: 1.11x faster                                                    |
| scimark_fft                | 382 ms                                                 | 348 ms: 1.10x faster                                                     |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 75.6 ms: 1.08x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.46 ms: 1.07x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 3.13 us: 1.07x faster                                                    |
| chameleon                  | 7.41 ms                                                | 6.93 ms: 1.07x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 70.7 ms: 1.06x faster                                                    |
| pickle_dict                | 35.5 us                                                | 33.5 us: 1.06x faster                                                    |
| raytrace                   | 312 ms                                                 | 294 ms: 1.06x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 38.5 us: 1.06x faster                                                    |
| deepcopy                   | 371 us                                                 | 351 us: 1.06x faster                                                     |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                    |
| async_tree_none            | 472 ms                                                 | 450 ms: 1.05x faster                                                     |
| unpickle_list              | 5.29 us                                                | 5.05 us: 1.05x faster                                                    |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                    |
| nbody                      | 97.0 ms                                                | 92.6 ms: 1.05x faster                                                    |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                                     |
| chaos                      | 67.0 ms                                                | 64.3 ms: 1.04x faster                                                    |
| float                      | 84.7 ms                                                | 81.4 ms: 1.04x faster                                                    |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                     |
| sympy_str                  | 300 ms                                                 | 289 ms: 1.04x faster                                                     |
| tornado_http               | 103 ms                                                 | 99.1 ms: 1.04x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 164 ms: 1.03x faster                                                     |
| pathlib                    | 19.3 ms                                                | 18.7 ms: 1.03x faster                                                    |
| pickle_list                | 5.08 us                                                | 4.93 us: 1.03x faster                                                    |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                    |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 760 ms: 1.02x faster                                                     |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.01x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 88.0 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 21.3 ms: 1.01x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.75 sec: 1.01x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                                    |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 848 us: 1.01x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                    |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                     |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.01x slower                                                    |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                   |
| richards_super             | 51.5 ms                                                | 52.5 ms: 1.02x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                                     |
| async_tree_none_tg         | 450 ms                                                 | 460 ms: 1.02x slower                                                     |
| sympy_expand               | 478 ms                                                 | 490 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 743 ms: 1.02x slower                                                     |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                     |
| dulwich_log                | 68.5 ms                                                | 70.2 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 109 ms: 1.02x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                     |
| pyflate                    | 482 ms                                                 | 495 ms: 1.03x slower                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 592 ms: 1.03x slower                                                     |
| unpickle_pure_python       | 230 us                                                 | 237 us: 1.03x slower                                                     |
| async_generators           | 463 ms                                                 | 478 ms: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.53 ms: 1.04x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                   |
| aiohttp                    | 1.15 ms                                                | 1.19 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                   |
| gunicorn                   | 1.24 ms                                                | 1.29 ms: 1.04x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 57.2 ms: 1.04x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                    |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.06x slower                                                   |
| nqueens                    | 83.3 ms                                                | 90.2 ms: 1.08x slower                                                    |
| hexiom                     | 6.41 ms                                                | 7.03 ms: 1.10x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 131 ms: 1.11x slower                                                     |
| go                         | 139 ms                                                 | 158 ms: 1.13x slower                                                     |
| telco                      | 7.10 ms                                                | 8.42 ms: 1.19x slower                                                    |
| python_startup             | 9.55 ms                                                | 11.5 ms: 1.21x slower                                                    |
| coverage                   | 72.7 ms                                                | 98.6 ms: 1.36x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 10.1 ms: 1.46x slower                                                    |
| unpack_sequence            | 54.0 ns                                                | 87.7 ns: 1.62x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (13): async_tree_memoization, pickle, django_template, scimark_sor, spectral_norm, dask, mdp, bench_mp_pool, scimark_sparse_mat_mult, json, async_tree_cpu_io_mixed, richards, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240319-3.13.0a5+-0fd96be-JIT/bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 73.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.07x