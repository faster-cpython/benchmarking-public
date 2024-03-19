# Results vs. base

- fork: faster-cpython
- ref: optimizer_trim_trace
- machine: linux-x86_64
- commit hash: f012ce0
- commit date: 2024-03-19
- overall geometric mean: 1.00x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 300 ms                                                                 | 299 ms: 1.00x faster                                                             |
| chameleon      | 7.04 ms                                                                | 7.35 ms: 1.04x slower                                                            |
| docutils       | 2.86 sec                                                               | 2.92 sec: 1.02x slower                                                           |
| html5lib       | 70.3 ms                                                                | 68.9 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io      | 1.24 sec                                                               | 1.25 sec: 1.01x slower                                                           |
| async_tree_io_tg   | 1.25 sec                                                               | 1.27 sec: 1.01x slower                                                           |
| async_tree_none_tg | 471 ms                                                                 | 476 ms: 1.01x slower                                                             |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 96.9 ms                                                                | 97.7 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 180 ms                                                                 | 178 ms: 1.01x faster                                                             |
| regex_v8       | 25.4 ms                                                                | 25.2 ms: 1.01x faster                                                            |
| regex_dna      | 225 ms                                                                 | 227 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_list       | 5.22 us                                                                | 5.07 us: 1.03x faster                                                            |
| json_loads          | 28.5 us                                                                | 27.9 us: 1.02x faster                                                            |
| pickle_pure_python  | 313 us                                                                 | 309 us: 1.01x faster                                                             |
| tomli_loads         | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                                           |
| xml_etree_process   | 63.8 ms                                                                | 63.5 ms: 1.01x faster                                                            |
| json_dumps          | 10.6 ms                                                                | 10.7 ms: 1.01x slower                                                            |
| xml_etree_iterparse | 112 ms                                                                 | 113 ms: 1.01x slower                                                             |
| pickle              | 11.5 us                                                                | 11.6 us: 1.01x slower                                                            |
| pickle_dict         | 34.3 us                                                                | 35.6 us: 1.04x slower                                                            |
| pickle_list         | 4.96 us                                                                | 5.19 us: 1.05x slower                                                            |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_generate, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 9.05 ms                                                                | 9.08 ms: 1.00x slower                                                            |
| python_startup         | 10.5 ms                                                                | 10.5 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 28.2 ms                                                                | 27.5 ms: 1.03x faster                                                            |
| mako            | 13.5 ms                                                                | 13.7 ms: 1.01x slower                                                            |
| django_template | 35.1 ms                                                                | 37.6 ms: 1.07x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 6.32 ms                                                                | 6.07 ms: 1.04x faster                                                            |
| scimark_sor             | 148 ms                                                                 | 144 ms: 1.03x faster                                                             |
| unpickle_list           | 5.22 us                                                                | 5.07 us: 1.03x faster                                                            |
| coroutines              | 23.3 ms                                                                | 22.7 ms: 1.03x faster                                                            |
| genshi_text             | 28.2 ms                                                                | 27.5 ms: 1.03x faster                                                            |
| pycparser               | 1.34 sec                                                               | 1.31 sec: 1.02x faster                                                           |
| scimark_fft             | 447 ms                                                                 | 437 ms: 1.02x faster                                                             |
| html5lib                | 70.3 ms                                                                | 68.9 ms: 1.02x faster                                                            |
| chaos                   | 77.2 ms                                                                | 75.7 ms: 1.02x faster                                                            |
| logging_silent          | 107 ns                                                                 | 105 ns: 1.02x faster                                                             |
| richards_super          | 63.1 ms                                                                | 62.0 ms: 1.02x faster                                                            |
| json_loads              | 28.5 us                                                                | 27.9 us: 1.02x faster                                                            |
| generators              | 30.1 ms                                                                | 29.6 ms: 1.02x faster                                                            |
| deepcopy_memo           | 42.9 us                                                                | 42.2 us: 1.01x faster                                                            |
| meteor_contest          | 121 ms                                                                 | 119 ms: 1.01x faster                                                             |
| pickle_pure_python      | 313 us                                                                 | 309 us: 1.01x faster                                                             |
| regex_compile           | 180 ms                                                                 | 178 ms: 1.01x faster                                                             |
| spectral_norm           | 142 ms                                                                 | 140 ms: 1.01x faster                                                             |
| raytrace                | 348 ms                                                                 | 345 ms: 1.01x faster                                                             |
| tomli_loads             | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                                           |
| deltablue               | 3.89 ms                                                                | 3.86 ms: 1.01x faster                                                            |
| telco                   | 8.91 ms                                                                | 8.85 ms: 1.01x faster                                                            |
| regex_v8                | 25.4 ms                                                                | 25.2 ms: 1.01x faster                                                            |
| sqlglot_transpile       | 1.80 ms                                                                | 1.79 ms: 1.01x faster                                                            |
| xml_etree_process       | 63.8 ms                                                                | 63.5 ms: 1.01x faster                                                            |
| sqlglot_parse           | 1.45 ms                                                                | 1.45 ms: 1.00x faster                                                            |
| richards                | 56.0 ms                                                                | 55.7 ms: 1.00x faster                                                            |
| 2to3                    | 300 ms                                                                 | 299 ms: 1.00x faster                                                             |
| asyncio_tcp_ssl         | 1.86 sec                                                               | 1.86 sec: 1.00x slower                                                           |
| python_startup_no_site  | 9.05 ms                                                                | 9.08 ms: 1.00x slower                                                            |
| python_startup          | 10.5 ms                                                                | 10.5 ms: 1.00x slower                                                            |
| go                      | 179 ms                                                                 | 180 ms: 1.00x slower                                                             |
| hexiom                  | 9.24 ms                                                                | 9.27 ms: 1.00x slower                                                            |
| sqlite_synth            | 2.94 us                                                                | 2.96 us: 1.00x slower                                                            |
| async_tree_io           | 1.24 sec                                                               | 1.25 sec: 1.01x slower                                                           |
| async_generators        | 474 ms                                                                 | 477 ms: 1.01x slower                                                             |
| regex_dna               | 225 ms                                                                 | 227 ms: 1.01x slower                                                             |
| sympy_expand            | 513 ms                                                                 | 517 ms: 1.01x slower                                                             |
| json_dumps              | 10.6 ms                                                                | 10.7 ms: 1.01x slower                                                            |
| fannkuch                | 478 ms                                                                 | 481 ms: 1.01x slower                                                             |
| float                   | 96.9 ms                                                                | 97.7 ms: 1.01x slower                                                            |
| xml_etree_iterparse     | 112 ms                                                                 | 113 ms: 1.01x slower                                                             |
| pickle                  | 11.5 us                                                                | 11.6 us: 1.01x slower                                                            |
| async_tree_io_tg        | 1.25 sec                                                               | 1.27 sec: 1.01x slower                                                           |
| sympy_sum               | 168 ms                                                                 | 170 ms: 1.01x slower                                                             |
| nqueens                 | 102 ms                                                                 | 103 ms: 1.01x slower                                                             |
| mako                    | 13.5 ms                                                                | 13.7 ms: 1.01x slower                                                            |
| async_tree_none_tg      | 471 ms                                                                 | 476 ms: 1.01x slower                                                             |
| create_gc_cycles        | 1.54 ms                                                                | 1.56 ms: 1.01x slower                                                            |
| thrift                  | 814 us                                                                 | 824 us: 1.01x slower                                                             |
| pprint_safe_repr        | 888 ms                                                                 | 901 ms: 1.01x slower                                                             |
| pprint_pformat          | 1.85 sec                                                               | 1.89 sec: 1.02x slower                                                           |
| docutils                | 2.86 sec                                                               | 2.92 sec: 1.02x slower                                                           |
| logging_simple          | 6.30 us                                                                | 6.45 us: 1.02x slower                                                            |
| scimark_monte_carlo     | 87.0 ms                                                                | 89.3 ms: 1.03x slower                                                            |
| logging_format          | 7.06 us                                                                | 7.26 us: 1.03x slower                                                            |
| deepcopy_reduce         | 3.21 us                                                                | 3.30 us: 1.03x slower                                                            |
| asyncio_tcp             | 494 ms                                                                 | 510 ms: 1.03x slower                                                             |
| sympy_integrate         | 21.6 ms                                                                | 22.3 ms: 1.03x slower                                                            |
| scimark_lu              | 162 ms                                                                 | 168 ms: 1.03x slower                                                             |
| comprehensions          | 21.8 us                                                                | 22.6 us: 1.04x slower                                                            |
| pickle_dict             | 34.3 us                                                                | 35.6 us: 1.04x slower                                                            |
| pathlib                 | 19.0 ms                                                                | 19.8 ms: 1.04x slower                                                            |
| gc_traversal            | 3.81 ms                                                                | 3.96 ms: 1.04x slower                                                            |
| chameleon               | 7.04 ms                                                                | 7.35 ms: 1.04x slower                                                            |
| pickle_list             | 4.96 us                                                                | 5.19 us: 1.05x slower                                                            |
| sqlglot_normalize       | 115 ms                                                                 | 120 ms: 1.05x slower                                                             |
| django_template         | 35.1 ms                                                                | 37.6 ms: 1.07x slower                                                            |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (34): json, typing_runtime_protocols, aiohttp, unpack_sequence, genshi_xml, crypto_pyaes, bench_thread_pool, mdp, deepcopy, pidigits, bench_mp_pool, unpickle_pure_python, asyncio_websockets, xml_etree_generate, async_tree_memoization_tg, nbody, sqlglot_optimize, gunicorn, dulwich_log, async_tree_memoization, pyflate, async_tree_cpu_io_mixed, coverage, sympy_str, tornado_http, async_tree_cpu_io_mixed_tg, xml_etree_parse, dask, regex_effbot, mypy2, async_tree_none, pylint, unpickle, djangocms


# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.01x