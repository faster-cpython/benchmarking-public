# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.08x slower
- HPT reliability: 51.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 317 ms: 1.11x slower                                                          |
| docutils       | 2.87 sec                                                     | 3.21 sec: 1.12x slower                                                        |
| tornado_http   | 121 ms                                                       | 124 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 373 ms: 1.45x faster                                                          |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                          |
| async_tree_none_tg         | 431 ms                                                       | 320 ms: 1.35x faster                                                          |
| async_tree_memoization     | 544 ms                                                       | 408 ms: 1.33x faster                                                          |
| async_tree_io              | 1.04 sec                                                     | 821 ms: 1.27x faster                                                          |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 559 ms: 1.25x faster                                                          |
| async_tree_io_tg           | 1.05 sec                                                     | 857 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                          |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                          |
| nbody          | 88.0 ms                                                      | 84.6 ms: 1.04x faster                                                         |
| float          | 76.6 ms                                                      | 78.7 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.42 ms: 1.05x faster                                                         |
| regex_dna      | 239 ms                                                       | 231 ms: 1.03x faster                                                          |
| regex_v8       | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                                         |
| regex_compile  | 144 ms                                                       | 153 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                          |
| xml_etree_process    | 58.4 ms                                                      | 56.9 ms: 1.03x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.13 sec: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 24.1 us: 1.01x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                          |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                         |
| pickle_dict          | 32.5 us                                                      | 32.9 us: 1.01x slower                                                         |
| pickle_list          | 4.43 us                                                      | 4.60 us: 1.04x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                          |
| unpickle_list        | 4.66 us                                                      | 4.90 us: 1.05x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 223 us: 1.06x slower                                                          |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                         |
| python_startup         | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.57 ms: 1.05x faster                                                         |
| django_template | 38.2 ms                                                      | 42.7 ms: 1.12x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 373 ms: 1.45x faster                                                          |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                          |
| async_tree_none_tg         | 431 ms                                                       | 320 ms: 1.35x faster                                                          |
| async_tree_memoization     | 544 ms                                                       | 408 ms: 1.33x faster                                                          |
| async_tree_io              | 1.04 sec                                                     | 821 ms: 1.27x faster                                                          |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 559 ms: 1.25x faster                                                          |
| deepcopy_memo              | 36.8 us                                                      | 29.7 us: 1.24x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 857 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                          |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                         |
| comprehensions             | 21.9 us                                                      | 18.6 us: 1.18x faster                                                         |
| deepcopy                   | 368 us                                                       | 319 us: 1.15x faster                                                          |
| crypto_pyaes               | 80.3 ms                                                      | 71.4 ms: 1.12x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.11 us: 1.08x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.06x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.04 us: 1.06x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                         |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                          |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                          |
| scimark_fft                | 301 ms                                                       | 288 ms: 1.05x faster                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.42 ms: 1.05x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.57 ms: 1.05x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 94.7 ms: 1.04x faster                                                         |
| nbody                      | 88.0 ms                                                      | 84.6 ms: 1.04x faster                                                         |
| regex_dna                  | 239 ms                                                       | 231 ms: 1.03x faster                                                          |
| logging_silent             | 94.4 ns                                                      | 91.4 ns: 1.03x faster                                                         |
| richards_super             | 51.3 ms                                                      | 49.8 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.69 us: 1.03x faster                                                         |
| richards                   | 45.7 ms                                                      | 44.5 ms: 1.03x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.53 us: 1.03x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                          |
| async_generators           | 390 ms                                                       | 380 ms: 1.03x faster                                                          |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 56.9 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 788 ms: 1.02x faster                                                          |
| json                       | 5.12 ms                                                      | 5.03 ms: 1.02x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.13 sec: 1.01x faster                                                        |
| json_loads                 | 24.4 us                                                      | 24.1 us: 1.01x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                          |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                          |
| dulwich_log                | 65.4 ms                                                      | 65.0 ms: 1.01x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                                          |
| raytrace                   | 298 ms                                                       | 299 ms: 1.00x slower                                                          |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                         |
| pickle_dict                | 32.5 us                                                      | 32.9 us: 1.01x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 69.7 ms: 1.01x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 93.3 ms: 1.02x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.2 ms: 1.02x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                                         |
| tornado_http               | 121 ms                                                       | 124 ms: 1.02x slower                                                          |
| float                      | 76.6 ms                                                      | 78.7 ms: 1.03x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.60 us: 1.04x slower                                                         |
| generators                 | 37.4 ms                                                      | 38.9 ms: 1.04x slower                                                         |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                          |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                          |
| go                         | 150 ms                                                       | 156 ms: 1.04x slower                                                          |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.41 ms: 1.05x slower                                                         |
| pyflate                    | 439 ms                                                       | 460 ms: 1.05x slower                                                          |
| unpickle_list              | 4.66 us                                                      | 4.90 us: 1.05x slower                                                         |
| meteor_contest             | 128 ms                                                       | 135 ms: 1.05x slower                                                          |
| regex_v8                   | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.06x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 223 us: 1.06x slower                                                          |
| regex_compile              | 144 ms                                                       | 153 ms: 1.07x slower                                                          |
| sympy_str                  | 302 ms                                                       | 322 ms: 1.07x slower                                                          |
| sympy_sum                  | 162 ms                                                       | 176 ms: 1.09x slower                                                          |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.10x slower                                                         |
| sympy_expand               | 484 ms                                                       | 535 ms: 1.11x slower                                                          |
| 2to3                       | 285 ms                                                       | 317 ms: 1.11x slower                                                          |
| telco                      | 6.96 ms                                                      | 7.74 ms: 1.11x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                                         |
| django_template            | 38.2 ms                                                      | 42.7 ms: 1.12x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.21 sec: 1.12x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 101 ms: 1.13x slower                                                          |
| sympy_integrate            | 23.9 ms                                                      | 27.6 ms: 1.15x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 133 ms: 1.15x slower                                                          |
| coverage                   | 66.7 ms                                                      | 79.8 ms: 1.20x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 182 us: 1.20x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 7.18 ms: 1.20x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 69.9 ms: 1.22x slower                                                         |
| python_startup             | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                                         |
| gc_traversal               | 3.48 ms                                                      | 5.35 ms: 1.54x slower                                                         |
| unpack_sequence            | 53.2 ns                                                      | 90.0 ns: 1.69x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 2.92 ms: 1.83x slower                                                         |
| bench_mp_pool              | 4.76 ms                                                      | 3.14 sec: 659.56x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                  |

Benchmark hidden because not significant (3): unpickle, asyncio_tcp_ssl, bench_thread_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 51.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x