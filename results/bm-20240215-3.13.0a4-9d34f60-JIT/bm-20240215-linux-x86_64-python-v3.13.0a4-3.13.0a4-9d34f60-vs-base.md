# Results vs. base

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.02x slower
- HPT reliability: 91.27%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                                               | 276 ms: 1.03x slower                                                                                     |
| chameleon      | 6.85 ms                                                                                              | 6.75 ms: 1.01x faster                                                                                    |
| docutils       | 2.65 sec                                                                                             | 2.64 sec: 1.00x faster                                                                                   |
| Geometric mean | (ref)                                                                                                | 1.00x slower                                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|--------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg   | 1.22 sec                                                                                             | 1.20 sec: 1.02x faster                                                                                   |
| async_tree_io      | 1.20 sec                                                                                             | 1.18 sec: 1.02x faster                                                                                   |
| async_tree_none_tg | 455 ms                                                                                               | 452 ms: 1.01x faster                                                                                     |
| Geometric mean     | (ref)                                                                                                | 1.01x faster                                                                                             |

Benchmark hidden because not significant (5): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                                               | 188 ms: 1.01x faster                                                                                     |
| float          | 83.1 ms                                                                                              | 86.1 ms: 1.04x slower                                                                                    |
| nbody          | 92.1 ms                                                                                              | 102 ms: 1.11x slower                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.05x slower                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.66 ms                                                                                              | 3.57 ms: 1.03x faster                                                                                    |
| regex_dna      | 224 ms                                                                                               | 225 ms: 1.01x slower                                                                                     |
| regex_v8       | 24.4 ms                                                                                              | 25.1 ms: 1.03x slower                                                                                    |
| regex_compile  | 132 ms                                                                                               | 141 ms: 1.07x slower                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.02x slower                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| pickle               | 12.0 us                                                                                              | 11.4 us: 1.06x faster                                                                                    |
| pickle_list          | 5.28 us                                                                                              | 5.07 us: 1.04x faster                                                                                    |
| pickle_dict          | 34.7 us                                                                                              | 33.6 us: 1.03x faster                                                                                    |
| json_loads           | 27.9 us                                                                                              | 27.3 us: 1.02x faster                                                                                    |
| xml_etree_process    | 59.3 ms                                                                                              | 57.9 ms: 1.02x faster                                                                                    |
| xml_etree_parse      | 160 ms                                                                                               | 157 ms: 1.02x faster                                                                                     |
| unpickle             | 15.4 us                                                                                              | 15.1 us: 1.02x faster                                                                                    |
| pickle_pure_python   | 302 us                                                                                               | 296 us: 1.02x faster                                                                                     |
| xml_etree_generate   | 86.9 ms                                                                                              | 85.7 ms: 1.01x faster                                                                                    |
| json_dumps           | 10.5 ms                                                                                              | 10.5 ms: 1.01x slower                                                                                    |
| unpickle_pure_python | 217 us                                                                                               | 228 us: 1.05x slower                                                                                     |
| Geometric mean       | (ref)                                                                                                | 1.01x faster                                                                                             |

Benchmark hidden because not significant (3): tomli_loads, unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.87 ms                                                                                              | 8.95 ms: 1.01x slower                                                                                    |
| Geometric mean         | (ref)                                                                                                | 1.00x slower                                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-----------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| mako      | 11.2 ms                                                                                              | 12.4 ms: 1.10x slower                                                                                    |

All benchmarks:
===============

| Benchmark                | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|--------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| richards                 | 48.1 ms                                                                                              | 44.8 ms: 1.07x faster                                                                                    |
| richards_super           | 54.1 ms                                                                                              | 50.8 ms: 1.06x faster                                                                                    |
| scimark_sor              | 129 ms                                                                                               | 122 ms: 1.06x faster                                                                                     |
| pickle                   | 12.0 us                                                                                              | 11.4 us: 1.06x faster                                                                                    |
| generators               | 30.3 ms                                                                                              | 29.1 ms: 1.04x faster                                                                                    |
| pickle_list              | 5.28 us                                                                                              | 5.07 us: 1.04x faster                                                                                    |
| logging_format           | 6.53 us                                                                                              | 6.30 us: 1.04x faster                                                                                    |
| pickle_dict              | 34.7 us                                                                                              | 33.6 us: 1.03x faster                                                                                    |
| pathlib                  | 18.7 ms                                                                                              | 18.1 ms: 1.03x faster                                                                                    |
| regex_effbot             | 3.66 ms                                                                                              | 3.57 ms: 1.03x faster                                                                                    |
| json_loads               | 27.9 us                                                                                              | 27.3 us: 1.02x faster                                                                                    |
| xml_etree_process        | 59.3 ms                                                                                              | 57.9 ms: 1.02x faster                                                                                    |
| asyncio_tcp_ssl          | 1.84 sec                                                                                             | 1.80 sec: 1.02x faster                                                                                   |
| xml_etree_parse          | 160 ms                                                                                               | 157 ms: 1.02x faster                                                                                     |
| unpickle                 | 15.4 us                                                                                              | 15.1 us: 1.02x faster                                                                                    |
| async_tree_io_tg         | 1.22 sec                                                                                             | 1.20 sec: 1.02x faster                                                                                   |
| asyncio_websockets       | 563 ms                                                                                               | 552 ms: 1.02x faster                                                                                     |
| async_tree_io            | 1.20 sec                                                                                             | 1.18 sec: 1.02x faster                                                                                   |
| pickle_pure_python       | 302 us                                                                                               | 296 us: 1.02x faster                                                                                     |
| typing_runtime_protocols | 112 us                                                                                               | 110 us: 1.02x faster                                                                                     |
| sqlite_synth             | 2.87 us                                                                                              | 2.82 us: 1.02x faster                                                                                    |
| logging_simple           | 5.83 us                                                                                              | 5.74 us: 1.02x faster                                                                                    |
| chameleon                | 6.85 ms                                                                                              | 6.75 ms: 1.01x faster                                                                                    |
| xml_etree_generate       | 86.9 ms                                                                                              | 85.7 ms: 1.01x faster                                                                                    |
| json                     | 5.19 ms                                                                                              | 5.12 ms: 1.01x faster                                                                                    |
| create_gc_cycles         | 1.51 ms                                                                                              | 1.49 ms: 1.01x faster                                                                                    |
| sqlglot_normalize        | 108 ms                                                                                               | 107 ms: 1.01x faster                                                                                     |
| asyncio_tcp              | 501 ms                                                                                               | 497 ms: 1.01x faster                                                                                     |
| pycparser                | 1.23 sec                                                                                             | 1.22 sec: 1.01x faster                                                                                   |
| async_tree_none_tg       | 455 ms                                                                                               | 452 ms: 1.01x faster                                                                                     |
| pidigits                 | 189 ms                                                                                               | 188 ms: 1.01x faster                                                                                     |
| deepcopy                 | 347 us                                                                                               | 345 us: 1.01x faster                                                                                     |
| docutils                 | 2.65 sec                                                                                             | 2.64 sec: 1.00x faster                                                                                   |
| bench_thread_pool        | 838 us                                                                                               | 836 us: 1.00x faster                                                                                     |
| regex_dna                | 224 ms                                                                                               | 225 ms: 1.01x slower                                                                                     |
| deepcopy_memo            | 37.9 us                                                                                              | 38.1 us: 1.01x slower                                                                                    |
| bench_mp_pool            | 23.8 ms                                                                                              | 24.0 ms: 1.01x slower                                                                                    |
| json_dumps               | 10.5 ms                                                                                              | 10.5 ms: 1.01x slower                                                                                    |
| python_startup_no_site   | 8.87 ms                                                                                              | 8.95 ms: 1.01x slower                                                                                    |
| async_generators         | 459 ms                                                                                               | 463 ms: 1.01x slower                                                                                     |
| sqlglot_parse            | 1.26 ms                                                                                              | 1.28 ms: 1.01x slower                                                                                    |
| meteor_contest           | 108 ms                                                                                               | 110 ms: 1.02x slower                                                                                     |
| sqlglot_optimize         | 54.2 ms                                                                                              | 55.1 ms: 1.02x slower                                                                                    |
| sqlglot_transpile        | 1.58 ms                                                                                              | 1.61 ms: 1.02x slower                                                                                    |
| scimark_fft              | 359 ms                                                                                               | 366 ms: 1.02x slower                                                                                     |
| dulwich_log              | 67.0 ms                                                                                              | 68.2 ms: 1.02x slower                                                                                    |
| sympy_integrate          | 19.9 ms                                                                                              | 20.3 ms: 1.02x slower                                                                                    |
| sympy_str                | 274 ms                                                                                               | 281 ms: 1.02x slower                                                                                     |
| deltablue                | 3.24 ms                                                                                              | 3.32 ms: 1.03x slower                                                                                    |
| 2to3                     | 269 ms                                                                                               | 276 ms: 1.03x slower                                                                                     |
| regex_v8                 | 24.4 ms                                                                                              | 25.1 ms: 1.03x slower                                                                                    |
| coroutines               | 23.0 ms                                                                                              | 23.7 ms: 1.03x slower                                                                                    |
| float                    | 83.1 ms                                                                                              | 86.1 ms: 1.04x slower                                                                                    |
| logging_silent           | 97.7 ns                                                                                              | 101 ns: 1.04x slower                                                                                     |
| sympy_expand             | 462 ms                                                                                               | 480 ms: 1.04x slower                                                                                     |
| sympy_sum                | 150 ms                                                                                               | 157 ms: 1.04x slower                                                                                     |
| go                       | 139 ms                                                                                               | 146 ms: 1.05x slower                                                                                     |
| unpickle_pure_python     | 217 us                                                                                               | 228 us: 1.05x slower                                                                                     |
| fannkuch                 | 401 ms                                                                                               | 422 ms: 1.05x slower                                                                                     |
| raytrace                 | 265 ms                                                                                               | 280 ms: 1.06x slower                                                                                     |
| pprint_safe_repr         | 734 ms                                                                                               | 775 ms: 1.06x slower                                                                                     |
| gc_traversal             | 3.55 ms                                                                                              | 3.76 ms: 1.06x slower                                                                                    |
| mdp                      | 2.61 sec                                                                                             | 2.78 sec: 1.07x slower                                                                                   |
| regex_compile            | 132 ms                                                                                               | 141 ms: 1.07x slower                                                                                     |
| pprint_pformat           | 1.51 sec                                                                                             | 1.61 sec: 1.07x slower                                                                                   |
| pyflate                  | 474 ms                                                                                               | 514 ms: 1.08x slower                                                                                     |
| crypto_pyaes             | 72.0 ms                                                                                              | 79.1 ms: 1.10x slower                                                                                    |
| scimark_monte_carlo      | 67.2 ms                                                                                              | 74.0 ms: 1.10x slower                                                                                    |
| mako                     | 11.2 ms                                                                                              | 12.4 ms: 1.10x slower                                                                                    |
| nqueens                  | 81.0 ms                                                                                              | 89.8 ms: 1.11x slower                                                                                    |
| nbody                    | 92.1 ms                                                                                              | 102 ms: 1.11x slower                                                                                     |
| comprehensions           | 16.2 us                                                                                              | 18.2 us: 1.12x slower                                                                                    |
| chaos                    | 61.2 ms                                                                                              | 69.1 ms: 1.13x slower                                                                                    |
| scimark_sparse_mat_mult  | 4.64 ms                                                                                              | 5.35 ms: 1.15x slower                                                                                    |
| spectral_norm            | 111 ms                                                                                               | 132 ms: 1.19x slower                                                                                     |
| hexiom                   | 6.20 ms                                                                                              | 7.72 ms: 1.25x slower                                                                                    |
| Geometric mean           | (ref)                                                                                                | 1.02x slower                                                                                             |

Benchmark hidden because not significant (15): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, coverage, deepcopy_reduce, mypy2, async_tree_cpu_io_mixed, tomli_loads, scimark_lu, tornado_http, telco, python_startup, unpickle_list, xml_etree_iterparse, async_tree_memoization_tg
Ignored benchmarks (10) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask, unpack_sequence

# HPT report

- Reliability score: 91.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x