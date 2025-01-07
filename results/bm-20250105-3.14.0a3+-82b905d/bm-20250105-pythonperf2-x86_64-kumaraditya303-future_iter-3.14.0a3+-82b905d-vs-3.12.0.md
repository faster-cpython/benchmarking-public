# Results vs. 3.12.0

- fork: kumaraditya303
- ref: future_iter
- machine: linux-x86_64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.048x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 280 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 604 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 320 ms: 1.69x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 618 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 262 ms: 1.64x faster                                                        |
| async_tree_none            | 452 ms                                                       | 282 ms: 1.60x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 346 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 489 ms: 1.43x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 512 ms: 1.36x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.8 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 86.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.25 ms: 1.10x faster                                                       |
| regex_compile  | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.4 ms: 1.08x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 201 us: 1.04x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 83.2 ms: 1.04x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                       |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                       |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 604 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 320 ms: 1.69x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 618 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 262 ms: 1.64x faster                                                        |
| async_tree_none            | 452 ms                                                       | 282 ms: 1.60x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 346 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 489 ms: 1.43x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 512 ms: 1.36x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.6 ms: 1.31x faster                                                       |
| deepcopy                   | 368 us                                                       | 282 us: 1.31x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.7 us: 1.24x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 30.7 us: 1.20x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| go                         | 150 ms                                                       | 126 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                       |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.6 ms: 1.11x faster                                                       |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.25 ms: 1.10x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 73.9 ms: 1.09x faster                                                       |
| django_template            | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.8 ms: 1.08x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.92 us: 1.08x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.4 ms: 1.08x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_compile              | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| float                      | 76.6 ms                                                      | 71.8 ms: 1.07x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.55 sec: 1.07x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.36 us: 1.05x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 767 ms: 1.05x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                      |
| chaos                      | 64.0 ms                                                      | 60.9 ms: 1.05x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 87.7 ms: 1.05x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 201 us: 1.04x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.32 ms: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.8 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 83.2 ms: 1.04x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.03x faster                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.72 ms: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 926 us: 1.03x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.2 ms: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 280 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.01x faster                                                        |
| json                       | 5.12 ms                                                      | 5.07 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 90.5 ms: 1.01x slower                                                       |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                       |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.3 ms: 1.01x slower                                                       |
| richards_super             | 51.3 ms                                                      | 52.2 ms: 1.02x slower                                                       |
| richards                   | 45.7 ms                                                      | 46.6 ms: 1.02x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.08 ms: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.03x slower                                                       |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                        |
| pyflate                    | 439 ms                                                       | 451 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.2 ns: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                                       |
| fannkuch                   | 350 ms                                                       | 373 ms: 1.07x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.64 ms: 1.10x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                       |
| async_generators           | 390 ms                                                       | 437 ms: 1.12x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.84 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| coverage                   | 66.7 ms                                                      | 77.3 ms: 1.16x slower                                                       |
| mypy2                      | 830 ms                                                       | 1.02 sec: 1.23x slower                                                      |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.79 ms: 1.75x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.63 ms: 1.91x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 891 ms: 186.98x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (5): asyncio_websockets, pycparser, sqlglot_optimize, docutils, scimark_fft
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x