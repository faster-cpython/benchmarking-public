# Results vs. 3.12.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 1baa231
- commit date: 2025-04-01
- overall geometric mean: 1.097x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                          |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                          |
| async_tree_io              | 1.16 sec                                               | 630 ms: 1.84x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                          |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 323 ms: 1.78x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                          |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 74.8 ms: 1.13x faster                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                          |
| nbody          | 97.0 ms                                                | 98.5 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                         |
| regex_v8       | 23.1 ms                                                | 22.9 ms: 1.01x faster                                         |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                         |
| unpickle_pure_python | 230 us                                                 | 225 us: 1.02x faster                                          |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                         |
| json_loads           | 28.5 us                                                | 32.0 us: 1.12x slower                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                         |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.5 ms: 1.07x faster                                         |
| mako            | 11.9 ms                                                | 11.9 ms: 1.00x slower                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.26 sec: 2.09x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                          |
| async_tree_io              | 1.16 sec                                               | 630 ms: 1.84x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                          |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 323 ms: 1.78x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                          |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.32x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                        |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                         |
| spectral_norm              | 115 ms                                                 | 98.2 ms: 1.17x faster                                         |
| chaos                      | 67.0 ms                                                | 57.5 ms: 1.17x faster                                         |
| async_generators           | 463 ms                                                 | 401 ms: 1.16x faster                                          |
| raytrace                   | 312 ms                                                 | 270 ms: 1.15x faster                                          |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                          |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                         |
| dulwich_log                | 68.5 ms                                                | 59.6 ms: 1.15x faster                                         |
| logging_simple             | 6.46 us                                                | 5.70 us: 1.13x faster                                         |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                          |
| float                      | 84.7 ms                                                | 74.8 ms: 1.13x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                          |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                         |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                          |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                         |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.7 ms: 1.09x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                         |
| coroutines                 | 23.2 ms                                                | 21.5 ms: 1.08x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                         |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.07x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.09 ms: 1.05x faster                                         |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                          |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                        |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                         |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                         |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                          |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                          |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                         |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                          |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 759 ms: 1.02x faster                                          |
| unpickle_pure_python       | 230 us                                                 | 225 us: 1.02x faster                                          |
| regex_v8                   | 23.1 ms                                                | 22.9 ms: 1.01x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                        |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                          |
| mako                       | 11.9 ms                                                | 11.9 ms: 1.00x slower                                         |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                         |
| richards                   | 45.8 ms                                                | 46.2 ms: 1.01x slower                                         |
| richards_super             | 51.5 ms                                                | 52.2 ms: 1.01x slower                                         |
| crypto_pyaes               | 81.9 ms                                                | 83.0 ms: 1.01x slower                                         |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                        |
| nbody                      | 97.0 ms                                                | 98.5 ms: 1.02x slower                                         |
| fannkuch                   | 417 ms                                                 | 430 ms: 1.03x slower                                          |
| scimark_fft                | 382 ms                                                 | 394 ms: 1.03x slower                                          |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                          |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                          |
| json                       | 5.26 ms                                                | 5.52 ms: 1.05x slower                                         |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                          |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.43 ms: 1.07x slower                                         |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                         |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                         |
| json_loads                 | 28.5 us                                                | 32.0 us: 1.12x slower                                         |
| coverage                   | 72.7 ms                                                | 83.9 ms: 1.15x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                         |
| gc_traversal               | 3.79 ms                                                | 5.07 ms: 1.34x slower                                         |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.6 ms: 3.48x slower                                         |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (3): nqueens, asyncio_websockets, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-1baa231/bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.097x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x