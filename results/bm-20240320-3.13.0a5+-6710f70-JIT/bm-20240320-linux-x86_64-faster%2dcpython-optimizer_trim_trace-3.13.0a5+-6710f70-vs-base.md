# Results vs. base

- fork: faster-cpython
- ref: optimizer_trim_trace
- machine: linux-x86_64
- commit hash: 6710f70
- commit date: 2024-03-20
- overall geometric mean: 1.01x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                 | 282 ms: 1.00x slower                                                             |
| chameleon      | 6.93 ms                                                                | 7.06 ms: 1.02x slower                                                            |
| docutils       | 2.76 sec                                                               | 2.80 sec: 1.01x slower                                                           |
| html5lib       | 67.5 ms                                                                | 65.9 ms: 1.02x faster                                                            |
| tornado_http   | 101 ms                                                                 | 98.8 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io             | 1.22 sec                                                               | 1.22 sec: 1.00x slower                                                           |
| async_tree_none_tg        | 457 ms                                                                 | 460 ms: 1.01x slower                                                             |
| async_tree_io_tg          | 1.22 sec                                                               | 1.24 sec: 1.02x slower                                                           |
| async_tree_memoization_tg | 584 ms                                                                 | 599 ms: 1.03x slower                                                             |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 92.5 ms                                                                | 94.6 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 230 ms                                                                 | 230 ms: 1.00x slower                                                             |
| regex_compile  | 143 ms                                                                 | 145 ms: 1.02x slower                                                             |
| regex_effbot   | 3.60 ms                                                                | 3.81 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 313 us                                                                 | 304 us: 1.03x faster                                                             |
| pickle_list          | 5.01 us                                                                | 4.95 us: 1.01x faster                                                            |
| xml_etree_process    | 60.8 ms                                                                | 60.1 ms: 1.01x faster                                                            |
| xml_etree_generate   | 87.9 ms                                                                | 87.2 ms: 1.01x faster                                                            |
| unpickle_pure_python | 241 us                                                                 | 239 us: 1.01x faster                                                             |
| json_dumps           | 10.4 ms                                                                | 10.5 ms: 1.01x slower                                                            |
| pickle_dict          | 34.0 us                                                                | 34.4 us: 1.01x slower                                                            |
| json_loads           | 28.0 us                                                                | 28.4 us: 1.01x slower                                                            |
| unpickle_list        | 4.88 us                                                                | 5.19 us: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (5): xml_etree_parse, tomli_loads, xml_etree_iterparse, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                                | 12.6 ms: 1.00x faster                                                            |
| python_startup_no_site | 11.2 ms                                                                | 11.1 ms: 1.00x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 55.7 ms                                                                | 55.1 ms: 1.01x faster                                                            |
| django_template | 34.8 ms                                                                | 35.2 ms: 1.01x slower                                                            |
| mako            | 10.9 ms                                                                | 11.0 ms: 1.01x slower                                                            |
| genshi_text     | 24.3 ms                                                                | 24.6 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                       | 2.79 sec                                                               | 2.68 sec: 1.04x faster                                                           |
| pickle_pure_python        | 313 us                                                                 | 304 us: 1.03x faster                                                             |
| go                        | 158 ms                                                                 | 154 ms: 1.03x faster                                                             |
| html5lib                  | 67.5 ms                                                                | 65.9 ms: 1.02x faster                                                            |
| tornado_http              | 101 ms                                                                 | 98.8 ms: 1.02x faster                                                            |
| richards_super            | 52.8 ms                                                                | 52.1 ms: 1.01x faster                                                            |
| raytrace                  | 297 ms                                                                 | 293 ms: 1.01x faster                                                             |
| pickle_list               | 5.01 us                                                                | 4.95 us: 1.01x faster                                                            |
| nqueens                   | 90.4 ms                                                                | 89.3 ms: 1.01x faster                                                            |
| deltablue                 | 3.47 ms                                                                | 3.43 ms: 1.01x faster                                                            |
| xml_etree_process         | 60.8 ms                                                                | 60.1 ms: 1.01x faster                                                            |
| deepcopy_memo             | 39.1 us                                                                | 38.6 us: 1.01x faster                                                            |
| genshi_xml                | 55.7 ms                                                                | 55.1 ms: 1.01x faster                                                            |
| richards                  | 46.5 ms                                                                | 46.0 ms: 1.01x faster                                                            |
| typing_runtime_protocols  | 113 us                                                                 | 112 us: 1.01x faster                                                             |
| xml_etree_generate        | 87.9 ms                                                                | 87.2 ms: 1.01x faster                                                            |
| unpickle_pure_python      | 241 us                                                                 | 239 us: 1.01x faster                                                             |
| pathlib                   | 18.8 ms                                                                | 18.6 ms: 1.01x faster                                                            |
| meteor_contest            | 110 ms                                                                 | 110 ms: 1.01x faster                                                             |
| bench_thread_pool         | 857 us                                                                 | 853 us: 1.01x faster                                                             |
| coroutines                | 23.1 ms                                                                | 23.0 ms: 1.00x faster                                                            |
| deepcopy                  | 350 us                                                                 | 349 us: 1.00x faster                                                             |
| python_startup            | 12.6 ms                                                                | 12.6 ms: 1.00x faster                                                            |
| python_startup_no_site    | 11.2 ms                                                                | 11.1 ms: 1.00x faster                                                            |
| regex_dna                 | 230 ms                                                                 | 230 ms: 1.00x slower                                                             |
| asyncio_tcp_ssl           | 1.85 sec                                                               | 1.85 sec: 1.00x slower                                                           |
| 2to3                      | 282 ms                                                                 | 282 ms: 1.00x slower                                                             |
| async_tree_io             | 1.22 sec                                                               | 1.22 sec: 1.00x slower                                                           |
| aiohttp                   | 1.20 ms                                                                | 1.20 ms: 1.00x slower                                                            |
| sympy_expand              | 483 ms                                                                 | 485 ms: 1.01x slower                                                             |
| logging_silent            | 100 ns                                                                 | 101 ns: 1.01x slower                                                             |
| sqlglot_normalize         | 109 ms                                                                 | 110 ms: 1.01x slower                                                             |
| async_tree_none_tg        | 457 ms                                                                 | 460 ms: 1.01x slower                                                             |
| generators                | 29.4 ms                                                                | 29.6 ms: 1.01x slower                                                            |
| sympy_str                 | 285 ms                                                                 | 288 ms: 1.01x slower                                                             |
| pyflate                   | 483 ms                                                                 | 488 ms: 1.01x slower                                                             |
| scimark_monte_carlo       | 70.3 ms                                                                | 70.9 ms: 1.01x slower                                                            |
| sqlite_synth              | 2.84 us                                                                | 2.87 us: 1.01x slower                                                            |
| django_template           | 34.8 ms                                                                | 35.2 ms: 1.01x slower                                                            |
| mako                      | 10.9 ms                                                                | 11.0 ms: 1.01x slower                                                            |
| json_dumps                | 10.4 ms                                                                | 10.5 ms: 1.01x slower                                                            |
| fannkuch                  | 393 ms                                                                 | 398 ms: 1.01x slower                                                             |
| pickle_dict               | 34.0 us                                                                | 34.4 us: 1.01x slower                                                            |
| sympy_sum                 | 161 ms                                                                 | 163 ms: 1.01x slower                                                             |
| genshi_text               | 24.3 ms                                                                | 24.6 ms: 1.01x slower                                                            |
| docutils                  | 2.76 sec                                                               | 2.80 sec: 1.01x slower                                                           |
| coverage                  | 96.6 ms                                                                | 98.0 ms: 1.01x slower                                                            |
| deepcopy_reduce           | 3.09 us                                                                | 3.13 us: 1.01x slower                                                            |
| json_loads                | 28.0 us                                                                | 28.4 us: 1.01x slower                                                            |
| asyncio_tcp               | 507 ms                                                                 | 515 ms: 1.02x slower                                                             |
| async_tree_io_tg          | 1.22 sec                                                               | 1.24 sec: 1.02x slower                                                           |
| spectral_norm             | 113 ms                                                                 | 115 ms: 1.02x slower                                                             |
| telco                     | 8.27 ms                                                                | 8.41 ms: 1.02x slower                                                            |
| comprehensions            | 17.5 us                                                                | 17.8 us: 1.02x slower                                                            |
| chameleon                 | 6.93 ms                                                                | 7.06 ms: 1.02x slower                                                            |
| pprint_safe_repr          | 748 ms                                                                 | 762 ms: 1.02x slower                                                             |
| regex_compile             | 143 ms                                                                 | 145 ms: 1.02x slower                                                             |
| async_generators          | 459 ms                                                                 | 469 ms: 1.02x slower                                                             |
| thrift                    | 808 us                                                                 | 827 us: 1.02x slower                                                             |
| nbody                     | 92.5 ms                                                                | 94.6 ms: 1.02x slower                                                            |
| sympy_integrate           | 21.3 ms                                                                | 21.8 ms: 1.02x slower                                                            |
| async_tree_memoization_tg | 584 ms                                                                 | 599 ms: 1.03x slower                                                             |
| scimark_fft               | 336 ms                                                                 | 345 ms: 1.03x slower                                                             |
| djangocms                 | 31.3 us                                                                | 32.4 us: 1.03x slower                                                            |
| gc_traversal              | 3.92 ms                                                                | 4.08 ms: 1.04x slower                                                            |
| regex_effbot              | 3.60 ms                                                                | 3.81 ms: 1.06x slower                                                            |
| scimark_sparse_mat_mult   | 4.79 ms                                                                | 5.07 ms: 1.06x slower                                                            |
| unpack_sequence           | 87.6 ns                                                                | 92.9 ns: 1.06x slower                                                            |
| unpickle_list             | 4.88 us                                                                | 5.19 us: 1.06x slower                                                            |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (33): chaos, scimark_sor, xml_etree_parse, logging_simple, dask, tomli_loads, bench_mp_pool, crypto_pyaes, sqlglot_parse, hexiom, json, float, dulwich_log, logging_format, asyncio_websockets, pycparser, sqlglot_optimize, pidigits, create_gc_cycles, sqlglot_transpile, regex_v8, gunicorn, xml_etree_iterparse, pickle, scimark_lu, pylint, mypy2, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, pprint_pformat, async_tree_none, unpickle


# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.01x