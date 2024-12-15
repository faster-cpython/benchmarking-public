# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.132x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 214 ms: 1.26x slower                                                   |
| Geometric mean | (ref)                                                  | 1.12x slower                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 429 ms: 1.56x faster                                                   |
| async_tree_io              | 668 ms                                                 | 449 ms: 1.49x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 189 ms: 1.36x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 237 ms: 1.36x faster                                                   |
| async_tree_none            | 266 ms                                                 | 206 ms: 1.29x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 255 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 441 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| nbody          | 68.8 ms                                                | 86.2 ms: 1.25x slower                                                  |
| float          | 55.8 ms                                                | 82.9 ms: 1.49x slower                                                  |
| Geometric mean | (ref)                                                  | 1.23x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.03 ms: 1.30x faster                                                  |
| regex_dna      | 154 ms                                                 | 134 ms: 1.15x faster                                                   |
| regex_v8       | 16.0 ms                                                | 15.5 ms: 1.03x faster                                                  |
| regex_compile  | 77.9 ms                                                | 89.4 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.0 ms                                                | 66.4 ms: 1.11x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 103 ms: 1.03x faster                                                   |
| json_loads           | 17.2 us                                                | 17.4 us: 1.01x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                | 57.4 ms: 1.03x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.58 sec: 1.13x slower                                                 |
| xml_etree_process    | 39.7 ms                                                | 45.8 ms: 1.15x slower                                                  |
| json_dumps           | 6.22 ms                                                | 8.26 ms: 1.33x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 209 us: 1.39x slower                                                   |
| pickle_pure_python   | 200 us                                                 | 296 us: 1.48x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 18.1 ms: 1.94x slower                                                  |
| python_startup         | 11.4 ms                                                | 22.8 ms: 2.00x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.97x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 27.0 ms: 1.21x slower                                                  |
| mako            | 7.71 ms                                                | 11.1 ms: 1.44x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.32x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 238 ms: 1.72x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 429 ms: 1.56x faster                                                   |
| async_tree_io              | 668 ms                                                 | 449 ms: 1.49x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 189 ms: 1.36x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 237 ms: 1.36x faster                                                   |
| deepcopy                   | 235 us                                                 | 178 us: 1.32x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.03 ms: 1.30x faster                                                  |
| async_tree_none            | 266 ms                                                 | 206 ms: 1.29x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 255 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 441 ms: 1.21x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 23.7 us: 1.17x faster                                                  |
| regex_dna                  | 154 ms                                                 | 134 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.38 us: 1.14x faster                                                  |
| generators                 | 31.1 ms                                                | 27.4 ms: 1.13x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 66.4 ms: 1.11x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.88 us: 1.10x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.5 ms: 1.10x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.8 ms: 1.06x faster                                                  |
| nqueens                    | 62.4 ms                                                | 59.2 ms: 1.06x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 103 ms: 1.03x faster                                                   |
| json                       | 3.09 ms                                                | 3.00 ms: 1.03x faster                                                  |
| regex_v8                   | 16.0 ms                                                | 15.5 ms: 1.03x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 74.6 ms: 1.02x faster                                                  |
| async_generators           | 304 ms                                                 | 300 ms: 1.01x faster                                                   |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| json_loads                 | 17.2 us                                                | 17.4 us: 1.01x slower                                                  |
| mdp                        | 1.58 sec                                               | 1.62 sec: 1.02x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 57.4 ms: 1.03x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.63 ms: 1.10x slower                                                  |
| sqlglot_normalize          | 186 ms                                                 | 204 ms: 1.10x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 37.4 ms: 1.10x slower                                                  |
| scimark_fft                | 195 ms                                                 | 217 ms: 1.11x slower                                                   |
| meteor_contest             | 71.7 ms                                                | 80.9 ms: 1.13x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.58 sec: 1.13x slower                                                 |
| regex_compile              | 77.9 ms                                                | 89.4 ms: 1.15x slower                                                  |
| xml_etree_process          | 39.7 ms                                                | 45.8 ms: 1.15x slower                                                  |
| pycparser                  | 677 ms                                                 | 786 ms: 1.16x slower                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.64 ms: 1.16x slower                                                  |
| comprehensions             | 14.5 us                                                | 17.1 us: 1.17x slower                                                  |
| fannkuch                   | 248 ms                                                 | 294 ms: 1.18x slower                                                   |
| dulwich_log                | 29.8 ms                                                | 35.3 ms: 1.18x slower                                                  |
| django_template            | 22.3 ms                                                | 27.0 ms: 1.21x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 63.1 ms: 1.22x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 14.1 ms: 1.24x slower                                                  |
| nbody                      | 68.8 ms                                                | 86.2 ms: 1.25x slower                                                  |
| 2to3                       | 169 ms                                                 | 214 ms: 1.26x slower                                                   |
| logging_simple             | 3.69 us                                                | 4.70 us: 1.28x slower                                                  |
| logging_format             | 3.98 us                                                | 5.10 us: 1.28x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 120 us: 1.29x slower                                                   |
| sqlalchemy_declarative     | 62.3 ms                                                | 80.9 ms: 1.30x slower                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 8.73 ms: 1.31x slower                                                  |
| pyflate                    | 316 ms                                                 | 413 ms: 1.31x slower                                                   |
| pprint_safe_repr           | 497 ms                                                 | 655 ms: 1.32x slower                                                   |
| pprint_pformat             | 1.01 sec                                               | 1.34 sec: 1.32x slower                                                 |
| sympy_str                  | 148 ms                                                 | 196 ms: 1.32x slower                                                   |
| json_dumps                 | 6.22 ms                                                | 8.26 ms: 1.33x slower                                                  |
| coverage                   | 38.9 ms                                                | 51.7 ms: 1.33x slower                                                  |
| hexiom                     | 4.54 ms                                                | 6.10 ms: 1.34x slower                                                  |
| telco                      | 3.68 ms                                                | 5.07 ms: 1.38x slower                                                  |
| unpickle_pure_python       | 151 us                                                 | 209 us: 1.39x slower                                                   |
| chaos                      | 42.5 ms                                                | 59.2 ms: 1.39x slower                                                  |
| raytrace                   | 212 ms                                                 | 297 ms: 1.40x slower                                                   |
| mako                       | 7.71 ms                                                | 11.1 ms: 1.44x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 129 ms: 1.47x slower                                                   |
| scimark_lu                 | 76.0 ms                                                | 112 ms: 1.47x slower                                                   |
| pickle_pure_python         | 200 us                                                 | 296 us: 1.48x slower                                                   |
| float                      | 55.8 ms                                                | 82.9 ms: 1.49x slower                                                  |
| richards_super             | 36.0 ms                                                | 53.8 ms: 1.49x slower                                                  |
| richards                   | 32.1 ms                                                | 48.6 ms: 1.51x slower                                                  |
| go                         | 102 ms                                                 | 154 ms: 1.52x slower                                                   |
| logging_silent             | 76.4 ns                                                | 117 ns: 1.53x slower                                                   |
| sympy_expand               | 241 ms                                                 | 372 ms: 1.54x slower                                                   |
| sympy_sum                  | 77.6 ms                                                | 121 ms: 1.55x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 70.2 ms: 1.56x slower                                                  |
| bench_thread_pool          | 504 us                                                 | 802 us: 1.59x slower                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.63 ms: 1.59x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.14 ms: 1.63x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 74.0 ms: 1.65x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 1.44 ms: 1.70x slower                                                  |
| mypy2                      | 380 ms                                                 | 661 ms: 1.74x slower                                                   |
| deltablue                  | 2.71 ms                                                | 4.89 ms: 1.81x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 18.1 ms: 1.94x slower                                                  |
| python_startup             | 11.4 ms                                                | 22.8 ms: 2.00x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.16x slower                                                           |

Benchmark hidden because not significant (1): docutils
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.132x slower

# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.35x