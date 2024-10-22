# Results vs. 3.13.0

- fork: python
- ref: 91b7f2e7f6593acefda4
- machine: linux-x86_64
- commit hash: 91b7f2e
- commit date: 2024-09-01
- overall geometric mean: 1.01x faster
- HPT reliability: 87.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                  |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                |
| tornado_http   | 91.5 ms                                                | 94.4 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 406 ms: 1.14x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 554 ms: 1.04x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                 |
| asyncio_tcp               | 488 ms                                                 | 495 ms: 1.01x slower                                                  |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 899 ms: 1.09x slower                                                  |
| async_tree_io             | 843 ms                                                 | 933 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                 |
| nbody          | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.52 ms: 1.10x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                 |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                  |
| regex_compile  | 131 ms                                                 | 141 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.6 ms: 1.12x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 55.1 ms: 1.10x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 98.3 ms: 1.04x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                  |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                                  |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.97 ms: 1.11x faster                                                 |
| django_template | 34.4 ms                                                | 36.3 ms: 1.06x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 58.3 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.7 us: 1.43x faster                                                 |
| deepcopy                  | 352 us                                                 | 267 us: 1.32x faster                                                  |
| richards                  | 48.1 ms                                                | 39.3 ms: 1.23x faster                                                 |
| richards_super            | 54.4 ms                                                | 45.4 ms: 1.20x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.65 us: 1.20x faster                                                 |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.34 ms: 1.16x faster                                                 |
| spectral_norm             | 115 ms                                                 | 99.9 ms: 1.15x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 406 ms: 1.14x faster                                                  |
| xml_etree_generate        | 87.0 ms                                                | 77.6 ms: 1.12x faster                                                 |
| float                     | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                 |
| mako                      | 11.1 ms                                                | 9.97 ms: 1.11x faster                                                 |
| crypto_pyaes              | 73.0 ms                                                | 65.7 ms: 1.11x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.52 ms: 1.10x faster                                                 |
| xml_etree_process         | 60.4 ms                                                | 55.1 ms: 1.10x faster                                                 |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                  |
| go                        | 142 ms                                                 | 131 ms: 1.08x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.55 sec: 1.08x faster                                                |
| nbody                     | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                 |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| gc_traversal              | 3.81 ms                                                | 3.56 ms: 1.07x faster                                                 |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                 |
| telco                     | 8.45 ms                                                | 7.93 ms: 1.07x faster                                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                |
| scimark_sor               | 122 ms                                                 | 116 ms: 1.06x faster                                                  |
| regex_v8                  | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 62.9 ms: 1.05x faster                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 98.3 ms: 1.04x faster                                                 |
| pprint_safe_repr          | 744 ms                                                 | 718 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 554 ms: 1.04x faster                                                  |
| scimark_lu                | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                  |
| logging_format            | 6.25 us                                                | 6.07 us: 1.03x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.51 us: 1.03x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                |
| fannkuch                  | 381 ms                                                 | 372 ms: 1.02x faster                                                  |
| pyflate                   | 460 ms                                                 | 449 ms: 1.02x faster                                                  |
| regex_dna                 | 220 ms                                                 | 217 ms: 1.01x faster                                                  |
| thrift                    | 796 us                                                 | 786 us: 1.01x faster                                                  |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                  |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                 |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                  |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                 |
| deltablue                 | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                 |
| pickle_pure_python        | 300 us                                                 | 304 us: 1.01x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 495 ms: 1.01x slower                                                  |
| coverage                  | 83.7 ms                                                | 85.4 ms: 1.02x slower                                                 |
| bench_thread_pool         | 815 us                                                 | 833 us: 1.02x slower                                                  |
| python_startup_no_site    | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                 |
| json                      | 5.20 ms                                                | 5.36 ms: 1.03x slower                                                 |
| tornado_http              | 91.5 ms                                                | 94.4 ms: 1.03x slower                                                 |
| typing_runtime_protocols  | 159 us                                                 | 165 us: 1.03x slower                                                  |
| 2to3                      | 265 ms                                                 | 276 ms: 1.04x slower                                                  |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                  |
| raytrace                  | 262 ms                                                 | 275 ms: 1.05x slower                                                  |
| nqueens                   | 80.6 ms                                                | 85.1 ms: 1.06x slower                                                 |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.06x slower                                                  |
| django_template           | 34.4 ms                                                | 36.3 ms: 1.06x slower                                                 |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                 |
| regex_compile             | 131 ms                                                 | 141 ms: 1.08x slower                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 58.4 ms: 1.08x slower                                                 |
| dulwich_log               | 63.0 ms                                                | 68.2 ms: 1.08x slower                                                 |
| genshi_text               | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 899 ms: 1.09x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                 |
| sympy_expand              | 462 ms                                                 | 507 ms: 1.10x slower                                                  |
| sympy_str                 | 274 ms                                                 | 301 ms: 1.10x slower                                                  |
| async_tree_io             | 843 ms                                                 | 933 ms: 1.11x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.86 ms: 1.12x slower                                                 |
| docutils                  | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                |
| sympy_integrate           | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                 |
| generators                | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                 |
| sympy_sum                 | 150 ms                                                 | 173 ms: 1.15x slower                                                  |
| genshi_xml                | 50.3 ms                                                | 58.3 ms: 1.16x slower                                                 |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, logging_silent, asyncio_websockets, bench_mp_pool, chaos, json_dumps, html5lib
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 87.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x