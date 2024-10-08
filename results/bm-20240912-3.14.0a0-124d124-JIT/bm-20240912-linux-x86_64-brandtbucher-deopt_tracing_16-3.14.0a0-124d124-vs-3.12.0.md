# Results vs. 3.12.0

- fork: brandtbucher
- ref: deopt_tracing_16
- machine: linux-x86_64
- commit hash: 124d124
- commit date: 2024-09-12
- overall geometric mean: 1.06x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                                    |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                  |
| tornado_http   | 103 ms                                                 | 94.7 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 314 ms: 1.50x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 885 ms: 1.31x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                   |
| nbody          | 97.0 ms                                                | 81.1 ms: 1.20x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                    |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                   |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 77.6 ms: 1.15x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                   |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                    |
| pickle_dict          | 35.5 us                                                | 33.8 us: 1.05x faster                                                   |
| json_loads           | 28.5 us                                                | 27.4 us: 1.04x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.03x faster                                                    |
| unpickle_list        | 5.29 us                                                | 5.12 us: 1.03x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.71 ms: 1.23x faster                                                   |
| django_template | 34.6 ms                                                | 37.4 ms: 1.08x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                   |
| async_tree_none            | 472 ms                                                 | 314 ms: 1.50x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                    |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 885 ms: 1.31x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                   |
| scimark_fft                | 382 ms                                                 | 306 ms: 1.25x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 65.9 ms: 1.24x faster                                                   |
| mako                       | 11.9 ms                                                | 9.71 ms: 1.23x faster                                                   |
| float                      | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                  |
| nbody                      | 97.0 ms                                                | 81.1 ms: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.05 us: 1.19x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.33 ms: 1.17x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 77.6 ms: 1.15x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                   |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                    |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                                    |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                    |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                    |
| raytrace                   | 312 ms                                                 | 286 ms: 1.09x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                    |
| tornado_http               | 103 ms                                                 | 94.7 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                   |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.53 ms: 1.07x faster                                                   |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                    |
| pickle_dict                | 35.5 us                                                | 33.8 us: 1.05x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.4 us: 1.04x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.03x faster                                                    |
| unpickle_list              | 5.29 us                                                | 5.12 us: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                    |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                   |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                    |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                    |
| go                         | 139 ms                                                 | 137 ms: 1.02x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.66 ms: 1.01x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| richards_super             | 51.5 ms                                                | 51.1 ms: 1.01x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 68.0 ms: 1.01x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.37 ms: 1.01x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 498 ms: 1.02x slower                                                    |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.02x slower                                                   |
| richards                   | 45.8 ms                                                | 46.7 ms: 1.02x slower                                                   |
| sympy_str                  | 300 ms                                                 | 307 ms: 1.03x slower                                                    |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                   |
| nqueens                    | 83.3 ms                                                | 86.5 ms: 1.04x slower                                                   |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 177 ms: 1.05x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                  |
| generators                 | 31.2 ms                                                | 33.6 ms: 1.08x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 59.1 ms: 1.08x slower                                                   |
| django_template            | 34.6 ms                                                | 37.4 ms: 1.08x slower                                                   |
| sympy_expand               | 478 ms                                                 | 521 ms: 1.09x slower                                                    |
| hexiom                     | 6.41 ms                                                | 7.00 ms: 1.09x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 23.4 ms: 1.09x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 122 ms: 1.11x slower                                                    |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                   |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                   |
| unpack_sequence            | 54.0 ns                                                | 110 ns: 2.04x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                            |

Benchmark hidden because not significant (3): pickle_list, bench_mp_pool, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-124d124-JIT/bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x