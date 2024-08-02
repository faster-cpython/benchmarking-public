
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 288 ms: 1.05x slower                                       |
| chameleon      | 7.41 ms                                                | 7.54 ms: 1.02x slower                                      |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.02x faster                                     |
| tornado_http   | 103 ms                                                 | 99.5 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 456 ms: 1.03x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 471 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 760 ms: 1.05x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.05x slower                                     |
| async_tree_io_tg           | 1.18 sec                                               | 1.25 sec: 1.06x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 611 ms: 1.06x slower                                       |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 196 ms: 1.04x slower                                       |
| float          | 84.7 ms                                                | 92.4 ms: 1.09x slower                                      |
| nbody          | 97.0 ms                                                | 119 ms: 1.22x slower                                       |
| Geometric mean | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                      |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                       |
| regex_compile  | 148 ms                                                 | 157 ms: 1.06x slower                                       |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                       |
| pickle_dict          | 35.5 us                                                | 34.0 us: 1.05x faster                                      |
| pickle               | 11.6 us                                                | 11.1 us: 1.04x faster                                      |
| pickle_list          | 5.08 us                                                | 4.94 us: 1.03x faster                                      |
| unpickle             | 15.9 us                                                | 15.6 us: 1.02x faster                                      |
| unpickle_list        | 5.29 us                                                | 5.21 us: 1.02x faster                                      |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                      |
| xml_etree_parse      | 159 ms                                                 | 158 ms: 1.01x faster                                       |
| xml_etree_generate   | 89.2 ms                                                | 90.2 ms: 1.01x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                      |
| tomli_loads          | 2.33 sec                                               | 2.39 sec: 1.03x slower                                     |
| xml_etree_iterparse  | 107 ms                                                 | 112 ms: 1.04x slower                                       |
| unpickle_pure_python | 230 us                                                 | 240 us: 1.04x slower                                       |
| Geometric mean       | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.3 ms: 1.08x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 9.00 ms: 1.30x slower                                      |
| Geometric mean         | (ref)                                                  | 1.18x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.9 ms                                                | 13.7 ms: 1.15x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 122 us: 1.29x faster                                       |
| unpack_sequence            | 54.0 ns                                                | 44.8 ns: 1.20x faster                                      |
| logging_simple             | 6.46 us                                                | 6.03 us: 1.07x faster                                      |
| sympy_sum                  | 169 ms                                                 | 160 ms: 1.06x faster                                       |
| logging_format             | 7.23 us                                                | 6.86 us: 1.05x faster                                      |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.18 us: 1.05x faster                                      |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                       |
| pickle_dict                | 35.5 us                                                | 34.0 us: 1.05x faster                                      |
| comprehensions             | 21.8 us                                                | 20.9 us: 1.04x faster                                      |
| pickle                     | 11.6 us                                                | 11.1 us: 1.04x faster                                      |
| async_tree_none            | 472 ms                                                 | 456 ms: 1.03x faster                                       |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.03x faster                                      |
| tornado_http               | 103 ms                                                 | 99.5 ms: 1.03x faster                                      |
| pickle_list                | 5.08 us                                                | 4.94 us: 1.03x faster                                      |
| deepcopy                   | 371 us                                                 | 362 us: 1.03x faster                                       |
| unpickle                   | 15.9 us                                                | 15.6 us: 1.02x faster                                      |
| sympy_str                  | 300 ms                                                 | 294 ms: 1.02x faster                                       |
| pathlib                    | 19.3 ms                                                | 19.0 ms: 1.02x faster                                      |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.02x faster                                     |
| unpickle_list              | 5.29 us                                                | 5.21 us: 1.02x faster                                      |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.46 ms: 1.01x faster                                      |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                      |
| asyncio_tcp                | 491 ms                                                 | 487 ms: 1.01x faster                                       |
| raytrace                   | 312 ms                                                 | 310 ms: 1.01x faster                                       |
| xml_etree_parse            | 159 ms                                                 | 158 ms: 1.01x faster                                       |
| sympy_integrate            | 21.4 ms                                                | 21.3 ms: 1.01x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 41.0 us: 1.01x slower                                      |
| dulwich_log                | 68.5 ms                                                | 69.0 ms: 1.01x slower                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| xml_etree_generate         | 89.2 ms                                                | 90.2 ms: 1.01x slower                                      |
| bench_thread_pool          | 842 us                                                 | 854 us: 1.01x slower                                       |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                       |
| chameleon                  | 7.41 ms                                                | 7.54 ms: 1.02x slower                                      |
| crypto_pyaes               | 81.9 ms                                                | 83.3 ms: 1.02x slower                                      |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                      |
| sqlite_synth               | 2.83 us                                                | 2.91 us: 1.03x slower                                      |
| tomli_loads                | 2.33 sec                                               | 2.39 sec: 1.03x slower                                     |
| meteor_contest             | 112 ms                                                 | 116 ms: 1.03x slower                                       |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                       |
| sympy_expand               | 478 ms                                                 | 493 ms: 1.03x slower                                       |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                      |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                       |
| pprint_safe_repr           | 776 ms                                                 | 809 ms: 1.04x slower                                       |
| xml_etree_iterparse        | 107 ms                                                 | 112 ms: 1.04x slower                                       |
| unpickle_pure_python       | 230 us                                                 | 240 us: 1.04x slower                                       |
| pidigits                   | 187 ms                                                 | 196 ms: 1.04x slower                                       |
| async_tree_none_tg         | 450 ms                                                 | 471 ms: 1.05x slower                                       |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 760 ms: 1.05x slower                                       |
| 2to3                       | 274 ms                                                 | 288 ms: 1.05x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.05x slower                                     |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.25 sec: 1.06x slower                                     |
| regex_compile              | 148 ms                                                 | 157 ms: 1.06x slower                                       |
| mdp                        | 2.63 sec                                               | 2.79 sec: 1.06x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 611 ms: 1.06x slower                                       |
| pycparser                  | 1.18 sec                                               | 1.26 sec: 1.07x slower                                     |
| sqlglot_optimize           | 54.8 ms                                                | 58.5 ms: 1.07x slower                                      |
| pprint_pformat             | 1.57 sec                                               | 1.68 sec: 1.07x slower                                     |
| fannkuch                   | 417 ms                                                 | 450 ms: 1.08x slower                                       |
| pyflate                    | 482 ms                                                 | 521 ms: 1.08x slower                                       |
| python_startup             | 9.55 ms                                                | 10.3 ms: 1.08x slower                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 81.4 ms: 1.08x slower                                      |
| richards                   | 45.8 ms                                                | 49.8 ms: 1.09x slower                                      |
| float                      | 84.7 ms                                                | 92.4 ms: 1.09x slower                                      |
| chaos                      | 67.0 ms                                                | 74.2 ms: 1.11x slower                                      |
| richards_super             | 51.5 ms                                                | 57.2 ms: 1.11x slower                                      |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                      |
| nqueens                    | 83.3 ms                                                | 94.1 ms: 1.13x slower                                      |
| gc_traversal               | 3.79 ms                                                | 4.29 ms: 1.13x slower                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.74 ms: 1.14x slower                                      |
| scimark_fft                | 382 ms                                                 | 436 ms: 1.14x slower                                       |
| mako                       | 11.9 ms                                                | 13.7 ms: 1.15x slower                                      |
| go                         | 139 ms                                                 | 163 ms: 1.17x slower                                       |
| telco                      | 7.10 ms                                                | 8.46 ms: 1.19x slower                                      |
| nbody                      | 97.0 ms                                                | 119 ms: 1.22x slower                                       |
| spectral_norm              | 115 ms                                                 | 140 ms: 1.22x slower                                       |
| deltablue                  | 3.72 ms                                                | 4.67 ms: 1.26x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 9.00 ms: 1.30x slower                                      |
| coverage                   | 72.7 ms                                                | 95.6 ms: 1.32x slower                                      |
| hexiom                     | 6.41 ms                                                | 8.49 ms: 1.32x slower                                      |
| Geometric mean             | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (9): json, bench_mp_pool, dask, xml_etree_process, asyncio_websockets, sqlglot_parse, async_tree_cpu_io_mixed, async_tree_memoization, mypy2
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x


# Memory

- memory change: 0.92x