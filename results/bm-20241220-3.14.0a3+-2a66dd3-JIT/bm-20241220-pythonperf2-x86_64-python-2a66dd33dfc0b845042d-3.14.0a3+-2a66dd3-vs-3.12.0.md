# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-x86_64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.017x faster
- HPT reliability: 76.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 292 ms: 1.02x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 644 ms: 1.64x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 657 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 505 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 526 ms: 1.32x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.51x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 72.4 ms: 1.06x faster                                                        |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| nbody          | 88.0 ms                                                      | 91.3 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.12 ms: 1.14x faster                                                        |
| regex_dna      | 239 ms                                                       | 230 ms: 1.04x faster                                                         |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 94.3 ms: 1.09x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 81.3 ms: 1.06x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 199 us: 1.05x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 57.2 ms: 1.02x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.6 us: 1.05x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.53 ms: 1.05x faster                                                        |
| django_template | 38.2 ms                                                      | 39.1 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 644 ms: 1.64x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 657 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 505 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 526 ms: 1.32x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 28.5 us: 1.29x faster                                                        |
| deepcopy                   | 368 us                                                       | 300 us: 1.23x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.12 ms: 1.14x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.98 us: 1.13x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.0 ms: 1.11x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.7 us: 1.11x faster                                                        |
| scimark_sor                | 109 ms                                                       | 98.7 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 94.3 ms: 1.09x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.09x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 74.7 ms: 1.08x faster                                                        |
| go                         | 150 ms                                                       | 140 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 81.3 ms: 1.06x faster                                                        |
| float                      | 76.6 ms                                                      | 72.4 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.08 us: 1.06x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 199 us: 1.05x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.53 ms: 1.05x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.44 us: 1.04x faster                                                        |
| regex_dna                  | 239 ms                                                       | 230 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.2 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 57.2 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 90.2 ms: 1.02x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 97.4 ms: 1.01x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 160 ms: 1.01x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                       |
| richards                   | 45.7 ms                                                      | 46.1 ms: 1.01x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| 2to3                       | 285 ms                                                       | 292 ms: 1.02x slower                                                         |
| sympy_str                  | 302 ms                                                       | 309 ms: 1.02x slower                                                         |
| richards_super             | 51.3 ms                                                      | 52.5 ms: 1.02x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.1 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                        |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.7 ms: 1.04x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 983 us: 1.04x slower                                                         |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                                        |
| nbody                      | 88.0 ms                                                      | 91.3 ms: 1.04x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.6 us: 1.05x slower                                                        |
| fannkuch                   | 350 ms                                                       | 373 ms: 1.07x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                         |
| chaos                      | 64.0 ms                                                      | 69.0 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 125 ms: 1.08x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 62.2 ms: 1.08x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                        |
| generators                 | 37.4 ms                                                      | 40.7 ms: 1.09x slower                                                        |
| sympy_expand               | 484 ms                                                       | 526 ms: 1.09x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 101 ms: 1.12x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.86 ms: 1.13x slower                                                        |
| raytrace                   | 298 ms                                                       | 337 ms: 1.13x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.84 ms: 1.15x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.17x slower                                                         |
| async_generators           | 390 ms                                                       | 457 ms: 1.17x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.16 ms: 1.20x slower                                                        |
| coverage                   | 66.7 ms                                                      | 80.4 ms: 1.21x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.05 sec: 1.27x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.69 ms: 1.69x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.32 ms: 1.82x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.22 sec: 255.50x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (5): asyncio_websockets, pyflate, mdp, scimark_fft, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 76.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x