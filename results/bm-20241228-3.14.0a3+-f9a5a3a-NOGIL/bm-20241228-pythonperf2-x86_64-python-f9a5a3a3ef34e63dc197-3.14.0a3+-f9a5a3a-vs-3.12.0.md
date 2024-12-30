# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-x86_64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.182x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 382 ms: 1.34x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 740 ms: 1.42x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 319 ms: 1.35x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 774 ms: 1.35x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 407 ms: 1.33x faster                                                         |
| async_tree_none            | 452 ms                                                       | 354 ms: 1.28x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 440 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 574 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 608 ms: 1.15x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 247 ms: 1.07x faster                                                         |
| float          | 76.6 ms                                                      | 109 ms: 1.42x slower                                                         |
| nbody          | 88.0 ms                                                      | 130 ms: 1.48x slower                                                         |
| Geometric mean | (ref)                                                        | 1.25x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.30 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.7 ms: 1.13x slower                                                        |
| regex_compile  | 144 ms                                                       | 173 ms: 1.20x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 93.6 ms: 1.10x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| json_loads           | 24.4 us                                                      | 26.8 us: 1.10x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 98.6 ms: 1.14x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.61 sec: 1.21x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 74.7 ms: 1.28x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.2 ms: 1.39x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 323 us: 1.54x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 506 us: 1.59x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.21x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.0 ms: 1.39x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.2 ms: 1.65x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.52x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 53.6 ms: 1.41x slower                                                        |
| mako            | 10.0 ms                                                      | 19.5 ms: 1.95x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.65x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 740 ms: 1.42x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 319 ms: 1.35x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 774 ms: 1.35x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 407 ms: 1.33x faster                                                         |
| async_tree_none            | 452 ms                                                       | 354 ms: 1.28x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 440 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 574 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 608 ms: 1.15x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 93.6 ms: 1.10x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.30 ms: 1.08x faster                                                        |
| pidigits                   | 265 ms                                                       | 247 ms: 1.07x faster                                                         |
| deepcopy                   | 368 us                                                       | 346 us: 1.06x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.65 us: 1.05x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 23.2 ms: 1.01x slower                                                        |
| generators                 | 37.4 ms                                                      | 38.2 ms: 1.02x slower                                                        |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| json                       | 5.12 ms                                                      | 5.43 ms: 1.06x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 39.3 us: 1.07x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 3.82 ms: 1.10x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.8 us: 1.10x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.75 us: 1.11x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 103 ms: 1.13x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.90 sec: 1.13x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.7 ms: 1.13x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 185 ms: 1.14x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 98.6 ms: 1.14x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.42 sec: 1.15x slower                                                       |
| scimark_fft                | 301 ms                                                       | 350 ms: 1.16x slower                                                         |
| sympy_str                  | 302 ms                                                       | 358 ms: 1.19x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 28.6 ms: 1.19x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 78.2 ms: 1.20x slower                                                        |
| regex_compile              | 144 ms                                                       | 173 ms: 1.20x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.61 sec: 1.21x slower                                                       |
| meteor_contest             | 128 ms                                                       | 155 ms: 1.21x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 22.9 ms: 1.22x slower                                                        |
| comprehensions             | 21.9 us                                                      | 27.0 us: 1.23x slower                                                        |
| sympy_expand               | 484 ms                                                       | 598 ms: 1.24x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 99.8 ms: 1.24x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 112 ms: 1.25x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 72.1 ms: 1.25x slower                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 200 ms: 1.26x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 146 ms: 1.26x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 74.7 ms: 1.28x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 1.03 sec: 1.28x slower                                                       |
| logging_format             | 7.48 us                                                      | 9.64 us: 1.29x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.14 sec: 1.30x slower                                                       |
| logging_simple             | 6.71 us                                                      | 8.74 us: 1.30x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.18 ms: 1.32x slower                                                        |
| async_generators           | 390 ms                                                       | 515 ms: 1.32x slower                                                         |
| 2to3                       | 285 ms                                                       | 382 ms: 1.34x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 135 ms: 1.37x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.78 ms: 1.37x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 14.2 ms: 1.39x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 12.0 ms: 1.39x slower                                                        |
| django_template            | 38.2 ms                                                      | 53.6 ms: 1.41x slower                                                        |
| float                      | 76.6 ms                                                      | 109 ms: 1.42x slower                                                         |
| fannkuch                   | 350 ms                                                       | 504 ms: 1.44x slower                                                         |
| pyflate                    | 439 ms                                                       | 646 ms: 1.47x slower                                                         |
| nbody                      | 88.0 ms                                                      | 130 ms: 1.48x slower                                                         |
| chaos                      | 64.0 ms                                                      | 94.9 ms: 1.48x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 229 us: 1.51x slower                                                         |
| richards_super             | 51.3 ms                                                      | 79.0 ms: 1.54x slower                                                        |
| coverage                   | 66.7 ms                                                      | 103 ms: 1.54x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 106 ms: 1.54x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 323 us: 1.54x slower                                                         |
| richards                   | 45.7 ms                                                      | 71.4 ms: 1.56x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.31 sec: 1.58x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 9.40 ms: 1.58x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 2.82 ms: 1.59x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 506 us: 1.59x slower                                                         |
| raytrace                   | 298 ms                                                       | 481 ms: 1.61x slower                                                         |
| go                         | 150 ms                                                       | 244 ms: 1.63x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.56 ms: 1.64x slower                                                        |
| python_startup             | 11.6 ms                                                      | 19.2 ms: 1.65x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.72 ms: 1.71x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.36 ms: 1.71x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 162 ns: 1.72x slower                                                         |
| scimark_sor                | 109 ms                                                       | 192 ms: 1.76x slower                                                         |
| mako                       | 10.0 ms                                                      | 19.5 ms: 1.95x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 7.13 ms: 2.20x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 52.3 ms: 10.98x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.26x slower                                                                 |
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.182x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.17x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: 1.24x