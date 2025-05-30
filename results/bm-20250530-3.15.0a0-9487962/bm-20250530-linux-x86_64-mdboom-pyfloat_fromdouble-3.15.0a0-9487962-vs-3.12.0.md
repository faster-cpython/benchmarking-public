# Results vs. 3.12.0

- fork: mdboom
- ref: pyfloat_fromdouble
- machine: linux-x86_64
- commit hash: 9487962
- commit date: 2025-05-30
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.3 ms: 1.19x faster                                               |
| nbody          | 97.0 ms                                                | 95.8 ms: 1.01x faster                                               |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.40 ms: 1.06x faster                                               |
| regex_v8       | 23.1 ms                                                | 23.6 ms: 1.02x slower                                               |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                               |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                               |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                |
| json_loads           | 28.5 us                                                | 29.3 us: 1.03x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                               |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 33.0 ms: 1.05x faster                                               |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                              |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                               |
| comprehensions             | 21.8 us                                                | 15.9 us: 1.37x faster                                               |
| go                         | 139 ms                                                 | 110 ms: 1.27x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                               |
| float                      | 84.7 ms                                                | 71.3 ms: 1.19x faster                                               |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                               |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 18.8 ms: 1.14x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.12x faster                                               |
| pyflate                    | 482 ms                                                 | 430 ms: 1.12x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                               |
| chaos                      | 67.0 ms                                                | 61.2 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 75.6 ms: 1.08x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.44 ms: 1.08x faster                                               |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.08x faster                                                |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                              |
| richards                   | 45.8 ms                                                | 42.7 ms: 1.07x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.04 ms: 1.06x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.40 ms: 1.06x faster                                               |
| richards_super             | 51.5 ms                                                | 48.5 ms: 1.06x faster                                               |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                |
| django_template            | 34.6 ms                                                | 33.0 ms: 1.05x faster                                               |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                               |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                               |
| logging_simple             | 6.46 us                                                | 6.21 us: 1.04x faster                                               |
| logging_format             | 7.23 us                                                | 6.97 us: 1.04x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                               |
| scimark_fft                | 382 ms                                                 | 371 ms: 1.03x faster                                                |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.0 ms: 1.02x faster                                               |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                |
| nbody                      | 97.0 ms                                                | 95.8 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                               |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                |
| regex_v8                   | 23.1 ms                                                | 23.6 ms: 1.02x slower                                               |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.02x slower                                               |
| json_loads                 | 28.5 us                                                | 29.3 us: 1.03x slower                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.20 ms: 1.03x slower                                               |
| pprint_safe_repr           | 776 ms                                                 | 810 ms: 1.04x slower                                                |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                |
| pprint_pformat             | 1.57 sec                                               | 1.65 sec: 1.05x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.9 ms: 1.08x slower                                               |
| telco                      | 7.10 ms                                                | 8.07 ms: 1.14x slower                                               |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| gc_traversal               | 3.79 ms                                                | 5.06 ms: 1.33x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                               |
| logging_silent             | 104 ns                                                 | 470 ns: 4.50x slower                                                |
| coverage                   | 72.7 ms                                                | 418 ms: 5.75x slower                                                |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (2): json, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250530-3.15.0a0-9487962/bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x