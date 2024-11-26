# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.302x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 430 ms: 1.51x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.40 sec: 1.18x slower                                                       |
| tornado_http   | 121 ms                                                       | 166 ms: 1.37x slower                                                         |
| Geometric mean | (ref)                                                        | 1.35x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 890 ms: 1.18x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 373 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 477 ms: 1.13x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 936 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 633 ms: 1.10x faster                                                         |
| async_tree_none            | 452 ms                                                       | 416 ms: 1.09x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 517 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 680 ms: 1.02x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                         |
| float          | 76.6 ms                                                      | 145 ms: 1.89x slower                                                         |
| nbody          | 88.0 ms                                                      | 194 ms: 2.21x slower                                                         |
| Geometric mean | (ref)                                                        | 1.58x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                        |
| regex_compile  | 144 ms                                                       | 226 ms: 1.57x slower                                                         |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                         |
| json_loads           | 24.4 us                                                      | 28.8 us: 1.18x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 116 ms: 1.34x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 15.1 ms: 1.48x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 3.41 sec: 1.58x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 95.3 ms: 1.63x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 598 us: 1.88x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 408 us: 1.95x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.41x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.3 ms: 1.66x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.51x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 67.2 ms: 1.76x slower                                                        |
| mako            | 10.0 ms                                                      | 22.3 ms: 2.23x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.98x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 890 ms: 1.18x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 373 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 477 ms: 1.13x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 936 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 633 ms: 1.10x faster                                                         |
| async_tree_none            | 452 ms                                                       | 416 ms: 1.09x faster                                                         |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 517 ms: 1.05x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 680 ms: 1.02x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.01x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.4 ms: 1.03x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 3.63 ms: 1.04x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                         |
| generators                 | 37.4 ms                                                      | 40.8 ms: 1.09x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                        |
| json                       | 5.12 ms                                                      | 5.96 ms: 1.16x slower                                                        |
| deepcopy                   | 368 us                                                       | 432 us: 1.17x slower                                                         |
| json_loads                 | 24.4 us                                                      | 28.8 us: 1.18x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.40 sec: 1.18x slower                                                       |
| coroutines                 | 23.0 ms                                                      | 28.0 ms: 1.22x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.24 sec: 1.26x slower                                                       |
| async_generators           | 390 ms                                                       | 492 ms: 1.26x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 23.9 ms: 1.28x slower                                                        |
| scimark_fft                | 301 ms                                                       | 397 ms: 1.32x slower                                                         |
| meteor_contest             | 128 ms                                                       | 169 ms: 1.32x slower                                                         |
| deepcopy_memo              | 36.8 us                                                      | 48.8 us: 1.33x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 116 ms: 1.34x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.68 ms: 1.35x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 88.6 ms: 1.36x slower                                                        |
| tornado_http               | 121 ms                                                       | 166 ms: 1.37x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 32.8 ms: 1.37x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                        |
| comprehensions             | 21.9 us                                                      | 30.3 us: 1.38x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 4.69 us: 1.39x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.73 sec: 1.40x slower                                                       |
| sqlalchemy_declarative     | 159 ms                                                       | 226 ms: 1.42x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 131 ms: 1.46x slower                                                         |
| telco                      | 6.96 ms                                                      | 10.2 ms: 1.46x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 15.1 ms: 1.48x slower                                                        |
| sympy_str                  | 302 ms                                                       | 449 ms: 1.49x slower                                                         |
| 2to3                       | 285 ms                                                       | 430 ms: 1.51x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 123 ms: 1.53x slower                                                         |
| regex_compile              | 144 ms                                                       | 226 ms: 1.57x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 3.41 sec: 1.58x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 184 ms: 1.59x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 92.3 ms: 1.61x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 261 ms: 1.61x slower                                                         |
| logging_format             | 7.48 us                                                      | 12.2 us: 1.63x slower                                                        |
| coverage                   | 66.7 ms                                                      | 108 ms: 1.63x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 95.3 ms: 1.63x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.60 ms: 1.64x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.57 ms: 1.65x slower                                                        |
| python_startup             | 11.6 ms                                                      | 19.3 ms: 1.66x slower                                                        |
| sympy_expand               | 484 ms                                                       | 805 ms: 1.66x slower                                                         |
| logging_simple             | 6.71 us                                                      | 11.3 us: 1.68x slower                                                        |
| fannkuch                   | 350 ms                                                       | 590 ms: 1.68x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 1.39 sec: 1.72x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.89 sec: 1.75x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 266 us: 1.76x slower                                                         |
| django_template            | 38.2 ms                                                      | 67.2 ms: 1.76x slower                                                        |
| pyflate                    | 439 ms                                                       | 774 ms: 1.76x slower                                                         |
| richards                   | 45.7 ms                                                      | 81.0 ms: 1.77x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 166 ms: 1.81x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 598 us: 1.88x slower                                                         |
| float                      | 76.6 ms                                                      | 145 ms: 1.89x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 3.39 ms: 1.91x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 183 ns: 1.94x slower                                                         |
| go                         | 150 ms                                                       | 291 ms: 1.94x slower                                                         |
| richards_super             | 51.3 ms                                                      | 99.9 ms: 1.95x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 134 ms: 1.95x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 408 us: 1.95x slower                                                         |
| chaos                      | 64.0 ms                                                      | 125 ms: 1.96x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 11.7 ms: 1.96x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.81 ms: 2.04x slower                                                        |
| raytrace                   | 298 ms                                                       | 616 ms: 2.07x slower                                                         |
| nbody                      | 88.0 ms                                                      | 194 ms: 2.21x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 218 ms: 2.21x slower                                                         |
| scimark_sor                | 109 ms                                                       | 242 ms: 2.23x slower                                                         |
| mako                       | 10.0 ms                                                      | 22.3 ms: 2.23x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.20 ms: 2.53x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 52.2 ms: 10.95x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.48x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.302x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.21x