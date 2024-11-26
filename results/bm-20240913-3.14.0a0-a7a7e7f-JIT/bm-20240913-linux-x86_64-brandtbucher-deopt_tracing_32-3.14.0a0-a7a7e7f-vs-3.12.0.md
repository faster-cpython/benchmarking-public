# Results vs. 3.12.0

- fork: brandtbucher
- ref: deopt_tracing_32
- machine: linux-x86_64
- commit hash: a7a7e7f
- commit date: 2024-09-13
- overall geometric mean: 1.087x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                    |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                  |
| tornado_http   | 103 ms                                                 | 94.6 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.47x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.46x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 852 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                   |
| nbody          | 97.0 ms                                                | 81.9 ms: 1.18x faster                                                   |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.13x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.05x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                   |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 77.5 ms: 1.15x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                   |
| pickle_dict          | 35.5 us                                                | 33.2 us: 1.07x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                    |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                                   |
| unpickle             | 15.9 us                                                | 15.2 us: 1.05x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| pickle               | 11.6 us                                                | 11.3 us: 1.02x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.04 us: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.79 ms: 1.21x faster                                                   |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                                   |
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.47x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.46x faster                                                    |
| deepcopy                   | 371 us                                                 | 264 us: 1.41x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 852 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 65.3 ms: 1.25x faster                                                   |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.25x faster                                                    |
| float                      | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                  |
| mako                       | 11.9 ms                                                | 9.79 ms: 1.21x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.21 ms: 1.20x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                   |
| nbody                      | 97.0 ms                                                | 81.9 ms: 1.18x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 77.5 ms: 1.15x faster                                                   |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                    |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                   |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                   |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.12x faster                                                   |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                    |
| fannkuch                   | 417 ms                                                 | 380 ms: 1.10x faster                                                    |
| richards_super             | 51.5 ms                                                | 47.3 ms: 1.09x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                    |
| tornado_http               | 103 ms                                                 | 94.6 ms: 1.08x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                                   |
| pickle_dict                | 35.5 us                                                | 33.2 us: 1.07x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                    |
| json                       | 5.26 ms                                                | 4.95 ms: 1.06x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                                   |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                    |
| regex_compile              | 148 ms                                                 | 142 ms: 1.05x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                                   |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.05x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                                   |
| go                         | 139 ms                                                 | 135 ms: 1.03x faster                                                    |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 66.7 ms: 1.03x faster                                                   |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                   |
| pickle                     | 11.6 us                                                | 11.3 us: 1.02x faster                                                   |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                    |
| pickle_list                | 5.08 us                                                | 5.04 us: 1.01x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 835 us: 1.01x faster                                                    |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 498 ms: 1.01x slower                                                    |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                    |
| nqueens                    | 83.3 ms                                                | 84.8 ms: 1.02x slower                                                   |
| sympy_str                  | 300 ms                                                 | 305 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.72 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                    |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                   |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                   |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                    |
| generators                 | 31.2 ms                                                | 33.2 ms: 1.06x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                  |
| coroutines                 | 23.2 ms                                                | 24.9 ms: 1.07x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.07x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.89 ms: 1.07x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 59.0 ms: 1.08x slower                                                   |
| sympy_expand               | 478 ms                                                 | 517 ms: 1.08x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                   |
| coverage                   | 72.7 ms                                                | 89.6 ms: 1.23x slower                                                   |
| unpack_sequence            | 54.0 ns                                                | 110 ns: 2.05x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240913-3.14.0a0-a7a7e7f-JIT/bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.087x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x