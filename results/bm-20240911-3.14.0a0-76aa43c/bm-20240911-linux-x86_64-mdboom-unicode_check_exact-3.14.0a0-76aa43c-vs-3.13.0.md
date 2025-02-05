# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.035x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                                 |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.02x slower                                               |
| html5lib       | 64.2 ms                                                | 63.0 ms: 1.02x faster                                                |
| tornado_http   | 92.4 ms                                                | 90.4 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                 |
| async_tree_none           | 351 ms                                                 | 313 ms: 1.12x faster                                                 |
| async_tree_none_tg        | 321 ms                                                 | 305 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 559 ms: 1.03x faster                                                 |
| async_generators          | 436 ms                                                 | 427 ms: 1.02x faster                                                 |
| asyncio_websockets        | 552 ms                                                 | 554 ms: 1.00x slower                                                 |
| async_tree_io             | 842 ms                                                 | 861 ms: 1.02x slower                                                 |
| coroutines                | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.7 ms: 1.02x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| nbody          | 87.0 ms                                                | 89.4 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.53 ms: 1.06x faster                                                |
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                 |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                               |
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                                 |
| xml_etree_process    | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 85.6 ms: 1.01x faster                                                |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                |
| python_startup_no_site | 6.96 ms                                                | 6.97 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 23.1 ms: 1.02x faster                                                |
| django_template | 35.2 ms                                                | 34.8 ms: 1.01x faster                                                |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                |
| genshi_xml      | 50.9 ms                                                | 52.2 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| create_gc_cycles          | 2.41 ms                                                | 1.71 ms: 1.41x faster                                                |
| deepcopy                  | 358 us                                                 | 261 us: 1.37x faster                                                 |
| deepcopy_memo             | 39.1 us                                                | 30.8 us: 1.27x faster                                                |
| go                        | 144 ms                                                 | 117 ms: 1.22x faster                                                 |
| deepcopy_reduce           | 3.20 us                                                | 2.67 us: 1.20x faster                                                |
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                 |
| gc_traversal              | 4.37 ms                                                | 3.66 ms: 1.19x faster                                                |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                 |
| async_tree_none           | 351 ms                                                 | 313 ms: 1.12x faster                                                 |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                |
| json                      | 5.36 ms                                                | 4.92 ms: 1.09x faster                                                |
| regex_effbot              | 3.73 ms                                                | 3.53 ms: 1.06x faster                                                |
| richards                  | 48.7 ms                                                | 46.0 ms: 1.06x faster                                                |
| regex_v8                  | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                |
| pycparser                 | 1.20 sec                                               | 1.14 sec: 1.06x faster                                               |
| richards_super            | 54.9 ms                                                | 51.9 ms: 1.06x faster                                                |
| mdp                       | 2.72 sec                                               | 2.58 sec: 1.05x faster                                               |
| thrift                    | 809 us                                                 | 770 us: 1.05x faster                                                 |
| async_tree_none_tg        | 321 ms                                                 | 305 ms: 1.05x faster                                                 |
| crypto_pyaes              | 75.3 ms                                                | 71.8 ms: 1.05x faster                                                |
| 2to3                      | 267 ms                                                 | 255 ms: 1.05x faster                                                 |
| bench_thread_pool         | 822 us                                                 | 789 us: 1.04x faster                                                 |
| generators                | 29.0 ms                                                | 27.9 ms: 1.04x faster                                                |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 559 ms: 1.03x faster                                                 |
| raytrace                  | 267 ms                                                 | 259 ms: 1.03x faster                                                 |
| tomli_loads               | 2.14 sec                                               | 2.08 sec: 1.03x faster                                               |
| pickle_pure_python        | 310 us                                                 | 301 us: 1.03x faster                                                 |
| spectral_norm             | 115 ms                                                 | 112 ms: 1.03x faster                                                 |
| typing_runtime_protocols  | 165 us                                                 | 161 us: 1.02x faster                                                 |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                 |
| xml_etree_process         | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                |
| tornado_http              | 92.4 ms                                                | 90.4 ms: 1.02x faster                                                |
| async_generators          | 436 ms                                                 | 427 ms: 1.02x faster                                                 |
| json_loads                | 27.2 us                                                | 26.7 us: 1.02x faster                                                |
| regex_compile             | 132 ms                                                 | 130 ms: 1.02x faster                                                 |
| float                     | 79.2 ms                                                | 77.7 ms: 1.02x faster                                                |
| genshi_text               | 23.5 ms                                                | 23.1 ms: 1.02x faster                                                |
| html5lib                  | 64.2 ms                                                | 63.0 ms: 1.02x faster                                                |
| sympy_str                 | 275 ms                                                 | 270 ms: 1.02x faster                                                 |
| sympy_integrate           | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                |
| telco                     | 8.54 ms                                                | 8.42 ms: 1.01x faster                                                |
| pprint_safe_repr          | 728 ms                                                 | 718 ms: 1.01x faster                                                 |
| logging_silent            | 102 ns                                                 | 100 ns: 1.01x faster                                                 |
| json_dumps                | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                |
| pprint_pformat            | 1.49 sec                                               | 1.47 sec: 1.01x faster                                               |
| xml_etree_generate        | 86.7 ms                                                | 85.6 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.98 ms: 1.01x faster                                                |
| unpickle_pure_python      | 216 us                                                 | 213 us: 1.01x faster                                                 |
| deltablue                 | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                |
| django_template           | 35.2 ms                                                | 34.8 ms: 1.01x faster                                                |
| xml_etree_parse           | 156 ms                                                 | 154 ms: 1.01x faster                                                 |
| sympy_expand              | 463 ms                                                 | 460 ms: 1.01x faster                                                 |
| regex_dna                 | 218 ms                                                 | 217 ms: 1.01x faster                                                 |
| comprehensions            | 16.5 us                                                | 16.4 us: 1.01x faster                                                |
| meteor_contest            | 109 ms                                                 | 108 ms: 1.01x faster                                                 |
| python_startup_no_site    | 6.96 ms                                                | 6.97 ms: 1.00x slower                                                |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| asyncio_websockets        | 552 ms                                                 | 554 ms: 1.00x slower                                                 |
| scimark_monte_carlo       | 67.4 ms                                                | 67.8 ms: 1.01x slower                                                |
| pyflate                   | 471 ms                                                 | 474 ms: 1.01x slower                                                 |
| mako                      | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                |
| sqlglot_normalize         | 108 ms                                                 | 109 ms: 1.01x slower                                                 |
| hexiom                    | 6.16 ms                                                | 6.22 ms: 1.01x slower                                                |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                |
| nqueens                   | 78.4 ms                                                | 79.3 ms: 1.01x slower                                                |
| scimark_lu                | 113 ms                                                 | 114 ms: 1.01x slower                                                 |
| chaos                     | 58.1 ms                                                | 58.9 ms: 1.01x slower                                                |
| scimark_fft               | 364 ms                                                 | 371 ms: 1.02x slower                                                 |
| bpe_tokeniser             | 4.75 sec                                               | 4.84 sec: 1.02x slower                                               |
| async_tree_io             | 842 ms                                                 | 861 ms: 1.02x slower                                                 |
| docutils                  | 2.59 sec                                               | 2.66 sec: 1.02x slower                                               |
| genshi_xml                | 50.9 ms                                                | 52.2 ms: 1.02x slower                                                |
| xml_etree_iterparse       | 101 ms                                                 | 104 ms: 1.02x slower                                                 |
| scimark_sor               | 124 ms                                                 | 127 ms: 1.02x slower                                                 |
| nbody                     | 87.0 ms                                                | 89.4 ms: 1.03x slower                                                |
| coverage                  | 84.0 ms                                                | 86.5 ms: 1.03x slower                                                |
| coroutines                | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (10): fannkuch, logging_format, sqlglot_optimize, sqlglot_transpile, bench_mp_pool, async_tree_cpu_io_mixed_tg, dulwich_log, logging_simple, async_tree_io_tg, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x