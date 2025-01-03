# Results vs. 3.12.0

- fork: python
- ref: e1baa778f602ede66831
- machine: linux-x86_64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.042x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.02x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 326 ms: 1.66x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 635 ms: 1.64x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                         |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 352 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 495 ms: 1.41x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 513 ms: 1.36x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 72.1 ms: 1.06x faster                                                        |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.19 ms: 1.12x faster                                                        |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| regex_dna      | 239 ms                                                       | 235 ms: 1.02x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 94.5 ms: 1.09x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 82.4 ms: 1.05x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| json_loads           | 24.4 us                                                      | 23.8 us: 1.03x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 208 us: 1.01x faster                                                         |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                                        |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 326 ms: 1.66x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 635 ms: 1.64x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                         |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 352 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 495 ms: 1.41x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 513 ms: 1.36x faster                                                         |
| deepcopy                   | 368 us                                                       | 285 us: 1.29x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.5 ms: 1.27x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.4 us: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                        |
| go                         | 150 ms                                                       | 127 ms: 1.17x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 2.88 us: 1.17x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.19 ms: 1.12x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.11x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.6 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.7 ms: 1.09x faster                                                        |
| raytrace                   | 298 ms                                                       | 274 ms: 1.09x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 94.5 ms: 1.09x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.00 us: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.31 us: 1.06x faster                                                        |
| float                      | 76.6 ms                                                      | 72.1 ms: 1.06x faster                                                        |
| django_template            | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.4 ms: 1.05x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 87.7 ms: 1.04x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 95.8 ms: 1.03x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.73 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| json_loads                 | 24.4 us                                                      | 23.8 us: 1.03x faster                                                        |
| chaos                      | 64.0 ms                                                      | 62.4 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.02x faster                                                         |
| 2to3                       | 285 ms                                                       | 281 ms: 1.02x faster                                                         |
| scimark_fft                | 301 ms                                                       | 297 ms: 1.01x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 796 ms: 1.01x faster                                                         |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 208 us: 1.01x faster                                                         |
| sqlglot_normalize          | 116 ms                                                       | 115 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 57.7 ms: 1.00x slower                                                        |
| richards_super             | 51.3 ms                                                      | 51.7 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.3 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 498 ms: 1.03x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.15 ms: 1.03x slower                                                        |
| pyflate                    | 439 ms                                                       | 453 ms: 1.03x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 98.4 ns: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                                        |
| scimark_sor                | 109 ms                                                       | 115 ms: 1.06x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.08x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.59 ms: 1.09x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                        |
| async_generators           | 390 ms                                                       | 437 ms: 1.12x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.90 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                         |
| coverage                   | 66.7 ms                                                      | 80.1 ms: 1.20x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.03 sec: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.85 ms: 1.79x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.41 ms: 1.84x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.59 sec: 334.30x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (8): bench_thread_pool, json, nqueens, asyncio_websockets, nbody, xml_etree_process, pycparser, richards
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x