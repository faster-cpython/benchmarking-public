# Results vs. base

- fork: brandtbucher
- ref: justin_invalidate
- machine: linux-x86_64
- commit hash: e63d148
- commit date: 2024-05-08
- overall geometric mean: 1.01x slower
- HPT reliability: 99.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 302 ms: 1.08x slower                                                     |
| docutils       | 2.96 sec                                                              | 3.34 sec: 1.13x slower                                                   |
| html5lib       | 70.7 ms                                                               | 72.1 ms: 1.02x slower                                                    |
| tornado_http   | 98.4 ms                                                               | 103 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg          | 1.02 sec                                                              | 996 ms: 1.02x faster                                                     |
| async_tree_none           | 370 ms                                                                | 379 ms: 1.03x slower                                                     |
| async_tree_io             | 933 ms                                                                | 962 ms: 1.03x slower                                                     |
| async_tree_memoization_tg | 453 ms                                                                | 478 ms: 1.05x slower                                                     |
| Geometric mean            | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 80.8 ms: 1.04x faster                                                    |
| float          | 71.1 ms                                                               | 72.8 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                | 219 ms: 1.04x faster                                                     |
| regex_v8       | 25.3 ms                                                               | 25.4 ms: 1.00x slower                                                    |
| regex_compile  | 140 ms                                                                | 140 ms: 1.01x slower                                                     |
| regex_effbot   | 3.68 ms                                                               | 3.84 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_list          | 5.56 us                                                               | 5.21 us: 1.07x faster                                                    |
| pickle_dict          | 34.7 us                                                               | 33.5 us: 1.04x faster                                                    |
| pickle               | 12.1 us                                                               | 11.7 us: 1.03x faster                                                    |
| pickle_pure_python   | 310 us                                                                | 300 us: 1.03x faster                                                     |
| unpickle_pure_python | 223 us                                                                | 225 us: 1.01x slower                                                     |
| unpickle_list        | 5.21 us                                                               | 5.39 us: 1.03x slower                                                    |
| xml_etree_process    | 58.9 ms                                                               | 60.9 ms: 1.03x slower                                                    |
| xml_etree_parse      | 151 ms                                                                | 157 ms: 1.04x slower                                                     |
| xml_etree_iterparse  | 102 ms                                                                | 107 ms: 1.05x slower                                                     |
| xml_etree_generate   | 83.2 ms                                                               | 88.2 ms: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (4): unpickle, json_loads, json_dumps, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.67 ms                                                               | 9.50 ms: 1.02x faster                                                    |
| django_template | 37.1 ms                                                               | 36.6 ms: 1.01x faster                                                    |
| genshi_text     | 25.1 ms                                                               | 25.8 ms: 1.03x slower                                                    |
| genshi_xml      | 59.9 ms                                                               | 61.6 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_list               | 5.56 us                                                               | 5.21 us: 1.07x faster                                                    |
| regex_dna                 | 228 ms                                                                | 219 ms: 1.04x faster                                                     |
| deltablue                 | 3.82 ms                                                               | 3.67 ms: 1.04x faster                                                    |
| nbody                     | 84.0 ms                                                               | 80.8 ms: 1.04x faster                                                    |
| pickle_dict               | 34.7 us                                                               | 33.5 us: 1.04x faster                                                    |
| pyflate                   | 460 ms                                                                | 444 ms: 1.04x faster                                                     |
| pickle                    | 12.1 us                                                               | 11.7 us: 1.03x faster                                                    |
| pickle_pure_python        | 310 us                                                                | 300 us: 1.03x faster                                                     |
| logging_silent            | 109 ns                                                                | 106 ns: 1.03x faster                                                     |
| coverage                  | 88.2 ms                                                               | 85.7 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult   | 4.58 ms                                                               | 4.47 ms: 1.02x faster                                                    |
| async_tree_io_tg          | 1.02 sec                                                              | 996 ms: 1.02x faster                                                     |
| gc_traversal              | 3.94 ms                                                               | 3.86 ms: 1.02x faster                                                    |
| pprint_safe_repr          | 739 ms                                                                | 725 ms: 1.02x faster                                                     |
| sympy_sum                 | 173 ms                                                                | 170 ms: 1.02x faster                                                     |
| mako                      | 9.67 ms                                                               | 9.50 ms: 1.02x faster                                                    |
| scimark_monte_carlo       | 64.6 ms                                                               | 63.7 ms: 1.01x faster                                                    |
| dulwich_log               | 70.7 ms                                                               | 69.6 ms: 1.01x faster                                                    |
| sqlglot_normalize         | 116 ms                                                                | 114 ms: 1.01x faster                                                     |
| scimark_fft               | 317 ms                                                                | 313 ms: 1.01x faster                                                     |
| django_template           | 37.1 ms                                                               | 36.6 ms: 1.01x faster                                                    |
| raytrace                  | 278 ms                                                                | 275 ms: 1.01x faster                                                     |
| richards                  | 43.6 ms                                                               | 43.4 ms: 1.01x faster                                                    |
| async_generators          | 471 ms                                                                | 468 ms: 1.01x faster                                                     |
| meteor_contest            | 110 ms                                                                | 110 ms: 1.01x faster                                                     |
| python_startup            | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                                    |
| sympy_integrate           | 22.7 ms                                                               | 22.6 ms: 1.00x faster                                                    |
| bench_thread_pool         | 874 us                                                                | 872 us: 1.00x faster                                                     |
| asyncio_tcp_ssl           | 1.86 sec                                                              | 1.86 sec: 1.00x faster                                                   |
| fannkuch                  | 362 ms                                                                | 364 ms: 1.00x slower                                                     |
| regex_v8                  | 25.3 ms                                                               | 25.4 ms: 1.00x slower                                                    |
| pathlib                   | 17.8 ms                                                               | 17.9 ms: 1.00x slower                                                    |
| unpickle_pure_python      | 223 us                                                                | 225 us: 1.01x slower                                                     |
| regex_compile             | 140 ms                                                                | 140 ms: 1.01x slower                                                     |
| mdp                       | 2.60 sec                                                              | 2.61 sec: 1.01x slower                                                   |
| comprehensions            | 16.8 us                                                               | 16.9 us: 1.01x slower                                                    |
| crypto_pyaes              | 68.9 ms                                                               | 69.6 ms: 1.01x slower                                                    |
| telco                     | 172 ms                                                                | 174 ms: 1.01x slower                                                     |
| typing_runtime_protocols  | 177 us                                                                | 179 us: 1.01x slower                                                     |
| go                        | 146 ms                                                                | 148 ms: 1.01x slower                                                     |
| scimark_sor               | 130 ms                                                                | 132 ms: 1.02x slower                                                     |
| hexiom                    | 6.56 ms                                                               | 6.68 ms: 1.02x slower                                                    |
| create_gc_cycles          | 1.83 ms                                                               | 1.87 ms: 1.02x slower                                                    |
| html5lib                  | 70.7 ms                                                               | 72.1 ms: 1.02x slower                                                    |
| float                     | 71.1 ms                                                               | 72.8 ms: 1.02x slower                                                    |
| deepcopy_reduce           | 3.35 us                                                               | 3.43 us: 1.03x slower                                                    |
| async_tree_none           | 370 ms                                                                | 379 ms: 1.03x slower                                                     |
| coroutines                | 23.3 ms                                                               | 23.9 ms: 1.03x slower                                                    |
| genshi_text               | 25.1 ms                                                               | 25.8 ms: 1.03x slower                                                    |
| genshi_xml                | 59.9 ms                                                               | 61.6 ms: 1.03x slower                                                    |
| asyncio_tcp               | 505 ms                                                                | 520 ms: 1.03x slower                                                     |
| sqlglot_optimize          | 58.0 ms                                                               | 59.9 ms: 1.03x slower                                                    |
| async_tree_io             | 933 ms                                                                | 962 ms: 1.03x slower                                                     |
| unpickle_list             | 5.21 us                                                               | 5.39 us: 1.03x slower                                                    |
| xml_etree_process         | 58.9 ms                                                               | 60.9 ms: 1.03x slower                                                    |
| xml_etree_parse           | 151 ms                                                                | 157 ms: 1.04x slower                                                     |
| thrift                    | 808 us                                                                | 840 us: 1.04x slower                                                     |
| regex_effbot              | 3.68 ms                                                               | 3.84 ms: 1.04x slower                                                    |
| tornado_http              | 98.4 ms                                                               | 103 ms: 1.04x slower                                                     |
| xml_etree_iterparse       | 102 ms                                                                | 107 ms: 1.05x slower                                                     |
| sqlglot_parse             | 1.31 ms                                                               | 1.39 ms: 1.05x slower                                                    |
| async_tree_memoization_tg | 453 ms                                                                | 478 ms: 1.05x slower                                                     |
| pycparser                 | 1.20 sec                                                              | 1.27 sec: 1.06x slower                                                   |
| xml_etree_generate        | 83.2 ms                                                               | 88.2 ms: 1.06x slower                                                    |
| flaskblogging             | 9.30 ms                                                               | 10.0 ms: 1.08x slower                                                    |
| 2to3                      | 280 ms                                                                | 302 ms: 1.08x slower                                                     |
| sqlglot_transpile         | 1.64 ms                                                               | 1.77 ms: 1.08x slower                                                    |
| dask                      | 380 ms                                                                | 410 ms: 1.08x slower                                                     |
| docutils                  | 2.96 sec                                                              | 3.34 sec: 1.13x slower                                                   |
| Geometric mean            | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (31): spectral_norm, unpickle, pprint_pformat, json, chameleon, richards_super, sqlite_synth, bench_mp_pool, generators, nqueens, sympy_expand, sympy_str, asyncio_websockets, logging_simple, logging_format, pidigits, python_startup_no_site, json_loads, aiohttp, json_dumps, deepcopy, gunicorn, tomli_loads, async_tree_cpu_io_mixed, scimark_lu, async_tree_cpu_io_mixed_tg, deepcopy_memo, chaos, pylint, async_tree_memoization, async_tree_none_tg

# HPT report

- Reliability score: 99.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x