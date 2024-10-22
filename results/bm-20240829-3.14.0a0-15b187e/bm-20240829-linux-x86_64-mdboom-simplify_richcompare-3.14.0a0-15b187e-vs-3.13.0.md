# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 96.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 256 ms: 1.04x faster                                                  |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| html5lib       | 64.5 ms                                                | 64.0 ms: 1.01x faster                                                 |
| tornado_http   | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 399 ms: 1.17x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 389 ms: 1.14x faster                                                  |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.04x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 473 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 557 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| async_generators          | 433 ms                                                 | 439 ms: 1.01x slower                                                  |
| coroutines                | 22.5 ms                                                | 23.8 ms: 1.06x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 887 ms: 1.07x slower                                                  |
| async_tree_io             | 843 ms                                                 | 920 ms: 1.09x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| nbody          | 85.7 ms                                                | 89.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                 |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                  |
| regex_v8       | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                 |
| xml_etree_generate  | 87.0 ms                                                | 84.6 ms: 1.03x faster                                                 |
| tomli_loads         | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                |
| xml_etree_parse     | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| xml_etree_iterparse | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| json_loads          | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (3): json_dumps, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.8 ms: 1.05x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 49.1 ms: 1.03x faster                                                 |
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                 |
| mako            | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 260 us: 1.35x faster                                                  |
| deepcopy_memo             | 38.0 us                                                | 30.1 us: 1.26x faster                                                 |
| go                        | 142 ms                                                 | 119 ms: 1.19x faster                                                  |
| deepcopy_reduce           | 3.17 us                                                | 2.67 us: 1.18x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 399 ms: 1.17x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 389 ms: 1.14x faster                                                  |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.50 sec: 1.10x faster                                                |
| pathlib                   | 17.1 ms                                                | 15.7 ms: 1.09x faster                                                 |
| genshi_text               | 22.9 ms                                                | 21.8 ms: 1.05x faster                                                 |
| richards                  | 48.1 ms                                                | 45.9 ms: 1.05x faster                                                 |
| richards_super            | 54.4 ms                                                | 51.9 ms: 1.05x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.83 ms: 1.04x faster                                                 |
| pprint_safe_repr          | 744 ms                                                 | 716 ms: 1.04x faster                                                  |
| bench_thread_pool         | 815 us                                                 | 784 us: 1.04x faster                                                  |
| thrift                    | 796 us                                                 | 767 us: 1.04x faster                                                  |
| 2to3                      | 265 ms                                                 | 256 ms: 1.04x faster                                                  |
| generators                | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 473 ms: 1.03x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 557 ms: 1.03x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 84.6 ms: 1.03x faster                                                 |
| gc_traversal              | 3.81 ms                                                | 3.71 ms: 1.03x faster                                                 |
| genshi_xml                | 50.3 ms                                                | 49.1 ms: 1.03x faster                                                 |
| sympy_integrate           | 19.9 ms                                                | 19.4 ms: 1.02x faster                                                 |
| sympy_sum                 | 150 ms                                                 | 146 ms: 1.02x faster                                                  |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| crypto_pyaes              | 73.0 ms                                                | 71.4 ms: 1.02x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.55 us: 1.02x faster                                                 |
| tornado_http              | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                 |
| django_template           | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                 |
| regex_compile             | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| sympy_str                 | 274 ms                                                 | 269 ms: 1.02x faster                                                  |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| tomli_loads               | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                |
| telco                     | 8.45 ms                                                | 8.32 ms: 1.02x faster                                                 |
| sympy_expand              | 462 ms                                                 | 455 ms: 1.01x faster                                                  |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                |
| logging_format            | 6.25 us                                                | 6.18 us: 1.01x faster                                                 |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| html5lib                  | 64.5 ms                                                | 64.0 ms: 1.01x faster                                                 |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| sqlglot_optimize          | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                 |
| nqueens                   | 80.6 ms                                                | 80.4 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| hexiom                    | 6.13 ms                                                | 6.11 ms: 1.00x faster                                                 |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| bench_mp_pool             | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                 |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| scimark_monte_carlo       | 66.3 ms                                                | 66.7 ms: 1.01x slower                                                 |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                 |
| sqlglot_normalize         | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| python_startup_no_site    | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| async_generators          | 433 ms                                                 | 439 ms: 1.01x slower                                                  |
| deltablue                 | 3.15 ms                                                | 3.20 ms: 1.02x slower                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| regex_dna                 | 220 ms                                                 | 224 ms: 1.02x slower                                                  |
| json                      | 5.20 ms                                                | 5.33 ms: 1.02x slower                                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.83 sec: 1.03x slower                                                |
| coverage                  | 83.7 ms                                                | 86.2 ms: 1.03x slower                                                 |
| pyflate                   | 460 ms                                                 | 474 ms: 1.03x slower                                                  |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                  |
| docutils                  | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| regex_v8                  | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                 |
| mako                      | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                 |
| nbody                     | 85.7 ms                                                | 89.8 ms: 1.05x slower                                                 |
| fannkuch                  | 381 ms                                                 | 403 ms: 1.06x slower                                                  |
| coroutines                | 22.5 ms                                                | 23.8 ms: 1.06x slower                                                 |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 887 ms: 1.07x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                 |
| async_tree_io             | 843 ms                                                 | 920 ms: 1.09x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed_tg, logging_silent, typing_runtime_protocols, float, json_dumps, scimark_fft, sqlglot_transpile, raytrace, pickle_pure_python, chaos, unpickle_pure_python, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 96.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x