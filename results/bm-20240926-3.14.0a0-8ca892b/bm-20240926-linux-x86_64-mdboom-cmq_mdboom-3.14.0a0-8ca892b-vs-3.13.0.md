# Results vs. 3.13.0

- fork: mdboom
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 8ca892b
- commit date: 2024-09-26
- overall geometric mean: 1.02x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 253 ms: 1.05x faster                                        |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                      |
| html5lib       | 64.5 ms                                                | 63.9 ms: 1.01x faster                                       |
| tornado_http   | 91.5 ms                                                | 90.4 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 389 ms: 1.19x faster                                        |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                        |
| async_tree_none           | 354 ms                                                 | 315 ms: 1.12x faster                                        |
| async_tree_none_tg        | 320 ms                                                 | 304 ms: 1.05x faster                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 560 ms: 1.02x faster                                        |
| asyncio_tcp               | 488 ms                                                 | 481 ms: 1.02x faster                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                      |
| asyncio_websockets        | 555 ms                                                 | 560 ms: 1.01x slower                                        |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                       |
| async_tree_io_tg          | 825 ms                                                 | 869 ms: 1.05x slower                                        |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                |

Benchmark hidden because not significant (3): async_generators, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.0 ms: 1.03x faster                                       |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                        |
| nbody          | 85.7 ms                                                | 88.0 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                       |
| regex_v8       | 25.3 ms                                                | 24.2 ms: 1.04x faster                                       |
| regex_compile  | 131 ms                                                 | 127 ms: 1.03x faster                                        |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.4 ms: 1.03x faster                                       |
| xml_etree_generate  | 87.0 ms                                                | 84.8 ms: 1.03x faster                                       |
| tomli_loads         | 2.11 sec                                               | 2.09 sec: 1.01x faster                                      |
| json_loads          | 27.0 us                                                | 26.8 us: 1.01x faster                                       |
| pickle_list         | 5.01 us                                                | 5.09 us: 1.02x slower                                       |
| pickle              | 11.6 us                                                | 11.8 us: 1.02x slower                                       |
| pickle_dict         | 33.2 us                                                | 33.9 us: 1.02x slower                                       |
| pickle_pure_python  | 300 us                                                 | 307 us: 1.02x slower                                        |
| xml_etree_iterparse | 102 ms                                                 | 104 ms: 1.02x slower                                        |
| unpickle_list       | 4.96 us                                                | 5.24 us: 1.06x slower                                       |
| Geometric mean      | (ref)                                                  | 1.00x slower                                                |

Benchmark hidden because not significant (4): unpickle, json_dumps, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                       |
| python_startup_no_site | 6.99 ms                                                | 6.98 ms: 1.00x faster                                       |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.8 ms: 1.05x faster                                       |
| genshi_xml      | 50.3 ms                                                | 49.2 ms: 1.02x faster                                       |
| django_template | 34.4 ms                                                | 34.0 ms: 1.01x faster                                       |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                       |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 258 us: 1.37x faster                                        |
| deepcopy_memo             | 38.0 us                                                | 29.7 us: 1.28x faster                                       |
| go                        | 142 ms                                                 | 117 ms: 1.21x faster                                        |
| async_tree_memoization_tg | 465 ms                                                 | 389 ms: 1.19x faster                                        |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                       |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                        |
| async_tree_none           | 354 ms                                                 | 315 ms: 1.12x faster                                        |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                       |
| mdp                       | 2.74 sec                                               | 2.57 sec: 1.07x faster                                      |
| pycparser                 | 1.19 sec                                               | 1.12 sec: 1.06x faster                                      |
| json                      | 5.20 ms                                                | 4.90 ms: 1.06x faster                                       |
| async_tree_none_tg        | 320 ms                                                 | 304 ms: 1.05x faster                                        |
| genshi_text               | 22.9 ms                                                | 21.8 ms: 1.05x faster                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.79 ms: 1.05x faster                                       |
| regex_effbot              | 3.88 ms                                                | 3.70 ms: 1.05x faster                                       |
| 2to3                      | 265 ms                                                 | 253 ms: 1.05x faster                                        |
| richards_super            | 54.4 ms                                                | 52.2 ms: 1.04x faster                                       |
| regex_v8                  | 25.3 ms                                                | 24.2 ms: 1.04x faster                                       |
| richards                  | 48.1 ms                                                | 46.2 ms: 1.04x faster                                       |
| generators                | 28.8 ms                                                | 27.8 ms: 1.04x faster                                       |
| xml_etree_process         | 60.4 ms                                                | 58.4 ms: 1.03x faster                                       |
| pprint_safe_repr          | 744 ms                                                 | 721 ms: 1.03x faster                                        |
| float                     | 78.5 ms                                                | 76.0 ms: 1.03x faster                                       |
| bench_thread_pool         | 815 us                                                 | 789 us: 1.03x faster                                        |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                      |
| scimark_fft               | 369 ms                                                 | 358 ms: 1.03x faster                                        |
| regex_compile             | 131 ms                                                 | 127 ms: 1.03x faster                                        |
| thrift                    | 796 us                                                 | 774 us: 1.03x faster                                        |
| xml_etree_generate        | 87.0 ms                                                | 84.8 ms: 1.03x faster                                       |
| scimark_lu                | 115 ms                                                 | 112 ms: 1.03x faster                                        |
| sympy_str                 | 274 ms                                                 | 267 ms: 1.03x faster                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 560 ms: 1.02x faster                                        |
| genshi_xml                | 50.3 ms                                                | 49.2 ms: 1.02x faster                                       |
| logging_simple            | 5.66 us                                                | 5.55 us: 1.02x faster                                       |
| sympy_expand              | 462 ms                                                 | 453 ms: 1.02x faster                                        |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                        |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                       |
| sqlglot_optimize          | 53.9 ms                                                | 53.0 ms: 1.02x faster                                       |
| sqlglot_normalize         | 107 ms                                                 | 106 ms: 1.02x faster                                        |
| asyncio_tcp               | 488 ms                                                 | 481 ms: 1.02x faster                                        |
| sqlite_synth              | 2.85 us                                                | 2.81 us: 1.01x faster                                       |
| logging_format            | 6.25 us                                                | 6.17 us: 1.01x faster                                       |
| django_template           | 34.4 ms                                                | 34.0 ms: 1.01x faster                                       |
| tornado_http              | 91.5 ms                                                | 90.4 ms: 1.01x faster                                       |
| chaos                     | 58.4 ms                                                | 57.7 ms: 1.01x faster                                       |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                        |
| tomli_loads               | 2.11 sec                                               | 2.09 sec: 1.01x faster                                      |
| spectral_norm             | 115 ms                                                 | 114 ms: 1.01x faster                                        |
| html5lib                  | 64.5 ms                                                | 63.9 ms: 1.01x faster                                       |
| telco                     | 8.45 ms                                                | 8.37 ms: 1.01x faster                                       |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                       |
| json_loads                | 27.0 us                                                | 26.8 us: 1.01x faster                                       |
| nqueens                   | 80.6 ms                                                | 80.4 ms: 1.00x faster                                       |
| crypto_pyaes              | 73.0 ms                                                | 72.7 ms: 1.00x faster                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                      |
| python_startup_no_site    | 6.99 ms                                                | 6.98 ms: 1.00x faster                                       |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                        |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.00x slower                                       |
| raytrace                  | 262 ms                                                 | 262 ms: 1.00x slower                                        |
| asyncio_websockets        | 555 ms                                                 | 560 ms: 1.01x slower                                        |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.01x slower                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                       |
| hexiom                    | 6.13 ms                                                | 6.20 ms: 1.01x slower                                       |
| scimark_monte_carlo       | 66.3 ms                                                | 67.2 ms: 1.01x slower                                       |
| mako                      | 11.1 ms                                                | 11.3 ms: 1.02x slower                                       |
| pickle_list               | 5.01 us                                                | 5.09 us: 1.02x slower                                       |
| bpe_tokeniser             | 4.69 sec                                               | 4.77 sec: 1.02x slower                                      |
| pickle                    | 11.6 us                                                | 11.8 us: 1.02x slower                                       |
| dulwich_log               | 63.0 ms                                                | 64.3 ms: 1.02x slower                                       |
| pickle_dict               | 33.2 us                                                | 33.9 us: 1.02x slower                                       |
| pickle_pure_python        | 300 us                                                 | 307 us: 1.02x slower                                        |
| xml_etree_iterparse       | 102 ms                                                 | 104 ms: 1.02x slower                                        |
| nbody                     | 85.7 ms                                                | 88.0 ms: 1.03x slower                                       |
| deltablue                 | 3.15 ms                                                | 3.24 ms: 1.03x slower                                       |
| gc_traversal              | 3.81 ms                                                | 3.92 ms: 1.03x slower                                       |
| logging_silent            | 102 ns                                                 | 105 ns: 1.03x slower                                        |
| docutils                  | 2.58 sec                                               | 2.66 sec: 1.03x slower                                      |
| pyflate                   | 460 ms                                                 | 476 ms: 1.04x slower                                        |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                       |
| regex_dna                 | 220 ms                                                 | 229 ms: 1.04x slower                                        |
| async_tree_io_tg          | 825 ms                                                 | 869 ms: 1.05x slower                                        |
| unpickle_list             | 4.96 us                                                | 5.24 us: 1.06x slower                                       |
| create_gc_cycles          | 1.61 ms                                                | 1.71 ms: 1.06x slower                                       |
| fannkuch                  | 381 ms                                                 | 405 ms: 1.06x slower                                        |
| coverage                  | 83.7 ms                                                | 89.8 ms: 1.07x slower                                       |
| unpack_sequence           | 42.4 ns                                                | 53.2 ns: 1.25x slower                                       |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                |

Benchmark hidden because not significant (11): unpickle, typing_runtime_protocols, json_dumps, xml_etree_parse, sqlglot_transpile, bench_mp_pool, unpickle_pure_python, async_generators, async_tree_cpu_io_mixed_tg, async_tree_io, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x