# Results vs. base

- fork: faster-cpython
- ref: exponential_backoff_
- machine: linux-x86_64
- commit hash: bdf272d
- commit date: 2024-03-19
- overall geometric mean: 1.00x faster
- HPT reliability: 96.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| chameleon      | 7.04 ms                                                                | 7.14 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io      | 1.24 sec                                                               | 1.23 sec: 1.01x faster                                                           |
| async_tree_none_tg | 471 ms                                                                 | 472 ms: 1.00x slower                                                             |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 125 ms                                                                 | 121 ms: 1.03x faster                                                             |
| float          | 96.9 ms                                                                | 93.9 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 25.4 ms                                                                | 24.5 ms: 1.04x faster                                                            |
| regex_compile  | 180 ms                                                                 | 175 ms: 1.03x faster                                                             |
| regex_dna      | 225 ms                                                                 | 219 ms: 1.03x faster                                                             |
| regex_effbot   | 3.65 ms                                                                | 3.56 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_list       | 5.22 us                                                                | 4.94 us: 1.06x faster                                                            |
| pickle_dict         | 34.3 us                                                                | 33.6 us: 1.02x faster                                                            |
| tomli_loads         | 2.50 sec                                                               | 2.46 sec: 1.02x faster                                                           |
| xml_etree_process   | 63.8 ms                                                                | 63.6 ms: 1.00x faster                                                            |
| json_dumps          | 10.6 ms                                                                | 10.7 ms: 1.01x slower                                                            |
| xml_etree_iterparse | 112 ms                                                                 | 113 ms: 1.01x slower                                                             |
| pickle_list         | 4.96 us                                                                | 5.02 us: 1.01x slower                                                            |
| pickle              | 11.5 us                                                                | 11.7 us: 1.01x slower                                                            |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (6): json_loads, unpickle, unpickle_pure_python, xml_etree_generate, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                                | 10.5 ms: 1.00x slower                                                            |
| python_startup_no_site | 9.05 ms                                                                | 9.07 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 64.1 ms                                                                | 62.4 ms: 1.03x faster                                                            |
| mako            | 13.5 ms                                                                | 13.2 ms: 1.02x faster                                                            |
| genshi_text     | 28.2 ms                                                                | 27.7 ms: 1.02x faster                                                            |
| django_template | 35.1 ms                                                                | 35.0 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5+-0f27801 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_list            | 5.22 us                                                                | 4.94 us: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 6.32 ms                                                                | 5.99 ms: 1.06x faster                                                            |
| go                       | 179 ms                                                                 | 172 ms: 1.04x faster                                                             |
| regex_v8                 | 25.4 ms                                                                | 24.5 ms: 1.04x faster                                                            |
| pycparser                | 1.34 sec                                                               | 1.30 sec: 1.04x faster                                                           |
| hexiom                   | 9.24 ms                                                                | 8.92 ms: 1.04x faster                                                            |
| nbody                    | 125 ms                                                                 | 121 ms: 1.03x faster                                                             |
| float                    | 96.9 ms                                                                | 93.9 ms: 1.03x faster                                                            |
| typing_runtime_protocols | 119 us                                                                 | 115 us: 1.03x faster                                                             |
| regex_compile            | 180 ms                                                                 | 175 ms: 1.03x faster                                                             |
| regex_dna                | 225 ms                                                                 | 219 ms: 1.03x faster                                                             |
| genshi_xml               | 64.1 ms                                                                | 62.4 ms: 1.03x faster                                                            |
| regex_effbot             | 3.65 ms                                                                | 3.56 ms: 1.03x faster                                                            |
| mako                     | 13.5 ms                                                                | 13.2 ms: 1.02x faster                                                            |
| pickle_dict              | 34.3 us                                                                | 33.6 us: 1.02x faster                                                            |
| nqueens                  | 102 ms                                                                 | 100 ms: 1.02x faster                                                             |
| comprehensions           | 21.8 us                                                                | 21.3 us: 1.02x faster                                                            |
| logging_silent           | 107 ns                                                                 | 105 ns: 1.02x faster                                                             |
| genshi_text              | 28.2 ms                                                                | 27.7 ms: 1.02x faster                                                            |
| coroutines               | 23.3 ms                                                                | 22.9 ms: 1.02x faster                                                            |
| deltablue                | 3.89 ms                                                                | 3.83 ms: 1.02x faster                                                            |
| meteor_contest           | 121 ms                                                                 | 119 ms: 1.02x faster                                                             |
| tomli_loads              | 2.50 sec                                                               | 2.46 sec: 1.02x faster                                                           |
| chaos                    | 77.2 ms                                                                | 76.1 ms: 1.02x faster                                                            |
| richards_super           | 63.1 ms                                                                | 62.3 ms: 1.01x faster                                                            |
| aiohttp                  | 1.23 ms                                                                | 1.21 ms: 1.01x faster                                                            |
| sqlglot_parse            | 1.45 ms                                                                | 1.44 ms: 1.01x faster                                                            |
| generators               | 30.1 ms                                                                | 29.8 ms: 1.01x faster                                                            |
| async_tree_io            | 1.24 sec                                                               | 1.23 sec: 1.01x faster                                                           |
| sqlglot_transpile        | 1.80 ms                                                                | 1.79 ms: 1.01x faster                                                            |
| gunicorn                 | 1.31 ms                                                                | 1.30 ms: 1.01x faster                                                            |
| scimark_fft              | 447 ms                                                                 | 444 ms: 1.01x faster                                                             |
| django_template          | 35.1 ms                                                                | 35.0 ms: 1.01x faster                                                            |
| sympy_integrate          | 21.6 ms                                                                | 21.5 ms: 1.00x faster                                                            |
| raytrace                 | 348 ms                                                                 | 346 ms: 1.00x faster                                                             |
| xml_etree_process        | 63.8 ms                                                                | 63.6 ms: 1.00x faster                                                            |
| pprint_pformat           | 1.85 sec                                                               | 1.85 sec: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 1.86 sec                                                               | 1.85 sec: 1.00x faster                                                           |
| python_startup           | 10.5 ms                                                                | 10.5 ms: 1.00x slower                                                            |
| sqlglot_optimize         | 61.1 ms                                                                | 61.2 ms: 1.00x slower                                                            |
| async_tree_none_tg       | 471 ms                                                                 | 472 ms: 1.00x slower                                                             |
| python_startup_no_site   | 9.05 ms                                                                | 9.07 ms: 1.00x slower                                                            |
| async_generators         | 474 ms                                                                 | 476 ms: 1.00x slower                                                             |
| sympy_expand             | 513 ms                                                                 | 516 ms: 1.00x slower                                                             |
| json_dumps               | 10.6 ms                                                                | 10.7 ms: 1.01x slower                                                            |
| scimark_sor              | 148 ms                                                                 | 149 ms: 1.01x slower                                                             |
| xml_etree_iterparse      | 112 ms                                                                 | 113 ms: 1.01x slower                                                             |
| scimark_monte_carlo      | 87.0 ms                                                                | 87.6 ms: 1.01x slower                                                            |
| deepcopy_memo            | 42.9 us                                                                | 43.2 us: 1.01x slower                                                            |
| pickle_list              | 4.96 us                                                                | 5.02 us: 1.01x slower                                                            |
| json                     | 5.23 ms                                                                | 5.29 ms: 1.01x slower                                                            |
| telco                    | 8.91 ms                                                                | 9.02 ms: 1.01x slower                                                            |
| thrift                   | 814 us                                                                 | 825 us: 1.01x slower                                                             |
| logging_simple           | 6.30 us                                                                | 6.38 us: 1.01x slower                                                            |
| pickle                   | 11.5 us                                                                | 11.7 us: 1.01x slower                                                            |
| chameleon                | 7.04 ms                                                                | 7.14 ms: 1.01x slower                                                            |
| asyncio_tcp              | 494 ms                                                                 | 508 ms: 1.03x slower                                                             |
| gc_traversal             | 3.81 ms                                                                | 3.91 ms: 1.03x slower                                                            |
| coverage                 | 96.6 ms                                                                | 99.2 ms: 1.03x slower                                                            |
| pathlib                  | 19.0 ms                                                                | 19.7 ms: 1.04x slower                                                            |
| unpack_sequence          | 53.2 ns                                                                | 58.9 ns: 1.11x slower                                                            |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (41): html5lib, tornado_http, json_loads, unpickle, async_tree_memoization_tg, sympy_str, sqlglot_normalize, bench_mp_pool, unpickle_pure_python, sympy_sum, deepcopy_reduce, pylint, xml_etree_generate, mdp, async_tree_io_tg, pprint_safe_repr, scimark_lu, dulwich_log, pidigits, 2to3, async_tree_memoization, mypy2, deepcopy, bench_thread_pool, docutils, asyncio_websockets, pickle_pure_python, spectral_norm, dask, create_gc_cycles, sqlite_synth, richards, logging_format, async_tree_cpu_io_mixed, djangocms, async_tree_none, crypto_pyaes, pyflate, xml_etree_parse, async_tree_cpu_io_mixed_tg, fannkuch


# HPT report

- Reliability score: 96.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.02x