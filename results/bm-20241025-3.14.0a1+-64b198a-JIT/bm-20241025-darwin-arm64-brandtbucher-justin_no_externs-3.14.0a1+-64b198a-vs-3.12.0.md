# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.028x faster
- HPT reliability: 92.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 186 ms: 1.10x slower                                                      |
| docutils       | 1.50 sec                                               | 1.57 sec: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.07x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                      |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                      |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                      |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                      |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 470 ms: 1.13x faster                                                      |
| async_tree_io_tg           | 669 ms                                                 | 611 ms: 1.10x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                     |
| nbody          | 68.8 ms                                                | 65.0 ms: 1.06x faster                                                     |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 144 ms: 1.07x faster                                                      |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                     |
| regex_compile  | 77.9 ms                                                | 76.6 ms: 1.02x faster                                                     |
| regex_v8       | 16.0 ms                                                | 16.7 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.6 ms: 1.15x faster                                                     |
| unpickle_pure_python | 151 us                                                 | 133 us: 1.13x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                | 49.6 ms: 1.13x faster                                                     |
| pickle_pure_python   | 200 us                                                 | 179 us: 1.11x faster                                                      |
| tomli_loads          | 1.39 sec                                               | 1.27 sec: 1.10x faster                                                    |
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 74.0 ms                                                | 72.6 ms: 1.02x faster                                                     |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                                      |
| json_dumps           | 6.22 ms                                                | 7.16 ms: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.3 ms: 1.52x slower                                                     |
| python_startup         | 11.4 ms                                                | 18.1 ms: 1.59x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.55x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.58 ms: 1.17x faster                                                     |
| django_template | 22.3 ms                                                | 24.1 ms: 1.08x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                      |
| deepcopy_memo              | 27.7 us                                                | 16.7 us: 1.66x faster                                                     |
| deepcopy                   | 235 us                                                 | 156 us: 1.50x faster                                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                      |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                                     |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                      |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                      |
| generators                 | 31.1 ms                                                | 24.9 ms: 1.25x faster                                                     |
| raytrace                   | 212 ms                                                 | 172 ms: 1.23x faster                                                      |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                                      |
| scimark_lu                 | 76.0 ms                                                | 64.1 ms: 1.19x faster                                                     |
| logging_simple             | 3.69 us                                                | 3.11 us: 1.18x faster                                                     |
| mako                       | 7.71 ms                                                | 6.58 ms: 1.17x faster                                                     |
| coroutines                 | 19.2 ms                                                | 16.5 ms: 1.16x faster                                                     |
| logging_format             | 3.98 us                                                | 3.42 us: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                      |
| float                      | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                     |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                      |
| xml_etree_process          | 39.7 ms                                                | 34.6 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 470 ms: 1.13x faster                                                      |
| unpickle_pure_python       | 151 us                                                 | 133 us: 1.13x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                | 49.6 ms: 1.13x faster                                                     |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.11x faster                                                      |
| deltablue                  | 2.71 ms                                                | 2.43 ms: 1.11x faster                                                     |
| tomli_loads                | 1.39 sec                                               | 1.27 sec: 1.10x faster                                                    |
| spectral_norm              | 76.4 ms                                                | 69.6 ms: 1.10x faster                                                     |
| async_tree_io_tg           | 669 ms                                                 | 611 ms: 1.10x faster                                                      |
| logging_silent             | 76.4 ns                                                | 70.3 ns: 1.09x faster                                                     |
| json                       | 3.09 ms                                                | 2.86 ms: 1.08x faster                                                     |
| comprehensions             | 14.5 us                                                | 13.5 us: 1.07x faster                                                     |
| pathlib                    | 24.2 ms                                                | 22.6 ms: 1.07x faster                                                     |
| regex_dna                  | 154 ms                                                 | 144 ms: 1.07x faster                                                      |
| bench_thread_pool          | 504 us                                                 | 471 us: 1.07x faster                                                      |
| nbody                      | 68.8 ms                                                | 65.0 ms: 1.06x faster                                                     |
| nqueens                    | 62.4 ms                                                | 59.4 ms: 1.05x faster                                                     |
| async_generators           | 304 ms                                                 | 292 ms: 1.04x faster                                                      |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                     |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                     |
| dulwich_log                | 29.8 ms                                                | 29.2 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 74.0 ms                                                | 72.6 ms: 1.02x faster                                                     |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.56 ms: 1.02x faster                                                     |
| scimark_fft                | 195 ms                                                 | 192 ms: 1.02x faster                                                      |
| regex_compile              | 77.9 ms                                                | 76.6 ms: 1.02x faster                                                     |
| xml_etree_parse            | 106 ms                                                 | 105 ms: 1.01x faster                                                      |
| mdp                        | 1.58 sec                                               | 1.56 sec: 1.01x faster                                                    |
| sqlalchemy_declarative     | 62.3 ms                                                | 61.9 ms: 1.01x faster                                                     |
| scimark_sor                | 87.4 ms                                                | 86.8 ms: 1.01x faster                                                     |
| chaos                      | 42.5 ms                                                | 42.3 ms: 1.00x faster                                                     |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.17 ms: 1.01x slower                                                     |
| scimark_monte_carlo        | 45.0 ms                                                | 45.8 ms: 1.02x slower                                                     |
| pycparser                  | 677 ms                                                 | 693 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 186 ms                                                 | 190 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 497 ms                                                 | 511 ms: 1.03x slower                                                      |
| pprint_pformat             | 1.01 sec                                               | 1.04 sec: 1.03x slower                                                    |
| sympy_sum                  | 77.6 ms                                                | 80.4 ms: 1.04x slower                                                     |
| sympy_expand               | 241 ms                                                 | 250 ms: 1.04x slower                                                      |
| sympy_str                  | 148 ms                                                 | 154 ms: 1.04x slower                                                      |
| meteor_contest             | 71.7 ms                                                | 74.6 ms: 1.04x slower                                                     |
| regex_v8                   | 16.0 ms                                                | 16.7 ms: 1.04x slower                                                     |
| pyflate                    | 316 ms                                                 | 330 ms: 1.05x slower                                                      |
| sqlglot_parse              | 848 us                                                 | 888 us: 1.05x slower                                                      |
| docutils                   | 1.50 sec                                               | 1.57 sec: 1.05x slower                                                    |
| typing_runtime_protocols   | 93.0 us                                                | 97.6 us: 1.05x slower                                                     |
| crypto_pyaes               | 51.9 ms                                                | 54.9 ms: 1.06x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                | 1.08 ms: 1.06x slower                                                     |
| richards_super             | 36.0 ms                                                | 38.4 ms: 1.07x slower                                                     |
| django_template            | 22.3 ms                                                | 24.1 ms: 1.08x slower                                                     |
| fannkuch                   | 248 ms                                                 | 269 ms: 1.08x slower                                                      |
| richards                   | 32.1 ms                                                | 34.8 ms: 1.08x slower                                                     |
| 2to3                       | 169 ms                                                 | 186 ms: 1.10x slower                                                      |
| sqlglot_optimize           | 34.0 ms                                                | 38.0 ms: 1.12x slower                                                     |
| sympy_integrate            | 11.4 ms                                                | 12.7 ms: 1.12x slower                                                     |
| coverage                   | 38.9 ms                                                | 44.0 ms: 1.13x slower                                                     |
| hexiom                     | 4.54 ms                                                | 5.17 ms: 1.14x slower                                                     |
| json_dumps                 | 6.22 ms                                                | 7.16 ms: 1.15x slower                                                     |
| gc_traversal               | 2.40 ms                                                | 2.94 ms: 1.22x slower                                                     |
| telco                      | 3.68 ms                                                | 4.57 ms: 1.24x slower                                                     |
| bench_mp_pool              | 44.9 ms                                                | 61.6 ms: 1.37x slower                                                     |
| python_startup_no_site     | 9.37 ms                                                | 14.3 ms: 1.52x slower                                                     |
| python_startup             | 11.4 ms                                                | 18.1 ms: 1.59x slower                                                     |
| create_gc_cycles           | 701 us                                                 | 1.32 ms: 1.88x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (2): go, tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 92.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.27x