# Results vs. 3.12.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: darwin-arm64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.76x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                                            |
| docutils       | 1.50 sec                                               | 1.40 sec: 1.07x faster                                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 192 ms: 1.38x faster                                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 245 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                                            |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                                            |
| async_tree_io_tg           | 669 ms                                                 | 562 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.15x faster                                                            |
| async_tree_io              | 668 ms                                                 | 593 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                           |
| nbody          | 68.8 ms                                                | 65.4 ms: 1.05x faster                                                           |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.8 ms: 1.15x faster                                                           |
| regex_dna      | 154 ms                                                 | 148 ms: 1.05x faster                                                            |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.00x faster                                                           |
| regex_v8       | 16.0 ms                                                | 16.7 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 184 us: 1.09x faster                                                            |
| xml_etree_generate   | 55.8 ms                                                | 52.1 ms: 1.07x faster                                                           |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                            |
| xml_etree_process    | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                           |
| json_loads           | 17.2 us                                                | 16.7 us: 1.03x faster                                                           |
| unpickle_list        | 3.02 us                                                | 2.96 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 74.0 ms                                                | 73.4 ms: 1.01x faster                                                           |
| unpickle             | 9.12 us                                                | 9.07 us: 1.01x faster                                                           |
| pickle               | 7.23 us                                                | 7.33 us: 1.01x slower                                                           |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.02x slower                                                            |
| pickle_list          | 2.89 us                                                | 2.96 us: 1.03x slower                                                           |
| tomli_loads          | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): json_dumps, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                           |
| python_startup_no_site | 9.37 ms                                                | 14.2 ms: 1.51x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                           |
| mako            | 7.71 ms                                                | 6.97 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.69x faster                                                            |
| deepcopy_memo              | 27.7 us                                                | 17.1 us: 1.62x faster                                                           |
| deepcopy                   | 235 us                                                 | 147 us: 1.60x faster                                                            |
| generators                 | 31.1 ms                                                | 20.3 ms: 1.53x faster                                                           |
| raytrace                   | 212 ms                                                 | 153 ms: 1.38x faster                                                            |
| async_tree_none            | 266 ms                                                 | 192 ms: 1.38x faster                                                            |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                                           |
| comprehensions             | 14.5 us                                                | 11.0 us: 1.32x faster                                                           |
| async_tree_memoization_tg  | 323 ms                                                 | 245 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                                            |
| logging_silent             | 76.4 ns                                                | 60.5 ns: 1.26x faster                                                           |
| go                         | 102 ms                                                 | 81.6 ms: 1.24x faster                                                           |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                                            |
| deltablue                  | 2.71 ms                                                | 2.23 ms: 1.22x faster                                                           |
| logging_simple             | 3.69 us                                                | 3.05 us: 1.21x faster                                                           |
| logging_format             | 3.98 us                                                | 3.34 us: 1.19x faster                                                           |
| unpack_sequence            | 31.5 ns                                                | 26.4 ns: 1.19x faster                                                           |
| async_tree_io_tg           | 669 ms                                                 | 562 ms: 1.19x faster                                                            |
| chaos                      | 42.5 ms                                                | 36.3 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                            |
| coroutines                 | 19.2 ms                                                | 16.6 ms: 1.16x faster                                                           |
| sqlglot_parse              | 848 us                                                 | 737 us: 1.15x faster                                                            |
| regex_compile              | 77.9 ms                                                | 67.8 ms: 1.15x faster                                                           |
| nqueens                    | 62.4 ms                                                | 54.4 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.15x faster                                                            |
| float                      | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                           |
| sqlglot_transpile          | 1.02 ms                                                | 896 us: 1.14x faster                                                            |
| scimark_lu                 | 76.0 ms                                                | 66.9 ms: 1.14x faster                                                           |
| async_tree_io              | 668 ms                                                 | 593 ms: 1.13x faster                                                            |
| django_template            | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                           |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                                            |
| sympy_sum                  | 77.6 ms                                                | 69.7 ms: 1.11x faster                                                           |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.82 ms: 1.11x faster                                                           |
| bench_thread_pool          | 504 us                                                 | 455 us: 1.11x faster                                                            |
| mako                       | 7.71 ms                                                | 6.97 ms: 1.11x faster                                                           |
| sympy_str                  | 148 ms                                                 | 134 ms: 1.10x faster                                                            |
| pathlib                    | 24.2 ms                                                | 21.9 ms: 1.10x faster                                                           |
| sqlglot_optimize           | 34.0 ms                                                | 30.9 ms: 1.10x faster                                                           |
| async_generators           | 304 ms                                                 | 276 ms: 1.10x faster                                                            |
| hexiom                     | 4.54 ms                                                | 4.14 ms: 1.10x faster                                                           |
| pickle_pure_python         | 200 us                                                 | 184 us: 1.09x faster                                                            |
| dulwich_log                | 29.8 ms                                                | 27.4 ms: 1.09x faster                                                           |
| pprint_safe_repr           | 497 ms                                                 | 457 ms: 1.09x faster                                                            |
| spectral_norm              | 76.4 ms                                                | 70.2 ms: 1.09x faster                                                           |
| mdp                        | 1.58 sec                                               | 1.46 sec: 1.09x faster                                                          |
| json                       | 3.09 ms                                                | 2.87 ms: 1.08x faster                                                           |
| pprint_pformat             | 1.01 sec                                               | 940 ms: 1.08x faster                                                            |
| docutils                   | 1.50 sec                                               | 1.40 sec: 1.07x faster                                                          |
| xml_etree_generate         | 55.8 ms                                                | 52.1 ms: 1.07x faster                                                           |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.07x faster                                                            |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                                            |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                            |
| pycparser                  | 677 ms                                                 | 639 ms: 1.06x faster                                                            |
| xml_etree_process          | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                           |
| nbody                      | 68.8 ms                                                | 65.4 ms: 1.05x faster                                                           |
| richards_super             | 36.0 ms                                                | 34.4 ms: 1.05x faster                                                           |
| regex_dna                  | 154 ms                                                 | 148 ms: 1.05x faster                                                            |
| sympy_integrate            | 11.4 ms                                                | 10.9 ms: 1.04x faster                                                           |
| sqlite_synth               | 1.57 us                                                | 1.52 us: 1.04x faster                                                           |
| json_loads                 | 17.2 us                                                | 16.7 us: 1.03x faster                                                           |
| richards                   | 32.1 ms                                                | 31.2 ms: 1.03x faster                                                           |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                            |
| unpickle_list              | 3.02 us                                                | 2.96 us: 1.02x faster                                                           |
| meteor_contest             | 71.7 ms                                                | 70.5 ms: 1.02x faster                                                           |
| crypto_pyaes               | 51.9 ms                                                | 51.2 ms: 1.01x faster                                                           |
| scimark_monte_carlo        | 45.0 ms                                                | 44.4 ms: 1.01x faster                                                           |
| xml_etree_iterparse        | 74.0 ms                                                | 73.4 ms: 1.01x faster                                                           |
| unpickle                   | 9.12 us                                                | 9.07 us: 1.01x faster                                                           |
| regex_effbot               | 2.64 ms                                                | 2.63 ms: 1.00x faster                                                           |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                            |
| pickle                     | 7.23 us                                                | 7.33 us: 1.01x slower                                                           |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.02x slower                                                            |
| pickle_list                | 2.89 us                                                | 2.96 us: 1.03x slower                                                           |
| pyflate                    | 316 ms                                                 | 326 ms: 1.03x slower                                                            |
| gc_traversal               | 2.40 ms                                                | 2.49 ms: 1.04x slower                                                           |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                          |
| regex_v8                   | 16.0 ms                                                | 16.7 ms: 1.05x slower                                                           |
| fannkuch                   | 248 ms                                                 | 262 ms: 1.06x slower                                                            |
| tomli_loads                | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                          |
| scimark_sor                | 87.4 ms                                                | 95.1 ms: 1.09x slower                                                           |
| bench_mp_pool              | 44.9 ms                                                | 49.3 ms: 1.10x slower                                                           |
| coverage                   | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                           |
| telco                      | 3.68 ms                                                | 4.64 ms: 1.26x slower                                                           |
| create_gc_cycles           | 701 us                                                 | 918 us: 1.31x slower                                                            |
| python_startup             | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                           |
| python_startup_no_site     | 9.37 ms                                                | 14.2 ms: 1.51x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (5): asyncio_tcp, json_dumps, typing_runtime_protocols, pickle_dict, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.76x