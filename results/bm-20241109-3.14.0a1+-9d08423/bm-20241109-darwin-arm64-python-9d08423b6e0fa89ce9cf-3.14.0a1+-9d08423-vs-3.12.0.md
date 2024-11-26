# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.038x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                                   |
| async_tree_none            | 266 ms                                                 | 206 ms: 1.29x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 254 ms: 1.23x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 221 ms: 1.17x faster                                                   |
| async_tree_io              | 668 ms                                                 | 590 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 469 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 480 ms: 1.11x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 629 ms: 1.06x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                  |
| nbody          | 68.8 ms                                                | 68.1 ms: 1.01x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.32 ms: 1.14x faster                                                  |
| regex_dna      | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| regex_compile  | 77.9 ms                                                | 71.9 ms: 1.08x faster                                                  |
| regex_v8       | 16.0 ms                                                | 15.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 54.5 ms: 1.03x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 39.5 ms: 1.00x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 154 us: 1.02x slower                                                   |
| pickle_pure_python   | 200 us                                                 | 208 us: 1.04x slower                                                   |
| tomli_loads          | 1.39 sec                                               | 1.54 sec: 1.10x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.22 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.4 ms: 1.43x slower                                                  |
| python_startup         | 11.4 ms                                                | 18.0 ms: 1.57x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 7.13 ms: 1.08x faster                                                  |
| django_template | 22.3 ms                                                | 21.1 ms: 1.06x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy                   | 235 us                                                 | 153 us: 1.53x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 18.3 us: 1.51x faster                                                  |
| generators                 | 31.1 ms                                                | 22.5 ms: 1.38x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.59 us: 1.30x faster                                                  |
| async_tree_none            | 266 ms                                                 | 206 ms: 1.29x faster                                                   |
| raytrace                   | 212 ms                                                 | 170 ms: 1.25x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 254 ms: 1.23x faster                                                   |
| comprehensions             | 14.5 us                                                | 12.4 us: 1.17x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 221 ms: 1.17x faster                                                   |
| go                         | 102 ms                                                 | 87.3 ms: 1.16x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.32 ms: 1.14x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.25 us: 1.13x faster                                                  |
| async_tree_io              | 668 ms                                                 | 590 ms: 1.13x faster                                                   |
| regex_dna                  | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 469 ms: 1.12x faster                                                   |
| logging_silent             | 76.4 ns                                                | 68.5 ns: 1.12x faster                                                  |
| logging_format             | 3.98 us                                                | 3.57 us: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 480 ms: 1.11x faster                                                   |
| pathlib                    | 24.2 ms                                                | 21.9 ms: 1.11x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.5 ms: 1.10x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.47 ms: 1.09x faster                                                  |
| chaos                      | 42.5 ms                                                | 39.1 ms: 1.09x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 465 us: 1.08x faster                                                   |
| regex_compile              | 77.9 ms                                                | 71.9 ms: 1.08x faster                                                  |
| mako                       | 7.71 ms                                                | 7.13 ms: 1.08x faster                                                  |
| nqueens                    | 62.4 ms                                                | 57.9 ms: 1.08x faster                                                  |
| async_generators           | 304 ms                                                 | 283 ms: 1.07x faster                                                   |
| sympy_sum                  | 77.6 ms                                                | 73.0 ms: 1.06x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 629 ms: 1.06x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 71.9 ms: 1.06x faster                                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.7 ms: 1.06x faster                                                  |
| django_template            | 22.3 ms                                                | 21.1 ms: 1.06x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 28.3 ms: 1.06x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 803 us: 1.06x faster                                                   |
| sympy_str                  | 148 ms                                                 | 140 ms: 1.05x faster                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.98 ms: 1.05x faster                                                  |
| float                      | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 975 us: 1.05x faster                                                   |
| mdp                        | 1.58 sec                                               | 1.51 sec: 1.05x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 178 ms: 1.05x faster                                                   |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.52 us: 1.03x faster                                                  |
| pycparser                  | 677 ms                                                 | 656 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 33.0 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 981 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 497 ms                                                 | 482 ms: 1.03x faster                                                   |
| scimark_lu                 | 76.0 ms                                                | 73.9 ms: 1.03x faster                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.50 ms: 1.03x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 54.5 ms: 1.03x faster                                                  |
| sympy_expand               | 241 ms                                                 | 236 ms: 1.02x faster                                                   |
| hexiom                     | 4.54 ms                                                | 4.47 ms: 1.02x faster                                                  |
| nbody                      | 68.8 ms                                                | 68.1 ms: 1.01x faster                                                  |
| scimark_fft                | 195 ms                                                 | 193 ms: 1.01x faster                                                   |
| regex_v8                   | 16.0 ms                                                | 15.8 ms: 1.01x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 39.5 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| sympy_integrate            | 11.4 ms                                                | 11.5 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 72.8 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 151 us                                                 | 154 us: 1.02x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 46.1 ms: 1.02x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 53.6 ms: 1.03x slower                                                  |
| richards_super             | 36.0 ms                                                | 37.4 ms: 1.04x slower                                                  |
| pickle_pure_python         | 200 us                                                 | 208 us: 1.04x slower                                                   |
| typing_runtime_protocols   | 93.0 us                                                | 97.6 us: 1.05x slower                                                  |
| richards                   | 32.1 ms                                                | 33.8 ms: 1.05x slower                                                  |
| fannkuch                   | 248 ms                                                 | 265 ms: 1.07x slower                                                   |
| pyflate                    | 316 ms                                                 | 338 ms: 1.07x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.54 sec: 1.10x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.4 ms: 1.14x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 99.8 ms: 1.14x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.22 ms: 1.16x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.92 ms: 1.22x slower                                                  |
| telco                      | 3.68 ms                                                | 4.57 ms: 1.24x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 60.7 ms: 1.35x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.4 ms: 1.43x slower                                                  |
| python_startup             | 11.4 ms                                                | 18.0 ms: 1.57x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.30 ms: 1.86x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, 2to3
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (18) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.038x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.18x