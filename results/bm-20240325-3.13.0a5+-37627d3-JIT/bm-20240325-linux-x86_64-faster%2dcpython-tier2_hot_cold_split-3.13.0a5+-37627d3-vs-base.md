# Results vs. base

- fork: faster-cpython
- ref: tier2_hot_cold_split
- machine: linux-x86_64
- commit hash: 37627d3
- commit date: 2024-03-25
- overall geometric mean: 1.00x faster
- HPT reliability: 66.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5+-507896d | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 278 ms: 1.01x faster                                                             |
| chameleon      | 7.09 ms                                                                | 7.14 ms: 1.01x slower                                                            |
| docutils       | 2.87 sec                                                               | 2.88 sec: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5+-507896d | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 92.5 ms                                                                | 91.1 ms: 1.02x faster                                                            |
| pidigits       | 189 ms                                                                 | 190 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5+-507896d | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.64 ms                                                                | 3.53 ms: 1.03x faster                                                            |
| regex_dna      | 225 ms                                                                 | 218 ms: 1.03x faster                                                             |
| regex_v8       | 25.0 ms                                                                | 24.2 ms: 1.03x faster                                                            |
| regex_compile  | 144 ms                                                                 | 146 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5+-507896d | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_list      | 5.26 us                                                                | 5.08 us: 1.04x faster                                                            |
| tomli_loads        | 2.10 sec                                                               | 2.07 sec: 1.01x faster                                                           |
| xml_etree_parse    | 162 ms                                                                 | 160 ms: 1.01x faster                                                             |
| json_loads         | 28.4 us                                                                | 28.6 us: 1.00x slower                                                            |
| pickle_pure_python | 306 us                                                                 | 310 us: 1.01x slower                                                             |
| json_dumps         | 10.3 ms                                                                | 10.5 ms: 1.02x slower                                                            |
| pickle             | 11.5 us                                                                | 11.8 us: 1.02x slower                                                            |
| pickle_dict        | 33.9 us                                                                | 34.8 us: 1.03x slower                                                            |
| pickle_list        | 4.89 us                                                                | 5.13 us: 1.05x slower                                                            |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (5): unpickle, xml_etree_iterparse, xml_etree_process, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5+-507896d | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 10.1 ms                                                                | 9.44 ms: 1.07x faster                                                            |
| python_startup         | 11.7 ms                                                                | 11.0 ms: 1.06x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5+-507896d | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 25.1 ms                                                                | 24.4 ms: 1.03x faster                                                            |
| mako            | 11.0 ms                                                                | 10.8 ms: 1.02x faster                                                            |
| genshi_xml      | 55.0 ms                                                                | 54.0 ms: 1.02x faster                                                            |
| django_template | 35.9 ms                                                                | 36.2 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5+-507896d | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 5.03 ms                                                                | 4.69 ms: 1.07x faster                                                            |
| python_startup_no_site   | 10.1 ms                                                                | 9.44 ms: 1.07x faster                                                            |
| python_startup           | 11.7 ms                                                                | 11.0 ms: 1.06x faster                                                            |
| unpickle_list            | 5.26 us                                                                | 5.08 us: 1.04x faster                                                            |
| regex_effbot             | 3.64 ms                                                                | 3.53 ms: 1.03x faster                                                            |
| regex_dna                | 225 ms                                                                 | 218 ms: 1.03x faster                                                             |
| regex_v8                 | 25.0 ms                                                                | 24.2 ms: 1.03x faster                                                            |
| logging_silent           | 102 ns                                                                 | 99.3 ns: 1.03x faster                                                            |
| genshi_text              | 25.1 ms                                                                | 24.4 ms: 1.03x faster                                                            |
| crypto_pyaes             | 76.1 ms                                                                | 74.1 ms: 1.03x faster                                                            |
| pyflate                  | 493 ms                                                                 | 481 ms: 1.03x faster                                                             |
| richards                 | 46.8 ms                                                                | 45.7 ms: 1.02x faster                                                            |
| pycparser                | 1.21 sec                                                               | 1.18 sec: 1.02x faster                                                           |
| mako                     | 11.0 ms                                                                | 10.8 ms: 1.02x faster                                                            |
| richards_super           | 53.2 ms                                                                | 52.0 ms: 1.02x faster                                                            |
| genshi_xml               | 55.0 ms                                                                | 54.0 ms: 1.02x faster                                                            |
| nbody                    | 92.5 ms                                                                | 91.1 ms: 1.02x faster                                                            |
| pprint_pformat           | 1.56 sec                                                               | 1.53 sec: 1.02x faster                                                           |
| tomli_loads              | 2.10 sec                                                               | 2.07 sec: 1.01x faster                                                           |
| coroutines               | 23.2 ms                                                                | 22.8 ms: 1.01x faster                                                            |
| typing_runtime_protocols | 113 us                                                                 | 112 us: 1.01x faster                                                             |
| scimark_sor              | 138 ms                                                                 | 136 ms: 1.01x faster                                                             |
| xml_etree_parse          | 162 ms                                                                 | 160 ms: 1.01x faster                                                             |
| scimark_fft              | 343 ms                                                                 | 339 ms: 1.01x faster                                                             |
| djangocms                | 31.6 us                                                                | 31.3 us: 1.01x faster                                                            |
| unpack_sequence          | 93.0 ns                                                                | 92.1 ns: 1.01x faster                                                            |
| coverage                 | 97.6 ms                                                                | 96.7 ms: 1.01x faster                                                            |
| go                       | 156 ms                                                                 | 155 ms: 1.01x faster                                                             |
| 2to3                     | 280 ms                                                                 | 278 ms: 1.01x faster                                                             |
| scimark_monte_carlo      | 70.6 ms                                                                | 70.0 ms: 1.01x faster                                                            |
| raytrace                 | 294 ms                                                                 | 292 ms: 1.01x faster                                                             |
| logging_simple           | 5.94 us                                                                | 5.90 us: 1.01x faster                                                            |
| fannkuch                 | 393 ms                                                                 | 391 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl          | 1.85 sec                                                               | 1.86 sec: 1.00x slower                                                           |
| create_gc_cycles         | 1.47 ms                                                                | 1.47 ms: 1.00x slower                                                            |
| bench_thread_pool        | 856 us                                                                 | 859 us: 1.00x slower                                                             |
| docutils                 | 2.87 sec                                                               | 2.88 sec: 1.00x slower                                                           |
| pidigits                 | 189 ms                                                                 | 190 ms: 1.00x slower                                                             |
| asyncio_websockets       | 568 ms                                                                 | 570 ms: 1.00x slower                                                             |
| sqlglot_normalize        | 113 ms                                                                 | 113 ms: 1.00x slower                                                             |
| json_loads               | 28.4 us                                                                | 28.6 us: 1.00x slower                                                            |
| django_template          | 35.9 ms                                                                | 36.2 ms: 1.01x slower                                                            |
| spectral_norm            | 115 ms                                                                 | 116 ms: 1.01x slower                                                             |
| sqlglot_transpile        | 1.65 ms                                                                | 1.66 ms: 1.01x slower                                                            |
| aiohttp                  | 1.21 ms                                                                | 1.22 ms: 1.01x slower                                                            |
| chameleon                | 7.09 ms                                                                | 7.14 ms: 1.01x slower                                                            |
| sqlglot_parse            | 1.32 ms                                                                | 1.33 ms: 1.01x slower                                                            |
| dulwich_log              | 70.2 ms                                                                | 70.9 ms: 1.01x slower                                                            |
| regex_compile            | 144 ms                                                                 | 146 ms: 1.01x slower                                                             |
| comprehensions           | 18.0 us                                                                | 18.2 us: 1.01x slower                                                            |
| generators               | 30.1 ms                                                                | 30.4 ms: 1.01x slower                                                            |
| thrift                   | 806 us                                                                 | 816 us: 1.01x slower                                                             |
| pickle_pure_python       | 306 us                                                                 | 310 us: 1.01x slower                                                             |
| telco                    | 8.37 ms                                                                | 8.51 ms: 1.02x slower                                                            |
| deepcopy                 | 357 us                                                                 | 363 us: 1.02x slower                                                             |
| pathlib                  | 18.8 ms                                                                | 19.1 ms: 1.02x slower                                                            |
| json_dumps               | 10.3 ms                                                                | 10.5 ms: 1.02x slower                                                            |
| pickle                   | 11.5 us                                                                | 11.8 us: 1.02x slower                                                            |
| scimark_lu               | 129 ms                                                                 | 132 ms: 1.02x slower                                                             |
| deepcopy_reduce          | 3.11 us                                                                | 3.18 us: 1.02x slower                                                            |
| pickle_dict              | 33.9 us                                                                | 34.8 us: 1.03x slower                                                            |
| hexiom                   | 7.03 ms                                                                | 7.22 ms: 1.03x slower                                                            |
| nqueens                  | 87.8 ms                                                                | 90.8 ms: 1.03x slower                                                            |
| pickle_list              | 4.89 us                                                                | 5.13 us: 1.05x slower                                                            |
| mdp                      | 2.64 sec                                                               | 2.80 sec: 1.06x slower                                                           |
| gc_traversal             | 3.54 ms                                                                | 3.82 ms: 1.08x slower                                                            |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (36): unpickle, async_tree_memoization, async_tree_none, deltablue, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, sqlite_synth, chaos, pprint_safe_repr, gunicorn, sqlglot_optimize, deepcopy_memo, async_tree_cpu_io_mixed, async_tree_io, float, html5lib, sympy_sum, xml_etree_process, bench_mp_pool, sympy_integrate, asyncio_tcp, tornado_http, async_tree_memoization_tg, xml_etree_generate, sympy_str, async_generators, logging_format, sympy_expand, meteor_contest, dask, unpickle_pure_python, async_tree_none_tg, mypy2, async_tree_io_tg, json, pylint


# HPT report

- Reliability score: 66.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 0.95x