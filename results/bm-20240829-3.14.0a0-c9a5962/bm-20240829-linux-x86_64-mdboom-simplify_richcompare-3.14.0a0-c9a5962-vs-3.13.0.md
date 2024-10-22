# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 253 ms: 1.05x faster                                                  |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| html5lib       | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                 |
| tornado_http   | 91.5 ms                                                | 89.5 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 400 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 389 ms: 1.14x faster                                                  |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 486 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| async_generators          | 433 ms                                                 | 439 ms: 1.02x slower                                                  |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 892 ms: 1.08x slower                                                  |
| async_tree_io             | 843 ms                                                 | 926 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.5 ms: 1.03x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.54 ms: 1.10x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                 |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.05 sec: 1.03x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                 |
| xml_etree_generate   | 87.0 ms                                                | 85.2 ms: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.00x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.5 ms: 1.06x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 48.2 ms: 1.05x faster                                                 |
| django_template | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                 |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 260 us: 1.35x faster                                                  |
| deepcopy_memo             | 38.0 us                                                | 29.6 us: 1.28x faster                                                 |
| go                        | 142 ms                                                 | 117 ms: 1.21x faster                                                  |
| deepcopy_reduce           | 3.17 us                                                | 2.66 us: 1.19x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 400 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 389 ms: 1.14x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.54 ms: 1.10x faster                                                 |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.50 sec: 1.10x faster                                                |
| gc_traversal              | 3.81 ms                                                | 3.54 ms: 1.08x faster                                                 |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                 |
| genshi_text               | 22.9 ms                                                | 21.5 ms: 1.06x faster                                                 |
| pycparser                 | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                |
| pprint_safe_repr          | 744 ms                                                 | 702 ms: 1.06x faster                                                  |
| richards_super            | 54.4 ms                                                | 51.6 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.77 ms: 1.05x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.44 sec: 1.05x faster                                                |
| richards                  | 48.1 ms                                                | 45.9 ms: 1.05x faster                                                 |
| 2to3                      | 265 ms                                                 | 253 ms: 1.05x faster                                                  |
| genshi_xml                | 50.3 ms                                                | 48.2 ms: 1.05x faster                                                 |
| thrift                    | 796 us                                                 | 762 us: 1.04x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                  |
| generators                | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                 |
| bench_thread_pool         | 815 us                                                 | 783 us: 1.04x faster                                                  |
| regex_v8                  | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 2.05 sec: 1.03x faster                                                |
| xml_etree_process         | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                 |
| sympy_str                 | 274 ms                                                 | 267 ms: 1.03x faster                                                  |
| float                     | 78.5 ms                                                | 76.5 ms: 1.03x faster                                                 |
| logging_format            | 6.25 us                                                | 6.10 us: 1.02x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                  |
| spectral_norm             | 115 ms                                                 | 112 ms: 1.02x faster                                                  |
| django_template           | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                 |
| tornado_http              | 91.5 ms                                                | 89.5 ms: 1.02x faster                                                 |
| sympy_expand              | 462 ms                                                 | 452 ms: 1.02x faster                                                  |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 85.2 ms: 1.02x faster                                                 |
| scimark_lu                | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| logging_silent            | 102 ns                                                 | 100 ns: 1.02x faster                                                  |
| regex_compile             | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                  |
| scimark_fft               | 369 ms                                                 | 363 ms: 1.02x faster                                                  |
| logging_simple            | 5.66 us                                                | 5.58 us: 1.01x faster                                                 |
| telco                     | 8.45 ms                                                | 8.34 ms: 1.01x faster                                                 |
| html5lib                  | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                 |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| nqueens                   | 80.6 ms                                                | 79.8 ms: 1.01x faster                                                 |
| sqlglot_optimize          | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                 |
| regex_dna                 | 220 ms                                                 | 218 ms: 1.01x faster                                                  |
| unpickle_pure_python      | 213 us                                                 | 212 us: 1.00x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 486 ms: 1.00x faster                                                  |
| raytrace                  | 262 ms                                                 | 261 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                 |
| sqlglot_normalize         | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| typing_runtime_protocols  | 159 us                                                 | 161 us: 1.01x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.01x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.19 ms: 1.01x slower                                                 |
| async_generators          | 433 ms                                                 | 439 ms: 1.02x slower                                                  |
| deltablue                 | 3.15 ms                                                | 3.22 ms: 1.02x slower                                                 |
| json                      | 5.20 ms                                                | 5.31 ms: 1.02x slower                                                 |
| docutils                  | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| bpe_tokeniser             | 4.69 sec                                               | 4.80 sec: 1.02x slower                                                |
| xml_etree_iterparse       | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| coverage                  | 83.7 ms                                                | 85.7 ms: 1.02x slower                                                 |
| mako                      | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                 |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                 |
| fannkuch                  | 381 ms                                                 | 402 ms: 1.05x slower                                                  |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| create_gc_cycles          | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 892 ms: 1.08x slower                                                  |
| async_tree_io             | 843 ms                                                 | 926 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (12): nbody, async_tree_cpu_io_mixed_tg, chaos, json_dumps, sqlglot_transpile, crypto_pyaes, xml_etree_parse, bench_mp_pool, scimark_monte_carlo, pyflate, pickle_pure_python, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x