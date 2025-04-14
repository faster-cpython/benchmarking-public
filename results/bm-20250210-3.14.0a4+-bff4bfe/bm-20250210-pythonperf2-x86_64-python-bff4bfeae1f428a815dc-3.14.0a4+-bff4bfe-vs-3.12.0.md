# Results vs. 3.12.0

- fork: python
- ref: bff4bfeae1f428a815dc
- machine: linux-x86_64
- commit hash: bff4bfe
- commit date: 2025-02-10
- overall geometric mean: 1.047x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 651 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 657 ms: 1.59x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 342 ms: 1.58x faster                                                         |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.52x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 285 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 515 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 526 ms: 1.32x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.50x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.7 ms: 1.10x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.12 ms: 1.15x faster                                                        |
| regex_compile  | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.4 ms: 1.08x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 327 us: 1.03x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.09x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.2 ms: 1.08x faster                                                        |
| mako            | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 651 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 657 ms: 1.59x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 342 ms: 1.58x faster                                                         |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.52x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 285 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 515 ms: 1.35x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.0 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 526 ms: 1.32x faster                                                         |
| deepcopy                   | 368 us                                                       | 281 us: 1.31x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.24x faster                                                        |
| go                         | 150 ms                                                       | 127 ms: 1.18x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.17x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.12 ms: 1.15x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 60.8 ms: 1.14x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 71.7 ms: 1.12x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.11x faster                                                         |
| logging_format             | 7.48 us                                                      | 6.78 us: 1.10x faster                                                        |
| float                      | 76.6 ms                                                      | 69.7 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.19 us: 1.08x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.2 ms: 1.08x faster                                                        |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.4 ms: 1.08x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 85.1 ms: 1.08x faster                                                        |
| regex_compile              | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                         |
| chaos                      | 64.0 ms                                                      | 60.2 ms: 1.06x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.8 ms: 1.05x faster                                                        |
| sympy_str                  | 302 ms                                                       | 287 ms: 1.05x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.03x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.03x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.72 ms: 1.03x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 87.1 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.7 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 783 ms: 1.03x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                       |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                        |
| 2to3                       | 285 ms                                                       | 281 ms: 1.02x faster                                                         |
| unpickle_pure_python       | 210 us                                                       | 207 us: 1.01x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 56.8 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 116 ms                                                       | 115 ms: 1.01x faster                                                         |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                         |
| sympy_expand               | 484 ms                                                       | 488 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                        |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                         |
| pyflate                    | 439 ms                                                       | 445 ms: 1.01x slower                                                         |
| richards_super             | 51.3 ms                                                      | 52.1 ms: 1.01x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.07 ms: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.6 ms: 1.02x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 327 us: 1.03x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.35 ms: 1.04x slower                                                        |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.04x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 97.7 ns: 1.04x slower                                                        |
| scimark_fft                | 301 ms                                                       | 313 ms: 1.04x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                        |
| async_generators           | 390 ms                                                       | 411 ms: 1.05x slower                                                         |
| json                       | 5.12 ms                                                      | 5.42 ms: 1.06x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.09x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 167 us: 1.10x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.95 ms: 1.14x slower                                                        |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.86 ms: 1.15x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.0 ms: 1.17x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.73 ms: 1.72x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.37 ms: 1.83x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.24 sec: 260.65x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (5): bench_thread_pool, asyncio_websockets, richards, docutils, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250210-3.14.0a4+-bff4bfe/bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x