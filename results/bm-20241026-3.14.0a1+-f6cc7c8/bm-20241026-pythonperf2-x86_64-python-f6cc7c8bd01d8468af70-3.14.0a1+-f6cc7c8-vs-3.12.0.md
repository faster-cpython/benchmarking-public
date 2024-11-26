# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.014x faster
- HPT reliability: 93.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                       |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 373 ms: 1.45x faster                                                         |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 417 ms: 1.30x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 837 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 560 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 563 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 863 ms: 1.22x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 91.1 ms: 1.04x slower                                                        |
| float          | 76.6 ms                                                      | 81.4 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.52 ms: 1.02x faster                                                        |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.4 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.01x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.3 ms: 1.01x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.47 sec: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.7 ms: 1.35x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 40.2 ms: 1.05x slower                                                        |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 373 ms: 1.45x faster                                                         |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 417 ms: 1.30x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 291 us: 1.27x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.2 us: 1.26x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 837 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 560 ms: 1.24x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.24x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 563 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 863 ms: 1.22x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 72.3 ms: 1.11x faster                                                        |
| go                         | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.09x faster                                                        |
| async_generators           | 390 ms                                                       | 365 ms: 1.07x faster                                                         |
| raytrace                   | 298 ms                                                       | 279 ms: 1.07x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                         |
| bench_thread_pool          | 950 us                                                       | 901 us: 1.05x faster                                                         |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.21 us: 1.04x faster                                                        |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.5 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.03x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 96.4 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                        |
| scimark_fft                | 301 ms                                                       | 294 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.4 ms: 1.02x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.60 us: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.52 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.01x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 796 ms: 1.01x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                         |
| chaos                      | 64.0 ms                                                      | 63.5 ms: 1.01x faster                                                        |
| fannkuch                   | 350 ms                                                       | 352 ms: 1.01x slower                                                         |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.01x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 90.4 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                        |
| json                       | 5.12 ms                                                      | 5.17 ms: 1.01x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.3 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.7 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.32 ms: 1.03x slower                                                        |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                         |
| nbody                      | 88.0 ms                                                      | 91.1 ms: 1.04x slower                                                        |
| sympy_expand               | 484 ms                                                       | 502 ms: 1.04x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 98.2 ns: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                         |
| django_template            | 38.2 ms                                                      | 40.2 ms: 1.05x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.42 ms: 1.06x slower                                                        |
| float                      | 76.6 ms                                                      | 81.4 ms: 1.06x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.07x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.4 ms: 1.07x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.40 ms: 1.07x slower                                                        |
| richards_super             | 51.3 ms                                                      | 55.4 ms: 1.08x slower                                                        |
| richards                   | 45.7 ms                                                      | 49.5 ms: 1.08x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 99.3 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 479 ms: 1.09x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.94 ms: 1.14x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.47 sec: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 178 us: 1.17x slower                                                         |
| coverage                   | 66.7 ms                                                      | 79.3 ms: 1.19x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.7 ms: 1.35x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.31 ms: 1.53x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.98 ms: 1.87x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.11 sec: 442.69x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, dulwich_log, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 93.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x