# Results vs. 3.12.0

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: a0f1853
- commit date: 2024-08-12
- overall geometric mean: 1.09x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 2.99 sec: 1.08x slower                                         |
| tornado_http   | 103 ms                                                 | 92.3 ms: 1.11x faster                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                           |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 866 ms: 1.37x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                           |
| async_tree_io              | 1.16 sec                                               | 910 ms: 1.27x faster                                           |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.0 ms: 1.21x faster                                          |
| float          | 84.7 ms                                                | 70.3 ms: 1.21x faster                                          |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                           |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                           |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                          |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.22x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                          |
| unpickle_pure_python | 230 us                                                 | 210 us: 1.10x faster                                           |
| xml_etree_process    | 61.7 ms                                                | 56.4 ms: 1.09x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                           |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                          |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                           |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                          |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                          |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                          |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                          |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.82 ms: 1.21x faster                                          |
| django_template | 34.6 ms                                                | 35.2 ms: 1.02x slower                                          |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.3 us: 1.55x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                           |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                           |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 866 ms: 1.37x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                           |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                           |
| async_tree_io              | 1.16 sec                                               | 910 ms: 1.27x faster                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                          |
| crypto_pyaes               | 81.9 ms                                                | 65.7 ms: 1.25x faster                                          |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                           |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.22x faster                                         |
| mako                       | 11.9 ms                                                | 9.82 ms: 1.21x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 62.0 ms: 1.21x faster                                          |
| logging_format             | 7.23 us                                                | 5.97 us: 1.21x faster                                          |
| nbody                      | 97.0 ms                                                | 80.0 ms: 1.21x faster                                          |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                          |
| float                      | 84.7 ms                                                | 70.3 ms: 1.21x faster                                          |
| deltablue                  | 3.72 ms                                                | 3.11 ms: 1.19x faster                                          |
| logging_simple             | 6.46 us                                                | 5.42 us: 1.19x faster                                          |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                           |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.15x faster                                          |
| richards                   | 45.8 ms                                                | 40.0 ms: 1.15x faster                                          |
| fannkuch                   | 417 ms                                                 | 365 ms: 1.14x faster                                           |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                           |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.50 ms: 1.12x faster                                          |
| richards_super             | 51.5 ms                                                | 46.1 ms: 1.12x faster                                          |
| tornado_http               | 103 ms                                                 | 92.3 ms: 1.11x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                          |
| unpickle_pure_python       | 230 us                                                 | 210 us: 1.10x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 56.4 ms: 1.09x faster                                          |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                           |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                           |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                           |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                          |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                           |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                           |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                           |
| logging_silent             | 104 ns                                                 | 98.0 ns: 1.07x faster                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                          |
| bench_thread_pool          | 842 us                                                 | 813 us: 1.04x faster                                           |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                          |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                          |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                          |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                          |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                           |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                         |
| gc_traversal               | 3.79 ms                                                | 3.76 ms: 1.01x faster                                          |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                           |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.01x faster                                           |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                          |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                           |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.02x slower                                         |
| django_template            | 34.6 ms                                                | 35.2 ms: 1.02x slower                                          |
| nqueens                    | 83.3 ms                                                | 84.9 ms: 1.02x slower                                          |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                           |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                           |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                          |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                          |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.03x slower                                           |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                           |
| sqlglot_optimize           | 54.8 ms                                                | 57.3 ms: 1.05x slower                                          |
| hexiom                     | 6.41 ms                                                | 6.73 ms: 1.05x slower                                          |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.05x slower                                           |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                          |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                          |
| generators                 | 31.2 ms                                                | 33.2 ms: 1.06x slower                                          |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                           |
| docutils                   | 2.77 sec                                               | 2.99 sec: 1.08x slower                                         |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                          |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                          |
| coverage                   | 72.7 ms                                                | 92.0 ms: 1.27x slower                                          |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                   |

Benchmark hidden because not significant (2): 2to3, bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240812-3.14.0a0-a0f1853-JIT/bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x