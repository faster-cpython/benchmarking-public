# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_trace_too_short
- machine: linux-x86_64
- commit hash: ea1e85d
- commit date: 2024-06-06
- overall geometric mean: 1.03x faster
- HPT reliability: 96.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.03x slower                                                      |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                    |
| tornado_http   | 103 ms                                                 | 97.1 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 339 ms: 1.32x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 931 ms: 1.27x faster                                                      |
| async_tree_none            | 472 ms                                                 | 376 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 599 ms: 1.21x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 481 ms: 1.20x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 979 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 637 ms: 1.14x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                     |
| float          | 84.7 ms                                                | 72.1 ms: 1.18x faster                                                     |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                     |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 81.4 ms: 1.09x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                      |
| unpickle             | 15.9 us                                                | 14.9 us: 1.07x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 58.0 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                      |
| unpickle_list        | 5.29 us                                                | 5.20 us: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                     |
| pickle_dict          | 35.5 us                                                | 36.3 us: 1.02x slower                                                     |
| pickle               | 11.6 us                                                | 12.1 us: 1.05x slower                                                     |
| pickle_list          | 5.08 us                                                | 5.34 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.60 ms: 1.10x slower                                                     |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.99 ms: 1.19x faster                                                     |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 339 ms: 1.32x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 931 ms: 1.27x faster                                                      |
| async_tree_none            | 472 ms                                                 | 376 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 599 ms: 1.21x faster                                                      |
| nbody                      | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 481 ms: 1.20x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 68.4 ms: 1.20x faster                                                     |
| mako                       | 11.9 ms                                                | 9.99 ms: 1.19x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 63.3 ms: 1.19x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 979 ms: 1.18x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                     |
| fannkuch                   | 417 ms                                                 | 355 ms: 1.18x faster                                                      |
| float                      | 84.7 ms                                                | 72.1 ms: 1.18x faster                                                     |
| scimark_fft                | 382 ms                                                 | 327 ms: 1.17x faster                                                      |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 637 ms: 1.14x faster                                                      |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.48 ms: 1.13x faster                                                     |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                      |
| richards                   | 45.8 ms                                                | 41.5 ms: 1.10x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 81.4 ms: 1.09x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                    |
| regex_compile              | 148 ms                                                 | 138 ms: 1.08x faster                                                      |
| richards_super             | 51.5 ms                                                | 47.9 ms: 1.08x faster                                                     |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                      |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.07x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 58.0 ms: 1.06x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 38.4 us: 1.06x faster                                                     |
| tornado_http               | 103 ms                                                 | 97.1 ms: 1.06x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                    |
| unpickle_list              | 5.29 us                                                | 5.20 us: 1.02x faster                                                     |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                      |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.01x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 3.84 ms: 1.01x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                      |
| dask                       | 372 ms                                                 | 378 ms: 1.02x slower                                                      |
| deltablue                  | 3.72 ms                                                | 3.78 ms: 1.02x slower                                                     |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                     |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                     |
| pickle_dict                | 35.5 us                                                | 36.3 us: 1.02x slower                                                     |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                      |
| 2to3                       | 274 ms                                                 | 281 ms: 1.03x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                      |
| json                       | 5.26 ms                                                | 5.43 ms: 1.03x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 878 us: 1.04x slower                                                      |
| nqueens                    | 83.3 ms                                                | 86.9 ms: 1.04x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.87 sec: 1.04x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 57.3 ms: 1.04x slower                                                     |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                     |
| pickle                     | 11.6 us                                                | 12.1 us: 1.05x slower                                                     |
| pickle_list                | 5.08 us                                                | 5.34 us: 1.05x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                                     |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                    |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                      |
| scimark_sor                | 129 ms                                                 | 137 ms: 1.06x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 523 ms: 1.07x slower                                                      |
| sympy_expand               | 478 ms                                                 | 511 ms: 1.07x slower                                                      |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.60 ms: 1.10x slower                                                     |
| telco                      | 7.10 ms                                                | 8.14 ms: 1.15x slower                                                     |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.17x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                     |
| coverage                   | 72.7 ms                                                | 92.9 ms: 1.28x slower                                                     |
| generators                 | 31.2 ms                                                | 49.4 ms: 1.58x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (5): async_generators, bench_mp_pool, sqlite_synth, deepcopy, deepcopy_reduce
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240606-3.14.0a0-ea1e85d-JIT/bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.63% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x