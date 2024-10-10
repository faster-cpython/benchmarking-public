# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.07x slower
- HPT reliability: 52.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 315 ms: 1.11x slower                                                     |
| docutils       | 2.87 sec                                                     | 3.17 sec: 1.11x slower                                                   |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                        | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 312 ms: 1.38x faster                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                     |
| async_tree_none            | 452 ms                                                       | 329 ms: 1.37x faster                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 782 ms: 1.35x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 407 ms: 1.34x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 805 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 547 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                     |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                    |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                     |
| float          | 76.6 ms                                                      | 75.3 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.04x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                     |
| regex_effbot   | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                    |
| regex_compile  | 144 ms                                                       | 150 ms: 1.04x slower                                                     |
| regex_v8       | 23.6 ms                                                      | 24.8 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 78.8 ms: 1.09x faster                                                    |
| pickle_dict          | 32.5 us                                                      | 29.8 us: 1.09x faster                                                    |
| xml_etree_process    | 58.4 ms                                                      | 56.4 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                       | 99.8 ms: 1.03x faster                                                    |
| pickle_list          | 4.43 us                                                      | 4.30 us: 1.03x faster                                                    |
| json_loads           | 24.4 us                                                      | 23.8 us: 1.02x faster                                                    |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                    |
| unpickle_list        | 4.66 us                                                      | 4.71 us: 1.01x slower                                                    |
| tomli_loads          | 2.16 sec                                                     | 2.20 sec: 1.02x slower                                                   |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                     |
| unpickle_pure_python | 210 us                                                       | 219 us: 1.05x slower                                                     |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                    |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                    |
| django_template | 38.2 ms                                                      | 46.0 ms: 1.21x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 312 ms: 1.38x faster                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                     |
| async_tree_none            | 452 ms                                                       | 329 ms: 1.37x faster                                                     |
| deepcopy_memo              | 36.8 us                                                      | 27.3 us: 1.35x faster                                                    |
| async_tree_io_tg           | 1.05 sec                                                     | 782 ms: 1.35x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 407 ms: 1.34x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 805 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 547 ms: 1.28x faster                                                     |
| deepcopy                   | 368 us                                                       | 300 us: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                     |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                    |
| comprehensions             | 21.9 us                                                      | 18.7 us: 1.17x faster                                                    |
| crypto_pyaes               | 80.3 ms                                                      | 70.0 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                    |
| spectral_norm              | 91.6 ms                                                      | 82.8 ms: 1.11x faster                                                    |
| xml_etree_generate         | 86.1 ms                                                      | 78.8 ms: 1.09x faster                                                    |
| mako                       | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                    |
| pickle_dict                | 32.5 us                                                      | 29.8 us: 1.09x faster                                                    |
| scimark_fft                | 301 ms                                                       | 280 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 807 ms                                                       | 762 ms: 1.06x faster                                                     |
| nbody                      | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                    |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                     |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                    |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                     |
| xml_etree_process          | 58.4 ms                                                      | 56.4 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 99.8 ms: 1.03x faster                                                    |
| pickle_list                | 4.43 us                                                      | 4.30 us: 1.03x faster                                                    |
| scimark_lu                 | 98.8 ms                                                      | 96.0 ms: 1.03x faster                                                    |
| logging_format             | 7.48 us                                                      | 7.28 us: 1.03x faster                                                    |
| json_loads                 | 24.4 us                                                      | 23.8 us: 1.02x faster                                                    |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                    |
| async_generators           | 390 ms                                                       | 382 ms: 1.02x faster                                                     |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                     |
| float                      | 76.6 ms                                                      | 75.3 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.77 us                                                      | 2.73 us: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.15 ms: 1.01x faster                                                    |
| logging_simple             | 6.71 us                                                      | 6.63 us: 1.01x faster                                                    |
| fannkuch                   | 350 ms                                                       | 346 ms: 1.01x faster                                                     |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                     |
| dulwich_log                | 65.4 ms                                                      | 64.8 ms: 1.01x faster                                                    |
| generators                 | 37.4 ms                                                      | 37.3 ms: 1.00x faster                                                    |
| regex_effbot               | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                    |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                     |
| unpickle_list              | 4.66 us                                                      | 4.71 us: 1.01x slower                                                    |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                   |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                     |
| json                       | 5.12 ms                                                      | 5.19 ms: 1.01x slower                                                    |
| tomli_loads                | 2.16 sec                                                     | 2.20 sec: 1.02x slower                                                   |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                     |
| richards                   | 45.7 ms                                                      | 47.3 ms: 1.03x slower                                                    |
| pyflate                    | 439 ms                                                       | 456 ms: 1.04x slower                                                     |
| python_startup_no_site     | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                    |
| logging_silent             | 94.4 ns                                                      | 98.1 ns: 1.04x slower                                                    |
| regex_compile              | 144 ms                                                       | 150 ms: 1.04x slower                                                     |
| unpickle_pure_python       | 210 us                                                       | 219 us: 1.05x slower                                                     |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.05x slower                                                     |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                    |
| regex_v8                   | 23.6 ms                                                      | 24.8 ms: 1.05x slower                                                    |
| sympy_str                  | 302 ms                                                       | 318 ms: 1.05x slower                                                     |
| go                         | 150 ms                                                       | 158 ms: 1.06x slower                                                     |
| sympy_sum                  | 162 ms                                                       | 172 ms: 1.06x slower                                                     |
| pycparser                  | 1.23 sec                                                     | 1.31 sec: 1.06x slower                                                   |
| chaos                      | 64.0 ms                                                      | 68.0 ms: 1.06x slower                                                    |
| richards_super             | 51.3 ms                                                      | 55.4 ms: 1.08x slower                                                    |
| raytrace                   | 298 ms                                                       | 323 ms: 1.08x slower                                                     |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                    |
| telco                      | 6.96 ms                                                      | 7.63 ms: 1.10x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.10x slower                                                    |
| sympy_expand               | 484 ms                                                       | 534 ms: 1.10x slower                                                     |
| 2to3                       | 285 ms                                                       | 315 ms: 1.11x slower                                                     |
| docutils                   | 2.87 sec                                                     | 3.17 sec: 1.11x slower                                                   |
| sympy_integrate            | 23.9 ms                                                      | 27.0 ms: 1.13x slower                                                    |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.14x slower                                                     |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                    |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                     |
| sqlglot_normalize          | 116 ms                                                       | 136 ms: 1.17x slower                                                     |
| hexiom                     | 5.96 ms                                                      | 7.09 ms: 1.19x slower                                                    |
| create_gc_cycles           | 1.59 ms                                                      | 1.90 ms: 1.20x slower                                                    |
| django_template            | 38.2 ms                                                      | 46.0 ms: 1.21x slower                                                    |
| sqlglot_optimize           | 57.5 ms                                                      | 69.6 ms: 1.21x slower                                                    |
| gc_traversal               | 3.48 ms                                                      | 4.31 ms: 1.24x slower                                                    |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                                    |
| unpack_sequence            | 53.2 ns                                                      | 94.8 ns: 1.78x slower                                                    |
| bench_mp_pool              | 4.76 ms                                                      | 3.26 sec: 683.71x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                             |

Benchmark hidden because not significant (6): bench_thread_pool, deltablue, asyncio_tcp_ssl, scimark_monte_carlo, xml_etree_parse, unpickle
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 52.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x