# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: f6b4125
- commit date: 2024-07-10
- overall geometric mean: 1.01x faster
- HPT reliability: 64.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                    |
| docutils       | 2.58 sec                                               | 2.90 sec: 1.12x slower                                                  |
| html5lib       | 64.5 ms                                                | 63.1 ms: 1.02x faster                                                   |
| tornado_http   | 91.5 ms                                                | 92.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 377 ms: 1.23x faster                                                    |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                    |
| async_tree_memoization    | 442 ms                                                 | 409 ms: 1.08x faster                                                    |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 500 ms: 1.02x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 848 ms: 1.03x slower                                                    |
| coroutines                | 22.5 ms                                                | 23.5 ms: 1.04x slower                                                   |
| async_generators          | 433 ms                                                 | 458 ms: 1.06x slower                                                    |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.9 ms: 1.12x faster                                                   |
| nbody          | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                   |
| regex_effbot   | 3.88 ms                                                | 4.02 ms: 1.03x slower                                                   |
| regex_compile  | 131 ms                                                 | 136 ms: 1.04x slower                                                    |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 81.6 ms: 1.07x faster                                                   |
| xml_etree_process    | 60.4 ms                                                | 57.1 ms: 1.06x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 207 us: 1.03x faster                                                    |
| pickle_pure_python   | 300 us                                                 | 292 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 102 ms                                                 | 99.4 ms: 1.03x faster                                                   |
| json_loads           | 27.0 us                                                | 27.8 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.91 ms: 1.12x faster                                                   |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                   |
| genshi_text     | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 58.7 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.4 us: 1.39x faster                                                   |
| deepcopy                  | 352 us                                                 | 271 us: 1.30x faster                                                    |
| async_tree_memoization_tg | 465 ms                                                 | 377 ms: 1.23x faster                                                    |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                                   |
| richards                  | 48.1 ms                                                | 40.9 ms: 1.18x faster                                                   |
| scimark_fft               | 369 ms                                                 | 320 ms: 1.15x faster                                                    |
| richards_super            | 54.4 ms                                                | 48.0 ms: 1.13x faster                                                   |
| scimark_monte_carlo       | 66.3 ms                                                | 58.5 ms: 1.13x faster                                                   |
| float                     | 78.5 ms                                                | 69.9 ms: 1.12x faster                                                   |
| mako                      | 11.1 ms                                                | 9.91 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.53 ms: 1.11x faster                                                   |
| tomli_loads               | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                  |
| spectral_norm             | 115 ms                                                 | 105 ms: 1.10x faster                                                    |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                    |
| crypto_pyaes              | 73.0 ms                                                | 67.0 ms: 1.09x faster                                                   |
| mdp                       | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 409 ms: 1.08x faster                                                    |
| nbody                     | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                   |
| pprint_safe_repr          | 744 ms                                                 | 697 ms: 1.07x faster                                                    |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                    |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| xml_etree_generate        | 87.0 ms                                                | 81.6 ms: 1.07x faster                                                   |
| xml_etree_process         | 60.4 ms                                                | 57.1 ms: 1.06x faster                                                   |
| telco                     | 8.45 ms                                                | 8.00 ms: 1.06x faster                                                   |
| pprint_pformat            | 1.51 sec                                               | 1.43 sec: 1.06x faster                                                  |
| pathlib                   | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                   |
| fannkuch                  | 381 ms                                                 | 362 ms: 1.05x faster                                                    |
| pyflate                   | 460 ms                                                 | 439 ms: 1.05x faster                                                    |
| logging_silent            | 102 ns                                                 | 98.0 ns: 1.04x faster                                                   |
| logging_format            | 6.25 us                                                | 6.02 us: 1.04x faster                                                   |
| logging_simple            | 5.66 us                                                | 5.49 us: 1.03x faster                                                   |
| unpickle_pure_python      | 213 us                                                 | 207 us: 1.03x faster                                                    |
| pickle_pure_python        | 300 us                                                 | 292 us: 1.03x faster                                                    |
| xml_etree_iterparse       | 102 ms                                                 | 99.4 ms: 1.03x faster                                                   |
| html5lib                  | 64.5 ms                                                | 63.1 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                    |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                   |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| tornado_http              | 91.5 ms                                                | 92.6 ms: 1.01x slower                                                   |
| sqlglot_transpile         | 1.57 ms                                                | 1.60 ms: 1.01x slower                                                   |
| bench_thread_pool         | 815 us                                                 | 829 us: 1.02x slower                                                    |
| python_startup_no_site    | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                   |
| regex_v8                  | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                   |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                   |
| raytrace                  | 262 ms                                                 | 267 ms: 1.02x slower                                                    |
| asyncio_tcp               | 488 ms                                                 | 500 ms: 1.02x slower                                                    |
| bpe_tokeniser             | 4.69 sec                                               | 4.81 sec: 1.02x slower                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                   |
| async_tree_io_tg          | 825 ms                                                 | 848 ms: 1.03x slower                                                    |
| json_loads                | 27.0 us                                                | 27.8 us: 1.03x slower                                                   |
| go                        | 142 ms                                                 | 146 ms: 1.03x slower                                                    |
| regex_effbot              | 3.88 ms                                                | 4.02 ms: 1.03x slower                                                   |
| sqlglot_normalize         | 107 ms                                                 | 111 ms: 1.03x slower                                                    |
| generators                | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                   |
| 2to3                      | 265 ms                                                 | 275 ms: 1.04x slower                                                    |
| regex_compile             | 131 ms                                                 | 136 ms: 1.04x slower                                                    |
| regex_dna                 | 220 ms                                                 | 229 ms: 1.04x slower                                                    |
| coroutines                | 22.5 ms                                                | 23.5 ms: 1.04x slower                                                   |
| django_template           | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                   |
| nqueens                   | 80.6 ms                                                | 85.1 ms: 1.06x slower                                                   |
| chaos                     | 58.4 ms                                                | 61.7 ms: 1.06x slower                                                   |
| async_generators          | 433 ms                                                 | 458 ms: 1.06x slower                                                    |
| typing_runtime_protocols  | 159 us                                                 | 169 us: 1.06x slower                                                    |
| dulwich_log               | 63.0 ms                                                | 67.0 ms: 1.06x slower                                                   |
| scimark_sor               | 122 ms                                                 | 131 ms: 1.07x slower                                                    |
| sympy_expand              | 462 ms                                                 | 496 ms: 1.07x slower                                                    |
| dask                      | 338 ms                                                 | 363 ms: 1.08x slower                                                    |
| sympy_str                 | 274 ms                                                 | 295 ms: 1.08x slower                                                    |
| hexiom                    | 6.13 ms                                                | 6.65 ms: 1.09x slower                                                   |
| scimark_lu                | 115 ms                                                 | 126 ms: 1.10x slower                                                    |
| sympy_sum                 | 150 ms                                                 | 164 ms: 1.10x slower                                                    |
| pylint                    | 313 ms                                                 | 344 ms: 1.10x slower                                                    |
| genshi_text               | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                   |
| coverage                  | 83.7 ms                                                | 92.4 ms: 1.10x slower                                                   |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.10x slower                                                   |
| sympy_integrate           | 19.9 ms                                                | 22.0 ms: 1.10x slower                                                   |
| docutils                  | 2.58 sec                                               | 2.90 sec: 1.12x slower                                                  |
| deltablue                 | 3.15 ms                                                | 3.60 ms: 1.14x slower                                                   |
| genshi_xml                | 50.3 ms                                                | 58.7 ms: 1.17x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (11): json, pycparser, async_tree_cpu_io_mixed_tg, meteor_contest, asyncio_websockets, bench_mp_pool, pidigits, json_dumps, sqlglot_parse, thrift, async_tree_io
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 64.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x