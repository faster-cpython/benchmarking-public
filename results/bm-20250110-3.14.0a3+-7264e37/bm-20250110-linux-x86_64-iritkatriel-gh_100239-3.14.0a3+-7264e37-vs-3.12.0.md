# Results vs. 3.12.0

- fork: iritkatriel
- ref: gh_100239
- machine: linux-x86_64
- commit hash: 7264e37
- commit date: 2025-01-10
- overall geometric mean: 1.115x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                             |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 587 ms: 2.01x faster                                             |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                             |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 461 ms: 1.57x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                             |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.9 ms: 1.18x faster                                            |
| nbody          | 97.0 ms                                                | 94.2 ms: 1.03x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                             |
| regex_effbot   | 3.61 ms                                                | 3.48 ms: 1.04x faster                                            |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                             |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                           |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 97.5 ms: 1.10x faster                                            |
| json_loads           | 28.5 us                                                | 26.5 us: 1.08x faster                                            |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 85.3 ms: 1.04x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 59.5 ms: 1.04x faster                                            |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                            |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                            |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                            |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                            |
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                            |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 587 ms: 2.01x faster                                             |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                             |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 461 ms: 1.57x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                             |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 31.2 us: 1.30x faster                                            |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                            |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                           |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                             |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                            |
| spectral_norm              | 115 ms                                                 | 96.3 ms: 1.19x faster                                            |
| float                      | 84.7 ms                                                | 71.9 ms: 1.18x faster                                            |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                            |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                             |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                            |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                             |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                            |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                            |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                             |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 72.0 ms: 1.14x faster                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.13x faster                                            |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                            |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                            |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                             |
| async_generators           | 463 ms                                                 | 421 ms: 1.10x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 97.5 ms: 1.10x faster                                            |
| scimark_fft                | 382 ms                                                 | 349 ms: 1.09x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.08x faster                                            |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                            |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                             |
| dulwich_log                | 68.5 ms                                                | 63.5 ms: 1.08x faster                                            |
| json_loads                 | 28.5 us                                                | 26.5 us: 1.08x faster                                            |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.07x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                             |
| json                       | 5.26 ms                                                | 4.91 ms: 1.07x faster                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                            |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                           |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                             |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.06x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                           |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                           |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                             |
| nqueens                    | 83.3 ms                                                | 79.4 ms: 1.05x faster                                            |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                           |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.05x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 85.3 ms: 1.04x faster                                            |
| sqlglot_optimize           | 54.8 ms                                                | 52.7 ms: 1.04x faster                                            |
| regex_effbot               | 3.61 ms                                                | 3.48 ms: 1.04x faster                                            |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                            |
| xml_etree_process          | 61.7 ms                                                | 59.5 ms: 1.04x faster                                            |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                            |
| nbody                      | 97.0 ms                                                | 94.2 ms: 1.03x faster                                            |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                            |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                             |
| richards_super             | 51.5 ms                                                | 50.8 ms: 1.01x faster                                            |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                            |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                            |
| bench_thread_pool          | 842 us                                                 | 861 us: 1.02x slower                                             |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                             |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                             |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.09x slower                                            |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                            |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                            |
| coverage                   | 72.7 ms                                                | 84.5 ms: 1.16x slower                                            |
| gc_traversal               | 3.79 ms                                                | 4.85 ms: 1.28x slower                                            |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                            |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                     |

Benchmark hidden because not significant (2): pickle_pure_python, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250110-3.14.0a3+-7264e37/bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.115x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x