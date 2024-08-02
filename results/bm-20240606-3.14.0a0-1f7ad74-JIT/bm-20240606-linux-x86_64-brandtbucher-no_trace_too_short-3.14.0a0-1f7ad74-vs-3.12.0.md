# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_trace_too_short
- machine: linux-x86_64
- commit hash: 1f7ad74
- commit date: 2024-06-06
- overall geometric mean: 1.03x faster
- HPT reliability: 97.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                      |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                    |
| tornado_http   | 103 ms                                                 | 96.8 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 442 ms: 1.30x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 916 ms: 1.29x faster                                                      |
| async_tree_none            | 472 ms                                                 | 376 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 479 ms: 1.21x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 963 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 633 ms: 1.15x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.8 ms: 1.19x faster                                                     |
| float          | 84.7 ms                                                | 73.0 ms: 1.16x faster                                                     |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 4.01 ms: 1.11x slower                                                     |
| regex_dna      | 212 ms                                                 | 238 ms: 1.12x slower                                                      |
| regex_v8       | 23.1 ms                                                | 26.6 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 81.3 ms: 1.10x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                      |
| unpickle             | 15.9 us                                                | 14.9 us: 1.07x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                                      |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| pickle_list          | 5.08 us                                                | 5.05 us: 1.01x faster                                                     |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                     |
| unpickle_list        | 5.29 us                                                | 5.43 us: 1.03x slower                                                     |
| pickle               | 11.6 us                                                | 12.0 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.62 ms: 1.10x slower                                                     |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                     |
| django_template | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 442 ms: 1.30x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 916 ms: 1.29x faster                                                      |
| async_tree_none            | 472 ms                                                 | 376 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 479 ms: 1.21x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 67.9 ms: 1.21x faster                                                     |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 963 ms: 1.20x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                    |
| fannkuch                   | 417 ms                                                 | 350 ms: 1.19x faster                                                      |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                     |
| nbody                      | 97.0 ms                                                | 81.8 ms: 1.19x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                                     |
| float                      | 84.7 ms                                                | 73.0 ms: 1.16x faster                                                     |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 633 ms: 1.15x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                     |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                      |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.55 ms: 1.11x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 81.3 ms: 1.10x faster                                                     |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                      |
| richards                   | 45.8 ms                                                | 42.5 ms: 1.08x faster                                                     |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 38.1 us: 1.07x faster                                                     |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.07x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                      |
| tornado_http               | 103 ms                                                 | 96.8 ms: 1.06x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                    |
| richards_super             | 51.5 ms                                                | 49.2 ms: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                     |
| generators                 | 31.2 ms                                                | 30.5 ms: 1.02x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.02x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                     |
| pickle_list                | 5.08 us                                                | 5.05 us: 1.01x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 68.3 ms: 1.00x faster                                                     |
| deepcopy                   | 371 us                                                 | 373 us: 1.01x slower                                                      |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 3.83 ms: 1.01x slower                                                     |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                      |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                                      |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                      |
| json                       | 5.26 ms                                                | 5.38 ms: 1.02x slower                                                     |
| unpickle_list              | 5.29 us                                                | 5.43 us: 1.03x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.59 ms: 1.03x slower                                                     |
| deltablue                  | 3.72 ms                                                | 3.82 ms: 1.03x slower                                                     |
| nqueens                    | 83.3 ms                                                | 85.7 ms: 1.03x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 568 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                      |
| pickle                     | 11.6 us                                                | 12.0 us: 1.03x slower                                                     |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.04x slower                                                    |
| logging_silent             | 104 ns                                                 | 108 ns: 1.04x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 57.0 ms: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 517 ms: 1.05x slower                                                      |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                     |
| django_template            | 34.6 ms                                                | 36.8 ms: 1.06x slower                                                     |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                      |
| scimark_sor                | 129 ms                                                 | 138 ms: 1.07x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                    |
| sympy_expand               | 478 ms                                                 | 515 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.62 ms: 1.10x slower                                                     |
| regex_effbot               | 3.61 ms                                                | 4.01 ms: 1.11x slower                                                     |
| regex_dna                  | 212 ms                                                 | 238 ms: 1.12x slower                                                      |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 26.6 ms: 1.15x slower                                                     |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.81 ms: 1.22x slower                                                     |
| coverage                   | 72.7 ms                                                | 93.8 ms: 1.29x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (5): pickle_dict, async_generators, sqlite_synth, deepcopy_reduce, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240606-3.14.0a0-1f7ad74-JIT/bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.72% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x