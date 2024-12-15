# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.059x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 198 ms: 1.17x slower                                                   |
| docutils       | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| async_tree_io              | 668 ms                                                 | 376 ms: 1.78x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 154 ms: 1.67x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 193 ms: 1.67x faster                                                   |
| async_tree_none            | 266 ms                                                 | 169 ms: 1.57x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 204 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 423 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 425 ms: 1.24x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.56x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.9 ms: 1.17x faster                                                  |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.01 ms: 1.31x faster                                                  |
| regex_dna      | 154 ms                                                 | 135 ms: 1.14x faster                                                   |
| regex_compile  | 77.9 ms                                                | 69.5 ms: 1.12x faster                                                  |
| regex_v8       | 16.0 ms                                                | 15.9 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 125 us: 1.21x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.22 sec: 1.14x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 49.2 ms: 1.13x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 35.0 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 70.4 ms: 1.05x faster                                                  |
| json_loads           | 17.2 us                                                | 16.5 us: 1.04x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 103 ms: 1.03x faster                                                   |
| pickle_pure_python   | 200 us                                                 | 195 us: 1.02x faster                                                   |
| json_dumps           | 6.22 ms                                                | 7.21 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 16.6 ms: 1.77x slower                                                  |
| python_startup         | 11.4 ms                                                | 21.6 ms: 1.89x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.83x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.26 ms: 1.23x faster                                                  |
| django_template | 22.3 ms                                                | 22.7 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| async_tree_io              | 668 ms                                                 | 376 ms: 1.78x faster                                                   |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 154 ms: 1.67x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 193 ms: 1.67x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 17.2 us: 1.61x faster                                                  |
| async_tree_none            | 266 ms                                                 | 169 ms: 1.57x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 204 ms: 1.53x faster                                                   |
| deepcopy                   | 235 us                                                 | 157 us: 1.50x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.01 ms: 1.31x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.58 us: 1.31x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 423 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 425 ms: 1.24x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 62.0 ms: 1.23x faster                                                  |
| mako                       | 7.71 ms                                                | 6.26 ms: 1.23x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 125 us: 1.21x faster                                                   |
| float                      | 55.8 ms                                                | 47.9 ms: 1.17x faster                                                  |
| raytrace                   | 212 ms                                                 | 185 ms: 1.15x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.22 sec: 1.14x faster                                                 |
| regex_dna                  | 154 ms                                                 | 135 ms: 1.14x faster                                                   |
| generators                 | 31.1 ms                                                | 27.3 ms: 1.14x faster                                                  |
| scimark_fft                | 195 ms                                                 | 171 ms: 1.14x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 49.2 ms: 1.13x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 35.0 ms: 1.13x faster                                                  |
| regex_compile              | 77.9 ms                                                | 69.5 ms: 1.12x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.3 ms: 1.11x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 69.3 ms: 1.10x faster                                                  |
| json                       | 3.09 ms                                                | 2.85 ms: 1.08x faster                                                  |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.5 ms: 1.08x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.44 us: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.94 ms: 1.07x faster                                                  |
| logging_format             | 3.98 us                                                | 3.74 us: 1.06x faster                                                  |
| scimark_sor                | 87.4 ms                                                | 82.2 ms: 1.06x faster                                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.9 ms: 1.06x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.56 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 70.4 ms: 1.05x faster                                                  |
| comprehensions             | 14.5 us                                                | 13.9 us: 1.04x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.04x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 28.8 ms: 1.04x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 103 ms: 1.03x faster                                                   |
| sympy_sum                  | 77.6 ms                                                | 75.6 ms: 1.03x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 195 us: 1.02x faster                                                   |
| async_generators           | 304 ms                                                 | 300 ms: 1.01x faster                                                   |
| sympy_str                  | 148 ms                                                 | 146 ms: 1.01x faster                                                   |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                                   |
| nqueens                    | 62.4 ms                                                | 61.7 ms: 1.01x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.01x faster                                                  |
| logging_silent             | 76.4 ns                                                | 75.6 ns: 1.01x faster                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.62 ms: 1.01x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.57 sec: 1.01x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 502 us: 1.00x faster                                                   |
| chaos                      | 42.5 ms                                                | 42.4 ms: 1.00x faster                                                  |
| regex_v8                   | 16.0 ms                                                | 15.9 ms: 1.00x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 500 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.01 sec                                               | 1.02 sec: 1.01x slower                                                 |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| pyflate                    | 316 ms                                                 | 318 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 34.3 ms: 1.01x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 856 us: 1.01x slower                                                   |
| sqlglot_normalize          | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| sympy_expand               | 241 ms                                                 | 244 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.04 ms: 1.01x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 72.9 ms: 1.02x slower                                                  |
| django_template            | 22.3 ms                                                | 22.7 ms: 1.02x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.8 ms: 1.03x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 53.8 ms: 1.04x slower                                                  |
| fannkuch                   | 248 ms                                                 | 267 ms: 1.07x slower                                                   |
| richards_super             | 36.0 ms                                                | 38.8 ms: 1.08x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 100 us: 1.08x slower                                                   |
| richards                   | 32.1 ms                                                | 35.0 ms: 1.09x slower                                                  |
| hexiom                     | 4.54 ms                                                | 4.96 ms: 1.09x slower                                                  |
| coverage                   | 38.9 ms                                                | 44.1 ms: 1.14x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.21 ms: 1.16x slower                                                  |
| 2to3                       | 169 ms                                                 | 198 ms: 1.17x slower                                                   |
| telco                      | 3.68 ms                                                | 4.46 ms: 1.21x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 3.07 ms: 1.28x slower                                                  |
| mypy2                      | 380 ms                                                 | 529 ms: 1.39x slower                                                   |
| bench_mp_pool              | 44.9 ms                                                | 63.3 ms: 1.41x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 16.6 ms: 1.77x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.29 ms: 1.84x slower                                                  |
| python_startup             | 11.4 ms                                                | 21.6 ms: 1.89x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (2): pycparser, scimark_monte_carlo
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.22x