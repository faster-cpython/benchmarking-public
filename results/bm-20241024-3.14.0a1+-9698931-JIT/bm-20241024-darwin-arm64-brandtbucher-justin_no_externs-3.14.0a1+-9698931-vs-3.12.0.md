# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.006x faster
- HPT reliability: 57.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 191 ms: 1.13x slower                                                      |
| docutils       | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.37x faster                                                      |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                      |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                      |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                      |
| async_tree_io              | 668 ms                                                 | 586 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                                      |
| async_tree_io_tg           | 669 ms                                                 | 614 ms: 1.09x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.8 ms: 1.12x faster                                                     |
| nbody          | 68.8 ms                                                | 66.1 ms: 1.04x faster                                                     |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 142 ms: 1.09x faster                                                      |
| regex_effbot   | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                     |
| regex_compile  | 77.9 ms                                                | 79.4 ms: 1.02x slower                                                     |
| regex_v8       | 16.0 ms                                                | 16.7 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 35.7 ms: 1.11x faster                                                     |
| pickle_pure_python   | 200 us                                                 | 181 us: 1.10x faster                                                      |
| unpickle_pure_python | 151 us                                                 | 137 us: 1.10x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                     |
| tomli_loads          | 1.39 sec                                               | 1.33 sec: 1.05x faster                                                    |
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                     |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                                      |
| json_dumps           | 6.22 ms                                                | 7.23 ms: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.0 ms: 1.49x slower                                                     |
| python_startup         | 11.4 ms                                                | 18.0 ms: 1.58x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.54x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 7.03 ms: 1.10x faster                                                     |
| django_template | 22.3 ms                                                | 25.0 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                      |
| deepcopy_memo              | 27.7 us                                                | 18.1 us: 1.53x faster                                                     |
| deepcopy                   | 235 us                                                 | 163 us: 1.44x faster                                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.37x faster                                                      |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.35x faster                                                     |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                      |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                      |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.20x faster                                                      |
| generators                 | 31.1 ms                                                | 26.0 ms: 1.19x faster                                                     |
| raytrace                   | 212 ms                                                 | 178 ms: 1.19x faster                                                      |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                                     |
| logging_simple             | 3.69 us                                                | 3.18 us: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                      |
| scimark_lu                 | 76.0 ms                                                | 66.1 ms: 1.15x faster                                                     |
| logging_format             | 3.98 us                                                | 3.48 us: 1.14x faster                                                     |
| async_tree_io              | 668 ms                                                 | 586 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                                      |
| float                      | 55.8 ms                                                | 49.8 ms: 1.12x faster                                                     |
| xml_etree_process          | 39.7 ms                                                | 35.7 ms: 1.11x faster                                                     |
| pickle_pure_python         | 200 us                                                 | 181 us: 1.10x faster                                                      |
| unpickle_pure_python       | 151 us                                                 | 137 us: 1.10x faster                                                      |
| mako                       | 7.71 ms                                                | 7.03 ms: 1.10x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                     |
| async_tree_io_tg           | 669 ms                                                 | 614 ms: 1.09x faster                                                      |
| regex_dna                  | 154 ms                                                 | 142 ms: 1.09x faster                                                      |
| deltablue                  | 2.71 ms                                                | 2.51 ms: 1.08x faster                                                     |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                                     |
| regex_effbot               | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                     |
| json                       | 3.09 ms                                                | 2.87 ms: 1.08x faster                                                     |
| bench_thread_pool          | 504 us                                                 | 481 us: 1.05x faster                                                      |
| tomli_loads                | 1.39 sec                                               | 1.33 sec: 1.05x faster                                                    |
| nbody                      | 68.8 ms                                                | 66.1 ms: 1.04x faster                                                     |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                     |
| spectral_norm              | 76.4 ms                                                | 73.6 ms: 1.04x faster                                                     |
| logging_silent             | 76.4 ns                                                | 74.8 ns: 1.02x faster                                                     |
| async_generators           | 304 ms                                                 | 298 ms: 1.02x faster                                                      |
| mdp                        | 1.58 sec                                               | 1.55 sec: 1.02x faster                                                    |
| comprehensions             | 14.5 us                                                | 14.3 us: 1.01x faster                                                     |
| nqueens                    | 62.4 ms                                                | 61.6 ms: 1.01x faster                                                     |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.73 ms: 1.01x slower                                                     |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.01x slower                                                      |
| regex_compile              | 77.9 ms                                                | 79.4 ms: 1.02x slower                                                     |
| chaos                      | 42.5 ms                                                | 43.7 ms: 1.03x slower                                                     |
| scimark_fft                | 195 ms                                                 | 203 ms: 1.04x slower                                                      |
| pycparser                  | 677 ms                                                 | 705 ms: 1.04x slower                                                      |
| go                         | 102 ms                                                 | 106 ms: 1.05x slower                                                      |
| regex_v8                   | 16.0 ms                                                | 16.7 ms: 1.05x slower                                                     |
| sqlglot_normalize          | 186 ms                                                 | 195 ms: 1.05x slower                                                      |
| scimark_sor                | 87.4 ms                                                | 91.6 ms: 1.05x slower                                                     |
| docutils                   | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                    |
| sympy_expand               | 241 ms                                                 | 256 ms: 1.06x slower                                                      |
| scimark_monte_carlo        | 45.0 ms                                                | 47.9 ms: 1.06x slower                                                     |
| sympy_sum                  | 77.6 ms                                                | 82.6 ms: 1.06x slower                                                     |
| sympy_str                  | 148 ms                                                 | 158 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 93.0 us                                                | 99.5 us: 1.07x slower                                                     |
| meteor_contest             | 71.7 ms                                                | 76.8 ms: 1.07x slower                                                     |
| crypto_pyaes               | 51.9 ms                                                | 55.6 ms: 1.07x slower                                                     |
| pprint_safe_repr           | 497 ms                                                 | 533 ms: 1.07x slower                                                      |
| sqlglot_parse              | 848 us                                                 | 916 us: 1.08x slower                                                      |
| pyflate                    | 316 ms                                                 | 343 ms: 1.09x slower                                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.42 ms: 1.09x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                | 1.12 ms: 1.10x slower                                                     |
| fannkuch                   | 248 ms                                                 | 275 ms: 1.11x slower                                                      |
| richards_super             | 36.0 ms                                                | 40.1 ms: 1.11x slower                                                     |
| pprint_pformat             | 1.01 sec                                               | 1.13 sec: 1.12x slower                                                    |
| coverage                   | 38.9 ms                                                | 43.5 ms: 1.12x slower                                                     |
| richards                   | 32.1 ms                                                | 36.0 ms: 1.12x slower                                                     |
| django_template            | 22.3 ms                                                | 25.0 ms: 1.12x slower                                                     |
| 2to3                       | 169 ms                                                 | 191 ms: 1.13x slower                                                      |
| sqlglot_optimize           | 34.0 ms                                                | 39.1 ms: 1.15x slower                                                     |
| json_dumps                 | 6.22 ms                                                | 7.23 ms: 1.16x slower                                                     |
| sympy_integrate            | 11.4 ms                                                | 13.2 ms: 1.16x slower                                                     |
| telco                      | 3.68 ms                                                | 4.47 ms: 1.21x slower                                                     |
| hexiom                     | 4.54 ms                                                | 5.52 ms: 1.22x slower                                                     |
| gc_traversal               | 2.40 ms                                                | 2.94 ms: 1.23x slower                                                     |
| bench_mp_pool              | 44.9 ms                                                | 61.6 ms: 1.37x slower                                                     |
| python_startup_no_site     | 9.37 ms                                                | 14.0 ms: 1.49x slower                                                     |
| python_startup             | 11.4 ms                                                | 18.0 ms: 1.58x slower                                                     |
| create_gc_cycles           | 701 us                                                 | 1.33 ms: 1.90x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (4): xml_etree_iterparse, dulwich_log, sqlalchemy_declarative, tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 57.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.26x