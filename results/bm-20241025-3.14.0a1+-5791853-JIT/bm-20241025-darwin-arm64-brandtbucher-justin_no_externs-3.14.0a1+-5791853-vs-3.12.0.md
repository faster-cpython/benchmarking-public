# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.025x faster
- HPT reliability: 86.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 185 ms: 1.09x slower                                                      |
| docutils       | 1.50 sec                                               | 1.57 sec: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                      |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                      |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                      |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                      |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                                      |
| async_tree_io_tg           | 669 ms                                                 | 612 ms: 1.09x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                     |
| nbody          | 68.8 ms                                                | 65.2 ms: 1.06x faster                                                     |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| regex_effbot   | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                     |
| regex_compile  | 77.9 ms                                                | 76.6 ms: 1.02x faster                                                     |
| regex_v8       | 16.0 ms                                                | 16.7 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 133 us: 1.13x faster                                                      |
| xml_etree_process    | 39.7 ms                                                | 35.2 ms: 1.13x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                | 49.7 ms: 1.12x faster                                                     |
| pickle_pure_python   | 200 us                                                 | 180 us: 1.11x faster                                                      |
| tomli_loads          | 1.39 sec                                               | 1.27 sec: 1.10x faster                                                    |
| json_loads           | 17.2 us                                                | 16.5 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 74.0 ms                                                | 72.7 ms: 1.02x faster                                                     |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.02x slower                                                      |
| json_dumps           | 6.22 ms                                                | 7.16 ms: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.3 ms: 1.52x slower                                                     |
| python_startup         | 11.4 ms                                                | 18.2 ms: 1.60x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.56x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.56 ms: 1.18x faster                                                     |
| django_template | 22.3 ms                                                | 23.2 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                      |
| deepcopy_memo              | 27.7 us                                                | 16.7 us: 1.65x faster                                                     |
| deepcopy                   | 235 us                                                 | 156 us: 1.50x faster                                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                      |
| deepcopy_reduce            | 2.07 us                                                | 1.53 us: 1.35x faster                                                     |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                      |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                      |
| generators                 | 31.1 ms                                                | 24.9 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.20x faster                                                      |
| raytrace                   | 212 ms                                                 | 177 ms: 1.20x faster                                                      |
| logging_simple             | 3.69 us                                                | 3.13 us: 1.18x faster                                                     |
| mako                       | 7.71 ms                                                | 6.56 ms: 1.18x faster                                                     |
| logging_format             | 3.98 us                                                | 3.42 us: 1.17x faster                                                     |
| scimark_lu                 | 76.0 ms                                                | 65.6 ms: 1.16x faster                                                     |
| coroutines                 | 19.2 ms                                                | 16.7 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                      |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.15x faster                                                      |
| float                      | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                                      |
| unpickle_pure_python       | 151 us                                                 | 133 us: 1.13x faster                                                      |
| xml_etree_process          | 39.7 ms                                                | 35.2 ms: 1.13x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                | 49.7 ms: 1.12x faster                                                     |
| pickle_pure_python         | 200 us                                                 | 180 us: 1.11x faster                                                      |
| deltablue                  | 2.71 ms                                                | 2.46 ms: 1.10x faster                                                     |
| tomli_loads                | 1.39 sec                                               | 1.27 sec: 1.10x faster                                                    |
| logging_silent             | 76.4 ns                                                | 69.7 ns: 1.10x faster                                                     |
| regex_dna                  | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| async_tree_io_tg           | 669 ms                                                 | 612 ms: 1.09x faster                                                      |
| spectral_norm              | 76.4 ms                                                | 70.1 ms: 1.09x faster                                                     |
| json                       | 3.09 ms                                                | 2.85 ms: 1.08x faster                                                     |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                                     |
| comprehensions             | 14.5 us                                                | 13.6 us: 1.07x faster                                                     |
| regex_effbot               | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                     |
| bench_thread_pool          | 504 us                                                 | 477 us: 1.06x faster                                                      |
| nbody                      | 68.8 ms                                                | 65.2 ms: 1.06x faster                                                     |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.04x faster                                                     |
| nqueens                    | 62.4 ms                                                | 60.1 ms: 1.04x faster                                                     |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                                      |
| dulwich_log                | 29.8 ms                                                | 29.1 ms: 1.03x faster                                                     |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 72.7 ms: 1.02x faster                                                     |
| regex_compile              | 77.9 ms                                                | 76.6 ms: 1.02x faster                                                     |
| mdp                        | 1.58 sec                                               | 1.56 sec: 1.01x faster                                                    |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                                      |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.64 ms: 1.01x faster                                                     |
| chaos                      | 42.5 ms                                                | 42.6 ms: 1.00x slower                                                     |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.17 ms: 1.01x slower                                                     |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 186 ms                                                 | 190 ms: 1.02x slower                                                      |
| pycparser                  | 677 ms                                                 | 694 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 45.0 ms                                                | 46.5 ms: 1.03x slower                                                     |
| django_template            | 22.3 ms                                                | 23.2 ms: 1.04x slower                                                     |
| sympy_str                  | 148 ms                                                 | 153 ms: 1.04x slower                                                      |
| sympy_sum                  | 77.6 ms                                                | 81.0 ms: 1.04x slower                                                     |
| regex_v8                   | 16.0 ms                                                | 16.7 ms: 1.05x slower                                                     |
| docutils                   | 1.50 sec                                               | 1.57 sec: 1.05x slower                                                    |
| meteor_contest             | 71.7 ms                                                | 75.1 ms: 1.05x slower                                                     |
| pprint_pformat             | 1.01 sec                                               | 1.06 sec: 1.05x slower                                                    |
| typing_runtime_protocols   | 93.0 us                                                | 97.5 us: 1.05x slower                                                     |
| sqlglot_parse              | 848 us                                                 | 889 us: 1.05x slower                                                      |
| pprint_safe_repr           | 497 ms                                                 | 521 ms: 1.05x slower                                                      |
| sympy_expand               | 241 ms                                                 | 253 ms: 1.05x slower                                                      |
| pyflate                    | 316 ms                                                 | 332 ms: 1.05x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                | 1.08 ms: 1.06x slower                                                     |
| crypto_pyaes               | 51.9 ms                                                | 55.2 ms: 1.06x slower                                                     |
| richards_super             | 36.0 ms                                                | 38.4 ms: 1.07x slower                                                     |
| richards                   | 32.1 ms                                                | 34.7 ms: 1.08x slower                                                     |
| 2to3                       | 169 ms                                                 | 185 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 34.0 ms                                                | 38.0 ms: 1.12x slower                                                     |
| sympy_integrate            | 11.4 ms                                                | 12.7 ms: 1.12x slower                                                     |
| coverage                   | 38.9 ms                                                | 44.0 ms: 1.13x slower                                                     |
| hexiom                     | 4.54 ms                                                | 5.15 ms: 1.13x slower                                                     |
| fannkuch                   | 248 ms                                                 | 282 ms: 1.13x slower                                                      |
| json_dumps                 | 6.22 ms                                                | 7.16 ms: 1.15x slower                                                     |
| gc_traversal               | 2.40 ms                                                | 2.96 ms: 1.23x slower                                                     |
| telco                      | 3.68 ms                                                | 4.57 ms: 1.24x slower                                                     |
| bench_mp_pool              | 44.9 ms                                                | 61.9 ms: 1.38x slower                                                     |
| python_startup_no_site     | 9.37 ms                                                | 14.3 ms: 1.52x slower                                                     |
| python_startup             | 11.4 ms                                                | 18.2 ms: 1.60x slower                                                     |
| create_gc_cycles           | 701 us                                                 | 1.34 ms: 1.91x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (3): scimark_sor, sqlalchemy_declarative, tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 86.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x