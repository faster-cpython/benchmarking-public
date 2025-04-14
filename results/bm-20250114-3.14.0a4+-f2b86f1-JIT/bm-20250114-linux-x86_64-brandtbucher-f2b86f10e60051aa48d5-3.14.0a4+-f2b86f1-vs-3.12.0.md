# Results vs. 3.12.0

- fork: brandtbucher
- ref: f2b86f10e60051aa48d5
- machine: linux-x86_64
- commit hash: f2b86f1
- commit date: 2025-01-14
- overall geometric mean: 1.100x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 593 ms: 2.00x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                         |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.78x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| nbody          | 97.0 ms                                                | 96.4 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.96 ms: 1.22x faster                                                        |
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_dna      | 212 ms                                                 | 196 ms: 1.08x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.18x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 94.9 ms: 1.13x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                         |
| json_loads           | 28.5 us                                                | 29.5 us: 1.04x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                        |
| django_template | 34.6 ms                                                | 33.4 ms: 1.04x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 593 ms: 2.00x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                         |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.78x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                         |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                       |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 2.96 ms: 1.22x faster                                                        |
| mako                       | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                        |
| float                      | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.18x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 70.7 ms: 1.16x faster                                                        |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| scimark_fft                | 382 ms                                                 | 333 ms: 1.15x faster                                                         |
| async_generators           | 463 ms                                                 | 405 ms: 1.14x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                        |
| logging_format             | 7.23 us                                                | 6.38 us: 1.13x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 94.9 ms: 1.13x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.76 us: 1.12x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                         |
| regex_dna                  | 212 ms                                                 | 196 ms: 1.08x faster                                                         |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.08x faster                                                         |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                         |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                        |
| chaos                      | 67.0 ms                                                | 62.8 ms: 1.07x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.78 ms: 1.06x faster                                                        |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                        |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                         |
| raytrace                   | 312 ms                                                 | 298 ms: 1.05x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                                        |
| django_template            | 34.6 ms                                                | 33.4 ms: 1.04x faster                                                        |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                        |
| go                         | 139 ms                                                 | 135 ms: 1.03x faster                                                         |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.6 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                         |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| nbody                      | 97.0 ms                                                | 96.4 ms: 1.01x faster                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.04x slower                                                        |
| spectral_norm              | 115 ms                                                 | 120 ms: 1.04x slower                                                         |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.05x slower                                                        |
| logging_silent             | 104 ns                                                 | 110 ns: 1.05x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.05x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 896 us: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.65 ms: 1.08x slower                                                        |
| nqueens                    | 83.3 ms                                                | 90.9 ms: 1.09x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.13 ms: 1.11x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                        |
| generators                 | 31.2 ms                                                | 37.3 ms: 1.20x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.55 ms: 1.20x slower                                                        |
| coverage                   | 72.7 ms                                                | 91.8 ms: 1.26x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (4): json, sqlglot_optimize, pycparser, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250114-3.14.0a4+-f2b86f1-JIT/bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.100x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x