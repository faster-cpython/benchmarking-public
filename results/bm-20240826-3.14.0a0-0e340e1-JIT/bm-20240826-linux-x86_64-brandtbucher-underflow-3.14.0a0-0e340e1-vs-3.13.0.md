# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 0e340e1
- commit date: 2024-08-26
- overall geometric mean: 1.00x slower
- HPT reliability: 51.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 283 ms: 1.07x slower                                             |
| docutils       | 2.58 sec                                               | 3.34 sec: 1.29x slower                                           |
| html5lib       | 64.5 ms                                                | 70.6 ms: 1.09x slower                                            |
| tornado_http   | 91.5 ms                                                | 102 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.14x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                             |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                             |
| async_tree_memoization    | 442 ms                                                 | 414 ms: 1.07x faster                                             |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 560 ms: 1.02x faster                                             |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                           |
| asyncio_tcp               | 488 ms                                                 | 514 ms: 1.05x slower                                             |
| async_generators          | 433 ms                                                 | 456 ms: 1.05x slower                                             |
| async_tree_io_tg          | 825 ms                                                 | 899 ms: 1.09x slower                                             |
| async_tree_io             | 843 ms                                                 | 941 ms: 1.12x slower                                             |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.0 ms: 1.11x faster                                            |
| nbody          | 85.7 ms                                                | 79.6 ms: 1.08x faster                                            |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.60 ms: 1.08x faster                                            |
| regex_v8       | 25.3 ms                                                | 24.2 ms: 1.04x faster                                            |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                             |
| regex_compile  | 131 ms                                                 | 150 ms: 1.15x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.0 ms: 1.13x faster                                            |
| xml_etree_process    | 60.4 ms                                                | 54.5 ms: 1.11x faster                                            |
| unpickle_pure_python | 213 us                                                 | 198 us: 1.08x faster                                             |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                             |
| json_dumps           | 10.4 ms                                                | 9.99 ms: 1.04x faster                                            |
| xml_etree_iterparse  | 102 ms                                                 | 98.8 ms: 1.03x faster                                            |
| tomli_loads          | 2.11 sec                                               | 2.05 sec: 1.03x faster                                           |
| pickle_pure_python   | 300 us                                                 | 310 us: 1.03x slower                                             |
| json_loads           | 27.0 us                                                | 29.6 us: 1.10x slower                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                            |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.61 ms: 1.16x faster                                            |
| genshi_text     | 22.9 ms                                                | 24.3 ms: 1.06x slower                                            |
| django_template | 34.4 ms                                                | 38.3 ms: 1.11x slower                                            |
| genshi_xml      | 50.3 ms                                                | 65.0 ms: 1.29x slower                                            |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.6 us: 1.43x faster                                            |
| deepcopy                  | 352 us                                                 | 263 us: 1.34x faster                                             |
| richards                  | 48.1 ms                                                | 38.1 ms: 1.26x faster                                            |
| richards_super            | 54.4 ms                                                | 43.1 ms: 1.26x faster                                            |
| scimark_fft               | 369 ms                                                 | 310 ms: 1.19x faster                                             |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                            |
| mako                      | 11.1 ms                                                | 9.61 ms: 1.16x faster                                            |
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                             |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                             |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.44 ms: 1.13x faster                                            |
| xml_etree_generate        | 87.0 ms                                                | 77.0 ms: 1.13x faster                                            |
| scimark_monte_carlo       | 66.3 ms                                                | 59.1 ms: 1.12x faster                                            |
| xml_etree_process         | 60.4 ms                                                | 54.5 ms: 1.11x faster                                            |
| crypto_pyaes              | 73.0 ms                                                | 65.9 ms: 1.11x faster                                            |
| float                     | 78.5 ms                                                | 71.0 ms: 1.11x faster                                            |
| telco                     | 8.45 ms                                                | 7.66 ms: 1.10x faster                                            |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                             |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                            |
| unpickle_pure_python      | 213 us                                                 | 198 us: 1.08x faster                                             |
| regex_effbot              | 3.88 ms                                                | 3.60 ms: 1.08x faster                                            |
| nbody                     | 85.7 ms                                                | 79.6 ms: 1.08x faster                                            |
| mdp                       | 2.74 sec                                               | 2.55 sec: 1.08x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 414 ms: 1.07x faster                                             |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                             |
| bpe_tokeniser             | 4.69 sec                                               | 4.44 sec: 1.06x faster                                           |
| pyflate                   | 460 ms                                                 | 440 ms: 1.04x faster                                             |
| regex_v8                  | 25.3 ms                                                | 24.2 ms: 1.04x faster                                            |
| json_dumps                | 10.4 ms                                                | 9.99 ms: 1.04x faster                                            |
| fannkuch                  | 381 ms                                                 | 367 ms: 1.04x faster                                             |
| xml_etree_iterparse       | 102 ms                                                 | 98.8 ms: 1.03x faster                                            |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                             |
| tomli_loads               | 2.11 sec                                               | 2.05 sec: 1.03x faster                                           |
| pprint_safe_repr          | 744 ms                                                 | 723 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 560 ms: 1.02x faster                                             |
| meteor_contest            | 108 ms                                                 | 105 ms: 1.02x faster                                             |
| regex_dna                 | 220 ms                                                 | 216 ms: 1.02x faster                                             |
| pprint_pformat            | 1.51 sec                                               | 1.49 sec: 1.01x faster                                           |
| thrift                    | 796 us                                                 | 789 us: 1.01x faster                                             |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                            |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                             |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                             |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                           |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.01x slower                                             |
| json                      | 5.20 ms                                                | 5.26 ms: 1.01x slower                                            |
| bench_thread_pool         | 815 us                                                 | 825 us: 1.01x slower                                             |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                            |
| python_startup_no_site    | 6.99 ms                                                | 7.16 ms: 1.02x slower                                            |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                             |
| logging_simple            | 5.66 us                                                | 5.84 us: 1.03x slower                                            |
| pycparser                 | 1.19 sec                                               | 1.23 sec: 1.03x slower                                           |
| pickle_pure_python        | 300 us                                                 | 310 us: 1.03x slower                                             |
| coverage                  | 83.7 ms                                                | 86.9 ms: 1.04x slower                                            |
| nqueens                   | 80.6 ms                                                | 83.7 ms: 1.04x slower                                            |
| deltablue                 | 3.15 ms                                                | 3.27 ms: 1.04x slower                                            |
| logging_format            | 6.25 us                                                | 6.51 us: 1.04x slower                                            |
| asyncio_tcp               | 488 ms                                                 | 514 ms: 1.05x slower                                             |
| async_generators          | 433 ms                                                 | 456 ms: 1.05x slower                                             |
| raytrace                  | 262 ms                                                 | 276 ms: 1.06x slower                                             |
| genshi_text               | 22.9 ms                                                | 24.3 ms: 1.06x slower                                            |
| 2to3                      | 265 ms                                                 | 283 ms: 1.07x slower                                             |
| async_tree_io_tg          | 825 ms                                                 | 899 ms: 1.09x slower                                             |
| html5lib                  | 64.5 ms                                                | 70.6 ms: 1.09x slower                                            |
| json_loads                | 27.0 us                                                | 29.6 us: 1.10x slower                                            |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                            |
| hexiom                    | 6.13 ms                                                | 6.82 ms: 1.11x slower                                            |
| django_template           | 34.4 ms                                                | 38.3 ms: 1.11x slower                                            |
| async_tree_io             | 843 ms                                                 | 941 ms: 1.12x slower                                             |
| tornado_http              | 91.5 ms                                                | 102 ms: 1.12x slower                                             |
| sqlglot_optimize          | 53.9 ms                                                | 60.4 ms: 1.12x slower                                            |
| sqlglot_normalize         | 107 ms                                                 | 121 ms: 1.13x slower                                             |
| sqlglot_transpile         | 1.57 ms                                                | 1.80 ms: 1.14x slower                                            |
| regex_compile             | 131 ms                                                 | 150 ms: 1.15x slower                                             |
| sympy_expand              | 462 ms                                                 | 536 ms: 1.16x slower                                             |
| generators                | 28.8 ms                                                | 33.7 ms: 1.17x slower                                            |
| sympy_str                 | 274 ms                                                 | 321 ms: 1.18x slower                                             |
| sqlglot_parse             | 1.27 ms                                                | 1.51 ms: 1.20x slower                                            |
| go                        | 142 ms                                                 | 170 ms: 1.20x slower                                             |
| sympy_integrate           | 19.9 ms                                                | 25.0 ms: 1.26x slower                                            |
| sympy_sum                 | 150 ms                                                 | 192 ms: 1.28x slower                                             |
| genshi_xml                | 50.3 ms                                                | 65.0 ms: 1.29x slower                                            |
| docutils                  | 2.58 sec                                               | 3.34 sec: 1.29x slower                                           |
| pylint                    | 313 ms                                                 | 415 ms: 1.33x slower                                             |
| Geometric mean            | (ref)                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, logging_silent, chaos, bench_mp_pool, asyncio_websockets, coroutines
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 51.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x