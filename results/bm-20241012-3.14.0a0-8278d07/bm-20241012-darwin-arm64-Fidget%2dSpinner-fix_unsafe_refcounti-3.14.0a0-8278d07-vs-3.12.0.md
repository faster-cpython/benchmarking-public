# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: darwin-arm64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 196 ms: 1.16x slower                                                            |
| docutils       | 1.50 sec                                               | 1.41 sec: 1.06x faster                                                          |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 192 ms: 1.38x faster                                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 245 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                                            |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                                            |
| async_tree_io_tg           | 669 ms                                                 | 563 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                            |
| async_tree_io              | 668 ms                                                 | 593 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.0 ms: 1.14x faster                                                           |
| nbody          | 68.8 ms                                                | 65.6 ms: 1.05x faster                                                           |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.3 ms: 1.14x faster                                                           |
| regex_dna      | 154 ms                                                 | 146 ms: 1.05x faster                                                            |
| regex_effbot   | 2.64 ms                                                | 2.60 ms: 1.02x faster                                                           |
| regex_v8       | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 183 us: 1.09x faster                                                            |
| xml_etree_generate   | 55.8 ms                                                | 52.4 ms: 1.07x faster                                                           |
| xml_etree_process    | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                           |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                            |
| json_loads           | 17.2 us                                                | 16.4 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 74.0 ms                                                | 73.1 ms: 1.01x faster                                                           |
| unpickle_list        | 3.02 us                                                | 2.99 us: 1.01x faster                                                           |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                           |
| pickle_list          | 2.89 us                                                | 2.91 us: 1.01x slower                                                           |
| pickle               | 7.23 us                                                | 7.34 us: 1.02x slower                                                           |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.02x slower                                                            |
| tomli_loads          | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                          |
| json_dumps           | 6.22 ms                                                | 7.25 ms: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 19.0 ms: 1.67x slower                                                           |
| python_startup_no_site | 9.37 ms                                                | 15.9 ms: 1.70x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.68x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.0 ms: 1.11x faster                                                           |
| mako            | 7.71 ms                                                | 7.00 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                            |
| deepcopy_memo              | 27.7 us                                                | 17.3 us: 1.60x faster                                                           |
| deepcopy                   | 235 us                                                 | 147 us: 1.60x faster                                                            |
| generators                 | 31.1 ms                                                | 20.3 ms: 1.53x faster                                                           |
| async_tree_none            | 266 ms                                                 | 192 ms: 1.38x faster                                                            |
| raytrace                   | 212 ms                                                 | 154 ms: 1.37x faster                                                            |
| deepcopy_reduce            | 2.07 us                                                | 1.53 us: 1.35x faster                                                           |
| async_tree_memoization_tg  | 323 ms                                                 | 245 ms: 1.32x faster                                                            |
| comprehensions             | 14.5 us                                                | 11.0 us: 1.32x faster                                                           |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                                            |
| logging_silent             | 76.4 ns                                                | 60.6 ns: 1.26x faster                                                           |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                                            |
| go                         | 102 ms                                                 | 81.8 ms: 1.24x faster                                                           |
| deltablue                  | 2.71 ms                                                | 2.22 ms: 1.22x faster                                                           |
| logging_simple             | 3.69 us                                                | 3.05 us: 1.21x faster                                                           |
| logging_format             | 3.98 us                                                | 3.34 us: 1.19x faster                                                           |
| unpack_sequence            | 31.5 ns                                                | 26.4 ns: 1.19x faster                                                           |
| async_tree_io_tg           | 669 ms                                                 | 563 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                                            |
| coroutines                 | 19.2 ms                                                | 16.7 ms: 1.15x faster                                                           |
| nqueens                    | 62.4 ms                                                | 54.2 ms: 1.15x faster                                                           |
| sqlglot_parse              | 848 us                                                 | 743 us: 1.14x faster                                                            |
| regex_compile              | 77.9 ms                                                | 68.3 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                            |
| float                      | 55.8 ms                                                | 49.0 ms: 1.14x faster                                                           |
| chaos                      | 42.5 ms                                                | 37.4 ms: 1.14x faster                                                           |
| sqlglot_transpile          | 1.02 ms                                                | 898 us: 1.14x faster                                                            |
| scimark_lu                 | 76.0 ms                                                | 67.0 ms: 1.13x faster                                                           |
| async_tree_io              | 668 ms                                                 | 593 ms: 1.13x faster                                                            |
| sympy_sum                  | 77.6 ms                                                | 69.3 ms: 1.12x faster                                                           |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                                            |
| django_template            | 22.3 ms                                                | 20.0 ms: 1.11x faster                                                           |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.82 ms: 1.11x faster                                                           |
| bench_thread_pool          | 504 us                                                 | 455 us: 1.11x faster                                                            |
| sympy_str                  | 148 ms                                                 | 133 ms: 1.11x faster                                                            |
| mako                       | 7.71 ms                                                | 7.00 ms: 1.10x faster                                                           |
| pathlib                    | 24.2 ms                                                | 22.0 ms: 1.10x faster                                                           |
| sqlglot_optimize           | 34.0 ms                                                | 31.0 ms: 1.10x faster                                                           |
| hexiom                     | 4.54 ms                                                | 4.14 ms: 1.10x faster                                                           |
| json                       | 3.09 ms                                                | 2.82 ms: 1.09x faster                                                           |
| pickle_pure_python         | 200 us                                                 | 183 us: 1.09x faster                                                            |
| async_generators           | 304 ms                                                 | 279 ms: 1.09x faster                                                            |
| dulwich_log                | 29.8 ms                                                | 27.4 ms: 1.09x faster                                                           |
| spectral_norm              | 76.4 ms                                                | 70.8 ms: 1.08x faster                                                           |
| mdp                        | 1.58 sec                                               | 1.47 sec: 1.08x faster                                                          |
| pprint_safe_repr           | 497 ms                                                 | 461 ms: 1.08x faster                                                            |
| pprint_pformat             | 1.01 sec                                               | 943 ms: 1.07x faster                                                            |
| sympy_expand               | 241 ms                                                 | 225 ms: 1.07x faster                                                            |
| xml_etree_generate         | 55.8 ms                                                | 52.4 ms: 1.07x faster                                                           |
| docutils                   | 1.50 sec                                               | 1.41 sec: 1.06x faster                                                          |
| pycparser                  | 677 ms                                                 | 638 ms: 1.06x faster                                                            |
| xml_etree_process          | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                           |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                            |
| regex_dna                  | 154 ms                                                 | 146 ms: 1.05x faster                                                            |
| nbody                      | 68.8 ms                                                | 65.6 ms: 1.05x faster                                                           |
| json_loads                 | 17.2 us                                                | 16.4 us: 1.05x faster                                                           |
| sqlite_synth               | 1.57 us                                                | 1.52 us: 1.04x faster                                                           |
| richards_super             | 36.0 ms                                                | 34.8 ms: 1.03x faster                                                           |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.03x faster                                                           |
| richards                   | 32.1 ms                                                | 31.2 ms: 1.03x faster                                                           |
| scimark_monte_carlo        | 45.0 ms                                                | 43.7 ms: 1.03x faster                                                           |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                                            |
| regex_effbot               | 2.64 ms                                                | 2.60 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 74.0 ms                                                | 73.1 ms: 1.01x faster                                                           |
| crypto_pyaes               | 51.9 ms                                                | 51.2 ms: 1.01x faster                                                           |
| unpickle_list              | 3.02 us                                                | 2.99 us: 1.01x faster                                                           |
| meteor_contest             | 71.7 ms                                                | 71.5 ms: 1.00x faster                                                           |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                            |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                           |
| pickle_list                | 2.89 us                                                | 2.91 us: 1.01x slower                                                           |
| pickle                     | 7.23 us                                                | 7.34 us: 1.02x slower                                                           |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.02x slower                                                            |
| regex_v8                   | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                           |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                          |
| pyflate                    | 316 ms                                                 | 327 ms: 1.04x slower                                                            |
| gc_traversal               | 2.40 ms                                                | 2.50 ms: 1.04x slower                                                           |
| fannkuch                   | 248 ms                                                 | 266 ms: 1.07x slower                                                            |
| tomli_loads                | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                          |
| scimark_sor                | 87.4 ms                                                | 95.9 ms: 1.10x slower                                                           |
| coverage                   | 38.9 ms                                                | 43.6 ms: 1.12x slower                                                           |
| bench_mp_pool              | 44.9 ms                                                | 50.5 ms: 1.12x slower                                                           |
| 2to3                       | 169 ms                                                 | 196 ms: 1.16x slower                                                            |
| json_dumps                 | 6.22 ms                                                | 7.25 ms: 1.17x slower                                                           |
| telco                      | 3.68 ms                                                | 4.57 ms: 1.24x slower                                                           |
| create_gc_cycles           | 701 us                                                 | 929 us: 1.32x slower                                                            |
| python_startup             | 11.4 ms                                                | 19.0 ms: 1.67x slower                                                           |
| python_startup_no_site     | 9.37 ms                                                | 15.9 ms: 1.70x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): asyncio_tcp, typing_runtime_protocols, unpickle, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.67x