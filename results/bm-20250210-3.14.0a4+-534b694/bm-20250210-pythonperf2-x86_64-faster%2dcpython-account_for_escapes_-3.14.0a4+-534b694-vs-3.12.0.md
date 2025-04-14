# Results vs. 3.12.0

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 534b694
- commit date: 2025-02-10
- overall geometric mean: 1.046x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 650 ms: 1.62x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 649 ms: 1.61x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.56x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 354 ms: 1.54x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 521 ms: 1.34x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.3 ms: 1.09x faster                                                                  |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                                   |
| nbody          | 88.0 ms                                                      | 90.8 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.15 ms: 1.14x faster                                                                  |
| regex_compile  | 144 ms                                                       | 135 ms: 1.06x faster                                                                   |
| regex_dna      | 239 ms                                                       | 242 ms: 1.02x slower                                                                   |
| regex_v8       | 23.6 ms                                                      | 26.6 ms: 1.12x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 94.8 ms: 1.09x faster                                                                  |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 83.7 ms: 1.03x faster                                                                  |
| unpickle_pure_python | 210 us                                                       | 212 us: 1.01x slower                                                                   |
| xml_etree_process    | 58.4 ms                                                      | 60.0 ms: 1.03x slower                                                                  |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                                   |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.10x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.15x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.8 ms: 1.06x faster                                                                  |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 650 ms: 1.62x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 649 ms: 1.61x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.56x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 354 ms: 1.54x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 521 ms: 1.34x faster                                                                   |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                                   |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.29x faster                                                                  |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 29.1 us: 1.26x faster                                                                  |
| go                         | 150 ms                                                       | 127 ms: 1.18x faster                                                                   |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.15x faster                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.15 ms: 1.14x faster                                                                  |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                                   |
| spectral_norm              | 91.6 ms                                                      | 83.7 ms: 1.09x faster                                                                  |
| float                      | 76.6 ms                                                      | 70.3 ms: 1.09x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.3 ms: 1.09x faster                                                                  |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 73.9 ms: 1.09x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 94.8 ms: 1.09x faster                                                                  |
| raytrace                   | 298 ms                                                       | 275 ms: 1.08x faster                                                                   |
| logging_format             | 7.48 us                                                      | 6.93 us: 1.08x faster                                                                  |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                                   |
| logging_simple             | 6.71 us                                                      | 6.26 us: 1.07x faster                                                                  |
| chaos                      | 64.0 ms                                                      | 60.0 ms: 1.07x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                                   |
| regex_compile              | 144 ms                                                       | 135 ms: 1.06x faster                                                                   |
| django_template            | 38.2 ms                                                      | 35.8 ms: 1.06x faster                                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 94.5 ms: 1.05x faster                                                                  |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                                   |
| meteor_contest             | 128 ms                                                       | 123 ms: 1.04x faster                                                                   |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                                   |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                                 |
| pprint_safe_repr           | 807 ms                                                       | 780 ms: 1.04x faster                                                                   |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 83.7 ms: 1.03x faster                                                                  |
| pyflate                    | 439 ms                                                       | 426 ms: 1.03x faster                                                                   |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.75 ms: 1.01x faster                                                                  |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.36 ms: 1.01x faster                                                                  |
| richards                   | 45.7 ms                                                      | 45.4 ms: 1.01x faster                                                                  |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                                   |
| sqlglot_normalize          | 116 ms                                                       | 116 ms: 1.00x slower                                                                   |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 51.9 ms: 1.01x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 212 us: 1.01x slower                                                                   |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.02x slower                                                                   |
| scimark_fft                | 301 ms                                                       | 306 ms: 1.02x slower                                                                   |
| sympy_expand               | 484 ms                                                       | 494 ms: 1.02x slower                                                                   |
| dulwich_log                | 65.4 ms                                                      | 67.0 ms: 1.03x slower                                                                  |
| logging_silent             | 94.4 ns                                                      | 96.9 ns: 1.03x slower                                                                  |
| xml_etree_process          | 58.4 ms                                                      | 60.0 ms: 1.03x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 90.8 ms: 1.03x slower                                                                  |
| hexiom                     | 5.96 ms                                                      | 6.16 ms: 1.03x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.35 ms: 1.04x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                                   |
| python_startup_no_site     | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                                  |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                                                   |
| async_generators           | 390 ms                                                       | 413 ms: 1.06x slower                                                                   |
| json                       | 5.12 ms                                                      | 5.43 ms: 1.06x slower                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.56 ms: 1.08x slower                                                                  |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.10x slower                                                                  |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                                  |
| telco                      | 6.96 ms                                                      | 7.76 ms: 1.11x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.12x slower                                                                   |
| regex_v8                   | 23.6 ms                                                      | 26.6 ms: 1.12x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.15x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                                  |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.77 ms: 1.74x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 6.35 ms: 1.83x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 1.32 sec: 277.62x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                           |

Benchmark hidden because not significant (6): pycparser, bench_thread_pool, nqueens, asyncio_websockets, sqlglot_optimize, docutils
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250210-3.14.0a4+-534b694/bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x