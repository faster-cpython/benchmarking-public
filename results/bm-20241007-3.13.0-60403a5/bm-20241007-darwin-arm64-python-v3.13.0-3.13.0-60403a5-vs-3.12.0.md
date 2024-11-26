# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: darwin-arm64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.034x slower
- HPT reliability: 87.37%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 187 ms: 1.11x slower                                   |
| chameleon      | 4.70 ms                                                | 5.08 ms: 1.08x slower                                  |
| docutils       | 1.50 sec                                               | 1.44 sec: 1.04x faster                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 497 ms: 1.35x faster                                   |
| async_tree_io              | 668 ms                                                 | 507 ms: 1.32x faster                                   |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                   |
| async_tree_none            | 266 ms                                                 | 215 ms: 1.23x faster                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 448 ms: 1.19x faster                                   |
| async_tree_memoization     | 312 ms                                                 | 268 ms: 1.16x faster                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 288 ms: 1.12x faster                                   |
| Geometric mean             | (ref)                                                  | 1.22x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 55.8 ms                                                | 56.0 ms: 1.00x slower                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                   |
| nbody          | 68.8 ms                                                | 74.0 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                   |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.01x faster                                  |
| regex_compile  | 77.9 ms                                                | 78.6 ms: 1.01x slower                                  |
| regex_v8       | 16.0 ms                                                | 17.0 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_loads           | 17.2 us                                                | 17.0 us: 1.02x faster                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 73.6 ms: 1.01x faster                                  |
| xml_etree_generate   | 55.8 ms                                                | 57.0 ms: 1.02x slower                                  |
| xml_etree_process    | 39.7 ms                                                | 41.0 ms: 1.03x slower                                  |
| json_dumps           | 6.22 ms                                                | 6.52 ms: 1.05x slower                                  |
| pickle_pure_python   | 200 us                                                 | 214 us: 1.07x slower                                   |
| unpickle_pure_python | 151 us                                                 | 164 us: 1.09x slower                                   |
| tomli_loads          | 1.39 sec                                               | 1.57 sec: 1.13x slower                                 |
| Geometric mean       | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.5 ms: 1.54x slower                                  |
| python_startup         | 11.4 ms                                                | 18.9 ms: 1.66x slower                                  |
| Geometric mean         | (ref)                                                  | 1.60x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 22.3 ms                                                | 22.2 ms: 1.00x faster                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                   |
| async_tree_io_tg           | 669 ms                                                 | 497 ms: 1.35x faster                                   |
| async_tree_io              | 668 ms                                                 | 507 ms: 1.32x faster                                   |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                   |
| async_tree_none            | 266 ms                                                 | 215 ms: 1.23x faster                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 448 ms: 1.19x faster                                   |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.19x faster                                  |
| raytrace                   | 212 ms                                                 | 181 ms: 1.17x faster                                   |
| async_tree_memoization     | 312 ms                                                 | 268 ms: 1.16x faster                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 288 ms: 1.12x faster                                   |
| logging_silent             | 76.4 ns                                                | 70.1 ns: 1.09x faster                                  |
| mdp                        | 1.58 sec                                               | 1.49 sec: 1.06x faster                                 |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.9 ms: 1.06x faster                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.99 ms: 1.05x faster                                  |
| dulwich_log                | 29.8 ms                                                | 28.5 ms: 1.05x faster                                  |
| docutils                   | 1.50 sec                                               | 1.44 sec: 1.04x faster                                 |
| pathlib                    | 24.2 ms                                                | 23.4 ms: 1.04x faster                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                   |
| chaos                      | 42.5 ms                                                | 41.2 ms: 1.03x faster                                  |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                   |
| sympy_sum                  | 77.6 ms                                                | 75.4 ms: 1.03x faster                                  |
| logging_format             | 3.98 us                                                | 3.89 us: 1.02x faster                                  |
| logging_simple             | 3.69 us                                                | 3.60 us: 1.02x faster                                  |
| json                       | 3.09 ms                                                | 3.03 ms: 1.02x faster                                  |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.02x faster                                  |
| sympy_str                  | 148 ms                                                 | 145 ms: 1.01x faster                                   |
| deltablue                  | 2.71 ms                                                | 2.68 ms: 1.01x faster                                  |
| deepcopy_memo              | 27.7 us                                                | 27.4 us: 1.01x faster                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 73.6 ms: 1.01x faster                                  |
| sympy_integrate            | 11.4 ms                                                | 11.3 ms: 1.01x faster                                  |
| regex_effbot               | 2.64 ms                                                | 2.63 ms: 1.01x faster                                  |
| django_template            | 22.3 ms                                                | 22.2 ms: 1.00x faster                                  |
| float                      | 55.8 ms                                                | 56.0 ms: 1.00x slower                                  |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                   |
| deepcopy                   | 235 us                                                 | 237 us: 1.01x slower                                   |
| scimark_lu                 | 76.0 ms                                                | 76.7 ms: 1.01x slower                                  |
| sqlglot_parse              | 848 us                                                 | 856 us: 1.01x slower                                   |
| regex_compile              | 77.9 ms                                                | 78.6 ms: 1.01x slower                                  |
| generators                 | 31.1 ms                                                | 31.5 ms: 1.01x slower                                  |
| sqlglot_normalize          | 186 ms                                                 | 189 ms: 1.02x slower                                   |
| xml_etree_generate         | 55.8 ms                                                | 57.0 ms: 1.02x slower                                  |
| sympy_expand               | 241 ms                                                 | 246 ms: 1.02x slower                                   |
| sqlglot_optimize           | 34.0 ms                                                | 34.9 ms: 1.03x slower                                  |
| coroutines                 | 19.2 ms                                                | 19.8 ms: 1.03x slower                                  |
| scimark_fft                | 195 ms                                                 | 201 ms: 1.03x slower                                   |
| meteor_contest             | 71.7 ms                                                | 74.0 ms: 1.03x slower                                  |
| xml_etree_process          | 39.7 ms                                                | 41.0 ms: 1.03x slower                                  |
| pycparser                  | 677 ms                                                 | 705 ms: 1.04x slower                                   |
| crypto_pyaes               | 51.9 ms                                                | 54.2 ms: 1.05x slower                                  |
| json_dumps                 | 6.22 ms                                                | 6.52 ms: 1.05x slower                                  |
| regex_v8                   | 16.0 ms                                                | 17.0 ms: 1.06x slower                                  |
| hexiom                     | 4.54 ms                                                | 4.86 ms: 1.07x slower                                  |
| pprint_pformat             | 1.01 sec                                               | 1.08 sec: 1.07x slower                                 |
| pprint_safe_repr           | 497 ms                                                 | 533 ms: 1.07x slower                                   |
| pickle_pure_python         | 200 us                                                 | 214 us: 1.07x slower                                   |
| nbody                      | 68.8 ms                                                | 74.0 ms: 1.08x slower                                  |
| chameleon                  | 4.70 ms                                                | 5.08 ms: 1.08x slower                                  |
| richards_super             | 36.0 ms                                                | 39.1 ms: 1.09x slower                                  |
| typing_runtime_protocols   | 93.0 us                                                | 101 us: 1.09x slower                                   |
| unpickle_pure_python       | 151 us                                                 | 164 us: 1.09x slower                                   |
| richards                   | 32.1 ms                                                | 35.2 ms: 1.10x slower                                  |
| 2to3                       | 169 ms                                                 | 187 ms: 1.11x slower                                   |
| pyflate                    | 316 ms                                                 | 351 ms: 1.11x slower                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 50.4 ms: 1.12x slower                                  |
| tomli_loads                | 1.39 sec                                               | 1.57 sec: 1.13x slower                                 |
| go                         | 102 ms                                                 | 115 ms: 1.13x slower                                   |
| fannkuch                   | 248 ms                                                 | 284 ms: 1.14x slower                                   |
| coverage                   | 38.9 ms                                                | 46.0 ms: 1.18x slower                                  |
| scimark_sor                | 87.4 ms                                                | 105 ms: 1.21x slower                                   |
| gc_traversal               | 2.40 ms                                                | 2.91 ms: 1.21x slower                                  |
| telco                      | 3.68 ms                                                | 4.76 ms: 1.29x slower                                  |
| bench_mp_pool              | 44.9 ms                                                | 62.5 ms: 1.39x slower                                  |
| python_startup_no_site     | 9.37 ms                                                | 14.5 ms: 1.54x slower                                  |
| python_startup             | 11.4 ms                                                | 18.9 ms: 1.66x slower                                  |
| create_gc_cycles           | 701 us                                                 | 1.17 ms: 1.67x slower                                  |
| mypy2                      | 380 ms                                                 | 701 ms: 1.84x slower                                   |
| dask                       | 222 ms                                                 | 790 ms: 3.56x slower                                   |
| Geometric mean             | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (9): mako, spectral_norm, deepcopy_reduce, sqlalchemy_imperative, bench_thread_pool, sqlglot_transpile, nqueens, xml_etree_parse, tornado_http
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.034x slower
# HPT report

- Reliability score: 87.37% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.15x