# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 169 ms: 1.00x faster                                                   |
| docutils       | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 380 ms: 1.76x faster                                                   |
| async_tree_io              | 668 ms                                                 | 381 ms: 1.75x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 194 ms: 1.66x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 157 ms: 1.64x faster                                                   |
| async_tree_none            | 266 ms                                                 | 170 ms: 1.56x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 206 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 421 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 426 ms: 1.23x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.54x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.4 ms: 1.09x faster                                                  |
| nbody          | 68.8 ms                                                | 68.4 ms: 1.01x faster                                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.03 ms: 1.30x faster                                                  |
| regex_dna      | 154 ms                                                 | 136 ms: 1.14x faster                                                   |
| regex_compile  | 77.9 ms                                                | 70.7 ms: 1.10x faster                                                  |
| regex_v8       | 16.0 ms                                                | 15.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                | 53.5 ms: 1.04x faster                                                  |
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 103 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 74.0 ms                                                | 72.7 ms: 1.02x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 39.3 ms: 1.01x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 153 us: 1.02x slower                                                   |
| pickle_pure_python   | 200 us                                                 | 208 us: 1.04x slower                                                   |
| tomli_loads          | 1.39 sec                                               | 1.46 sec: 1.05x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.35 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 16.5 ms: 1.77x slower                                                  |
| python_startup         | 11.4 ms                                                | 21.4 ms: 1.87x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.82x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.93 ms: 1.11x faster                                                  |
| django_template | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 380 ms: 1.76x faster                                                   |
| async_tree_io              | 668 ms                                                 | 381 ms: 1.75x faster                                                   |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 194 ms: 1.66x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 157 ms: 1.64x faster                                                   |
| async_tree_none            | 266 ms                                                 | 170 ms: 1.56x faster                                                   |
| deepcopy                   | 235 us                                                 | 151 us: 1.55x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 18.1 us: 1.52x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 206 ms: 1.51x faster                                                   |
| generators                 | 31.1 ms                                                | 22.8 ms: 1.36x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.03 ms: 1.30x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.61 us: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 421 ms: 1.27x faster                                                   |
| raytrace                   | 212 ms                                                 | 170 ms: 1.24x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 61.8 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 426 ms: 1.23x faster                                                   |
| go                         | 102 ms                                                 | 86.9 ms: 1.17x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.5 us: 1.16x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.72 ms: 1.15x faster                                                  |
| regex_dna                  | 154 ms                                                 | 136 ms: 1.14x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.26 us: 1.13x faster                                                  |
| scimark_fft                | 195 ms                                                 | 174 ms: 1.12x faster                                                   |
| logging_format             | 3.98 us                                                | 3.57 us: 1.12x faster                                                  |
| mako                       | 7.71 ms                                                | 6.93 ms: 1.11x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.4 ms: 1.10x faster                                                  |
| logging_silent             | 76.4 ns                                                | 69.3 ns: 1.10x faster                                                  |
| regex_compile              | 77.9 ms                                                | 70.7 ms: 1.10x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.47 ms: 1.10x faster                                                  |
| chaos                      | 42.5 ms                                                | 39.0 ms: 1.09x faster                                                  |
| float                      | 55.8 ms                                                | 51.4 ms: 1.09x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                                  |
| json                       | 3.09 ms                                                | 2.86 ms: 1.08x faster                                                  |
| async_generators           | 304 ms                                                 | 283 ms: 1.07x faster                                                   |
| nqueens                    | 62.4 ms                                                | 58.2 ms: 1.07x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 27.8 ms: 1.07x faster                                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.7 ms: 1.06x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 800 us: 1.06x faster                                                   |
| django_template            | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 971 us: 1.05x faster                                                   |
| sympy_sum                  | 77.6 ms                                                | 73.9 ms: 1.05x faster                                                  |
| sympy_str                  | 148 ms                                                 | 141 ms: 1.04x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 53.5 ms: 1.04x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 483 us: 1.04x faster                                                   |
| mdp                        | 1.58 sec                                               | 1.52 sec: 1.04x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 32.7 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 179 ms: 1.04x faster                                                   |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 103 ms: 1.03x faster                                                   |
| scimark_lu                 | 76.0 ms                                                | 73.6 ms: 1.03x faster                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.49 ms: 1.03x faster                                                  |
| pycparser                  | 677 ms                                                 | 658 ms: 1.03x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.53 us: 1.03x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 986 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 497 ms                                                 | 485 ms: 1.03x faster                                                   |
| regex_v8                   | 16.0 ms                                                | 15.7 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 72.7 ms: 1.02x faster                                                  |
| sympy_expand               | 241 ms                                                 | 237 ms: 1.02x faster                                                   |
| xml_etree_process          | 39.7 ms                                                | 39.3 ms: 1.01x faster                                                  |
| nbody                      | 68.8 ms                                                | 68.4 ms: 1.01x faster                                                  |
| 2to3                       | 169 ms                                                 | 169 ms: 1.00x faster                                                   |
| hexiom                     | 4.54 ms                                                | 4.54 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                                   |
| meteor_contest             | 71.7 ms                                                | 72.3 ms: 1.01x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.5 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 151 us                                                 | 153 us: 1.02x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 46.1 ms: 1.02x slower                                                  |
| richards_super             | 36.0 ms                                                | 36.9 ms: 1.02x slower                                                  |
| pyflate                    | 316 ms                                                 | 327 ms: 1.04x slower                                                   |
| richards                   | 32.1 ms                                                | 33.4 ms: 1.04x slower                                                  |
| pickle_pure_python         | 200 us                                                 | 208 us: 1.04x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.46 sec: 1.05x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 54.5 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 98.6 us: 1.06x slower                                                  |
| fannkuch                   | 248 ms                                                 | 266 ms: 1.07x slower                                                   |
| scimark_sor                | 87.4 ms                                                | 95.6 ms: 1.09x slower                                                  |
| coverage                   | 38.9 ms                                                | 44.2 ms: 1.14x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.35 ms: 1.18x slower                                                  |
| telco                      | 3.68 ms                                                | 4.60 ms: 1.25x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 3.07 ms: 1.28x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 63.4 ms: 1.41x slower                                                  |
| mypy2                      | 380 ms                                                 | 644 ms: 1.70x slower                                                   |
| python_startup_no_site     | 9.37 ms                                                | 16.5 ms: 1.77x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.27 ms: 1.81x slower                                                  |
| python_startup             | 11.4 ms                                                | 21.4 ms: 1.87x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                           |
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.20x