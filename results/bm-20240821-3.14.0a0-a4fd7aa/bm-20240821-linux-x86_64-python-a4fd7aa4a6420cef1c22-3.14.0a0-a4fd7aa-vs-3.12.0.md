# Results vs. 3.12.0

- fork: python
- ref: a4fd7aa4a6420cef1c22
- machine: linux-x86_64
- commit hash: a4fd7aa
- commit date: 2024-08-21
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                  |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                |
| tornado_http   | 103 ms                                                 | 90.5 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 404 ms: 1.42x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.32x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 905 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.23x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                 |
| float          | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 404 ms: 1.42x faster                                                  |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.32x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 905 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.23x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                 |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                 |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.5 ms: 1.13x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 72.5 ms: 1.13x faster                                                 |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                |
| nbody                      | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                 |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                  |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                 |
| float                      | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                  |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 789 us: 1.07x faster                                                  |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                  |
| nqueens                    | 83.3 ms                                                | 79.7 ms: 1.04x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                  |
| scimark_fft                | 382 ms                                                 | 368 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| asyncio_tcp                | 491 ms                                                 | 474 ms: 1.03x faster                                                  |
| pyflate                    | 482 ms                                                 | 466 ms: 1.03x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.03x faster                                                  |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.30 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.86 ms: 1.02x slower                                                 |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                  |
| richards                   | 45.8 ms                                                | 47.4 ms: 1.03x slower                                                 |
| richards_super             | 51.5 ms                                                | 53.3 ms: 1.04x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                 |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                 |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (4): spectral_norm, coroutines, json_loads, bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240821-3.14.0a0-a4fd7aa/bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x