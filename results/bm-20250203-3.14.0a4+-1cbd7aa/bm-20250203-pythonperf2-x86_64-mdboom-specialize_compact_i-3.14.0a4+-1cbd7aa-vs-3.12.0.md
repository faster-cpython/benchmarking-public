# Results vs. 3.12.0

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: 1cbd7aa
- commit date: 2025-02-03
- overall geometric mean: 1.057x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 279 ms: 1.02x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 645 ms: 1.63x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 651 ms: 1.60x faster                                                         |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.1 ms: 1.11x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                        |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| regex_dna      | 239 ms                                                       | 233 ms: 1.02x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse     | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| xml_etree_iterparse | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| tomli_loads         | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| xml_etree_generate  | 86.1 ms                                                      | 83.7 ms: 1.03x faster                                                        |
| xml_etree_process   | 58.4 ms                                                      | 59.0 ms: 1.01x slower                                                        |
| pickle_pure_python  | 318 us                                                       | 324 us: 1.02x slower                                                         |
| json_loads          | 24.4 us                                                      | 26.3 us: 1.08x slower                                                        |
| json_dumps          | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.4 ms: 1.08x faster                                                        |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 645 ms: 1.63x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 651 ms: 1.60x faster                                                         |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| deepcopy                   | 368 us                                                       | 278 us: 1.33x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.7 ms: 1.30x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.9 us: 1.30x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.3 us: 1.25x faster                                                        |
| go                         | 150 ms                                                       | 123 ms: 1.22x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 79.9 ms: 1.15x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 72.0 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.0 ms: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.7 ms: 1.11x faster                                                        |
| float                      | 76.6 ms                                                      | 69.1 ms: 1.11x faster                                                        |
| raytrace                   | 298 ms                                                       | 269 ms: 1.11x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| django_template            | 38.2 ms                                                      | 35.4 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.97 us: 1.07x faster                                                        |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.6 ms: 1.07x faster                                                        |
| chaos                      | 64.0 ms                                                      | 60.0 ms: 1.07x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.35 us: 1.06x faster                                                        |
| sympy_str                  | 302 ms                                                       | 287 ms: 1.05x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.0 ms: 1.05x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.45 sec: 1.05x faster                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.32 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.59 sec: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.71 ms: 1.04x faster                                                        |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 781 ms: 1.03x faster                                                         |
| bench_thread_pool          | 950 us                                                       | 920 us: 1.03x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 83.7 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.02x faster                                                         |
| 2to3                       | 285 ms                                                       | 279 ms: 1.02x faster                                                         |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                         |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.02x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 56.5 ms: 1.02x faster                                                        |
| richards                   | 45.7 ms                                                      | 45.1 ms: 1.01x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.9 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                       |
| sympy_expand               | 484 ms                                                       | 485 ms: 1.00x slower                                                         |
| pyflate                    | 439 ms                                                       | 442 ms: 1.01x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.01 ms: 1.01x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.0 ms: 1.01x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.2 ms: 1.01x slower                                                        |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 324 us: 1.02x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 96.7 ns: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                        |
| async_generators           | 390 ms                                                       | 408 ms: 1.05x slower                                                         |
| json                       | 5.12 ms                                                      | 5.52 ms: 1.08x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.3 us: 1.08x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 167 us: 1.10x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.64 ms: 1.10x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.86 ms: 1.13x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.71 ms: 1.71x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.33 ms: 1.82x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.26 sec: 264.56x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (5): deltablue, richards_super, unpickle_pure_python, nbody, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250203-3.14.0a4+-1cbd7aa/bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x