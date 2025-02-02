# Results vs. 3.12.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                |
| tornado_http   | 103 ms                                                 | 89.9 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 402 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 544 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 903 ms: 1.31x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.5 ms: 1.13x faster                                                 |
| float          | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                 |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 402 ms: 1.44x faster                                                  |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 544 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 903 ms: 1.31x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                 |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                 |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                 |
| tornado_http               | 103 ms                                                 | 89.9 ms: 1.14x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 72.0 ms: 1.14x faster                                                 |
| nbody                      | 97.0 ms                                                | 85.5 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                 |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 67.3 ms: 1.12x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                 |
| float                      | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 783 us: 1.08x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                 |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                 |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                 |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| nqueens                    | 83.3 ms                                                | 79.3 ms: 1.05x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                                 |
| scimark_fft                | 382 ms                                                 | 365 ms: 1.05x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                  |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                  |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 477 ms: 1.03x faster                                                  |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                                  |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| richards                   | 45.8 ms                                                | 46.2 ms: 1.01x slower                                                 |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                 |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| go                         | 139 ms                                                 | 162 ms: 1.16x slower                                                  |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.18x slower                                                 |
| telco                      | 7.10 ms                                                | 8.36 ms: 1.18x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (3): bench_mp_pool, asyncio_tcp_ssl, typing_runtime_protocols
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.089x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x