# Results vs. 3.12.0

- fork: brandtbucher
- ref: hoist_partial
- machine: linux-x86_64
- commit hash: 1ce3b25
- commit date: 2024-05-09
- overall geometric mean: 1.00x slower
- HPT reliability: 92.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                 |
| chameleon      | 7.41 ms                                                | 7.17 ms: 1.03x faster                                                |
| docutils       | 2.77 sec                                               | 2.98 sec: 1.08x slower                                               |
| tornado_http   | 103 ms                                                 | 98.1 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 345 ms: 1.30x faster                                                 |
| async_tree_none            | 472 ms                                                 | 363 ms: 1.30x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 454 ms: 1.27x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 477 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 618 ms: 1.17x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                               |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                |
| nbody          | 97.0 ms                                                | 86.1 ms: 1.13x faster                                                |
| pidigits       | 187 ms                                                 | 197 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.06x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                               |
| pickle_dict          | 35.5 us                                                | 33.1 us: 1.07x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 152 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.03x faster                                                 |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (3): unpickle_list, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.70 ms: 1.11x slower                                                |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.17x slower                                                |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.62 ms: 1.24x faster                                                |
| django_template | 34.6 ms                                                | 36.5 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.4 us: 1.32x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 345 ms: 1.30x faster                                                 |
| async_tree_none            | 472 ms                                                 | 363 ms: 1.30x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 454 ms: 1.27x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                 |
| mako                       | 11.9 ms                                                | 9.62 ms: 1.24x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 477 ms: 1.21x faster                                                 |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                               |
| scimark_fft                | 382 ms                                                 | 321 ms: 1.19x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 69.6 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 618 ms: 1.17x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                               |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                 |
| fannkuch                   | 417 ms                                                 | 368 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.47 ms: 1.13x faster                                                |
| logging_format             | 7.23 us                                                | 6.40 us: 1.13x faster                                                |
| nbody                      | 97.0 ms                                                | 86.1 ms: 1.13x faster                                                |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                                |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 37.5 us: 1.09x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.9 ms: 1.08x faster                                                |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                 |
| pickle_dict                | 35.5 us                                                | 33.1 us: 1.07x faster                                                |
| richards                   | 45.8 ms                                                | 42.7 ms: 1.07x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                 |
| regex_compile              | 148 ms                                                 | 139 ms: 1.06x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 152 ms: 1.05x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.1 ms: 1.05x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                 |
| tornado_http               | 103 ms                                                 | 98.1 ms: 1.05x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.03x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                |
| chameleon                  | 7.41 ms                                                | 7.17 ms: 1.03x faster                                                |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                |
| async_generators           | 463 ms                                                 | 468 ms: 1.01x slower                                                 |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                                 |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                                 |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                 |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 70.4 ms: 1.03x slower                                                |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                 |
| deepcopy                   | 371 us                                                 | 383 us: 1.03x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.04x slower                                                 |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                               |
| pickle_list                | 5.08 us                                                | 5.29 us: 1.04x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.69 ms: 1.04x slower                                                |
| pidigits                   | 187 ms                                                 | 197 ms: 1.05x slower                                                 |
| nqueens                    | 83.3 ms                                                | 87.7 ms: 1.05x slower                                                |
| django_template            | 34.6 ms                                                | 36.5 ms: 1.06x slower                                                |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                 |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 519 ms: 1.06x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                                |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                 |
| sympy_expand               | 478 ms                                                 | 512 ms: 1.07x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.98 sec: 1.08x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.11 ms: 1.08x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                |
| gunicorn                   | 1.24 ms                                                | 1.35 ms: 1.09x slower                                                |
| aiohttp                    | 1.15 ms                                                | 1.26 ms: 1.10x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.70 ms: 1.11x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 176 us: 1.12x slower                                                 |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.17x slower                                                |
| coverage                   | 72.7 ms                                                | 88.2 ms: 1.21x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.84 ms: 1.25x slower                                                |
| telco                      | 7.10 ms                                                | 172 ms: 24.21x slower                                                |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (6): unpickle_list, json_dumps, deepcopy_reduce, bench_mp_pool, unpickle, deltablue
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240509-3.14.0a0-1ce3b25-JIT/bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 92.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x