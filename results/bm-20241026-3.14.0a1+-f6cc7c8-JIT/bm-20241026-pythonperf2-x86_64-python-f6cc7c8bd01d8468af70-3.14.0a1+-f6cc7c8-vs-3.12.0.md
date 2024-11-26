# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.010x slower
- HPT reliability: 64.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 317 ms: 1.11x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.20 sec: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.41x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                         |
| async_tree_none            | 452 ms                                                       | 334 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 333 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 836 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 558 ms: 1.25x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 838 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 573 ms: 1.21x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 83.8 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                        |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.1 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.9 ms: 1.06x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 221 us: 1.06x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 336 us: 1.06x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.8 ms: 1.36x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.49 ms: 1.05x faster                                                        |
| django_template | 38.2 ms                                                      | 44.4 ms: 1.16x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.41x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                         |
| async_tree_none            | 452 ms                                                       | 334 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 333 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 836 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 558 ms: 1.25x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 838 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 573 ms: 1.21x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 31.2 us: 1.18x faster                                                        |
| deepcopy                   | 368 us                                                       | 319 us: 1.15x faster                                                         |
| comprehensions             | 21.9 us                                                      | 19.4 us: 1.13x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.0 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.14 us: 1.07x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.9 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.49 ms: 1.05x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.13 us: 1.05x faster                                                        |
| nbody                      | 88.0 ms                                                      | 83.8 ms: 1.05x faster                                                        |
| richards                   | 45.7 ms                                                      | 43.7 ms: 1.05x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| richards_super             | 51.3 ms                                                      | 49.3 ms: 1.04x faster                                                        |
| scimark_fft                | 301 ms                                                       | 290 ms: 1.04x faster                                                         |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 63.2 ms: 1.03x faster                                                        |
| async_generators           | 390 ms                                                       | 379 ms: 1.03x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 96.0 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.57 us: 1.02x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.4 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 795 ms: 1.02x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 69.7 ms: 1.01x slower                                                        |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                                        |
| go                         | 150 ms                                                       | 153 ms: 1.02x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 93.6 ms: 1.02x slower                                                        |
| pyflate                    | 439 ms                                                       | 450 ms: 1.03x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                        |
| generators                 | 37.4 ms                                                      | 38.8 ms: 1.04x slower                                                        |
| raytrace                   | 298 ms                                                       | 310 ms: 1.04x slower                                                         |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                         |
| float                      | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.05x slower                                                       |
| sqlalchemy_declarative     | 159 ms                                                       | 168 ms: 1.05x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 221 us: 1.06x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 336 us: 1.06x slower                                                         |
| fannkuch                   | 350 ms                                                       | 372 ms: 1.06x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.1 ms: 1.06x slower                                                        |
| sympy_str                  | 302 ms                                                       | 323 ms: 1.07x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                        |
| chaos                      | 64.0 ms                                                      | 69.2 ms: 1.08x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 176 ms: 1.09x slower                                                         |
| sympy_expand               | 484 ms                                                       | 535 ms: 1.11x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.97 ms: 1.11x slower                                                        |
| 2to3                       | 285 ms                                                       | 317 ms: 1.11x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.20 sec: 1.12x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.81 ms: 1.12x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 27.3 ms: 1.14x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 104 ms: 1.16x slower                                                         |
| django_template            | 38.2 ms                                                      | 44.4 ms: 1.16x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 135 ms: 1.17x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 68.9 ms: 1.20x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.18 ms: 1.20x slower                                                        |
| coverage                   | 66.7 ms                                                      | 82.1 ms: 1.23x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 187 us: 1.23x slower                                                         |
| python_startup             | 11.6 ms                                                      | 15.8 ms: 1.36x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.52 ms: 1.59x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.87 ms: 1.80x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.79 sec: 586.22x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (7): logging_silent, scimark_sparse_mat_mult, asyncio_websockets, xml_etree_parse, bench_thread_pool, json, tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.010x slower
# HPT report

- Reliability score: 64.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x