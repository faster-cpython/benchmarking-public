# Results vs. 3.12.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-x86_64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.028x faster
- HPT reliability: 95.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 290 ms: 1.02x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 657 ms: 1.60x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 654 ms: 1.59x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 343 ms: 1.58x faster                                                         |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 356 ms: 1.53x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 283 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 515 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 526 ms: 1.32x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.50x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.5 ms: 1.09x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 104 ms: 1.19x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.10 ms: 1.15x faster                                                        |
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.8 ms: 1.08x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.4 ms: 1.04x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 56.1 ms: 1.04x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 204 us: 1.03x faster                                                         |
| pickle_pure_python   | 318 us                                                       | 337 us: 1.06x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.8 us: 1.10x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.8 ms: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.6 ms: 1.04x faster                                                        |
| mako            | 10.0 ms                                                      | 9.66 ms: 1.04x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 657 ms: 1.60x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 654 ms: 1.59x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 343 ms: 1.58x faster                                                         |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 356 ms: 1.53x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 283 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 515 ms: 1.35x faster                                                         |
| deepcopy                   | 368 us                                                       | 278 us: 1.33x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 526 ms: 1.32x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.0 us: 1.27x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.88 us: 1.17x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.10 ms: 1.15x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.4 us: 1.13x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.1 ms: 1.13x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 145 ms: 1.10x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 83.9 ms: 1.09x faster                                                        |
| float                      | 76.6 ms                                                      | 70.5 ms: 1.09x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.90 us: 1.09x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 79.8 ms: 1.08x faster                                                        |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.41 us: 1.05x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 98.4 ms: 1.04x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                        |
| django_template            | 38.2 ms                                                      | 36.6 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 56.1 ms: 1.04x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 77.4 ms: 1.04x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.66 ms: 1.04x faster                                                        |
| chaos                      | 64.0 ms                                                      | 62.0 ms: 1.03x faster                                                        |
| pyflate                    | 439 ms                                                       | 425 ms: 1.03x faster                                                         |
| unpickle_pure_python       | 210 us                                                       | 204 us: 1.03x faster                                                         |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                         |
| richards                   | 45.7 ms                                                      | 44.9 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.01x faster                                                         |
| go                         | 150 ms                                                       | 148 ms: 1.01x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                        |
| richards_super             | 51.3 ms                                                      | 50.8 ms: 1.01x faster                                                        |
| scimark_sor                | 109 ms                                                       | 109 ms: 1.00x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.38 ms: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                       |
| raytrace                   | 298 ms                                                       | 302 ms: 1.01x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 100 ms: 1.01x slower                                                         |
| scimark_fft                | 301 ms                                                       | 306 ms: 1.02x slower                                                         |
| 2to3                       | 285 ms                                                       | 290 ms: 1.02x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 96.8 ns: 1.03x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.6 ms: 1.03x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 59.9 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| sympy_expand               | 484 ms                                                       | 508 ms: 1.05x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 337 us: 1.06x slower                                                         |
| json                       | 5.12 ms                                                      | 5.43 ms: 1.06x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.06x slower                                                        |
| fannkuch                   | 350 ms                                                       | 381 ms: 1.09x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.53 ms: 1.09x slower                                                        |
| async_generators           | 390 ms                                                       | 426 ms: 1.09x slower                                                         |
| json_loads                 | 24.4 us                                                      | 26.8 us: 1.10x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 100.0 ms: 1.11x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.76 ms: 1.12x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.84 ms: 1.15x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.8 ms: 1.15x slower                                                        |
| nbody                      | 88.0 ms                                                      | 104 ms: 1.19x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.14 ms: 1.20x slower                                                        |
| coverage                   | 66.7 ms                                                      | 82.8 ms: 1.24x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.73 ms: 1.72x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.50 ms: 1.87x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.55 sec: 325.92x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (6): pprint_safe_repr, pprint_pformat, sqlglot_transpile, sqlite_synth, asyncio_websockets, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 95.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x