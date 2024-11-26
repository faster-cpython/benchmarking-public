# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.229x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 244 ms: 1.44x slower                                                   |
| docutils       | 1.50 sec                                               | 1.69 sec: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 500 ms: 1.34x faster                                                   |
| async_tree_io              | 668 ms                                                 | 520 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 205 ms: 1.25x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 262 ms: 1.23x faster                                                   |
| async_tree_none            | 266 ms                                                 | 228 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 464 ms: 1.15x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 284 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 487 ms: 1.08x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| float          | 55.8 ms                                                | 90.9 ms: 1.63x slower                                                  |
| nbody          | 68.8 ms                                                | 134 ms: 1.94x slower                                                   |
| Geometric mean | (ref)                                                  | 1.47x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 138 ms: 1.11x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.42 ms: 1.09x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                  |
| regex_compile  | 77.9 ms                                                | 116 ms: 1.49x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 98.6 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                  |
| json_loads           | 17.2 us                                                | 17.8 us: 1.03x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                | 64.7 ms: 1.16x slower                                                  |
| xml_etree_process    | 39.7 ms                                                | 52.9 ms: 1.33x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.88 sec: 1.35x slower                                                 |
| json_dumps           | 6.22 ms                                                | 8.58 ms: 1.38x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 256 us: 1.70x slower                                                   |
| pickle_pure_python   | 200 us                                                 | 347 us: 1.74x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 16.0 ms: 1.71x slower                                                  |
| python_startup         | 11.4 ms                                                | 20.6 ms: 1.80x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.76x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 34.8 ms: 1.56x slower                                                  |
| mako            | 7.71 ms                                                | 13.4 ms: 1.74x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.65x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 238 ms: 1.72x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 500 ms: 1.34x faster                                                   |
| async_tree_io              | 668 ms                                                 | 520 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 205 ms: 1.25x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 262 ms: 1.23x faster                                                   |
| async_tree_none            | 266 ms                                                 | 228 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 464 ms: 1.15x faster                                                   |
| regex_dna                  | 154 ms                                                 | 138 ms: 1.11x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 284 ms: 1.10x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.42 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 487 ms: 1.08x faster                                                   |
| xml_etree_parse            | 106 ms                                                 | 98.6 ms: 1.08x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.46 us: 1.07x faster                                                  |
| deepcopy                   | 235 us                                                 | 230 us: 1.02x faster                                                   |
| generators                 | 31.1 ms                                                | 30.6 ms: 1.02x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| xml_etree_iterparse        | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                  |
| json                       | 3.09 ms                                                | 3.16 ms: 1.02x slower                                                  |
| json_loads                 | 17.2 us                                                | 17.8 us: 1.03x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                  |
| async_generators           | 304 ms                                                 | 316 ms: 1.04x slower                                                   |
| gc_traversal               | 2.40 ms                                                | 2.51 ms: 1.04x slower                                                  |
| deepcopy_memo              | 27.7 us                                                | 29.0 us: 1.05x slower                                                  |
| coroutines                 | 19.2 ms                                                | 20.8 ms: 1.08x slower                                                  |
| deepcopy_reduce            | 2.07 us                                                | 2.32 us: 1.12x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.69 sec: 1.12x slower                                                 |
| nqueens                    | 62.4 ms                                                | 70.4 ms: 1.13x slower                                                  |
| mdp                        | 1.58 sec                                               | 1.80 sec: 1.14x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 64.7 ms: 1.16x slower                                                  |
| scimark_fft                | 195 ms                                                 | 233 ms: 1.19x slower                                                   |
| meteor_contest             | 71.7 ms                                                | 87.9 ms: 1.22x slower                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.99 ms: 1.27x slower                                                  |
| comprehensions             | 14.5 us                                                | 19.2 us: 1.32x slower                                                  |
| dulwich_log                | 29.8 ms                                                | 39.6 ms: 1.33x slower                                                  |
| xml_etree_process          | 39.7 ms                                                | 52.9 ms: 1.33x slower                                                  |
| spectral_norm              | 76.4 ms                                                | 102 ms: 1.33x slower                                                   |
| pycparser                  | 677 ms                                                 | 909 ms: 1.34x slower                                                   |
| fannkuch                   | 248 ms                                                 | 334 ms: 1.35x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.88 sec: 1.35x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 8.58 ms: 1.38x slower                                                  |
| coverage                   | 38.9 ms                                                | 54.1 ms: 1.39x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 15.8 ms: 1.39x slower                                                  |
| sqlglot_normalize          | 186 ms                                                 | 262 ms: 1.41x slower                                                   |
| sqlalchemy_declarative     | 62.3 ms                                                | 89.8 ms: 1.44x slower                                                  |
| telco                      | 3.68 ms                                                | 5.30 ms: 1.44x slower                                                  |
| 2to3                       | 169 ms                                                 | 244 ms: 1.44x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 49.7 ms: 1.46x slower                                                  |
| pyflate                    | 316 ms                                                 | 464 ms: 1.47x slower                                                   |
| regex_compile              | 77.9 ms                                                | 116 ms: 1.49x slower                                                   |
| sqlalchemy_imperative      | 6.68 ms                                                | 9.97 ms: 1.49x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 77.6 ms: 1.50x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 140 us: 1.51x slower                                                   |
| create_gc_cycles           | 701 us                                                 | 1.08 ms: 1.53x slower                                                  |
| sympy_str                  | 148 ms                                                 | 226 ms: 1.53x slower                                                   |
| django_template            | 22.3 ms                                                | 34.8 ms: 1.56x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 784 ms: 1.58x slower                                                   |
| pprint_pformat             | 1.01 sec                                               | 1.60 sec: 1.58x slower                                                 |
| logging_simple             | 3.69 us                                                | 5.89 us: 1.60x slower                                                  |
| raytrace                   | 212 ms                                                 | 340 ms: 1.61x slower                                                   |
| bench_thread_pool          | 504 us                                                 | 811 us: 1.61x slower                                                   |
| logging_format             | 3.98 us                                                | 6.44 us: 1.62x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 72.9 ms: 1.63x slower                                                  |
| float                      | 55.8 ms                                                | 90.9 ms: 1.63x slower                                                  |
| chaos                      | 42.5 ms                                                | 69.6 ms: 1.64x slower                                                  |
| richards                   | 32.1 ms                                                | 53.3 ms: 1.66x slower                                                  |
| hexiom                     | 4.54 ms                                                | 7.55 ms: 1.66x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 76.3 ms: 1.69x slower                                                  |
| logging_silent             | 76.4 ns                                                | 130 ns: 1.70x slower                                                   |
| unpickle_pure_python       | 151 us                                                 | 256 us: 1.70x slower                                                   |
| python_startup_no_site     | 9.37 ms                                                | 16.0 ms: 1.71x slower                                                  |
| richards_super             | 36.0 ms                                                | 62.2 ms: 1.73x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 151 ms: 1.73x slower                                                   |
| sympy_expand               | 241 ms                                                 | 417 ms: 1.73x slower                                                   |
| pickle_pure_python         | 200 us                                                 | 347 us: 1.74x slower                                                   |
| mako                       | 7.71 ms                                                | 13.4 ms: 1.74x slower                                                  |
| go                         | 102 ms                                                 | 177 ms: 1.74x slower                                                   |
| sympy_sum                  | 77.6 ms                                                | 137 ms: 1.76x slower                                                   |
| python_startup             | 11.4 ms                                                | 20.6 ms: 1.80x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.84 ms: 1.80x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 141 ms: 1.86x slower                                                   |
| sqlglot_parse              | 848 us                                                 | 1.61 ms: 1.90x slower                                                  |
| nbody                      | 68.8 ms                                                | 134 ms: 1.94x slower                                                   |
| deltablue                  | 2.71 ms                                                | 5.45 ms: 2.01x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.31x slower                                                           |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (18) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.229x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: 1.34x