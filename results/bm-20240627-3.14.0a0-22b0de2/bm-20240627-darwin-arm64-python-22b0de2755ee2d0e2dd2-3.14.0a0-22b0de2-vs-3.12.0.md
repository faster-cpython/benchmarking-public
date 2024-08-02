# Results vs. 3.12.0

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: darwin-arm64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 188 ms: 1.11x slower                                                  |
| docutils       | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 175 ms: 1.47x faster                                                  |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 233 ms: 1.34x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 511 ms: 1.31x faster                                                  |
| async_tree_io              | 668 ms                                                 | 539 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 452 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 60.0 ms: 1.15x faster                                                 |
| float          | 55.8 ms                                                | 50.6 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 69.4 ms: 1.12x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.54 ms: 1.04x faster                                                 |
| regex_dna      | 154 ms                                                 | 150 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 185 us: 1.08x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 38.2 ms: 1.04x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 54.0 ms: 1.03x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 146 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 73.0 ms: 1.01x faster                                                 |
| json_loads           | 17.2 us                                                | 17.6 us: 1.02x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.46 ms: 1.04x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.6 ms: 1.67x slower                                                 |
| python_startup         | 11.4 ms                                                | 21.5 ms: 1.89x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.77x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.0 ms: 1.12x faster                                                 |
| mako            | 7.71 ms                                                | 7.12 ms: 1.08x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.1 us: 1.62x faster                                                 |
| deepcopy                   | 235 us                                                 | 147 us: 1.59x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 175 ms: 1.47x faster                                                  |
| raytrace                   | 212 ms                                                 | 148 ms: 1.43x faster                                                  |
| generators                 | 31.1 ms                                                | 22.7 ms: 1.37x faster                                                 |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                                 |
| comprehensions             | 14.5 us                                                | 10.8 us: 1.35x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 233 ms: 1.34x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 511 ms: 1.31x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.14 ms: 1.27x faster                                                 |
| logging_silent             | 76.4 ns                                                | 61.0 ns: 1.25x faster                                                 |
| async_tree_io              | 668 ms                                                 | 539 ms: 1.24x faster                                                  |
| chaos                      | 42.5 ms                                                | 35.3 ms: 1.21x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.08 us: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.39 us: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 452 ms: 1.16x faster                                                  |
| nqueens                    | 62.4 ms                                                | 54.0 ms: 1.16x faster                                                 |
| nbody                      | 68.8 ms                                                | 60.0 ms: 1.15x faster                                                 |
| regex_compile              | 77.9 ms                                                | 69.4 ms: 1.12x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 68.4 ms: 1.12x faster                                                 |
| django_template            | 22.3 ms                                                | 20.0 ms: 1.12x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 763 us: 1.11x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 455 us: 1.11x faster                                                  |
| float                      | 55.8 ms                                                | 50.6 ms: 1.10x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                |
| hexiom                     | 4.54 ms                                                | 4.13 ms: 1.10x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 929 us: 1.10x faster                                                  |
| sympy_str                  | 148 ms                                                 | 136 ms: 1.09x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 171 ms: 1.09x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 71.7 ms: 1.08x faster                                                 |
| mako                       | 7.71 ms                                                | 7.12 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.90 ms: 1.08x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 185 us: 1.08x faster                                                  |
| async_generators           | 304 ms                                                 | 282 ms: 1.08x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.6 ms: 1.08x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 31.8 ms: 1.07x faster                                                 |
| pycparser                  | 677 ms                                                 | 643 ms: 1.05x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 72.4 ms: 1.05x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.54 ms: 1.04x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 38.2 ms: 1.04x faster                                                 |
| sympy_expand               | 241 ms                                                 | 233 ms: 1.04x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.4 ms: 1.04x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 54.0 ms: 1.03x faster                                                 |
| regex_dna                  | 154 ms                                                 | 150 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 981 ms: 1.03x faster                                                  |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 483 ms: 1.03x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 146 us: 1.03x faster                                                  |
| richards_super             | 36.0 ms                                                | 35.0 ms: 1.03x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.5 ms: 1.03x faster                                                 |
| json                       | 3.09 ms                                                | 3.01 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 44.0 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 73.0 ms: 1.01x faster                                                 |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                |
| richards                   | 32.1 ms                                                | 31.8 ms: 1.01x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 72.2 ms: 1.01x slower                                                 |
| json_loads                 | 17.2 us                                                | 17.6 us: 1.02x slower                                                 |
| pyflate                    | 316 ms                                                 | 323 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.46 ms: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| tomli_loads                | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                |
| fannkuch                   | 248 ms                                                 | 268 ms: 1.08x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 95.8 ms: 1.10x slower                                                 |
| 2to3                       | 169 ms                                                 | 188 ms: 1.11x slower                                                  |
| coverage                   | 38.9 ms                                                | 45.5 ms: 1.17x slower                                                 |
| telco                      | 3.68 ms                                                | 4.65 ms: 1.26x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 887 us: 1.26x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 57.2 ms: 1.28x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 15.6 ms: 1.67x slower                                                 |
| python_startup             | 11.4 ms                                                | 21.5 ms: 1.89x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (7): tornado_http, asyncio_tcp, typing_runtime_protocols, xml_etree_parse, dask, asyncio_websockets, pidigits
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240627-3.14.0a0-22b0de2/bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.07x