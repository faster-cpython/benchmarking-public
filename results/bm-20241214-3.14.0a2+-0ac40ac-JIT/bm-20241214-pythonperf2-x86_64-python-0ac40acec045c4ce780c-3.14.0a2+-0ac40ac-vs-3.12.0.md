# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.017x faster
- HPT reliability: 52.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 640 ms: 1.65x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 329 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 648 ms: 1.61x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                         |
| async_tree_none            | 452 ms                                                       | 293 ms: 1.54x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 359 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 500 ms: 1.40x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| float          | 76.6 ms                                                      | 72.9 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 92.2 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.31 ms: 1.08x faster                                                        |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| regex_dna      | 239 ms                                                       | 235 ms: 1.02x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 94.0 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.2 ms: 1.07x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 200 us: 1.05x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 56.5 ms: 1.03x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.04x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 338 us: 1.06x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.38 ms: 1.07x faster                                                        |
| django_template | 38.2 ms                                                      | 40.2 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 640 ms: 1.65x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 329 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 648 ms: 1.61x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                         |
| async_tree_none            | 452 ms                                                       | 293 ms: 1.54x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 359 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 500 ms: 1.40x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 28.5 us: 1.29x faster                                                        |
| deepcopy                   | 368 us                                                       | 295 us: 1.25x faster                                                         |
| comprehensions             | 21.9 us                                                      | 18.9 us: 1.16x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.8 ms: 1.13x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.12x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 94.0 ms: 1.09x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.1 ms: 1.09x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.31 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.2 ms: 1.07x faster                                                        |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.38 ms: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.4 ms: 1.07x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| float                      | 76.6 ms                                                      | 72.9 ms: 1.05x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.15 us: 1.05x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 200 us: 1.05x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 56.5 ms: 1.03x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 157 ms: 1.03x faster                                                         |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.53 us: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.02x faster                                                         |
| go                         | 150 ms                                                       | 147 ms: 1.02x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 98.2 ms: 1.01x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 91.9 ms: 1.00x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                       |
| json                       | 5.12 ms                                                      | 5.16 ms: 1.01x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                        |
| sympy_str                  | 302 ms                                                       | 305 ms: 1.01x slower                                                         |
| scimark_fft                | 301 ms                                                       | 304 ms: 1.01x slower                                                         |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.04x slower                                                        |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.9 ms: 1.04x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                        |
| chaos                      | 64.0 ms                                                      | 66.8 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                        |
| nbody                      | 88.0 ms                                                      | 92.2 ms: 1.05x slower                                                        |
| generators                 | 37.4 ms                                                      | 39.3 ms: 1.05x slower                                                        |
| django_template            | 38.2 ms                                                      | 40.2 ms: 1.05x slower                                                        |
| richards                   | 45.7 ms                                                      | 48.4 ms: 1.06x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 338 us: 1.06x slower                                                         |
| fannkuch                   | 350 ms                                                       | 374 ms: 1.07x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 124 ms: 1.07x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.02 ms: 1.07x slower                                                        |
| sympy_expand               | 484 ms                                                       | 519 ms: 1.07x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 61.9 ms: 1.08x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.53 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                        |
| richards_super             | 51.3 ms                                                      | 55.8 ms: 1.09x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 99.4 ms: 1.11x slower                                                        |
| raytrace                   | 298 ms                                                       | 330 ms: 1.11x slower                                                         |
| coverage                   | 66.7 ms                                                      | 76.8 ms: 1.15x slower                                                        |
| async_generators           | 390 ms                                                       | 465 ms: 1.19x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.13 ms: 1.20x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 184 us: 1.21x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.13 ms: 1.22x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.04 sec: 1.25x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.69 ms: 1.69x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.53 ms: 1.88x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.01 sec: 211.28x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (4): pyflate, pycparser, asyncio_websockets, pprint_safe_repr
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 52.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x