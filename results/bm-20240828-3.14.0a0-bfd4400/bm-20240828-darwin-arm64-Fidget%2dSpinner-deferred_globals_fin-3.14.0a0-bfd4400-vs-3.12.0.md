# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: darwin-arm64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 163 ms: 1.04x faster                                                            |
| docutils       | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                          |
| tornado_http   | 69.3 ms                                                | 78.8 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 229 ms: 1.41x faster                                                            |
| async_tree_none_tg         | 258 ms                                                 | 184 ms: 1.40x faster                                                            |
| async_tree_none            | 266 ms                                                 | 196 ms: 1.35x faster                                                            |
| async_tree_io_tg           | 669 ms                                                 | 507 ms: 1.32x faster                                                            |
| async_tree_memoization     | 312 ms                                                 | 242 ms: 1.29x faster                                                            |
| async_tree_io              | 668 ms                                                 | 547 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 442 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.4 ms: 1.16x faster                                                           |
| float          | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.5 ms: 1.14x faster                                                           |
| regex_dna      | 154 ms                                                 | 146 ms: 1.06x faster                                                            |
| regex_effbot   | 2.64 ms                                                | 2.50 ms: 1.06x faster                                                           |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 184 us: 1.09x faster                                                            |
| unpickle_pure_python | 151 us                                                 | 144 us: 1.05x faster                                                            |
| xml_etree_generate   | 55.8 ms                                                | 53.4 ms: 1.05x faster                                                           |
| xml_etree_process    | 39.7 ms                                                | 38.3 ms: 1.04x faster                                                           |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                                            |
| json_dumps           | 6.22 ms                                                | 6.52 ms: 1.05x slower                                                           |
| tomli_loads          | 1.39 sec                                               | 1.50 sec: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.4 ms: 1.43x slower                                                           |
| python_startup         | 11.4 ms                                                | 16.4 ms: 1.44x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.8 ms: 1.13x faster                                                           |
| mako            | 7.71 ms                                                | 7.16 ms: 1.08x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.1 us: 1.62x faster                                                           |
| deepcopy                   | 235 us                                                 | 146 us: 1.61x faster                                                            |
| generators                 | 31.1 ms                                                | 20.6 ms: 1.51x faster                                                           |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 229 ms: 1.41x faster                                                            |
| async_tree_none_tg         | 258 ms                                                 | 184 ms: 1.40x faster                                                            |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                                           |
| async_tree_none            | 266 ms                                                 | 196 ms: 1.35x faster                                                            |
| async_tree_io_tg           | 669 ms                                                 | 507 ms: 1.32x faster                                                            |
| comprehensions             | 14.5 us                                                | 11.0 us: 1.32x faster                                                           |
| async_tree_memoization     | 312 ms                                                 | 242 ms: 1.29x faster                                                            |
| deltablue                  | 2.71 ms                                                | 2.12 ms: 1.28x faster                                                           |
| logging_silent             | 76.4 ns                                                | 60.4 ns: 1.27x faster                                                           |
| async_tree_io              | 668 ms                                                 | 547 ms: 1.22x faster                                                            |
| logging_simple             | 3.69 us                                                | 3.06 us: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 442 ms: 1.20x faster                                                            |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                                           |
| logging_format             | 3.98 us                                                | 3.37 us: 1.18x faster                                                           |
| chaos                      | 42.5 ms                                                | 36.2 ms: 1.18x faster                                                           |
| nqueens                    | 62.4 ms                                                | 53.1 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                            |
| nbody                      | 68.8 ms                                                | 59.4 ms: 1.16x faster                                                           |
| float                      | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                           |
| spectral_norm              | 76.4 ms                                                | 66.5 ms: 1.15x faster                                                           |
| sqlglot_parse              | 848 us                                                 | 744 us: 1.14x faster                                                            |
| regex_compile              | 77.9 ms                                                | 68.5 ms: 1.14x faster                                                           |
| django_template            | 22.3 ms                                                | 19.8 ms: 1.13x faster                                                           |
| sqlglot_transpile          | 1.02 ms                                                | 907 us: 1.13x faster                                                            |
| scimark_lu                 | 76.0 ms                                                | 67.5 ms: 1.13x faster                                                           |
| bench_thread_pool          | 504 us                                                 | 449 us: 1.12x faster                                                            |
| hexiom                     | 4.54 ms                                                | 4.06 ms: 1.12x faster                                                           |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.80 ms: 1.12x faster                                                           |
| dulwich_log                | 29.8 ms                                                | 26.9 ms: 1.11x faster                                                           |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                          |
| sympy_sum                  | 77.6 ms                                                | 70.8 ms: 1.10x faster                                                           |
| sympy_str                  | 148 ms                                                 | 135 ms: 1.09x faster                                                            |
| async_generators           | 304 ms                                                 | 279 ms: 1.09x faster                                                            |
| sympy_integrate            | 11.4 ms                                                | 10.5 ms: 1.09x faster                                                           |
| pickle_pure_python         | 200 us                                                 | 184 us: 1.09x faster                                                            |
| sqlglot_normalize          | 186 ms                                                 | 172 ms: 1.08x faster                                                            |
| mako                       | 7.71 ms                                                | 7.16 ms: 1.08x faster                                                           |
| asyncio_tcp                | 449 ms                                                 | 418 ms: 1.07x faster                                                            |
| sqlglot_optimize           | 34.0 ms                                                | 31.8 ms: 1.07x faster                                                           |
| pycparser                  | 677 ms                                                 | 639 ms: 1.06x faster                                                            |
| regex_dna                  | 154 ms                                                 | 146 ms: 1.06x faster                                                            |
| regex_effbot               | 2.64 ms                                                | 2.50 ms: 1.06x faster                                                           |
| scimark_fft                | 195 ms                                                 | 186 ms: 1.05x faster                                                            |
| unpickle_pure_python       | 151 us                                                 | 144 us: 1.05x faster                                                            |
| pprint_safe_repr           | 497 ms                                                 | 475 ms: 1.05x faster                                                            |
| xml_etree_generate         | 55.8 ms                                                | 53.4 ms: 1.05x faster                                                           |
| go                         | 102 ms                                                 | 97.2 ms: 1.05x faster                                                           |
| pprint_pformat             | 1.01 sec                                               | 969 ms: 1.04x faster                                                            |
| sympy_expand               | 241 ms                                                 | 231 ms: 1.04x faster                                                            |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                                           |
| pathlib                    | 24.2 ms                                                | 23.3 ms: 1.04x faster                                                           |
| 2to3                       | 169 ms                                                 | 163 ms: 1.04x faster                                                            |
| xml_etree_process          | 39.7 ms                                                | 38.3 ms: 1.04x faster                                                           |
| scimark_monte_carlo        | 45.0 ms                                                | 43.5 ms: 1.04x faster                                                           |
| json                       | 3.09 ms                                                | 3.01 ms: 1.03x faster                                                           |
| richards                   | 32.1 ms                                                | 31.4 ms: 1.02x faster                                                           |
| crypto_pyaes               | 51.9 ms                                                | 51.1 ms: 1.02x faster                                                           |
| docutils                   | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                          |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                            |
| pyflate                    | 316 ms                                                 | 322 ms: 1.02x slower                                                            |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.02x slower                                                            |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 93.0 us                                                | 95.6 us: 1.03x slower                                                           |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                           |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.04x slower                                                          |
| json_dumps                 | 6.22 ms                                                | 6.52 ms: 1.05x slower                                                           |
| fannkuch                   | 248 ms                                                 | 262 ms: 1.06x slower                                                            |
| scimark_sor                | 87.4 ms                                                | 93.7 ms: 1.07x slower                                                           |
| tomli_loads                | 1.39 sec                                               | 1.50 sec: 1.07x slower                                                          |
| bench_mp_pool              | 44.9 ms                                                | 48.6 ms: 1.08x slower                                                           |
| tornado_http               | 69.3 ms                                                | 78.8 ms: 1.14x slower                                                           |
| coverage                   | 38.9 ms                                                | 44.9 ms: 1.15x slower                                                           |
| create_gc_cycles           | 701 us                                                 | 886 us: 1.26x slower                                                            |
| telco                      | 3.68 ms                                                | 4.67 ms: 1.27x slower                                                           |
| python_startup_no_site     | 9.37 ms                                                | 13.4 ms: 1.43x slower                                                           |
| python_startup             | 11.4 ms                                                | 16.4 ms: 1.44x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): pidigits, meteor_contest, xml_etree_iterparse, json_loads
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.58x