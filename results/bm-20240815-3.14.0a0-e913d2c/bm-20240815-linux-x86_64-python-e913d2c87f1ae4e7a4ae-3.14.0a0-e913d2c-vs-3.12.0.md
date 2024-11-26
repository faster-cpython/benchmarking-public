# Results vs. 3.12.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                  |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 297 ms: 1.51x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 397 ms: 1.45x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 885 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 556 ms: 1.31x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.7 ms: 1.14x faster                                                 |
| float          | 84.7 ms                                                | 77.9 ms: 1.09x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                 |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                |
| unpickle_pure_python | 230 us                                                 | 209 us: 1.10x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 298 us: 1.09x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.08x faster                                                 |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 297 ms: 1.51x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 397 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 885 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 556 ms: 1.31x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                 |
| raytrace                   | 312 ms                                                 | 253 ms: 1.24x faster                                                  |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                 |
| nbody                      | 97.0 ms                                                | 84.7 ms: 1.14x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.13x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.52 ms: 1.12x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 209 us: 1.10x faster                                                  |
| float                      | 84.7 ms                                                | 77.9 ms: 1.09x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 298 us: 1.09x faster                                                  |
| logging_silent             | 104 ns                                                 | 96.5 ns: 1.08x faster                                                 |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.08x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.08x faster                                                 |
| scimark_fft                | 382 ms                                                 | 356 ms: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 787 us: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                 |
| async_generators           | 463 ms                                                 | 436 ms: 1.06x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.57 ms: 1.06x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                  |
| nqueens                    | 83.3 ms                                                | 78.7 ms: 1.06x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                  |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.17 ms: 1.04x faster                                                 |
| pyflate                    | 482 ms                                                 | 466 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                 |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.02x faster                                                  |
| richards                   | 45.8 ms                                                | 45.1 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| go                         | 139 ms                                                 | 138 ms: 1.01x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 487 ms: 1.01x faster                                                  |
| richards_super             | 51.5 ms                                                | 51.2 ms: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.15 ms: 1.15x slower                                                 |
| coverage                   | 72.7 ms                                                | 83.9 ms: 1.15x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (6): bench_mp_pool, spectral_norm, json_loads, asyncio_tcp_ssl, regex_effbot, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.092x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x