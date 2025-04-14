# Results vs. 3.12.0

- fork: python
- ref: v3.13.1
- machine: darwin-arm64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.029x slower
- HPT reliability: 86.27%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 181 ms: 1.07x slower                                   |
| chameleon      | 4.70 ms                                                | 5.06 ms: 1.08x slower                                  |
| docutils       | 1.50 sec                                               | 1.43 sec: 1.05x faster                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io              | 668 ms                                                 | 514 ms: 1.30x faster                                   |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.29x faster                                   |
| async_tree_io_tg           | 669 ms                                                 | 520 ms: 1.29x faster                                   |
| async_tree_none            | 266 ms                                                 | 213 ms: 1.25x faster                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 278 ms: 1.16x faster                                   |
| async_tree_memoization     | 312 ms                                                 | 271 ms: 1.15x faster                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 481 ms: 1.11x faster                                   |
| Geometric mean             | (ref)                                                  | 1.21x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 55.8 ms                                                | 56.0 ms: 1.00x slower                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                   |
| nbody          | 68.8 ms                                                | 73.3 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.25 ms: 1.17x faster                                  |
| regex_dna      | 154 ms                                                 | 141 ms: 1.09x faster                                   |
| regex_compile  | 77.9 ms                                                | 80.8 ms: 1.04x slower                                  |
| regex_v8       | 16.0 ms                                                | 16.9 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_loads           | 17.2 us                                                | 17.0 us: 1.01x faster                                  |
| xml_etree_generate   | 55.8 ms                                                | 56.7 ms: 1.02x slower                                  |
| xml_etree_process    | 39.7 ms                                                | 41.0 ms: 1.03x slower                                  |
| json_dumps           | 6.22 ms                                                | 6.55 ms: 1.05x slower                                  |
| unpickle_pure_python | 151 us                                                 | 165 us: 1.10x slower                                   |
| pickle_pure_python   | 200 us                                                 | 221 us: 1.11x slower                                   |
| tomli_loads          | 1.39 sec                                               | 1.57 sec: 1.13x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.6 ms: 1.67x slower                                  |
| python_startup         | 11.4 ms                                                | 20.5 ms: 1.80x slower                                  |
| Geometric mean         | (ref)                                                  | 1.73x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 22.3 ms                                                | 21.0 ms: 1.07x faster                                  |
| mako            | 7.71 ms                                                | 7.67 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                   |
| async_tree_io              | 668 ms                                                 | 514 ms: 1.30x faster                                   |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.29x faster                                   |
| async_tree_io_tg           | 669 ms                                                 | 520 ms: 1.29x faster                                   |
| async_tree_none            | 266 ms                                                 | 213 ms: 1.25x faster                                   |
| comprehensions             | 14.5 us                                                | 12.4 us: 1.18x faster                                  |
| regex_effbot               | 2.64 ms                                                | 2.25 ms: 1.17x faster                                  |
| raytrace                   | 212 ms                                                 | 182 ms: 1.17x faster                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 278 ms: 1.16x faster                                   |
| async_tree_memoization     | 312 ms                                                 | 271 ms: 1.15x faster                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 481 ms: 1.11x faster                                   |
| regex_dna                  | 154 ms                                                 | 141 ms: 1.09x faster                                   |
| logging_silent             | 76.4 ns                                                | 70.5 ns: 1.08x faster                                  |
| django_template            | 22.3 ms                                                | 21.0 ms: 1.07x faster                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 59.0 ms: 1.06x faster                                  |
| docutils                   | 1.50 sec                                               | 1.43 sec: 1.05x faster                                 |
| dulwich_log                | 29.8 ms                                                | 28.5 ms: 1.05x faster                                  |
| mdp                        | 1.58 sec                                               | 1.51 sec: 1.05x faster                                 |
| async_generators           | 304 ms                                                 | 292 ms: 1.04x faster                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.01 ms: 1.04x faster                                  |
| logging_simple             | 3.69 us                                                | 3.56 us: 1.04x faster                                  |
| pathlib                    | 24.2 ms                                                | 23.4 ms: 1.03x faster                                  |
| logging_format             | 3.98 us                                                | 3.86 us: 1.03x faster                                  |
| sympy_sum                  | 77.6 ms                                                | 75.9 ms: 1.02x faster                                  |
| chaos                      | 42.5 ms                                                | 41.7 ms: 1.02x faster                                  |
| deltablue                  | 2.71 ms                                                | 2.66 ms: 1.02x faster                                  |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.01x faster                                  |
| sympy_str                  | 148 ms                                                 | 146 ms: 1.01x faster                                   |
| sqlite_synth               | 1.57 us                                                | 1.56 us: 1.01x faster                                  |
| deepcopy_memo              | 27.7 us                                                | 27.5 us: 1.01x faster                                  |
| json                       | 3.09 ms                                                | 3.06 ms: 1.01x faster                                  |
| mako                       | 7.71 ms                                                | 7.67 ms: 1.01x faster                                  |
| deepcopy                   | 235 us                                                 | 234 us: 1.01x faster                                   |
| float                      | 55.8 ms                                                | 56.0 ms: 1.00x slower                                  |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.03 ms: 1.01x slower                                  |
| bench_thread_pool          | 504 us                                                 | 508 us: 1.01x slower                                   |
| sqlglot_parse              | 848 us                                                 | 855 us: 1.01x slower                                   |
| generators                 | 31.1 ms                                                | 31.4 ms: 1.01x slower                                  |
| nqueens                    | 62.4 ms                                                | 63.2 ms: 1.01x slower                                  |
| xml_etree_generate         | 55.8 ms                                                | 56.7 ms: 1.02x slower                                  |
| scimark_fft                | 195 ms                                                 | 200 ms: 1.02x slower                                   |
| sqlglot_normalize          | 186 ms                                                 | 190 ms: 1.03x slower                                   |
| sympy_expand               | 241 ms                                                 | 249 ms: 1.03x slower                                   |
| sqlglot_optimize           | 34.0 ms                                                | 35.2 ms: 1.03x slower                                  |
| xml_etree_process          | 39.7 ms                                                | 41.0 ms: 1.03x slower                                  |
| coroutines                 | 19.2 ms                                                | 19.9 ms: 1.04x slower                                  |
| pycparser                  | 677 ms                                                 | 701 ms: 1.04x slower                                   |
| regex_compile              | 77.9 ms                                                | 80.8 ms: 1.04x slower                                  |
| meteor_contest             | 71.7 ms                                                | 74.5 ms: 1.04x slower                                  |
| spectral_norm              | 76.4 ms                                                | 79.9 ms: 1.05x slower                                  |
| json_dumps                 | 6.22 ms                                                | 6.55 ms: 1.05x slower                                  |
| crypto_pyaes               | 51.9 ms                                                | 54.6 ms: 1.05x slower                                  |
| regex_v8                   | 16.0 ms                                                | 16.9 ms: 1.06x slower                                  |
| nbody                      | 68.8 ms                                                | 73.3 ms: 1.06x slower                                  |
| 2to3                       | 169 ms                                                 | 181 ms: 1.07x slower                                   |
| pprint_safe_repr           | 497 ms                                                 | 535 ms: 1.08x slower                                   |
| pprint_pformat             | 1.01 sec                                               | 1.09 sec: 1.08x slower                                 |
| chameleon                  | 4.70 ms                                                | 5.06 ms: 1.08x slower                                  |
| typing_runtime_protocols   | 93.0 us                                                | 100 us: 1.08x slower                                   |
| hexiom                     | 4.54 ms                                                | 4.92 ms: 1.08x slower                                  |
| unpickle_pure_python       | 151 us                                                 | 165 us: 1.10x slower                                   |
| richards                   | 32.1 ms                                                | 35.3 ms: 1.10x slower                                  |
| richards_super             | 36.0 ms                                                | 39.7 ms: 1.10x slower                                  |
| pickle_pure_python         | 200 us                                                 | 221 us: 1.11x slower                                   |
| pyflate                    | 316 ms                                                 | 351 ms: 1.11x slower                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 50.2 ms: 1.11x slower                                  |
| tomli_loads                | 1.39 sec                                               | 1.57 sec: 1.13x slower                                 |
| fannkuch                   | 248 ms                                                 | 280 ms: 1.13x slower                                   |
| go                         | 102 ms                                                 | 115 ms: 1.13x slower                                   |
| coverage                   | 38.9 ms                                                | 45.8 ms: 1.18x slower                                  |
| scimark_sor                | 87.4 ms                                                | 106 ms: 1.21x slower                                   |
| gc_traversal               | 2.40 ms                                                | 2.92 ms: 1.22x slower                                  |
| telco                      | 3.68 ms                                                | 4.77 ms: 1.30x slower                                  |
| bench_mp_pool              | 44.9 ms                                                | 64.7 ms: 1.44x slower                                  |
| python_startup_no_site     | 9.37 ms                                                | 15.6 ms: 1.67x slower                                  |
| create_gc_cycles           | 701 us                                                 | 1.18 ms: 1.68x slower                                  |
| python_startup             | 11.4 ms                                                | 20.5 ms: 1.80x slower                                  |
| dask                       | 222 ms                                                 | 771 ms: 3.47x slower                                   |
| Geometric mean             | (ref)                                                  | 1.03x slower                                           |

Benchmark hidden because not significant (8): deepcopy_reduce, xml_etree_iterparse, scimark_lu, sympy_integrate, sqlalchemy_imperative, xml_etree_parse, tornado_http, gunicorn
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20241203-3.13.1-0671451/bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, flaskblogging, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 86.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.16x