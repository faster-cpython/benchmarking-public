# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: darwin-arm64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.069x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 171 ms: 1.01x slower                                                             |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 374 ms: 1.79x faster                                                             |
| async_tree_io              | 668 ms                                                 | 376 ms: 1.78x faster                                                             |
| async_tree_memoization_tg  | 323 ms                                                 | 192 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 258 ms                                                 | 155 ms: 1.66x faster                                                             |
| async_tree_none            | 266 ms                                                 | 167 ms: 1.59x faster                                                             |
| async_tree_memoization     | 312 ms                                                 | 201 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 420 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 419 ms: 1.25x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.56x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 50.5 ms: 1.11x faster                                                            |
| nbody          | 68.8 ms                                                | 63.7 ms: 1.08x faster                                                            |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.03 ms: 1.30x faster                                                            |
| regex_dna      | 154 ms                                                 | 136 ms: 1.14x faster                                                             |
| regex_compile  | 77.9 ms                                                | 69.8 ms: 1.11x faster                                                            |
| regex_v8       | 16.0 ms                                                | 15.9 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 127 us: 1.19x faster                                                             |
| tomli_loads          | 1.39 sec                                               | 1.21 sec: 1.16x faster                                                           |
| xml_etree_generate   | 55.8 ms                                                | 49.0 ms: 1.14x faster                                                            |
| xml_etree_process    | 39.7 ms                                                | 35.1 ms: 1.13x faster                                                            |
| pickle_pure_python   | 200 us                                                 | 190 us: 1.05x faster                                                             |
| json_loads           | 17.2 us                                                | 16.5 us: 1.04x faster                                                            |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.04x faster                                                             |
| xml_etree_iterparse  | 74.0 ms                                                | 71.9 ms: 1.03x faster                                                            |
| json_dumps           | 6.22 ms                                                | 7.16 ms: 1.15x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 16.6 ms: 1.77x slower                                                            |
| python_startup         | 11.4 ms                                                | 21.6 ms: 1.89x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.83x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.26 ms: 1.23x faster                                                            |
| django_template | 22.3 ms                                                | 21.1 ms: 1.06x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 374 ms: 1.79x faster                                                             |
| async_tree_io              | 668 ms                                                 | 376 ms: 1.78x faster                                                             |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 323 ms                                                 | 192 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 258 ms                                                 | 155 ms: 1.66x faster                                                             |
| async_tree_none            | 266 ms                                                 | 167 ms: 1.59x faster                                                             |
| async_tree_memoization     | 312 ms                                                 | 201 ms: 1.55x faster                                                             |
| deepcopy                   | 235 us                                                 | 153 us: 1.53x faster                                                             |
| deepcopy_memo              | 27.7 us                                                | 18.3 us: 1.51x faster                                                            |
| generators                 | 31.1 ms                                                | 23.4 ms: 1.33x faster                                                            |
| regex_effbot               | 2.64 ms                                                | 2.03 ms: 1.30x faster                                                            |
| deepcopy_reduce            | 2.07 us                                                | 1.61 us: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 420 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 419 ms: 1.25x faster                                                             |
| mako                       | 7.71 ms                                                | 6.26 ms: 1.23x faster                                                            |
| raytrace                   | 212 ms                                                 | 173 ms: 1.22x faster                                                             |
| spectral_norm              | 76.4 ms                                                | 63.0 ms: 1.21x faster                                                            |
| unpickle_pure_python       | 151 us                                                 | 127 us: 1.19x faster                                                             |
| tomli_loads                | 1.39 sec                                               | 1.21 sec: 1.16x faster                                                           |
| xml_etree_generate         | 55.8 ms                                                | 49.0 ms: 1.14x faster                                                            |
| go                         | 102 ms                                                 | 89.3 ms: 1.14x faster                                                            |
| regex_dna                  | 154 ms                                                 | 136 ms: 1.14x faster                                                             |
| scimark_fft                | 195 ms                                                 | 172 ms: 1.14x faster                                                             |
| xml_etree_process          | 39.7 ms                                                | 35.1 ms: 1.13x faster                                                            |
| comprehensions             | 14.5 us                                                | 13.0 us: 1.12x faster                                                            |
| regex_compile              | 77.9 ms                                                | 69.8 ms: 1.11x faster                                                            |
| float                      | 55.8 ms                                                | 50.5 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.88 ms: 1.09x faster                                                            |
| logging_simple             | 3.69 us                                                | 3.39 us: 1.09x faster                                                            |
| coroutines                 | 19.2 ms                                                | 17.7 ms: 1.09x faster                                                            |
| nbody                      | 68.8 ms                                                | 63.7 ms: 1.08x faster                                                            |
| nqueens                    | 62.4 ms                                                | 57.8 ms: 1.08x faster                                                            |
| async_generators           | 304 ms                                                 | 282 ms: 1.08x faster                                                             |
| logging_format             | 3.98 us                                                | 3.70 us: 1.08x faster                                                            |
| pathlib                    | 24.2 ms                                                | 22.5 ms: 1.07x faster                                                            |
| json                       | 3.09 ms                                                | 2.89 ms: 1.07x faster                                                            |
| logging_silent             | 76.4 ns                                                | 71.9 ns: 1.06x faster                                                            |
| chaos                      | 42.5 ms                                                | 40.2 ms: 1.06x faster                                                            |
| django_template            | 22.3 ms                                                | 21.1 ms: 1.06x faster                                                            |
| deltablue                  | 2.71 ms                                                | 2.56 ms: 1.06x faster                                                            |
| sympy_sum                  | 77.6 ms                                                | 73.5 ms: 1.06x faster                                                            |
| sqlalchemy_declarative     | 62.3 ms                                                | 59.0 ms: 1.06x faster                                                            |
| pickle_pure_python         | 200 us                                                 | 190 us: 1.05x faster                                                             |
| mdp                        | 1.58 sec                                               | 1.50 sec: 1.05x faster                                                           |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.04x faster                                                            |
| xml_etree_parse            | 106 ms                                                 | 102 ms: 1.04x faster                                                             |
| sympy_str                  | 148 ms                                                 | 143 ms: 1.03x faster                                                             |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                           |
| xml_etree_iterparse        | 74.0 ms                                                | 71.9 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.01 sec                                               | 991 ms: 1.02x faster                                                             |
| pyflate                    | 316 ms                                                 | 310 ms: 1.02x faster                                                             |
| sqlglot_normalize          | 186 ms                                                 | 182 ms: 1.02x faster                                                             |
| scimark_lu                 | 76.0 ms                                                | 74.7 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 497 ms                                                 | 489 ms: 1.02x faster                                                             |
| bench_thread_pool          | 504 us                                                 | 497 us: 1.01x faster                                                             |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.01x faster                                                            |
| sqlglot_optimize           | 34.0 ms                                                | 33.6 ms: 1.01x faster                                                            |
| dulwich_log                | 29.8 ms                                                | 29.6 ms: 1.01x faster                                                            |
| scimark_monte_carlo        | 45.0 ms                                                | 44.8 ms: 1.01x faster                                                            |
| regex_v8                   | 16.0 ms                                                | 15.9 ms: 1.00x faster                                                            |
| meteor_contest             | 71.7 ms                                                | 71.7 ms: 1.00x faster                                                            |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                             |
| hexiom                     | 4.54 ms                                                | 4.58 ms: 1.01x slower                                                            |
| 2to3                       | 169 ms                                                 | 171 ms: 1.01x slower                                                             |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.79 ms: 1.02x slower                                                            |
| sqlglot_transpile          | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                            |
| sqlglot_parse              | 848 us                                                 | 867 us: 1.02x slower                                                             |
| sympy_integrate            | 11.4 ms                                                | 11.6 ms: 1.02x slower                                                            |
| richards_super             | 36.0 ms                                                | 37.3 ms: 1.04x slower                                                            |
| crypto_pyaes               | 51.9 ms                                                | 53.9 ms: 1.04x slower                                                            |
| richards                   | 32.1 ms                                                | 33.6 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 93.0 us                                                | 100 us: 1.08x slower                                                             |
| fannkuch                   | 248 ms                                                 | 270 ms: 1.09x slower                                                             |
| scimark_sor                | 87.4 ms                                                | 97.3 ms: 1.11x slower                                                            |
| coverage                   | 38.9 ms                                                | 44.2 ms: 1.14x slower                                                            |
| json_dumps                 | 6.22 ms                                                | 7.16 ms: 1.15x slower                                                            |
| telco                      | 3.68 ms                                                | 4.51 ms: 1.23x slower                                                            |
| gc_traversal               | 2.40 ms                                                | 3.07 ms: 1.28x slower                                                            |
| mypy2                      | 380 ms                                                 | 525 ms: 1.38x slower                                                             |
| bench_mp_pool              | 44.9 ms                                                | 63.7 ms: 1.42x slower                                                            |
| python_startup_no_site     | 9.37 ms                                                | 16.6 ms: 1.77x slower                                                            |
| create_gc_cycles           | 701 us                                                 | 1.26 ms: 1.80x slower                                                            |
| python_startup             | 11.4 ms                                                | 21.6 ms: 1.89x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                     |

Benchmark hidden because not significant (2): sympy_expand, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.21x