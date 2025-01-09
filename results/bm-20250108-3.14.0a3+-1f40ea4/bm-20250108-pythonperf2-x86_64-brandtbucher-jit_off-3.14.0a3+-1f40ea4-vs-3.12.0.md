# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_off
- machine: linux-x86_64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.051x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                  |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                        | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 623 ms: 1.69x faster                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                  |
| async_tree_io              | 1.04 sec                                                     | 633 ms: 1.65x faster                                                  |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                  |
| async_tree_none            | 452 ms                                                       | 282 ms: 1.60x faster                                                  |
| async_tree_memoization     | 544 ms                                                       | 347 ms: 1.57x faster                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 496 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 513 ms: 1.36x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 73.0 ms: 1.05x faster                                                 |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                  |
| nbody          | 88.0 ms                                                      | 89.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.15 ms: 1.14x faster                                                 |
| regex_compile  | 144 ms                                                       | 135 ms: 1.06x faster                                                  |
| regex_dna      | 239 ms                                                       | 233 ms: 1.02x faster                                                  |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.4 ms: 1.07x faster                                                 |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.07x faster                                                  |
| tomli_loads          | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                |
| xml_etree_generate   | 86.1 ms                                                      | 82.2 ms: 1.05x faster                                                 |
| json_loads           | 24.4 us                                                      | 24.0 us: 1.02x faster                                                 |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                  |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                 |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                  |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                 |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.7 ms: 1.07x faster                                                 |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                 |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 623 ms: 1.69x faster                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                  |
| async_tree_io              | 1.04 sec                                                     | 633 ms: 1.65x faster                                                  |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                  |
| async_tree_none            | 452 ms                                                       | 282 ms: 1.60x faster                                                  |
| async_tree_memoization     | 544 ms                                                       | 347 ms: 1.57x faster                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 496 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 513 ms: 1.36x faster                                                  |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                 |
| deepcopy                   | 368 us                                                       | 283 us: 1.30x faster                                                  |
| deepcopy_memo              | 36.8 us                                                      | 29.4 us: 1.25x faster                                                 |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.25x faster                                                 |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.18x faster                                                 |
| go                         | 150 ms                                                       | 128 ms: 1.17x faster                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                                 |
| regex_effbot               | 3.57 ms                                                      | 3.15 ms: 1.14x faster                                                 |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.4 ms: 1.11x faster                                                 |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.10x faster                                                 |
| raytrace                   | 298 ms                                                       | 271 ms: 1.10x faster                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 73.3 ms: 1.10x faster                                                 |
| logging_format             | 7.48 us                                                      | 6.96 us: 1.08x faster                                                 |
| django_template            | 38.2 ms                                                      | 35.7 ms: 1.07x faster                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 96.4 ms: 1.07x faster                                                 |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                  |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.07x faster                                                  |
| regex_compile              | 144 ms                                                       | 135 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.06x faster                                                |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                |
| logging_simple             | 6.71 us                                                      | 6.37 us: 1.05x faster                                                 |
| float                      | 76.6 ms                                                      | 73.0 ms: 1.05x faster                                                 |
| pprint_safe_repr           | 807 ms                                                       | 770 ms: 1.05x faster                                                  |
| scimark_lu                 | 98.8 ms                                                      | 94.2 ms: 1.05x faster                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 82.2 ms: 1.05x faster                                                 |
| spectral_norm              | 91.6 ms                                                      | 87.5 ms: 1.05x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                 |
| mdp                        | 2.57 sec                                                     | 2.47 sec: 1.04x faster                                                |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.04x faster                                                 |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.72 ms: 1.03x faster                                                 |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                                  |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                  |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.02x faster                                                  |
| bench_thread_pool          | 950 us                                                       | 932 us: 1.02x faster                                                  |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.02x faster                                                  |
| json_loads                 | 24.4 us                                                      | 24.0 us: 1.02x faster                                                 |
| chaos                      | 64.0 ms                                                      | 63.0 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 210 us                                                       | 207 us: 1.01x faster                                                  |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                  |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                 |
| scimark_fft                | 301 ms                                                       | 304 ms: 1.01x slower                                                  |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                  |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                |
| nbody                      | 88.0 ms                                                      | 89.3 ms: 1.01x slower                                                 |
| richards                   | 45.7 ms                                                      | 46.4 ms: 1.02x slower                                                 |
| dulwich_log                | 65.4 ms                                                      | 66.7 ms: 1.02x slower                                                 |
| hexiom                     | 5.96 ms                                                      | 6.09 ms: 1.02x slower                                                 |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.85 us: 1.03x slower                                                 |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                  |
| richards_super             | 51.3 ms                                                      | 53.1 ms: 1.03x slower                                                 |
| sympy_expand               | 484 ms                                                       | 502 ms: 1.04x slower                                                  |
| logging_silent             | 94.4 ns                                                      | 98.1 ns: 1.04x slower                                                 |
| pyflate                    | 439 ms                                                       | 456 ms: 1.04x slower                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                 |
| deltablue                  | 3.24 ms                                                      | 3.40 ms: 1.05x slower                                                 |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.59 ms: 1.09x slower                                                 |
| telco                      | 6.96 ms                                                      | 7.68 ms: 1.10x slower                                                 |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                 |
| async_generators           | 390 ms                                                       | 436 ms: 1.12x slower                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                 |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                  |
| coverage                   | 66.7 ms                                                      | 77.7 ms: 1.16x slower                                                 |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.74 ms: 1.72x slower                                                 |
| gc_traversal               | 3.48 ms                                                      | 6.25 ms: 1.80x slower                                                 |
| bench_mp_pool              | 4.76 ms                                                      | 1.52 sec: 318.81x slower                                              |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                          |

Benchmark hidden because not significant (5): asyncio_websockets, json, pycparser, sqlglot_optimize, nqueens
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250108-3.14.0a3+-1f40ea4/bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x