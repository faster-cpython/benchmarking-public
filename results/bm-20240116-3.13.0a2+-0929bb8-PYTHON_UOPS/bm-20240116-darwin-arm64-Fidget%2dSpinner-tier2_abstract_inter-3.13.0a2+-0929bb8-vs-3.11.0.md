
# Results vs. 3.11.0

- fork: Fidget-Spinner
- ref: tier2_abstract_inter
- machine: darwin-arm64
- commit hash: 0929bb8
- commit date: 2024-01-16
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240116-darwin-arm64-Fidget%2dSpinner-tier2_abstract_inter-3.13.0a2+-0929bb8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 176 ms: 1.14x slower                                                             |
| chameleon      | 4.30 ms                                                | 5.16 ms: 1.20x slower                                                            |
| docutils       | 1.43 sec                                               | 1.51 sec: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240116-darwin-arm64-Fidget%2dSpinner-tier2_abstract_inter-3.13.0a2+-0929bb8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 282 ms                                                 | 259 ms: 1.09x faster                                                             |
| async_tree_memoization_tg  | 352 ms                                                 | 334 ms: 1.06x faster                                                             |
| async_tree_io_tg           | 724 ms                                                 | 687 ms: 1.05x faster                                                             |
| async_tree_none_tg         | 276 ms                                                 | 266 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 537 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 528 ms: 1.02x slower                                                             |
| async_tree_io              | 697 ms                                                 | 716 ms: 1.03x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240116-darwin-arm64-Fidget%2dSpinner-tier2_abstract_inter-3.13.0a2+-0929bb8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                             |
| float          | 50.8 ms                                                | 68.1 ms: 1.34x slower                                                            |
| nbody          | 61.7 ms                                                | 118 ms: 1.91x slower                                                             |
| Geometric mean | (ref)                                                  | 1.37x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240116-darwin-arm64-Fidget%2dSpinner-tier2_abstract_inter-3.13.0a2+-0929bb8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 156 ms: 1.05x slower                                                             |
| regex_compile  | 72.8 ms                                                | 82.0 ms: 1.13x slower                                                            |
| regex_effbot   | 2.43 ms                                                | 2.75 ms: 1.13x slower                                                            |
| regex_v8       | 15.1 ms                                                | 17.9 ms: 1.18x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240116-darwin-arm64-Fidget%2dSpinner-tier2_abstract_inter-3.13.0a2+-0929bb8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.58 ms: 1.14x faster                                                            |
| pickle_pure_python   | 191 us                                                 | 197 us: 1.03x slower                                                             |
| pickle_dict          | 17.1 us                                                | 18.2 us: 1.06x slower                                                            |
| xml_etree_parse      | 100 ms                                                 | 107 ms: 1.07x slower                                                             |
| pickle               | 6.98 us                                                | 7.48 us: 1.07x slower                                                            |
| pickle_list          | 2.70 us                                                | 2.95 us: 1.09x slower                                                            |
| unpickle_pure_python | 149 us                                                 | 164 us: 1.11x slower                                                             |
| unpickle             | 8.29 us                                                | 9.17 us: 1.11x slower                                                            |
| json_loads           | 15.3 us                                                | 17.1 us: 1.11x slower                                                            |
| unpickle_list        | 2.69 us                                                | 3.00 us: 1.12x slower                                                            |
| xml_etree_iterparse  | 68.3 ms                                                | 80.4 ms: 1.18x slower                                                            |
| xml_etree_process    | 33.6 ms                                                | 40.6 ms: 1.21x slower                                                            |
| tomli_loads          | 1.27 sec                                               | 1.64 sec: 1.29x slower                                                           |
| xml_etree_generate   | 45.8 ms                                                | 59.4 ms: 1.30x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240116-darwin-arm64-Fidget%2dSpinner-tier2_abstract_inter-3.13.0a2+-0929bb8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 12.3 ms: 1.15x slower                                                            |
| python_startup_no_site | 8.57 ms                                                | 11.0 ms: 1.28x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240116-darwin-arm64-Fidget%2dSpinner-tier2_abstract_inter-3.13.0a2+-0929bb8 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako      | 7.93 ms                                                | 9.66 ms: 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240116-darwin-arm64-Fidget%2dSpinner-tier2_abstract_inter-3.13.0a2+-0929bb8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 74.3 us: 4.05x faster                                                            |
| asyncio_tcp                | 643 ms                                                 | 374 ms: 1.72x faster                                                             |
| json_dumps                 | 7.53 ms                                                | 6.58 ms: 1.14x faster                                                            |
| unpack_sequence            | 33.6 ns                                                | 29.9 ns: 1.13x faster                                                            |
| raytrace                   | 206 ms                                                 | 186 ms: 1.10x faster                                                             |
| sqlglot_parse              | 890 us                                                 | 813 us: 1.09x faster                                                             |
| async_tree_none            | 282 ms                                                 | 259 ms: 1.09x faster                                                             |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.06x faster                                                           |
| sqlglot_transpile          | 1.05 ms                                                | 994 us: 1.06x faster                                                             |
| async_tree_memoization_tg  | 352 ms                                                 | 334 ms: 1.06x faster                                                             |
| async_tree_io_tg           | 724 ms                                                 | 687 ms: 1.05x faster                                                             |
| generators                 | 30.3 ms                                                | 28.9 ms: 1.05x faster                                                            |
| async_tree_none_tg         | 276 ms                                                 | 266 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 537 ms: 1.02x faster                                                             |
| create_gc_cycles           | 711 us                                                 | 704 us: 1.01x faster                                                             |
| richards_super             | 37.3 ms                                                | 36.9 ms: 1.01x faster                                                            |
| sympy_sum                  | 80.2 ms                                                | 80.6 ms: 1.01x slower                                                            |
| gc_traversal               | 2.38 ms                                                | 2.40 ms: 1.01x slower                                                            |
| pidigits                   | 280 ms                                                 | 284 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 528 ms: 1.02x slower                                                             |
| chaos                      | 47.4 ms                                                | 48.4 ms: 1.02x slower                                                            |
| async_tree_io              | 697 ms                                                 | 716 ms: 1.03x slower                                                             |
| pickle_pure_python         | 191 us                                                 | 197 us: 1.03x slower                                                             |
| deepcopy_memo              | 25.7 us                                                | 26.7 us: 1.04x slower                                                            |
| sympy_str                  | 144 ms                                                 | 149 ms: 1.04x slower                                                             |
| dask                       | 219 ms                                                 | 228 ms: 1.04x slower                                                             |
| logging_simple             | 3.41 us                                                | 3.57 us: 1.05x slower                                                            |
| logging_format             | 3.67 us                                                | 3.85 us: 1.05x slower                                                            |
| sympy_integrate            | 11.3 ms                                                | 11.8 ms: 1.05x slower                                                            |
| regex_dna                  | 148 ms                                                 | 156 ms: 1.05x slower                                                             |
| richards                   | 31.1 ms                                                | 32.6 ms: 1.05x slower                                                            |
| deepcopy                   | 215 us                                                 | 226 us: 1.05x slower                                                             |
| dulwich_log                | 28.6 ms                                                | 30.1 ms: 1.05x slower                                                            |
| go                         | 105 ms                                                 | 111 ms: 1.05x slower                                                             |
| docutils                   | 1.43 sec                                               | 1.51 sec: 1.05x slower                                                           |
| pickle_dict                | 17.1 us                                                | 18.2 us: 1.06x slower                                                            |
| xml_etree_parse            | 100 ms                                                 | 107 ms: 1.07x slower                                                             |
| json                       | 2.75 ms                                                | 2.94 ms: 1.07x slower                                                            |
| pycparser                  | 659 ms                                                 | 706 ms: 1.07x slower                                                             |
| pickle                     | 6.98 us                                                | 7.48 us: 1.07x slower                                                            |
| sympy_expand               | 229 ms                                                 | 246 ms: 1.08x slower                                                             |
| meteor_contest             | 71.1 ms                                                | 76.7 ms: 1.08x slower                                                            |
| coverage                   | 43.9 ms                                                | 47.4 ms: 1.08x slower                                                            |
| logging_silent             | 66.5 ns                                                | 72.1 ns: 1.08x slower                                                            |
| comprehensions             | 14.4 us                                                | 15.7 us: 1.09x slower                                                            |
| mdp                        | 1.48 sec                                               | 1.62 sec: 1.09x slower                                                           |
| pickle_list                | 2.70 us                                                | 2.95 us: 1.09x slower                                                            |
| pathlib                    | 23.2 ms                                                | 25.6 ms: 1.10x slower                                                            |
| unpickle_pure_python       | 149 us                                                 | 164 us: 1.11x slower                                                             |
| unpickle                   | 8.29 us                                                | 9.17 us: 1.11x slower                                                            |
| bench_mp_pool              | 41.0 ms                                                | 45.4 ms: 1.11x slower                                                            |
| deepcopy_reduce            | 1.79 us                                                | 1.99 us: 1.11x slower                                                            |
| bench_thread_pool          | 465 us                                                 | 517 us: 1.11x slower                                                             |
| json_loads                 | 15.3 us                                                | 17.1 us: 1.11x slower                                                            |
| unpickle_list              | 2.69 us                                                | 3.00 us: 1.12x slower                                                            |
| regex_compile              | 72.8 ms                                                | 82.0 ms: 1.13x slower                                                            |
| scimark_lu                 | 67.7 ms                                                | 76.5 ms: 1.13x slower                                                            |
| regex_effbot               | 2.43 ms                                                | 2.75 ms: 1.13x slower                                                            |
| 2to3                       | 154 ms                                                 | 176 ms: 1.14x slower                                                             |
| python_startup             | 10.8 ms                                                | 12.3 ms: 1.15x slower                                                            |
| coroutines                 | 17.2 ms                                                | 19.8 ms: 1.15x slower                                                            |
| crypto_pyaes               | 47.5 ms                                                | 54.7 ms: 1.15x slower                                                            |
| sqlglot_normalize          | 162 ms                                                 | 190 ms: 1.18x slower                                                             |
| xml_etree_iterparse        | 68.3 ms                                                | 80.4 ms: 1.18x slower                                                            |
| regex_v8                   | 15.1 ms                                                | 17.9 ms: 1.18x slower                                                            |
| chameleon                  | 4.30 ms                                                | 5.16 ms: 1.20x slower                                                            |
| xml_etree_process          | 33.6 ms                                                | 40.6 ms: 1.21x slower                                                            |
| nqueens                    | 55.9 ms                                                | 67.7 ms: 1.21x slower                                                            |
| sqlglot_optimize           | 29.6 ms                                                | 36.0 ms: 1.22x slower                                                            |
| mako                       | 7.93 ms                                                | 9.66 ms: 1.22x slower                                                            |
| pprint_pformat             | 979 ms                                                 | 1.21 sec: 1.23x slower                                                           |
| pprint_safe_repr           | 478 ms                                                 | 590 ms: 1.23x slower                                                             |
| python_startup_no_site     | 8.57 ms                                                | 11.0 ms: 1.28x slower                                                            |
| tomli_loads                | 1.27 sec                                               | 1.64 sec: 1.29x slower                                                           |
| pyflate                    | 284 ms                                                 | 366 ms: 1.29x slower                                                             |
| xml_etree_generate         | 45.8 ms                                                | 59.4 ms: 1.30x slower                                                            |
| deltablue                  | 2.75 ms                                                | 3.58 ms: 1.30x slower                                                            |
| sqlite_synth               | 1.26 us                                                | 1.64 us: 1.30x slower                                                            |
| hexiom                     | 4.58 ms                                                | 5.97 ms: 1.30x slower                                                            |
| scimark_monte_carlo        | 43.5 ms                                                | 57.1 ms: 1.31x slower                                                            |
| fannkuch                   | 240 ms                                                 | 316 ms: 1.32x slower                                                             |
| float                      | 50.8 ms                                                | 68.1 ms: 1.34x slower                                                            |
| scimark_sor                | 79.2 ms                                                | 107 ms: 1.35x slower                                                             |
| mypy2                      | 372 ms                                                 | 529 ms: 1.42x slower                                                             |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 4.06 ms: 1.45x slower                                                            |
| telco                      | 3.17 ms                                                | 4.68 ms: 1.48x slower                                                            |
| scimark_fft                | 173 ms                                                 | 255 ms: 1.48x slower                                                             |
| spectral_norm              | 65.7 ms                                                | 101 ms: 1.54x slower                                                             |
| async_generators           | 192 ms                                                 | 299 ms: 1.55x slower                                                             |
| nbody                      | 61.7 ms                                                | 118 ms: 1.91x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.09x slower                                                                     |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_memoization, tornado_http
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x


# Memory

- memory change: 1.31x