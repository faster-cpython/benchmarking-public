# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_invalidate
- machine: linux-x86_64
- commit hash: e63d148
- commit date: 2024-05-08
- overall geometric mean: 1.04x slower
- HPT reliability: 97.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 302 ms: 1.10x slower                                                     |
| chameleon      | 7.22 ms                                                    | 7.17 ms: 1.01x faster                                                    |
| docutils       | 2.83 sec                                                   | 3.34 sec: 1.18x slower                                                   |
| html5lib       | 67.2 ms                                                    | 72.1 ms: 1.07x slower                                                    |
| tornado_http   | 94.6 ms                                                    | 103 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                      | 1.09x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|---------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 611 ms                                                     | 635 ms: 1.04x slower                                                     |
| async_tree_none_tg        | 336 ms                                                     | 358 ms: 1.06x slower                                                     |
| async_tree_io_tg          | 936 ms                                                     | 996 ms: 1.06x slower                                                     |
| async_tree_memoization    | 463 ms                                                     | 494 ms: 1.07x slower                                                     |
| async_tree_memoization_tg | 444 ms                                                     | 478 ms: 1.08x slower                                                     |
| Geometric mean            | (ref)                                                      | 1.04x slower                                                             |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                    |
| float          | 78.9 ms                                                    | 72.8 ms: 1.08x faster                                                    |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                      | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                     |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                    |
| regex_compile  | 137 ms                                                     | 140 ms: 1.03x slower                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.84 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                      | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.99 sec: 1.06x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                    |
| pickle_dict          | 34.8 us                                                    | 33.5 us: 1.04x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 60.9 ms: 1.01x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 88.2 ms: 1.01x slower                                                    |
| pickle_list          | 5.11 us                                                    | 5.21 us: 1.02x slower                                                    |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                    |
| unpickle_pure_python | 218 us                                                     | 225 us: 1.03x slower                                                     |
| unpickle             | 15.1 us                                                    | 15.6 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.67 ms: 1.08x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.50 ms: 1.18x faster                                                    |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                    |
| genshi_text     | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                    |
| genshi_xml      | 51.6 ms                                                    | 61.6 ms: 1.19x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|---------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| scimark_fft               | 392 ms                                                     | 313 ms: 1.25x faster                                                     |
| mako                      | 11.2 ms                                                    | 9.50 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult   | 5.27 ms                                                    | 4.47 ms: 1.18x faster                                                    |
| richards                  | 50.9 ms                                                    | 43.4 ms: 1.17x faster                                                    |
| richards_super            | 57.4 ms                                                    | 49.4 ms: 1.16x faster                                                    |
| spectral_norm             | 116 ms                                                     | 102 ms: 1.14x faster                                                     |
| crypto_pyaes              | 77.5 ms                                                    | 69.6 ms: 1.11x faster                                                    |
| fannkuch                  | 402 ms                                                     | 364 ms: 1.11x faster                                                     |
| nbody                     | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                    |
| pyflate                   | 484 ms                                                     | 444 ms: 1.09x faster                                                     |
| scimark_monte_carlo       | 69.2 ms                                                    | 63.7 ms: 1.09x faster                                                    |
| coverage                  | 93.1 ms                                                    | 85.7 ms: 1.09x faster                                                    |
| float                     | 78.9 ms                                                    | 72.8 ms: 1.08x faster                                                    |
| mdp                       | 2.79 sec                                                   | 2.61 sec: 1.07x faster                                                   |
| tomli_loads               | 2.12 sec                                                   | 1.99 sec: 1.06x faster                                                   |
| deepcopy_memo             | 39.7 us                                                    | 37.8 us: 1.05x faster                                                    |
| pprint_safe_repr          | 758 ms                                                     | 725 ms: 1.05x faster                                                     |
| sqlite_synth              | 2.99 us                                                    | 2.86 us: 1.05x faster                                                    |
| pprint_pformat            | 1.56 sec                                                   | 1.49 sec: 1.04x faster                                                   |
| json_dumps                | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                    |
| pickle_dict               | 34.8 us                                                    | 33.5 us: 1.04x faster                                                    |
| xml_etree_parse           | 162 ms                                                     | 157 ms: 1.03x faster                                                     |
| gc_traversal              | 3.98 ms                                                    | 3.86 ms: 1.03x faster                                                    |
| chaos                     | 61.3 ms                                                    | 59.7 ms: 1.03x faster                                                    |
| pidigits                  | 191 ms                                                     | 188 ms: 1.02x faster                                                     |
| pickle_pure_python        | 305 us                                                     | 300 us: 1.02x faster                                                     |
| regex_dna                 | 221 ms                                                     | 219 ms: 1.01x faster                                                     |
| chameleon                 | 7.22 ms                                                    | 7.17 ms: 1.01x faster                                                    |
| xml_etree_process         | 61.2 ms                                                    | 60.9 ms: 1.01x faster                                                    |
| xml_etree_generate        | 87.4 ms                                                    | 88.2 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl           | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                   |
| logging_format            | 6.47 us                                                    | 6.53 us: 1.01x slower                                                    |
| regex_v8                  | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                    |
| logging_silent            | 105 ns                                                     | 106 ns: 1.01x slower                                                     |
| generators                | 29.6 ms                                                    | 30.0 ms: 1.01x slower                                                    |
| deepcopy                  | 367 us                                                     | 372 us: 1.01x slower                                                     |
| logging_simple            | 5.74 us                                                    | 5.85 us: 1.02x slower                                                    |
| pickle_list               | 5.11 us                                                    | 5.21 us: 1.02x slower                                                    |
| comprehensions            | 16.6 us                                                    | 16.9 us: 1.02x slower                                                    |
| scimark_lu                | 122 ms                                                     | 124 ms: 1.02x slower                                                     |
| thrift                    | 823 us                                                     | 840 us: 1.02x slower                                                     |
| pickle                    | 11.5 us                                                    | 11.7 us: 1.02x slower                                                    |
| asyncio_tcp               | 508 ms                                                     | 520 ms: 1.02x slower                                                     |
| deepcopy_reduce           | 3.35 us                                                    | 3.43 us: 1.03x slower                                                    |
| go                        | 145 ms                                                     | 148 ms: 1.03x slower                                                     |
| regex_compile             | 137 ms                                                     | 140 ms: 1.03x slower                                                     |
| create_gc_cycles          | 1.82 ms                                                    | 1.87 ms: 1.03x slower                                                    |
| python_startup            | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                    |
| unpickle_pure_python      | 218 us                                                     | 225 us: 1.03x slower                                                     |
| unpickle                  | 15.1 us                                                    | 15.6 us: 1.03x slower                                                    |
| coroutines                | 23.2 ms                                                    | 23.9 ms: 1.03x slower                                                    |
| raytrace                  | 267 ms                                                     | 275 ms: 1.03x slower                                                     |
| pathlib                   | 17.3 ms                                                    | 17.9 ms: 1.03x slower                                                    |
| sqlglot_normalize         | 110 ms                                                     | 114 ms: 1.04x slower                                                     |
| scimark_sor               | 127 ms                                                     | 132 ms: 1.04x slower                                                     |
| dulwich_log               | 67.2 ms                                                    | 69.6 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed   | 611 ms                                                     | 635 ms: 1.04x slower                                                     |
| bench_thread_pool         | 834 us                                                     | 872 us: 1.05x slower                                                     |
| regex_effbot              | 3.67 ms                                                    | 3.84 ms: 1.05x slower                                                    |
| sqlglot_parse             | 1.32 ms                                                    | 1.39 ms: 1.05x slower                                                    |
| django_template           | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                    |
| async_generators          | 442 ms                                                     | 468 ms: 1.06x slower                                                     |
| hexiom                    | 6.30 ms                                                    | 6.68 ms: 1.06x slower                                                    |
| nqueens                   | 81.4 ms                                                    | 86.5 ms: 1.06x slower                                                    |
| aiohttp                   | 1.18 ms                                                    | 1.26 ms: 1.06x slower                                                    |
| async_tree_none_tg        | 336 ms                                                     | 358 ms: 1.06x slower                                                     |
| async_tree_io_tg          | 936 ms                                                     | 996 ms: 1.06x slower                                                     |
| async_tree_memoization    | 463 ms                                                     | 494 ms: 1.07x slower                                                     |
| gunicorn                  | 1.28 ms                                                    | 1.36 ms: 1.07x slower                                                    |
| sympy_str                 | 282 ms                                                     | 302 ms: 1.07x slower                                                     |
| html5lib                  | 67.2 ms                                                    | 72.1 ms: 1.07x slower                                                    |
| async_tree_memoization_tg | 444 ms                                                     | 478 ms: 1.08x slower                                                     |
| sqlglot_optimize          | 55.5 ms                                                    | 59.9 ms: 1.08x slower                                                    |
| python_startup_no_site    | 7.11 ms                                                    | 7.67 ms: 1.08x slower                                                    |
| sqlglot_transpile         | 1.63 ms                                                    | 1.77 ms: 1.08x slower                                                    |
| sympy_expand              | 473 ms                                                     | 513 ms: 1.08x slower                                                     |
| tornado_http              | 94.6 ms                                                    | 103 ms: 1.09x slower                                                     |
| typing_runtime_protocols  | 165 us                                                     | 179 us: 1.09x slower                                                     |
| genshi_text               | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                    |
| sympy_sum                 | 156 ms                                                     | 170 ms: 1.09x slower                                                     |
| pycparser                 | 1.16 sec                                                   | 1.27 sec: 1.09x slower                                                   |
| sympy_integrate           | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                    |
| 2to3                      | 274 ms                                                     | 302 ms: 1.10x slower                                                     |
| dask                      | 369 ms                                                     | 410 ms: 1.11x slower                                                     |
| flaskblogging             | 9.01 ms                                                    | 10.0 ms: 1.11x slower                                                    |
| deltablue                 | 3.25 ms                                                    | 3.67 ms: 1.13x slower                                                    |
| pylint                    | 317 ms                                                     | 366 ms: 1.15x slower                                                     |
| docutils                  | 2.83 sec                                                   | 3.34 sec: 1.18x slower                                                   |
| genshi_xml                | 51.6 ms                                                    | 61.6 ms: 1.19x slower                                                    |
| telco                     | 8.41 ms                                                    | 174 ms: 20.69x slower                                                    |
| Geometric mean            | (ref)                                                      | 1.04x slower                                                             |

Benchmark hidden because not significant (10): json, meteor_contest, xml_etree_iterparse, json_loads, asyncio_websockets, async_tree_none, bench_mp_pool, unpickle_list, async_tree_cpu_io_mixed_tg, async_tree_io
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms, mypy2

# HPT report

- Reliability score: 97.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x