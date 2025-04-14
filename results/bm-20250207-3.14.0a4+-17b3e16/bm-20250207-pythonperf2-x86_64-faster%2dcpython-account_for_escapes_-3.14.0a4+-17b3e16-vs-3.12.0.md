# Results vs. 3.12.0

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 17b3e16
- commit date: 2025-02-07
- overall geometric mean: 1.045x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 645 ms: 1.63x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 654 ms: 1.59x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 288 ms: 1.57x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 353 ms: 1.54x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.2 ms: 1.09x faster                                                                  |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                                   |
| nbody          | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.19 ms: 1.12x faster                                                                  |
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                                   |
| regex_dna      | 239 ms                                                       | 250 ms: 1.05x slower                                                                   |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.1 ms: 1.08x faster                                                                  |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| xml_etree_generate   | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                                  |
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                                 |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.02x faster                                                                   |
| xml_etree_process    | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                                  |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                                   |
| json_loads           | 24.4 us                                                      | 26.5 us: 1.09x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.9 ms: 1.06x faster                                                                  |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 645 ms: 1.63x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 654 ms: 1.59x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 288 ms: 1.57x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 353 ms: 1.54x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                                   |
| deepcopy                   | 368 us                                                       | 282 us: 1.31x faster                                                                   |
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                                  |
| generators                 | 37.4 ms                                                      | 30.2 ms: 1.24x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 29.7 us: 1.24x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                                  |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                                   |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.5 ms: 1.12x faster                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.19 ms: 1.12x faster                                                                  |
| spectral_norm              | 91.6 ms                                                      | 82.5 ms: 1.11x faster                                                                  |
| sqlalchemy_declarative     | 159 ms                                                       | 144 ms: 1.11x faster                                                                   |
| float                      | 76.6 ms                                                      | 70.2 ms: 1.09x faster                                                                  |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 95.1 ms: 1.08x faster                                                                  |
| raytrace                   | 298 ms                                                       | 277 ms: 1.08x faster                                                                   |
| crypto_pyaes               | 80.3 ms                                                      | 75.0 ms: 1.07x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                                   |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| chaos                      | 64.0 ms                                                      | 60.2 ms: 1.06x faster                                                                  |
| django_template            | 38.2 ms                                                      | 35.9 ms: 1.06x faster                                                                  |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.8 ms: 1.05x faster                                                                  |
| logging_format             | 7.48 us                                                      | 7.14 us: 1.05x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 94.4 ms: 1.05x faster                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.04x faster                                                                 |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                                   |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                                   |
| pprint_safe_repr           | 807 ms                                                       | 776 ms: 1.04x faster                                                                   |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                                 |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                                  |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                                   |
| logging_simple             | 6.71 us                                                      | 6.50 us: 1.03x faster                                                                  |
| bench_thread_pool          | 950 us                                                       | 928 us: 1.02x faster                                                                   |
| sqlglot_transpile          | 1.78 ms                                                      | 1.74 ms: 1.02x faster                                                                  |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.02x faster                                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.36 ms: 1.02x faster                                                                  |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                                   |
| scimark_sor                | 109 ms                                                       | 109 ms: 1.00x faster                                                                   |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                                   |
| xml_etree_process          | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                                  |
| dulwich_log                | 65.4 ms                                                      | 66.3 ms: 1.01x slower                                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                                  |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                                 |
| richards                   | 45.7 ms                                                      | 46.7 ms: 1.02x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 495 ms: 1.02x slower                                                                   |
| logging_silent             | 94.4 ns                                                      | 96.9 ns: 1.03x slower                                                                  |
| async_generators           | 390 ms                                                       | 402 ms: 1.03x slower                                                                   |
| hexiom                     | 5.96 ms                                                      | 6.16 ms: 1.03x slower                                                                  |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                                   |
| deltablue                  | 3.24 ms                                                      | 3.37 ms: 1.04x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 53.4 ms: 1.04x slower                                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                                   |
| regex_dna                  | 239 ms                                                       | 250 ms: 1.05x slower                                                                   |
| json                       | 5.12 ms                                                      | 5.46 ms: 1.07x slower                                                                  |
| json_loads                 | 24.4 us                                                      | 26.5 us: 1.09x slower                                                                  |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                                  |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.12x slower                                                                   |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.73 ms: 1.12x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                                  |
| telco                      | 6.96 ms                                                      | 8.04 ms: 1.15x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 78.3 ms: 1.17x slower                                                                  |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.76 ms: 1.73x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 6.12 ms: 1.76x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 1.03 sec: 216.36x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                           |

Benchmark hidden because not significant (6): docutils, sqlglot_optimize, 2to3, pyflate, nqueens, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250207-3.14.0a4+-17b3e16/bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x