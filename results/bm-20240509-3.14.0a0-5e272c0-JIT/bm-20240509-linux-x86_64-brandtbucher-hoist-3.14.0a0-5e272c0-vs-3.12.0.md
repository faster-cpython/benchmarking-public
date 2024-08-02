# Results vs. 3.12.0

- fork: brandtbucher
- ref: hoist
- machine: linux-x86_64
- commit hash: 5e272c0
- commit date: 2024-05-09
- overall geometric mean: 1.00x slower
- HPT reliability: 90.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                         |
| chameleon      | 7.41 ms                                                | 7.17 ms: 1.03x faster                                        |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                       |
| tornado_http   | 103 ms                                                 | 97.9 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                         |
| async_tree_none            | 472 ms                                                 | 368 ms: 1.28x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 455 ms: 1.26x faster                                         |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 623 ms: 1.16x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                       |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.0 ms: 1.20x faster                                        |
| float          | 84.7 ms                                                | 71.3 ms: 1.19x faster                                        |
| pidigits       | 187 ms                                                 | 197 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.06x faster                                         |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                         |
| regex_effbot   | 3.61 ms                                                | 3.82 ms: 1.06x slower                                        |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                       |
| xml_etree_generate   | 89.2 ms                                                | 83.4 ms: 1.07x faster                                        |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                         |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                        |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                         |
| pickle_dict          | 35.5 us                                                | 34.2 us: 1.04x faster                                        |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                         |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                        |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                        |
| unpickle             | 15.9 us                                                | 16.0 us: 1.01x slower                                        |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                        |
| pickle               | 11.6 us                                                | 12.2 us: 1.05x slower                                        |
| pickle_list          | 5.08 us                                                | 5.47 us: 1.08x slower                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.65 ms: 1.10x slower                                        |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.16x slower                                        |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.53 ms: 1.25x faster                                        |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                        |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                        |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                         |
| async_tree_none            | 472 ms                                                 | 368 ms: 1.28x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 455 ms: 1.26x faster                                         |
| mako                       | 11.9 ms                                                | 9.53 ms: 1.25x faster                                        |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                         |
| nbody                      | 97.0 ms                                                | 81.0 ms: 1.20x faster                                        |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                       |
| float                      | 84.7 ms                                                | 71.3 ms: 1.19x faster                                        |
| scimark_fft                | 382 ms                                                 | 323 ms: 1.18x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 69.4 ms: 1.18x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 64.5 ms: 1.17x faster                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 623 ms: 1.16x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                       |
| spectral_norm              | 115 ms                                                 | 99.0 ms: 1.16x faster                                        |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                        |
| fannkuch                   | 417 ms                                                 | 365 ms: 1.14x faster                                         |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                         |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                        |
| logging_format             | 7.23 us                                                | 6.48 us: 1.12x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.56 ms: 1.11x faster                                        |
| deepcopy_memo              | 40.7 us                                                | 37.5 us: 1.09x faster                                        |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                         |
| pathlib                    | 19.3 ms                                                | 17.9 ms: 1.08x faster                                        |
| richards                   | 45.8 ms                                                | 42.6 ms: 1.08x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 83.4 ms: 1.07x faster                                        |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                         |
| regex_compile              | 148 ms                                                 | 139 ms: 1.06x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                         |
| richards_super             | 51.5 ms                                                | 48.7 ms: 1.06x faster                                        |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                         |
| tornado_http               | 103 ms                                                 | 97.9 ms: 1.05x faster                                        |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                        |
| pickle_dict                | 35.5 us                                                | 34.2 us: 1.04x faster                                        |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                       |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                         |
| chameleon                  | 7.41 ms                                                | 7.17 ms: 1.03x faster                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.26 us: 1.03x faster                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                        |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                        |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                        |
| deepcopy                   | 371 us                                                 | 369 us: 1.00x faster                                         |
| coroutines                 | 23.2 ms                                                | 23.1 ms: 1.00x faster                                        |
| unpickle                   | 15.9 us                                                | 16.0 us: 1.01x slower                                        |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                        |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                        |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.01x slower                                         |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                         |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                         |
| async_generators           | 463 ms                                                 | 472 ms: 1.02x slower                                         |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                         |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                         |
| dulwich_log                | 68.5 ms                                                | 70.5 ms: 1.03x slower                                        |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                         |
| bench_thread_pool          | 842 us                                                 | 869 us: 1.03x slower                                         |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                         |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                       |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                        |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                         |
| pidigits                   | 187 ms                                                 | 197 ms: 1.05x slower                                         |
| nqueens                    | 83.3 ms                                                | 87.7 ms: 1.05x slower                                        |
| pickle                     | 11.6 us                                                | 12.2 us: 1.05x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.01 ms: 1.06x slower                                        |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                        |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                         |
| regex_effbot               | 3.61 ms                                                | 3.82 ms: 1.06x slower                                        |
| asyncio_tcp                | 491 ms                                                 | 521 ms: 1.06x slower                                         |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                         |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.07x slower                                        |
| hexiom                     | 6.41 ms                                                | 6.85 ms: 1.07x slower                                        |
| mdp                        | 2.63 sec                                               | 2.81 sec: 1.07x slower                                       |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                       |
| pickle_list                | 5.08 us                                                | 5.47 us: 1.08x slower                                        |
| aiohttp                    | 1.15 ms                                                | 1.25 ms: 1.09x slower                                        |
| gunicorn                   | 1.24 ms                                                | 1.36 ms: 1.09x slower                                        |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.65 ms: 1.10x slower                                        |
| typing_runtime_protocols   | 158 us                                                 | 176 us: 1.11x slower                                         |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.16x slower                                        |
| coverage                   | 72.7 ms                                                | 87.1 ms: 1.20x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.23x slower                                        |
| telco                      | 7.10 ms                                                | 173 ms: 24.34x slower                                        |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (4): scimark_sor, bench_mp_pool, json, deltablue
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240509-3.14.0a0-5e272c0-JIT/bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 90.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x