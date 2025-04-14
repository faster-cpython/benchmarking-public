# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.023x faster
- HPT reliability: 80.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 657 ms: 1.60x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 656 ms: 1.59x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 344 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 298 ms: 1.52x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 284 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 359 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 518 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 528 ms: 1.32x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.49x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.7 ms: 1.13x faster                                                        |
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 89.5 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                        |
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| regex_dna      | 239 ms                                                       | 239 ms: 1.00x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 94.5 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.3 ms: 1.07x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| unpickle             | 14.8 us                                                      | 14.1 us: 1.05x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 203 us: 1.03x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 57.1 ms: 1.02x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 32.2 us: 1.01x faster                                                        |
| unpickle_list        | 4.66 us                                                      | 4.79 us: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 334 us: 1.05x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.10x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.99 us: 1.13x slower                                                        |
| pickle               | 10.5 us                                                      | 12.0 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.42 ms: 1.06x faster                                                        |
| django_template | 38.2 ms                                                      | 37.7 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 657 ms: 1.60x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 656 ms: 1.59x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 344 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 298 ms: 1.52x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 284 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 359 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 518 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 528 ms: 1.32x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                        |
| deepcopy                   | 368 us                                                       | 308 us: 1.20x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.0 us: 1.15x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                        |
| float                      | 76.6 ms                                                      | 67.7 ms: 1.13x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.7 ms: 1.11x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 145 ms: 1.10x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 94.5 ms: 1.09x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.90 us: 1.09x faster                                                        |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.08x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.3 ms: 1.07x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.3 ms: 1.07x faster                                                        |
| go                         | 150 ms                                                       | 140 ms: 1.07x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.30 us: 1.06x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.42 ms: 1.06x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                        |
| unpickle                   | 14.8 us                                                      | 14.1 us: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 87.8 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| unpickle_pure_python       | 210 us                                                       | 203 us: 1.03x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 157 ms: 1.03x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 367 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 785 ms: 1.03x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 78.2 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                       |
| scimark_fft                | 301 ms                                                       | 294 ms: 1.02x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 57.1 ms: 1.02x faster                                                        |
| django_template            | 38.2 ms                                                      | 37.7 ms: 1.01x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 32.2 us: 1.01x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.75 us: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| regex_dna                  | 239 ms                                                       | 239 ms: 1.00x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                       |
| sympy_str                  | 302 ms                                                       | 303 ms: 1.00x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| nbody                      | 88.0 ms                                                      | 89.5 ms: 1.02x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 969 us: 1.02x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 66.8 ms: 1.02x slower                                                        |
| richards                   | 45.7 ms                                                      | 46.8 ms: 1.02x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 101 ms: 1.02x slower                                                         |
| raytrace                   | 298 ms                                                       | 306 ms: 1.03x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 4.79 us: 1.03x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| richards_super             | 51.3 ms                                                      | 53.2 ms: 1.04x slower                                                        |
| pyflate                    | 439 ms                                                       | 458 ms: 1.05x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 99.1 ns: 1.05x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 334 us: 1.05x slower                                                         |
| chaos                      | 64.0 ms                                                      | 67.6 ms: 1.06x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.43 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 61.1 ms: 1.06x slower                                                        |
| sympy_expand               | 484 ms                                                       | 517 ms: 1.07x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 125 ms: 1.08x slower                                                         |
| json                       | 5.12 ms                                                      | 5.56 ms: 1.09x slower                                                        |
| async_generators           | 390 ms                                                       | 426 ms: 1.09x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.10x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.71 ms: 1.11x slower                                                        |
| fannkuch                   | 350 ms                                                       | 388 ms: 1.11x slower                                                         |
| generators                 | 37.4 ms                                                      | 42.0 ms: 1.12x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.99 us: 1.13x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.0 us: 1.14x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 103 ms: 1.15x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.88 ms: 1.16x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 61.8 ns: 1.16x slower                                                        |
| coverage                   | 66.7 ms                                                      | 79.2 ms: 1.19x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.54 ms: 1.27x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.65 ms: 1.67x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.29 ms: 1.81x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.33 sec: 278.53x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (3): sympy_integrate, asyncio_websockets, pycparser
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 80.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x