# Results vs. 3.12.0

- fork: eendebakpt
- ref: int_freelist
- machine: darwin-arm64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.048x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 168 ms: 1.01x faster                                               |
| docutils       | 1.50 sec                                               | 1.44 sec: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 236 ms: 1.36x faster                                               |
| async_tree_none            | 266 ms                                                 | 203 ms: 1.31x faster                                               |
| async_tree_none_tg         | 258 ms                                                 | 203 ms: 1.27x faster                                               |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                               |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                               |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 468 ms: 1.12x faster                                               |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 477 ms: 1.12x faster                                               |
| async_tree_io_tg           | 669 ms                                                 | 613 ms: 1.09x faster                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 52.5 ms: 1.06x faster                                              |
| nbody          | 68.8 ms                                                | 68.2 ms: 1.01x faster                                              |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.29 ms: 1.15x faster                                              |
| regex_dna      | 154 ms                                                 | 135 ms: 1.14x faster                                               |
| regex_compile  | 77.9 ms                                                | 70.6 ms: 1.10x faster                                              |
| regex_v8       | 16.0 ms                                                | 15.8 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                              |
| xml_etree_generate   | 55.8 ms                                                | 54.2 ms: 1.03x faster                                              |
| xml_etree_process    | 39.7 ms                                                | 39.5 ms: 1.00x faster                                              |
| unpickle_pure_python | 151 us                                                 | 153 us: 1.02x slower                                               |
| xml_etree_parse      | 106 ms                                                 | 110 ms: 1.03x slower                                               |
| pickle_pure_python   | 200 us                                                 | 207 us: 1.03x slower                                               |
| xml_etree_iterparse  | 74.0 ms                                                | 76.6 ms: 1.04x slower                                              |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.06x slower                                             |
| json_dumps           | 6.22 ms                                                | 7.29 ms: 1.17x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.9 ms: 1.48x slower                                              |
| python_startup         | 11.4 ms                                                | 19.4 ms: 1.70x slower                                              |
| Geometric mean         | (ref)                                                  | 1.59x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.92 ms: 1.12x faster                                              |
| django_template | 22.3 ms                                                | 20.9 ms: 1.07x faster                                              |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                               |
| deepcopy                   | 235 us                                                 | 154 us: 1.53x faster                                               |
| deepcopy_memo              | 27.7 us                                                | 18.4 us: 1.51x faster                                              |
| generators                 | 31.1 ms                                                | 22.5 ms: 1.38x faster                                              |
| async_tree_memoization_tg  | 323 ms                                                 | 236 ms: 1.36x faster                                               |
| async_tree_none            | 266 ms                                                 | 203 ms: 1.31x faster                                               |
| deepcopy_reduce            | 2.07 us                                                | 1.60 us: 1.30x faster                                              |
| async_tree_none_tg         | 258 ms                                                 | 203 ms: 1.27x faster                                               |
| raytrace                   | 212 ms                                                 | 169 ms: 1.26x faster                                               |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                               |
| spectral_norm              | 76.4 ms                                                | 62.1 ms: 1.23x faster                                              |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.67 ms: 1.17x faster                                              |
| comprehensions             | 14.5 us                                                | 12.4 us: 1.17x faster                                              |
| go                         | 102 ms                                                 | 87.3 ms: 1.16x faster                                              |
| regex_effbot               | 2.64 ms                                                | 2.29 ms: 1.15x faster                                              |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                               |
| regex_dna                  | 154 ms                                                 | 135 ms: 1.14x faster                                               |
| logging_simple             | 3.69 us                                                | 3.26 us: 1.13x faster                                              |
| logging_silent             | 76.4 ns                                                | 67.9 ns: 1.13x faster                                              |
| scimark_fft                | 195 ms                                                 | 173 ms: 1.13x faster                                               |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 468 ms: 1.12x faster                                               |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 477 ms: 1.12x faster                                               |
| mako                       | 7.71 ms                                                | 6.92 ms: 1.12x faster                                              |
| logging_format             | 3.98 us                                                | 3.58 us: 1.11x faster                                              |
| deltablue                  | 2.71 ms                                                | 2.45 ms: 1.10x faster                                              |
| regex_compile              | 77.9 ms                                                | 70.6 ms: 1.10x faster                                              |
| coroutines                 | 19.2 ms                                                | 17.4 ms: 1.10x faster                                              |
| pathlib                    | 24.2 ms                                                | 22.1 ms: 1.10x faster                                              |
| async_tree_io_tg           | 669 ms                                                 | 613 ms: 1.09x faster                                               |
| nqueens                    | 62.4 ms                                                | 57.4 ms: 1.09x faster                                              |
| async_generators           | 304 ms                                                 | 281 ms: 1.08x faster                                               |
| dulwich_log                | 29.8 ms                                                | 27.8 ms: 1.07x faster                                              |
| sympy_sum                  | 77.6 ms                                                | 72.7 ms: 1.07x faster                                              |
| json                       | 3.09 ms                                                | 2.89 ms: 1.07x faster                                              |
| sqlglot_parse              | 848 us                                                 | 794 us: 1.07x faster                                               |
| bench_thread_pool          | 504 us                                                 | 473 us: 1.07x faster                                               |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.5 ms: 1.07x faster                                              |
| django_template            | 22.3 ms                                                | 20.9 ms: 1.07x faster                                              |
| float                      | 55.8 ms                                                | 52.5 ms: 1.06x faster                                              |
| sqlglot_transpile          | 1.02 ms                                                | 966 us: 1.06x faster                                               |
| sympy_str                  | 148 ms                                                 | 140 ms: 1.05x faster                                               |
| chaos                      | 42.5 ms                                                | 40.5 ms: 1.05x faster                                              |
| mdp                        | 1.58 sec                                               | 1.51 sec: 1.05x faster                                             |
| sqlglot_normalize          | 186 ms                                                 | 177 ms: 1.05x faster                                               |
| docutils                   | 1.50 sec                                               | 1.44 sec: 1.04x faster                                             |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                              |
| pycparser                  | 677 ms                                                 | 655 ms: 1.03x faster                                               |
| sqlite_synth               | 1.57 us                                                | 1.52 us: 1.03x faster                                              |
| pprint_pformat             | 1.01 sec                                               | 980 ms: 1.03x faster                                               |
| pprint_safe_repr           | 497 ms                                                 | 482 ms: 1.03x faster                                               |
| scimark_lu                 | 76.0 ms                                                | 73.7 ms: 1.03x faster                                              |
| xml_etree_generate         | 55.8 ms                                                | 54.2 ms: 1.03x faster                                              |
| sqlglot_optimize           | 34.0 ms                                                | 33.2 ms: 1.03x faster                                              |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.52 ms: 1.03x faster                                              |
| sympy_expand               | 241 ms                                                 | 235 ms: 1.02x faster                                               |
| hexiom                     | 4.54 ms                                                | 4.47 ms: 1.02x faster                                              |
| regex_v8                   | 16.0 ms                                                | 15.8 ms: 1.01x faster                                              |
| 2to3                       | 169 ms                                                 | 168 ms: 1.01x faster                                               |
| nbody                      | 68.8 ms                                                | 68.2 ms: 1.01x faster                                              |
| xml_etree_process          | 39.7 ms                                                | 39.5 ms: 1.00x faster                                              |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                               |
| scimark_monte_carlo        | 45.0 ms                                                | 45.3 ms: 1.01x slower                                              |
| sympy_integrate            | 11.4 ms                                                | 11.5 ms: 1.01x slower                                              |
| meteor_contest             | 71.7 ms                                                | 72.7 ms: 1.01x slower                                              |
| unpickle_pure_python       | 151 us                                                 | 153 us: 1.02x slower                                               |
| xml_etree_parse            | 106 ms                                                 | 110 ms: 1.03x slower                                               |
| richards_super             | 36.0 ms                                                | 37.2 ms: 1.03x slower                                              |
| pickle_pure_python         | 200 us                                                 | 207 us: 1.03x slower                                               |
| pyflate                    | 316 ms                                                 | 326 ms: 1.03x slower                                               |
| xml_etree_iterparse        | 74.0 ms                                                | 76.6 ms: 1.04x slower                                              |
| crypto_pyaes               | 51.9 ms                                                | 54.1 ms: 1.04x slower                                              |
| richards                   | 32.1 ms                                                | 33.7 ms: 1.05x slower                                              |
| typing_runtime_protocols   | 93.0 us                                                | 97.8 us: 1.05x slower                                              |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.06x slower                                             |
| fannkuch                   | 248 ms                                                 | 268 ms: 1.08x slower                                               |
| scimark_sor                | 87.4 ms                                                | 95.4 ms: 1.09x slower                                              |
| coverage                   | 38.9 ms                                                | 44.2 ms: 1.14x slower                                              |
| json_dumps                 | 6.22 ms                                                | 7.29 ms: 1.17x slower                                              |
| gc_traversal               | 2.40 ms                                                | 2.92 ms: 1.22x slower                                              |
| telco                      | 3.68 ms                                                | 4.53 ms: 1.23x slower                                              |
| bench_mp_pool              | 44.9 ms                                                | 60.9 ms: 1.36x slower                                              |
| python_startup_no_site     | 9.37 ms                                                | 13.9 ms: 1.48x slower                                              |
| python_startup             | 11.4 ms                                                | 19.4 ms: 1.70x slower                                              |
| create_gc_cycles           | 701 us                                                 | 1.30 ms: 1.86x slower                                              |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                       |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.18x