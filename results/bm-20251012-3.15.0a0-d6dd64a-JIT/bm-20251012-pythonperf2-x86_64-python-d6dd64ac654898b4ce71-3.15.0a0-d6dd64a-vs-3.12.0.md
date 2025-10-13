# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.039x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.02x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 629 ms: 1.67x faster                                                        |
| async_tree_none            | 452 ms                                                       | 272 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 502 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 512 ms: 1.36x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.8 ms: 1.13x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 103 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.30 ms: 1.08x faster                                                       |
| regex_dna      | 239 ms                                                       | 225 ms: 1.06x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 24.2 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.90 sec: 1.13x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 194 us: 1.08x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.1 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 96.5 ms: 1.07x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.5 ms: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.1 ms: 1.02x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 33.5 us: 1.03x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 329 us: 1.03x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.07 us: 1.09x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.98 us: 1.12x slower                                                       |
| pickle               | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                       |
| mako            | 10.0 ms                                                      | 9.85 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.03x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 629 ms: 1.67x faster                                                        |
| async_tree_none            | 452 ms                                                       | 272 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                        |
| deepcopy                   | 368 us                                                       | 262 us: 1.40x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 26.2 us: 1.40x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 502 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 512 ms: 1.36x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                       |
| go                         | 150 ms                                                       | 119 ms: 1.26x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.1 ms: 1.24x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.2 ms: 1.24x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.87 us: 1.17x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.49 us: 1.15x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.89 us: 1.14x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.90 sec: 1.13x faster                                                      |
| float                      | 76.6 ms                                                      | 67.8 ms: 1.13x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.47 sec: 1.13x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 727 ms: 1.11x faster                                                        |
| pyflate                    | 439 ms                                                       | 395 ms: 1.11x faster                                                        |
| scimark_fft                | 301 ms                                                       | 273 ms: 1.10x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 59.6 ms: 1.10x faster                                                       |
| chaos                      | 64.0 ms                                                      | 58.4 ms: 1.10x faster                                                       |
| django_template            | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                       |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 194 us: 1.08x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.30 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.9 ms: 1.08x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.2 ms: 1.08x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.1 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 96.5 ms: 1.07x faster                                                       |
| raytrace                   | 298 ms                                                       | 280 ms: 1.06x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.2 ms: 1.06x faster                                                       |
| regex_dna                  | 239 ms                                                       | 225 ms: 1.06x faster                                                        |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                        |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.5 ms: 1.05x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 76.9 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.6 ms: 1.04x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.20 sec: 1.03x faster                                                      |
| bench_thread_pool          | 950 us                                                       | 930 us: 1.02x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 92.4 ns: 1.02x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.1 ms: 1.02x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.85 ms: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 281 ms: 1.02x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.19 ms: 1.01x faster                                                       |
| richards                   | 45.7 ms                                                      | 45.3 ms: 1.01x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                        |
| hexiom                     | 5.96 ms                                                      | 5.94 ms: 1.00x faster                                                       |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 24.2 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 92.0 ms: 1.02x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 33.5 us: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 329 us: 1.03x slower                                                        |
| fannkuch                   | 350 ms                                                       | 363 ms: 1.04x slower                                                        |
| sympy_expand               | 484 ms                                                       | 502 ms: 1.04x slower                                                        |
| json                       | 5.12 ms                                                      | 5.44 ms: 1.06x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.07 us: 1.09x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.98 us: 1.12x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                        |
| async_generators           | 390 ms                                                       | 442 ms: 1.13x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.78 ms: 1.14x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| nbody                      | 88.0 ms                                                      | 103 ms: 1.17x slower                                                        |
| coverage                   | 66.7 ms                                                      | 80.3 ms: 1.20x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.51 ms: 1.87x slower                                                       |
| telco                      | 6.96 ms                                                      | 154 ms: 22.07x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 2.57 sec: 538.48x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (5): unpack_sequence, asyncio_tcp_ssl, sqlite_synth, richards_super, unpickle
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x