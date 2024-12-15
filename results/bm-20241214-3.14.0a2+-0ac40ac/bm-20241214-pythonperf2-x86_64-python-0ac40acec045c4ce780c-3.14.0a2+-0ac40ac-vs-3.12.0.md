# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.032x faster
- HPT reliability: 98.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 639 ms: 1.65x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 654 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                         |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 360 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.36x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 524 ms: 1.33x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.51x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| float          | 76.6 ms                                                      | 77.9 ms: 1.02x slower                                                        |
| nbody          | 88.0 ms                                                      | 97.3 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.24 ms: 1.10x faster                                                        |
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 97.0 ms: 1.06x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| json_loads           | 24.4 us                                                      | 23.9 us: 1.02x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.9 ms: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.6 ms: 1.04x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 331 us: 1.04x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 218 us: 1.04x slower                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.4 ms: 1.05x faster                                                        |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 639 ms: 1.65x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 654 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                         |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 360 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.36x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 524 ms: 1.33x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.6 ms: 1.31x faster                                                        |
| deepcopy                   | 368 us                                                       | 285 us: 1.29x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.6 us: 1.24x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.7 us: 1.24x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 140 ms: 1.14x faster                                                         |
| go                         | 150 ms                                                       | 133 ms: 1.12x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 72.3 ms: 1.11x faster                                                        |
| raytrace                   | 298 ms                                                       | 269 ms: 1.11x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.24 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.3 ms: 1.09x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.00 us: 1.07x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.0 ms: 1.06x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.37 us: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| django_template            | 38.2 ms                                                      | 36.4 ms: 1.05x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 87.7 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.46 sec: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                         |
| chaos                      | 64.0 ms                                                      | 62.0 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.7 ms: 1.03x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.20 sec: 1.03x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                        |
| scimark_fft                | 301 ms                                                       | 295 ms: 1.02x faster                                                         |
| json_loads                 | 24.4 us                                                      | 23.9 us: 1.02x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.35 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.9 ms: 1.01x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.6 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.75 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.01x faster                                                         |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| json                       | 5.12 ms                                                      | 5.07 ms: 1.01x faster                                                        |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 57.7 ms: 1.00x slower                                                        |
| fannkuch                   | 350 ms                                                       | 353 ms: 1.01x slower                                                         |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                         |
| float                      | 76.6 ms                                                      | 77.9 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| sympy_expand               | 484 ms                                                       | 493 ms: 1.02x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.5 ms: 1.03x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 60.6 ms: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 331 us: 1.04x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 218 us: 1.04x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.21 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.44 ms: 1.06x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                         |
| pyflate                    | 439 ms                                                       | 473 ms: 1.08x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.50 ms: 1.08x slower                                                        |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                        |
| async_generators           | 390 ms                                                       | 431 ms: 1.10x slower                                                         |
| nbody                      | 88.0 ms                                                      | 97.3 ms: 1.11x slower                                                        |
| richards                   | 45.7 ms                                                      | 50.6 ms: 1.11x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| richards_super             | 51.3 ms                                                      | 56.9 ms: 1.11x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.74 ms: 1.11x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                        |
| coverage                   | 66.7 ms                                                      | 77.3 ms: 1.16x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                         |
| mypy2                      | 830 ms                                                       | 1.03 sec: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.75 ms: 1.73x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.59 ms: 1.89x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.21 sec: 253.20x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (4): bench_thread_pool, pprint_pformat, pprint_safe_repr, docutils
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 98.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x