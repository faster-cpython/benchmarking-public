# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.217x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 391 ms: 1.37x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.18 sec: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.23x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 785 ms: 1.34x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 811 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 344 ms: 1.25x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 445 ms: 1.21x faster                                                         |
| async_tree_none            | 452 ms                                                       | 373 ms: 1.21x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 463 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 602 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 625 ms: 1.11x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 247 ms: 1.07x faster                                                         |
| nbody          | 88.0 ms                                                      | 137 ms: 1.56x slower                                                         |
| float          | 76.6 ms                                                      | 130 ms: 1.70x slower                                                         |
| Geometric mean | (ref)                                                        | 1.35x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.32 ms: 1.07x faster                                                        |
| regex_dna      | 239 ms                                                       | 242 ms: 1.02x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                        |
| regex_compile  | 144 ms                                                       | 182 ms: 1.27x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.7 ms: 1.07x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| json_loads           | 24.4 us                                                      | 27.5 us: 1.13x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 102 ms: 1.18x slower                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.71 sec: 1.26x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 81.2 ms: 1.39x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.3 ms: 1.39x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 330 us: 1.58x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 525 us: 1.65x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.25x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.3 ms: 1.42x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.7 ms: 1.70x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.55x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 54.3 ms: 1.42x slower                                                        |
| mako            | 10.0 ms                                                      | 19.3 ms: 1.93x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.66x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 785 ms: 1.34x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 811 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 344 ms: 1.25x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 445 ms: 1.21x faster                                                         |
| async_tree_none            | 452 ms                                                       | 373 ms: 1.21x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 463 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 602 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 625 ms: 1.11x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.32 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.7 ms: 1.07x faster                                                        |
| pidigits                   | 265 ms                                                       | 247 ms: 1.07x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 17.6 ms: 1.07x faster                                                        |
| deepcopy                   | 368 us                                                       | 350 us: 1.05x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.72 us: 1.02x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 380 ms: 1.02x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 23.2 ms: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.02x slower                                                         |
| generators                 | 37.4 ms                                                      | 38.6 ms: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.59 ms: 1.09x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 40.4 us: 1.10x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.11x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.18 sec: 1.11x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 3.88 ms: 1.11x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.90 sec: 1.13x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.81 us: 1.13x slower                                                        |
| json_loads                 | 24.4 us                                                      | 27.5 us: 1.13x slower                                                        |
| scimark_fft                | 301 ms                                                       | 343 ms: 1.14x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 102 ms: 1.18x slower                                                         |
| meteor_contest             | 128 ms                                                       | 157 ms: 1.22x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 110 ms: 1.23x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 99.6 ms: 1.24x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 144 ms: 1.24x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 81.5 ms: 1.25x slower                                                        |
| comprehensions             | 21.9 us                                                      | 27.3 us: 1.25x slower                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 23.4 ms: 1.25x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 30.0 ms: 1.25x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 72.2 ms: 1.26x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.71 sec: 1.26x slower                                                       |
| regex_compile              | 144 ms                                                       | 182 ms: 1.27x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.59 sec: 1.29x slower                                                       |
| sqlalchemy_declarative     | 159 ms                                                       | 210 ms: 1.32x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 1.07 sec: 1.32x slower                                                       |
| async_generators           | 390 ms                                                       | 519 ms: 1.33x slower                                                         |
| sympy_str                  | 302 ms                                                       | 403 ms: 1.33x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 2.21 sec: 1.33x slower                                                       |
| telco                      | 6.96 ms                                                      | 9.49 ms: 1.36x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.76 ms: 1.37x slower                                                        |
| 2to3                       | 285 ms                                                       | 391 ms: 1.37x slower                                                         |
| logging_format             | 7.48 us                                                      | 10.3 us: 1.38x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 81.2 ms: 1.39x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 14.3 ms: 1.39x slower                                                        |
| logging_simple             | 6.71 us                                                      | 9.49 us: 1.41x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 12.3 ms: 1.42x slower                                                        |
| django_template            | 38.2 ms                                                      | 54.3 ms: 1.42x slower                                                        |
| fannkuch                   | 350 ms                                                       | 509 ms: 1.45x slower                                                         |
| sympy_sum                  | 162 ms                                                       | 239 ms: 1.48x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 226 us: 1.49x slower                                                         |
| sympy_expand               | 484 ms                                                       | 739 ms: 1.53x slower                                                         |
| pyflate                    | 439 ms                                                       | 680 ms: 1.55x slower                                                         |
| nbody                      | 88.0 ms                                                      | 137 ms: 1.56x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 330 us: 1.58x slower                                                         |
| coverage                   | 66.7 ms                                                      | 105 ms: 1.58x slower                                                         |
| chaos                      | 64.0 ms                                                      | 101 ms: 1.58x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 9.76 ms: 1.64x slower                                                        |
| richards_super             | 51.3 ms                                                      | 84.1 ms: 1.64x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 525 us: 1.65x slower                                                         |
| mypy2                      | 830 ms                                                       | 1.37 sec: 1.66x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.59 ms: 1.67x slower                                                        |
| python_startup             | 11.6 ms                                                      | 19.7 ms: 1.70x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.70 ms: 1.70x slower                                                        |
| float                      | 76.6 ms                                                      | 130 ms: 1.70x slower                                                         |
| richards                   | 45.7 ms                                                      | 78.2 ms: 1.71x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.04 ms: 1.71x slower                                                        |
| raytrace                   | 298 ms                                                       | 513 ms: 1.72x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 121 ms: 1.76x slower                                                         |
| go                         | 150 ms                                                       | 266 ms: 1.77x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 179 ms: 1.82x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 174 ns: 1.84x slower                                                         |
| scimark_sor                | 109 ms                                                       | 202 ms: 1.85x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 2.58 ms: 1.87x slower                                                        |
| mako                       | 10.0 ms                                                      | 19.3 ms: 1.93x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 7.77 ms: 2.40x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 53.8 ms: 11.30x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.32x slower                                                                 |
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.217x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.22x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.24x