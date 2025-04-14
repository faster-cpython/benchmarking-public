# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: darwin-arm64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.037x faster
- HPT reliability: 87.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 169 ms: 1.11x faster                                   |
| chameleon      | 5.08 ms                                                | 4.70 ms: 1.08x faster                                  |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| coroutines                 | 19.8 ms                                                | 19.2 ms: 1.03x faster                                  |
| async_generators           | 295 ms                                                 | 304 ms: 1.03x slower                                   |
| async_tree_memoization_tg  | 288 ms                                                 | 323 ms: 1.12x slower                                   |
| async_tree_cpu_io_mixed    | 460 ms                                                 | 526 ms: 1.14x slower                                   |
| async_tree_memoization     | 268 ms                                                 | 312 ms: 1.16x slower                                   |
| async_tree_cpu_io_mixed_tg | 448 ms                                                 | 532 ms: 1.19x slower                                   |
| async_tree_none            | 215 ms                                                 | 266 ms: 1.23x slower                                   |
| async_tree_none_tg         | 198 ms                                                 | 258 ms: 1.30x slower                                   |
| async_tree_io              | 507 ms                                                 | 668 ms: 1.32x slower                                   |
| async_tree_io_tg           | 497 ms                                                 | 669 ms: 1.35x slower                                   |
| asyncio_websockets         | 242 ms                                                 | 409 ms: 1.69x slower                                   |
| Geometric mean             | (ref)                                                  | 1.22x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 68.8 ms: 1.08x faster                                  |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                   |
| float          | 56.0 ms                                                | 55.8 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 17.0 ms                                                | 16.0 ms: 1.06x faster                                  |
| regex_compile  | 78.6 ms                                                | 77.9 ms: 1.01x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.64 ms: 1.01x slower                                  |
| regex_dna      | 149 ms                                                 | 154 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.39 sec: 1.13x faster                                 |
| unpickle_pure_python | 164 us                                                 | 151 us: 1.09x faster                                   |
| pickle_pure_python   | 214 us                                                 | 200 us: 1.07x faster                                   |
| json_dumps           | 6.52 ms                                                | 6.22 ms: 1.05x faster                                  |
| xml_etree_process    | 41.0 ms                                                | 39.7 ms: 1.03x faster                                  |
| xml_etree_generate   | 57.0 ms                                                | 55.8 ms: 1.02x faster                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 74.0 ms: 1.01x slower                                  |
| json_loads           | 17.0 us                                                | 17.2 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 11.4 ms: 1.66x faster                                  |
| python_startup_no_site | 14.5 ms                                                | 9.37 ms: 1.54x faster                                  |
| Geometric mean         | (ref)                                                  | 1.60x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 22.2 ms                                                | 22.3 ms: 1.00x slower                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| dask                       | 790 ms                                                 | 222 ms: 3.56x faster                                   |
| mypy2                      | 701 ms                                                 | 380 ms: 1.84x faster                                   |
| create_gc_cycles           | 1.17 ms                                                | 701 us: 1.67x faster                                   |
| python_startup             | 18.9 ms                                                | 11.4 ms: 1.66x faster                                  |
| python_startup_no_site     | 14.5 ms                                                | 9.37 ms: 1.54x faster                                  |
| bench_mp_pool              | 62.5 ms                                                | 44.9 ms: 1.39x faster                                  |
| telco                      | 4.76 ms                                                | 3.68 ms: 1.29x faster                                  |
| gc_traversal               | 2.91 ms                                                | 2.40 ms: 1.21x faster                                  |
| scimark_sor                | 105 ms                                                 | 87.4 ms: 1.21x faster                                  |
| coverage                   | 46.0 ms                                                | 38.9 ms: 1.18x faster                                  |
| fannkuch                   | 284 ms                                                 | 248 ms: 1.14x faster                                   |
| go                         | 115 ms                                                 | 102 ms: 1.13x faster                                   |
| tomli_loads                | 1.57 sec                                               | 1.39 sec: 1.13x faster                                 |
| scimark_monte_carlo        | 50.4 ms                                                | 45.0 ms: 1.12x faster                                  |
| pyflate                    | 351 ms                                                 | 316 ms: 1.11x faster                                   |
| 2to3                       | 187 ms                                                 | 169 ms: 1.11x faster                                   |
| richards                   | 35.2 ms                                                | 32.1 ms: 1.10x faster                                  |
| unpickle_pure_python       | 164 us                                                 | 151 us: 1.09x faster                                   |
| typing_runtime_protocols   | 101 us                                                 | 93.0 us: 1.09x faster                                  |
| richards_super             | 39.1 ms                                                | 36.0 ms: 1.09x faster                                  |
| chameleon                  | 5.08 ms                                                | 4.70 ms: 1.08x faster                                  |
| nbody                      | 74.0 ms                                                | 68.8 ms: 1.08x faster                                  |
| pickle_pure_python         | 214 us                                                 | 200 us: 1.07x faster                                   |
| pprint_safe_repr           | 533 ms                                                 | 497 ms: 1.07x faster                                   |
| pprint_pformat             | 1.08 sec                                               | 1.01 sec: 1.07x faster                                 |
| hexiom                     | 4.86 ms                                                | 4.54 ms: 1.07x faster                                  |
| regex_v8                   | 17.0 ms                                                | 16.0 ms: 1.06x faster                                  |
| json_dumps                 | 6.52 ms                                                | 6.22 ms: 1.05x faster                                  |
| crypto_pyaes               | 54.2 ms                                                | 51.9 ms: 1.05x faster                                  |
| pycparser                  | 705 ms                                                 | 677 ms: 1.04x faster                                   |
| xml_etree_process          | 41.0 ms                                                | 39.7 ms: 1.03x faster                                  |
| meteor_contest             | 74.0 ms                                                | 71.7 ms: 1.03x faster                                  |
| scimark_fft                | 201 ms                                                 | 195 ms: 1.03x faster                                   |
| coroutines                 | 19.8 ms                                                | 19.2 ms: 1.03x faster                                  |
| sqlglot_optimize           | 34.9 ms                                                | 34.0 ms: 1.03x faster                                  |
| sympy_expand               | 246 ms                                                 | 241 ms: 1.02x faster                                   |
| xml_etree_generate         | 57.0 ms                                                | 55.8 ms: 1.02x faster                                  |
| sqlglot_normalize          | 189 ms                                                 | 186 ms: 1.02x faster                                   |
| generators                 | 31.5 ms                                                | 31.1 ms: 1.01x faster                                  |
| regex_compile              | 78.6 ms                                                | 77.9 ms: 1.01x faster                                  |
| sqlglot_parse              | 856 us                                                 | 848 us: 1.01x faster                                   |
| scimark_lu                 | 76.7 ms                                                | 76.0 ms: 1.01x faster                                  |
| deepcopy                   | 237 us                                                 | 235 us: 1.01x faster                                   |
| pidigits                   | 284 ms                                                 | 282 ms: 1.01x faster                                   |
| float                      | 56.0 ms                                                | 55.8 ms: 1.00x faster                                  |
| django_template            | 22.2 ms                                                | 22.3 ms: 1.00x slower                                  |
| regex_effbot               | 2.63 ms                                                | 2.64 ms: 1.01x slower                                  |
| sympy_integrate            | 11.3 ms                                                | 11.4 ms: 1.01x slower                                  |
| xml_etree_iterparse        | 73.6 ms                                                | 74.0 ms: 1.01x slower                                  |
| deepcopy_memo              | 27.4 us                                                | 27.7 us: 1.01x slower                                  |
| deltablue                  | 2.68 ms                                                | 2.71 ms: 1.01x slower                                  |
| sympy_str                  | 145 ms                                                 | 148 ms: 1.01x slower                                   |
| json_loads                 | 17.0 us                                                | 17.2 us: 1.02x slower                                  |
| json                       | 3.03 ms                                                | 3.09 ms: 1.02x slower                                  |
| logging_simple             | 3.60 us                                                | 3.69 us: 1.02x slower                                  |
| logging_format             | 3.89 us                                                | 3.98 us: 1.02x slower                                  |
| sympy_sum                  | 75.4 ms                                                | 77.6 ms: 1.03x slower                                  |
| async_generators           | 295 ms                                                 | 304 ms: 1.03x slower                                   |
| chaos                      | 41.2 ms                                                | 42.5 ms: 1.03x slower                                  |
| regex_dna                  | 149 ms                                                 | 154 ms: 1.04x slower                                   |
| pathlib                    | 23.4 ms                                                | 24.2 ms: 1.04x slower                                  |
| docutils                   | 1.44 sec                                               | 1.50 sec: 1.04x slower                                 |
| dulwich_log                | 28.5 ms                                                | 29.8 ms: 1.05x slower                                  |
| scimark_sparse_mat_mult    | 2.99 ms                                                | 3.14 ms: 1.05x slower                                  |
| sqlalchemy_declarative     | 58.9 ms                                                | 62.3 ms: 1.06x slower                                  |
| mdp                        | 1.49 sec                                               | 1.58 sec: 1.06x slower                                 |
| logging_silent             | 70.1 ns                                                | 76.4 ns: 1.09x slower                                  |
| async_tree_memoization_tg  | 288 ms                                                 | 323 ms: 1.12x slower                                   |
| async_tree_cpu_io_mixed    | 460 ms                                                 | 526 ms: 1.14x slower                                   |
| async_tree_memoization     | 268 ms                                                 | 312 ms: 1.16x slower                                   |
| raytrace                   | 181 ms                                                 | 212 ms: 1.17x slower                                   |
| comprehensions             | 12.3 us                                                | 14.5 us: 1.19x slower                                  |
| async_tree_cpu_io_mixed_tg | 448 ms                                                 | 532 ms: 1.19x slower                                   |
| async_tree_none            | 215 ms                                                 | 266 ms: 1.23x slower                                   |
| async_tree_none_tg         | 198 ms                                                 | 258 ms: 1.30x slower                                   |
| async_tree_io              | 507 ms                                                 | 668 ms: 1.32x slower                                   |
| async_tree_io_tg           | 497 ms                                                 | 669 ms: 1.35x slower                                   |
| asyncio_websockets         | 242 ms                                                 | 409 ms: 1.69x slower                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (9): tornado_http, xml_etree_parse, nqueens, sqlglot_transpile, bench_thread_pool, sqlalchemy_imperative, deepcopy_reduce, spectral_norm, mako
Ignored benchmarks (19) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 87.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.88x