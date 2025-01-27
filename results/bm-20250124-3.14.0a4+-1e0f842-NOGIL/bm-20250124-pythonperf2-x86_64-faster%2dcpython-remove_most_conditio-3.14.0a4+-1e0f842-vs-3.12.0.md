# Results vs. 3.12.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.072x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 336 ms: 1.18x slower                                                                   |
| docutils       | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 577 ms: 1.82x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 256 ms: 1.68x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 329 ms: 1.64x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 364 ms: 1.49x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 495 ms: 1.41x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 532 ms: 1.31x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.07x faster                                                                   |
| float          | 76.6 ms                                                      | 75.0 ms: 1.02x faster                                                                  |
| nbody          | 88.0 ms                                                      | 138 ms: 1.57x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.13x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.16 ms: 1.13x faster                                                                  |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                                   |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                                  |
| regex_compile  | 144 ms                                                       | 156 ms: 1.08x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 89.3 ms: 1.15x faster                                                                  |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.41 sec: 1.12x slower                                                                 |
| json_loads           | 24.4 us                                                      | 27.7 us: 1.14x slower                                                                  |
| unpickle_pure_python | 210 us                                                       | 242 us: 1.16x slower                                                                   |
| xml_etree_generate   | 86.1 ms                                                      | 100 ms: 1.16x slower                                                                   |
| pickle_pure_python   | 318 us                                                       | 380 us: 1.19x slower                                                                   |
| xml_etree_process    | 58.4 ms                                                      | 72.4 ms: 1.24x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 13.5 ms: 1.32x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 18.6 ms: 1.60x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 47.2 ms: 1.24x slower                                                                  |
| mako            | 10.0 ms                                                      | 18.0 ms: 1.80x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.49x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 577 ms: 1.82x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 256 ms: 1.68x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 329 ms: 1.64x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 364 ms: 1.49x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 495 ms: 1.41x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 532 ms: 1.31x faster                                                                   |
| generators                 | 37.4 ms                                                      | 31.1 ms: 1.20x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 89.3 ms: 1.15x faster                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.16 ms: 1.13x faster                                                                  |
| deepcopy                   | 368 us                                                       | 341 us: 1.08x faster                                                                   |
| sqlite_synth               | 2.77 us                                                      | 2.59 us: 1.07x faster                                                                  |
| pidigits                   | 265 ms                                                       | 249 ms: 1.07x faster                                                                   |
| coroutines                 | 23.0 ms                                                      | 21.8 ms: 1.05x faster                                                                  |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                                   |
| comprehensions             | 21.9 us                                                      | 21.2 us: 1.03x faster                                                                  |
| float                      | 76.6 ms                                                      | 75.0 ms: 1.02x faster                                                                  |
| asyncio_websockets         | 387 ms                                                       | 380 ms: 1.02x faster                                                                   |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                                   |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                                   |
| deepcopy_memo              | 36.8 us                                                      | 37.4 us: 1.02x slower                                                                  |
| docutils                   | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                                                 |
| logging_format             | 7.48 us                                                      | 7.95 us: 1.06x slower                                                                  |
| logging_simple             | 6.71 us                                                      | 7.16 us: 1.07x slower                                                                  |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                                  |
| dulwich_log                | 65.4 ms                                                      | 70.0 ms: 1.07x slower                                                                  |
| mdp                        | 2.57 sec                                                     | 2.77 sec: 1.08x slower                                                                 |
| regex_compile              | 144 ms                                                       | 156 ms: 1.08x slower                                                                   |
| json                       | 5.12 ms                                                      | 5.54 ms: 1.08x slower                                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 3.65 us: 1.08x slower                                                                  |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                                   |
| sympy_sum                  | 162 ms                                                       | 177 ms: 1.09x slower                                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.7 ms: 1.11x slower                                                                  |
| scimark_sor                | 109 ms                                                       | 121 ms: 1.11x slower                                                                   |
| spectral_norm              | 91.6 ms                                                      | 102 ms: 1.11x slower                                                                   |
| sqlalchemy_declarative     | 159 ms                                                       | 177 ms: 1.11x slower                                                                   |
| chaos                      | 64.0 ms                                                      | 71.3 ms: 1.11x slower                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 900 ms: 1.12x slower                                                                   |
| tomli_loads                | 2.16 sec                                                     | 2.41 sec: 1.12x slower                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.86 sec: 1.12x slower                                                                 |
| sympy_str                  | 302 ms                                                       | 341 ms: 1.13x slower                                                                   |
| pyflate                    | 439 ms                                                       | 496 ms: 1.13x slower                                                                   |
| sqlglot_normalize          | 116 ms                                                       | 131 ms: 1.13x slower                                                                   |
| json_loads                 | 24.4 us                                                      | 27.7 us: 1.14x slower                                                                  |
| sympy_integrate            | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 65.9 ms: 1.15x slower                                                                  |
| raytrace                   | 298 ms                                                       | 342 ms: 1.15x slower                                                                   |
| scimark_fft                | 301 ms                                                       | 347 ms: 1.15x slower                                                                   |
| crypto_pyaes               | 80.3 ms                                                      | 92.9 ms: 1.16x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 242 us: 1.16x slower                                                                   |
| xml_etree_generate         | 86.1 ms                                                      | 100 ms: 1.16x slower                                                                   |
| gc_traversal               | 3.48 ms                                                      | 4.05 ms: 1.17x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.62 ms: 1.17x slower                                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 2.09 ms: 1.18x slower                                                                  |
| 2to3                       | 285 ms                                                       | 336 ms: 1.18x slower                                                                   |
| sympy_expand               | 484 ms                                                       | 575 ms: 1.19x slower                                                                   |
| pickle_pure_python         | 318 us                                                       | 380 us: 1.19x slower                                                                   |
| async_generators           | 390 ms                                                       | 469 ms: 1.20x slower                                                                   |
| hexiom                     | 5.96 ms                                                      | 7.21 ms: 1.21x slower                                                                  |
| meteor_contest             | 128 ms                                                       | 155 ms: 1.21x slower                                                                   |
| scimark_lu                 | 98.8 ms                                                      | 120 ms: 1.22x slower                                                                   |
| django_template            | 38.2 ms                                                      | 47.2 ms: 1.24x slower                                                                  |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.24x slower                                                                   |
| xml_etree_process          | 58.4 ms                                                      | 72.4 ms: 1.24x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 87.9 ms: 1.27x slower                                                                  |
| richards                   | 45.7 ms                                                      | 58.5 ms: 1.28x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 67.3 ms: 1.31x slower                                                                  |
| telco                      | 6.96 ms                                                      | 9.13 ms: 1.31x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 13.5 ms: 1.32x slower                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.66 ms: 1.35x slower                                                                  |
| fannkuch                   | 350 ms                                                       | 475 ms: 1.36x slower                                                                   |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 4.51 ms: 1.39x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 221 us: 1.46x slower                                                                   |
| coverage                   | 66.7 ms                                                      | 100 ms: 1.50x slower                                                                   |
| bench_thread_pool          | 950 us                                                       | 1.47 ms: 1.54x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 138 ms: 1.57x slower                                                                   |
| python_startup             | 11.6 ms                                                      | 18.6 ms: 1.60x slower                                                                  |
| mako                       | 10.0 ms                                                      | 18.0 ms: 1.80x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 48.8 ms: 10.25x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                                           |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250124-3.14.0a4+-1e0f842-NOGIL/bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.072x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.26x