# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.020x faster
- HPT reliability: 79.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 290 ms: 1.02x slower                                                |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                              |
| Geometric mean | (ref)                                                        | 1.03x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 629 ms: 1.67x faster                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 328 ms: 1.64x faster                                                |
| async_tree_io              | 1.04 sec                                                     | 637 ms: 1.64x faster                                                |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.60x faster                                                |
| async_tree_none            | 452 ms                                                       | 287 ms: 1.58x faster                                                |
| async_tree_memoization     | 544 ms                                                       | 355 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 499 ms: 1.40x faster                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 68.1 ms: 1.13x faster                                               |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                |
| nbody          | 88.0 ms                                                      | 98.2 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                        | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.17 ms: 1.13x faster                                               |
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                |
| regex_dna      | 239 ms                                                       | 231 ms: 1.03x faster                                                |
| regex_v8       | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 93.9 ms: 1.10x faster                                               |
| tomli_loads          | 2.16 sec                                                     | 2.03 sec: 1.06x faster                                              |
| unpickle_pure_python | 210 us                                                       | 198 us: 1.06x faster                                                |
| xml_etree_generate   | 86.1 ms                                                      | 81.7 ms: 1.05x faster                                               |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                |
| json_loads           | 24.4 us                                                      | 24.0 us: 1.02x faster                                               |
| xml_etree_process    | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                               |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                               |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                               |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.61 ms: 1.04x faster                                               |
| django_template | 38.2 ms                                                      | 39.2 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 629 ms: 1.67x faster                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 328 ms: 1.64x faster                                                |
| async_tree_io              | 1.04 sec                                                     | 637 ms: 1.64x faster                                                |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.60x faster                                                |
| async_tree_none            | 452 ms                                                       | 287 ms: 1.58x faster                                                |
| async_tree_memoization     | 544 ms                                                       | 355 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 499 ms: 1.40x faster                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                |
| deepcopy_memo              | 36.8 us                                                      | 27.9 us: 1.32x faster                                               |
| deepcopy                   | 368 us                                                       | 299 us: 1.23x faster                                                |
| pathlib                    | 18.9 ms                                                      | 16.5 ms: 1.14x faster                                               |
| comprehensions             | 21.9 us                                                      | 19.3 us: 1.14x faster                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.98 us: 1.13x faster                                               |
| regex_effbot               | 3.57 ms                                                      | 3.17 ms: 1.13x faster                                               |
| float                      | 76.6 ms                                                      | 68.1 ms: 1.13x faster                                               |
| scimark_sor                | 109 ms                                                       | 98.7 ms: 1.10x faster                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.6 ms: 1.10x faster                                               |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                               |
| xml_etree_iterparse        | 103 ms                                                       | 93.9 ms: 1.10x faster                                               |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                |
| crypto_pyaes               | 80.3 ms                                                      | 74.5 ms: 1.08x faster                                               |
| tomli_loads                | 2.16 sec                                                     | 2.03 sec: 1.06x faster                                              |
| unpickle_pure_python       | 210 us                                                       | 198 us: 1.06x faster                                                |
| xml_etree_generate         | 86.1 ms                                                      | 81.7 ms: 1.05x faster                                               |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                |
| scimark_lu                 | 98.8 ms                                                      | 94.7 ms: 1.04x faster                                               |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                |
| mako                       | 10.0 ms                                                      | 9.61 ms: 1.04x faster                                               |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                |
| regex_dna                  | 239 ms                                                       | 231 ms: 1.03x faster                                                |
| go                         | 150 ms                                                       | 145 ms: 1.03x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.1 ms: 1.03x faster                                               |
| logging_format             | 7.48 us                                                      | 7.36 us: 1.02x faster                                               |
| json_loads                 | 24.4 us                                                      | 24.0 us: 1.02x faster                                               |
| sympy_sum                  | 162 ms                                                       | 159 ms: 1.02x faster                                                |
| spectral_norm              | 91.6 ms                                                      | 90.1 ms: 1.02x faster                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.36 ms: 1.01x faster                                               |
| xml_etree_process          | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                               |
| logging_simple             | 6.71 us                                                      | 6.63 us: 1.01x faster                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                              |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                              |
| sympy_integrate            | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                               |
| sympy_str                  | 302 ms                                                       | 305 ms: 1.01x slower                                                |
| richards                   | 45.7 ms                                                      | 46.3 ms: 1.01x slower                                               |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.01x slower                                               |
| 2to3                       | 285 ms                                                       | 290 ms: 1.02x slower                                                |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                              |
| richards_super             | 51.3 ms                                                      | 52.5 ms: 1.02x slower                                               |
| dulwich_log                | 65.4 ms                                                      | 66.9 ms: 1.02x slower                                               |
| django_template            | 38.2 ms                                                      | 39.2 ms: 1.03x slower                                               |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                              |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                               |
| bench_thread_pool          | 950 us                                                       | 995 us: 1.05x slower                                                |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                |
| pyflate                    | 439 ms                                                       | 463 ms: 1.05x slower                                                |
| sqlglot_normalize          | 116 ms                                                       | 123 ms: 1.07x slower                                                |
| chaos                      | 64.0 ms                                                      | 68.2 ms: 1.07x slower                                               |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                |
| generators                 | 37.4 ms                                                      | 39.9 ms: 1.07x slower                                               |
| sqlglot_optimize           | 57.5 ms                                                      | 61.4 ms: 1.07x slower                                               |
| sympy_expand               | 484 ms                                                       | 520 ms: 1.07x slower                                                |
| deltablue                  | 3.24 ms                                                      | 3.51 ms: 1.08x slower                                               |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                               |
| regex_v8                   | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                               |
| fannkuch                   | 350 ms                                                       | 382 ms: 1.09x slower                                                |
| nbody                      | 88.0 ms                                                      | 98.2 ms: 1.12x slower                                               |
| telco                      | 6.96 ms                                                      | 7.79 ms: 1.12x slower                                               |
| raytrace                   | 298 ms                                                       | 334 ms: 1.12x slower                                                |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.14x slower                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.88 ms: 1.16x slower                                               |
| typing_runtime_protocols   | 152 us                                                       | 180 us: 1.18x slower                                                |
| coverage                   | 66.7 ms                                                      | 79.4 ms: 1.19x slower                                               |
| async_generators           | 390 ms                                                       | 467 ms: 1.20x slower                                                |
| hexiom                     | 5.96 ms                                                      | 7.42 ms: 1.24x slower                                               |
| mypy2                      | 830 ms                                                       | 1.04 sec: 1.25x slower                                              |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.69 ms: 1.69x slower                                               |
| gc_traversal               | 3.48 ms                                                      | 6.32 ms: 1.82x slower                                               |
| bench_mp_pool              | 4.76 ms                                                      | 1.48 sec: 311.61x slower                                            |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                        |

Benchmark hidden because not significant (4): json, sqlglot_transpile, scimark_fft, pprint_safe_repr
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.020x faster

# HPT report

- Reliability score: 79.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x