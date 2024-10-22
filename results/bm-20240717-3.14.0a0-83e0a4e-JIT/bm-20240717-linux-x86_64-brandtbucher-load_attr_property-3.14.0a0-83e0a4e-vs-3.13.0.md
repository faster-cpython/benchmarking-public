# Results vs. 3.13.0

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 83e0a4e
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 61.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 270 ms: 1.02x slower                                                      |
| docutils       | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                    |
| html5lib       | 64.5 ms                                                | 64.0 ms: 1.01x faster                                                     |
| tornado_http   | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 377 ms: 1.23x faster                                                      |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 405 ms: 1.09x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 297 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                                      |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 842 ms: 1.02x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 504 ms: 1.03x slower                                                      |
| async_generators          | 433 ms                                                 | 462 ms: 1.07x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                     |
| nbody          | 85.7 ms                                                | 80.7 ms: 1.06x faster                                                     |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                     |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                      |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                      |
| regex_v8       | 25.3 ms                                                | 25.9 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 80.9 ms: 1.07x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| xml_etree_process    | 60.4 ms                                                | 57.2 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                      |
| json_loads           | 27.0 us                                                | 27.7 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (2): pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                     |
| django_template | 34.4 ms                                                | 35.2 ms: 1.02x slower                                                     |
| genshi_text     | 22.9 ms                                                | 24.7 ms: 1.08x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 56.2 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.7 us: 1.33x faster                                                     |
| deepcopy                  | 352 us                                                 | 272 us: 1.30x faster                                                      |
| async_tree_memoization_tg | 465 ms                                                 | 377 ms: 1.23x faster                                                      |
| scimark_fft               | 369 ms                                                 | 307 ms: 1.20x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                                     |
| richards                  | 48.1 ms                                                | 41.0 ms: 1.17x faster                                                     |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.37 ms: 1.15x faster                                                     |
| richards_super            | 54.4 ms                                                | 47.4 ms: 1.15x faster                                                     |
| mako                      | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                     |
| float                     | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                     |
| spectral_norm             | 115 ms                                                 | 104 ms: 1.10x faster                                                      |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 60.6 ms: 1.09x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 405 ms: 1.09x faster                                                      |
| tomli_loads               | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                    |
| async_tree_none_tg        | 320 ms                                                 | 297 ms: 1.08x faster                                                      |
| crypto_pyaes              | 73.0 ms                                                | 67.8 ms: 1.08x faster                                                     |
| xml_etree_generate        | 87.0 ms                                                | 80.9 ms: 1.07x faster                                                     |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                     |
| nbody                     | 85.7 ms                                                | 80.7 ms: 1.06x faster                                                     |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| pprint_safe_repr          | 744 ms                                                 | 702 ms: 1.06x faster                                                      |
| xml_etree_process         | 60.4 ms                                                | 57.2 ms: 1.05x faster                                                     |
| telco                     | 8.45 ms                                                | 8.01 ms: 1.05x faster                                                     |
| mdp                       | 2.74 sec                                               | 2.60 sec: 1.05x faster                                                    |
| fannkuch                  | 381 ms                                                 | 363 ms: 1.05x faster                                                      |
| pyflate                   | 460 ms                                                 | 442 ms: 1.04x faster                                                      |
| logging_format            | 6.25 us                                                | 6.06 us: 1.03x faster                                                     |
| logging_simple            | 5.66 us                                                | 5.50 us: 1.03x faster                                                     |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                    |
| xml_etree_iterparse       | 102 ms                                                 | 99.1 ms: 1.03x faster                                                     |
| regex_effbot              | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                     |
| json                      | 5.20 ms                                                | 5.07 ms: 1.03x faster                                                     |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                    |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                                      |
| html5lib                  | 64.5 ms                                                | 64.0 ms: 1.01x faster                                                     |
| chaos                     | 58.4 ms                                                | 58.0 ms: 1.01x faster                                                     |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                      |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.00x faster                                                      |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                     |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                     |
| regex_dna                 | 220 ms                                                 | 221 ms: 1.01x slower                                                      |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| tornado_http              | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                     |
| generators                | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                     |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                     |
| go                        | 142 ms                                                 | 144 ms: 1.02x slower                                                      |
| gc_traversal              | 3.81 ms                                                | 3.88 ms: 1.02x slower                                                     |
| bench_thread_pool         | 815 us                                                 | 831 us: 1.02x slower                                                      |
| 2to3                      | 265 ms                                                 | 270 ms: 1.02x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 842 ms: 1.02x slower                                                      |
| django_template           | 34.4 ms                                                | 35.2 ms: 1.02x slower                                                     |
| raytrace                  | 262 ms                                                 | 267 ms: 1.02x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                     |
| regex_compile             | 131 ms                                                 | 134 ms: 1.02x slower                                                      |
| regex_v8                  | 25.3 ms                                                | 25.9 ms: 1.02x slower                                                     |
| json_loads                | 27.0 us                                                | 27.7 us: 1.03x slower                                                     |
| logging_silent            | 102 ns                                                 | 105 ns: 1.03x slower                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.82 sec: 1.03x slower                                                    |
| sqlglot_optimize          | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 504 ms: 1.03x slower                                                      |
| scimark_sor               | 122 ms                                                 | 127 ms: 1.04x slower                                                      |
| typing_runtime_protocols  | 159 us                                                 | 166 us: 1.04x slower                                                      |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.05x slower                                                      |
| dulwich_log               | 63.0 ms                                                | 66.1 ms: 1.05x slower                                                     |
| nqueens                   | 80.6 ms                                                | 85.6 ms: 1.06x slower                                                     |
| async_generators          | 433 ms                                                 | 462 ms: 1.07x slower                                                      |
| dask                      | 338 ms                                                 | 361 ms: 1.07x slower                                                      |
| sympy_str                 | 274 ms                                                 | 292 ms: 1.07x slower                                                      |
| pylint                    | 313 ms                                                 | 335 ms: 1.07x slower                                                      |
| sympy_expand              | 462 ms                                                 | 494 ms: 1.07x slower                                                      |
| scimark_lu                | 115 ms                                                 | 123 ms: 1.07x slower                                                      |
| hexiom                    | 6.13 ms                                                | 6.58 ms: 1.07x slower                                                     |
| genshi_text               | 22.9 ms                                                | 24.7 ms: 1.08x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.10x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 165 ms: 1.11x slower                                                      |
| docutils                  | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                    |
| sympy_integrate           | 19.9 ms                                                | 22.2 ms: 1.11x slower                                                     |
| genshi_xml                | 50.3 ms                                                | 56.2 ms: 1.12x slower                                                     |
| deltablue                 | 3.15 ms                                                | 3.55 ms: 1.13x slower                                                     |
| coverage                  | 83.7 ms                                                | 94.9 ms: 1.13x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (8): pickle_pure_python, async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets, sqlglot_parse, bench_mp_pool, json_dumps, thrift
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 61.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x