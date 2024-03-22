# Results vs. base

- fork: brandtbucher
- ref: justin_ghccc
- machine: linux-x86_64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.01x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                                       | 331 ms: 1.00x faster                                                       |
| chameleon      | 7.21 ms                                                                      | 7.32 ms: 1.01x slower                                                      |
| docutils       | 4.70 sec                                                                     | 4.68 sec: 1.00x faster                                                     |
| html5lib       | 82.5 ms                                                                      | 81.5 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none           | 2.74 sec                                                                     | 2.68 sec: 1.02x faster                                                     |
| async_tree_cpu_io_mixed   | 3.32 sec                                                                     | 3.26 sec: 1.02x faster                                                     |
| async_tree_memoization    | 3.44 sec                                                                     | 3.39 sec: 1.02x faster                                                     |
| async_tree_none_tg        | 2.88 sec                                                                     | 2.83 sec: 1.02x faster                                                     |
| async_tree_io             | 9.75 sec                                                                     | 9.59 sec: 1.02x faster                                                     |
| async_tree_io_tg          | 10.2 sec                                                                     | 10.1 sec: 1.01x faster                                                     |
| async_tree_memoization_tg | 3.53 sec                                                                     | 3.49 sec: 1.01x faster                                                     |
| Geometric mean            | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 94.7 ms                                                                      | 83.6 ms: 1.13x faster                                                      |
| float          | 154 ms                                                                       | 149 ms: 1.03x faster                                                       |
| pidigits       | 261 ms                                                                       | 261 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                        | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                                      | 3.48 ms: 1.03x faster                                                      |
| regex_compile  | 146 ms                                                                       | 144 ms: 1.01x faster                                                       |
| regex_dna      | 241 ms                                                                       | 247 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 168 ms                                                                       | 162 ms: 1.04x faster                                                       |
| tomli_loads          | 2.15 sec                                                                     | 2.08 sec: 1.03x faster                                                     |
| xml_etree_parse      | 209 ms                                                                       | 202 ms: 1.03x faster                                                       |
| pickle_pure_python   | 319 us                                                                       | 313 us: 1.02x faster                                                       |
| unpickle_pure_python | 229 us                                                                       | 226 us: 1.01x faster                                                       |
| unpickle_list        | 4.64 us                                                                      | 4.58 us: 1.01x faster                                                      |
| unpickle             | 15.4 us                                                                      | 15.3 us: 1.01x faster                                                      |
| xml_etree_generate   | 98.9 ms                                                                      | 98.6 ms: 1.00x faster                                                      |
| json_loads           | 24.8 us                                                                      | 24.9 us: 1.00x slower                                                      |
| pickle_dict          | 33.0 us                                                                      | 33.6 us: 1.02x slower                                                      |
| json_dumps           | 10.5 ms                                                                      | 10.7 ms: 1.02x slower                                                      |
| pickle_list          | 4.44 us                                                                      | 4.55 us: 1.02x slower                                                      |
| pickle               | 10.5 us                                                                      | 10.9 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 12.6 ms                                                                      | 12.6 ms: 1.00x faster                                                      |
| python_startup         | 14.5 ms                                                                      | 14.5 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.98 ms                                                                      | 9.30 ms: 1.07x faster                                                      |
| genshi_text     | 29.5 ms                                                                      | 29.1 ms: 1.01x faster                                                      |
| genshi_xml      | 66.9 ms                                                                      | 68.1 ms: 1.02x slower                                                      |
| django_template | 38.1 ms                                                                      | 39.8 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody                     | 94.7 ms                                                                      | 83.6 ms: 1.13x faster                                                      |
| spectral_norm             | 93.8 ms                                                                      | 82.8 ms: 1.13x faster                                                      |
| gc_traversal              | 4.47 ms                                                                      | 3.99 ms: 1.12x faster                                                      |
| fannkuch                  | 396 ms                                                                       | 359 ms: 1.11x faster                                                       |
| scimark_fft               | 322 ms                                                                       | 292 ms: 1.10x faster                                                       |
| scimark_monte_carlo       | 76.6 ms                                                                      | 69.6 ms: 1.10x faster                                                      |
| scimark_sparse_mat_mult   | 4.37 ms                                                                      | 4.05 ms: 1.08x faster                                                      |
| crypto_pyaes              | 77.8 ms                                                                      | 72.2 ms: 1.08x faster                                                      |
| mako                      | 9.98 ms                                                                      | 9.30 ms: 1.07x faster                                                      |
| hexiom                    | 7.21 ms                                                                      | 6.80 ms: 1.06x faster                                                      |
| chaos                     | 66.7 ms                                                                      | 63.4 ms: 1.05x faster                                                      |
| create_gc_cycles          | 1.68 ms                                                                      | 1.60 ms: 1.05x faster                                                      |
| xml_etree_iterparse       | 168 ms                                                                       | 162 ms: 1.04x faster                                                       |
| tomli_loads               | 2.15 sec                                                                     | 2.08 sec: 1.03x faster                                                     |
| float                     | 154 ms                                                                       | 149 ms: 1.03x faster                                                       |
| xml_etree_parse           | 209 ms                                                                       | 202 ms: 1.03x faster                                                       |
| raytrace                  | 310 ms                                                                       | 301 ms: 1.03x faster                                                       |
| regex_effbot              | 3.57 ms                                                                      | 3.48 ms: 1.03x faster                                                      |
| pyflate                   | 513 ms                                                                       | 501 ms: 1.02x faster                                                       |
| nqueens                   | 100 ms                                                                       | 98.2 ms: 1.02x faster                                                      |
| async_tree_none           | 2.74 sec                                                                     | 2.68 sec: 1.02x faster                                                     |
| pickle_pure_python        | 319 us                                                                       | 313 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 3.32 sec                                                                     | 3.26 sec: 1.02x faster                                                     |
| async_tree_memoization    | 3.44 sec                                                                     | 3.39 sec: 1.02x faster                                                     |
| async_tree_none_tg        | 2.88 sec                                                                     | 2.83 sec: 1.02x faster                                                     |
| async_tree_io             | 9.75 sec                                                                     | 9.59 sec: 1.02x faster                                                     |
| coroutines                | 22.8 ms                                                                      | 22.4 ms: 1.02x faster                                                      |
| unpickle_pure_python      | 229 us                                                                       | 226 us: 1.01x faster                                                       |
| comprehensions            | 19.1 us                                                                      | 18.8 us: 1.01x faster                                                      |
| regex_compile             | 146 ms                                                                       | 144 ms: 1.01x faster                                                       |
| scimark_sor               | 153 ms                                                                       | 151 ms: 1.01x faster                                                       |
| unpickle_list             | 4.64 us                                                                      | 4.58 us: 1.01x faster                                                      |
| async_tree_io_tg          | 10.2 sec                                                                     | 10.1 sec: 1.01x faster                                                     |
| meteor_contest            | 131 ms                                                                       | 130 ms: 1.01x faster                                                       |
| html5lib                  | 82.5 ms                                                                      | 81.5 ms: 1.01x faster                                                      |
| genshi_text               | 29.5 ms                                                                      | 29.1 ms: 1.01x faster                                                      |
| async_tree_memoization_tg | 3.53 sec                                                                     | 3.49 sec: 1.01x faster                                                     |
| generators                | 33.3 ms                                                                      | 33.0 ms: 1.01x faster                                                      |
| mdp                       | 2.68 sec                                                                     | 2.65 sec: 1.01x faster                                                     |
| unpickle                  | 15.4 us                                                                      | 15.3 us: 1.01x faster                                                      |
| sqlite_synth              | 2.71 us                                                                      | 2.69 us: 1.01x faster                                                      |
| asyncio_tcp               | 371 ms                                                                       | 368 ms: 1.01x faster                                                       |
| python_startup_no_site    | 12.6 ms                                                                      | 12.6 ms: 1.00x faster                                                      |
| 2to3                      | 332 ms                                                                       | 331 ms: 1.00x faster                                                       |
| docutils                  | 4.70 sec                                                                     | 4.68 sec: 1.00x faster                                                     |
| python_startup            | 14.5 ms                                                                      | 14.5 ms: 1.00x faster                                                      |
| xml_etree_generate        | 98.9 ms                                                                      | 98.6 ms: 1.00x faster                                                      |
| pidigits                  | 261 ms                                                                       | 261 ms: 1.00x faster                                                       |
| json_loads                | 24.8 us                                                                      | 24.9 us: 1.00x slower                                                      |
| sympy_sum                 | 159 ms                                                                       | 160 ms: 1.00x slower                                                       |
| deltablue                 | 4.02 ms                                                                      | 4.04 ms: 1.01x slower                                                      |
| sympy_integrate           | 24.3 ms                                                                      | 24.5 ms: 1.01x slower                                                      |
| sympy_str                 | 300 ms                                                                       | 303 ms: 1.01x slower                                                       |
| richards_super            | 57.3 ms                                                                      | 57.9 ms: 1.01x slower                                                      |
| aiohttp                   | 1.15 ms                                                                      | 1.16 ms: 1.01x slower                                                      |
| logging_simple            | 6.52 us                                                                      | 6.60 us: 1.01x slower                                                      |
| chameleon                 | 7.21 ms                                                                      | 7.32 ms: 1.01x slower                                                      |
| json                      | 5.36 ms                                                                      | 5.45 ms: 1.02x slower                                                      |
| genshi_xml                | 66.9 ms                                                                      | 68.1 ms: 1.02x slower                                                      |
| pickle_dict               | 33.0 us                                                                      | 33.6 us: 1.02x slower                                                      |
| json_dumps                | 10.5 ms                                                                      | 10.7 ms: 1.02x slower                                                      |
| sqlglot_normalize         | 119 ms                                                                       | 121 ms: 1.02x slower                                                       |
| logging_format            | 7.16 us                                                                      | 7.30 us: 1.02x slower                                                      |
| sympy_expand              | 511 ms                                                                       | 521 ms: 1.02x slower                                                       |
| regex_dna                 | 241 ms                                                                       | 247 ms: 1.02x slower                                                       |
| deepcopy_memo             | 36.9 us                                                                      | 37.8 us: 1.02x slower                                                      |
| coverage                  | 81.0 ms                                                                      | 83.0 ms: 1.02x slower                                                      |
| pickle_list               | 4.44 us                                                                      | 4.55 us: 1.02x slower                                                      |
| pycparser                 | 1.60 sec                                                                     | 1.65 sec: 1.03x slower                                                     |
| deepcopy                  | 379 us                                                                       | 391 us: 1.03x slower                                                       |
| pickle                    | 10.5 us                                                                      | 10.9 us: 1.03x slower                                                      |
| typing_runtime_protocols  | 115 us                                                                       | 119 us: 1.04x slower                                                       |
| thrift                    | 859 us                                                                       | 893 us: 1.04x slower                                                       |
| django_template           | 38.1 ms                                                                      | 39.8 ms: 1.04x slower                                                      |
| scimark_lu                | 115 ms                                                                       | 126 ms: 1.10x slower                                                       |
| unpack_sequence           | 74.0 ns                                                                      | 118 ns: 1.60x slower                                                       |
| Geometric mean            | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (25): telco, pprint_pformat, sqlglot_parse, pylint, richards, dask, pprint_safe_repr, async_tree_cpu_io_mixed_tg, sqlglot_optimize, regex_v8, go, async_generators, asyncio_tcp_ssl, tornado_http, pathlib, gunicorn, dulwich_log, deepcopy_reduce, xml_etree_process, bench_thread_pool, logging_silent, sqlglot_transpile, mypy2, asyncio_websockets, bench_mp_pool


# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.00x