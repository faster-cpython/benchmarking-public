# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmer_side_exits
- machine: darwin-arm64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.06x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 181 ms: 1.07x slower                                                     |
| docutils       | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 176 ms: 1.46x faster                                                     |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                     |
| async_tree_memoization     | 312 ms                                                 | 233 ms: 1.34x faster                                                     |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                     |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.31x faster                                                     |
| async_tree_io              | 668 ms                                                 | 529 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 449 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 452 ms: 1.16x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.1 ms: 1.19x faster                                                    |
| nbody          | 68.8 ms                                                | 63.9 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 74.3 ms: 1.05x faster                                                    |
| regex_dna      | 154 ms                                                 | 150 ms: 1.03x faster                                                     |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                    |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 124 us: 1.22x faster                                                     |
| pickle_pure_python   | 200 us                                                 | 176 us: 1.14x faster                                                     |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                   |
| xml_etree_process    | 39.7 ms                                                | 36.0 ms: 1.10x faster                                                    |
| xml_etree_generate   | 55.8 ms                                                | 52.0 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 74.0 ms                                                | 71.2 ms: 1.04x faster                                                    |
| xml_etree_parse      | 106 ms                                                 | 107 ms: 1.01x slower                                                     |
| json_dumps           | 6.22 ms                                                | 6.45 ms: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.5 ms: 1.55x slower                                                    |
| python_startup         | 11.4 ms                                                | 21.0 ms: 1.84x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.69x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.50 ms: 1.19x faster                                                    |
| django_template | 22.3 ms                                                | 21.5 ms: 1.04x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.1 us: 1.62x faster                                                    |
| deepcopy                   | 235 us                                                 | 151 us: 1.55x faster                                                     |
| async_tree_none_tg         | 258 ms                                                 | 176 ms: 1.46x faster                                                     |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                     |
| deepcopy_reduce            | 2.07 us                                                | 1.53 us: 1.35x faster                                                    |
| generators                 | 31.1 ms                                                | 23.1 ms: 1.34x faster                                                    |
| async_tree_memoization     | 312 ms                                                 | 233 ms: 1.34x faster                                                     |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                     |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.31x faster                                                     |
| raytrace                   | 212 ms                                                 | 165 ms: 1.28x faster                                                     |
| async_tree_io              | 668 ms                                                 | 529 ms: 1.26x faster                                                     |
| logging_silent             | 76.4 ns                                                | 62.4 ns: 1.22x faster                                                    |
| unpickle_pure_python       | 151 us                                                 | 124 us: 1.22x faster                                                     |
| logging_simple             | 3.69 us                                                | 3.05 us: 1.21x faster                                                    |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                                    |
| mako                       | 7.71 ms                                                | 6.50 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 449 ms: 1.19x faster                                                     |
| float                      | 55.8 ms                                                | 47.1 ms: 1.19x faster                                                    |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.18x faster                                                    |
| logging_format             | 3.98 us                                                | 3.39 us: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 452 ms: 1.16x faster                                                     |
| pickle_pure_python         | 200 us                                                 | 176 us: 1.14x faster                                                     |
| deltablue                  | 2.71 ms                                                | 2.39 ms: 1.13x faster                                                    |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 68.7 ms: 1.11x faster                                                    |
| richards_super             | 36.0 ms                                                | 32.5 ms: 1.11x faster                                                    |
| richards                   | 32.1 ms                                                | 29.1 ms: 1.10x faster                                                    |
| xml_etree_process          | 39.7 ms                                                | 36.0 ms: 1.10x faster                                                    |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                   |
| nbody                      | 68.8 ms                                                | 63.9 ms: 1.08x faster                                                    |
| xml_etree_generate         | 55.8 ms                                                | 52.0 ms: 1.07x faster                                                    |
| chaos                      | 42.5 ms                                                | 39.8 ms: 1.07x faster                                                    |
| nqueens                    | 62.4 ms                                                | 58.6 ms: 1.07x faster                                                    |
| sympy_str                  | 148 ms                                                 | 139 ms: 1.06x faster                                                     |
| bench_thread_pool          | 504 us                                                 | 478 us: 1.06x faster                                                     |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                                    |
| pprint_safe_repr           | 497 ms                                                 | 473 ms: 1.05x faster                                                     |
| regex_compile              | 77.9 ms                                                | 74.3 ms: 1.05x faster                                                    |
| sympy_sum                  | 77.6 ms                                                | 74.4 ms: 1.04x faster                                                    |
| xml_etree_iterparse        | 74.0 ms                                                | 71.2 ms: 1.04x faster                                                    |
| django_template            | 22.3 ms                                                | 21.5 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.01 sec                                               | 976 ms: 1.04x faster                                                     |
| sqlglot_normalize          | 186 ms                                                 | 180 ms: 1.03x faster                                                     |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.04 ms: 1.03x faster                                                    |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                                     |
| regex_dna                  | 154 ms                                                 | 150 ms: 1.03x faster                                                     |
| sympy_integrate            | 11.4 ms                                                | 11.1 ms: 1.03x faster                                                    |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                    |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                     |
| scimark_monte_carlo        | 45.0 ms                                                | 44.2 ms: 1.02x faster                                                    |
| sqlglot_parse              | 848 us                                                 | 833 us: 1.02x faster                                                     |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.02x faster                                                    |
| hexiom                     | 4.54 ms                                                | 4.48 ms: 1.01x faster                                                    |
| sqlglot_optimize           | 34.0 ms                                                | 33.8 ms: 1.01x faster                                                    |
| meteor_contest             | 71.7 ms                                                | 72.2 ms: 1.01x slower                                                    |
| go                         | 102 ms                                                 | 102 ms: 1.01x slower                                                     |
| sympy_expand               | 241 ms                                                 | 243 ms: 1.01x slower                                                     |
| xml_etree_parse            | 106 ms                                                 | 107 ms: 1.01x slower                                                     |
| docutils                   | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                   |
| pyflate                    | 316 ms                                                 | 323 ms: 1.02x slower                                                     |
| dask                       | 222 ms                                                 | 228 ms: 1.03x slower                                                     |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                    |
| json_dumps                 | 6.22 ms                                                | 6.45 ms: 1.04x slower                                                    |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.05x slower                                                   |
| typing_runtime_protocols   | 93.0 us                                                | 97.5 us: 1.05x slower                                                    |
| 2to3                       | 169 ms                                                 | 181 ms: 1.07x slower                                                     |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                    |
| scimark_lu                 | 76.0 ms                                                | 83.0 ms: 1.09x slower                                                    |
| scimark_sor                | 87.4 ms                                                | 103 ms: 1.18x slower                                                     |
| coverage                   | 38.9 ms                                                | 46.9 ms: 1.21x slower                                                    |
| telco                      | 3.68 ms                                                | 4.54 ms: 1.23x slower                                                    |
| create_gc_cycles           | 701 us                                                 | 906 us: 1.29x slower                                                     |
| bench_mp_pool              | 44.9 ms                                                | 59.0 ms: 1.32x slower                                                    |
| python_startup_no_site     | 9.37 ms                                                | 14.5 ms: 1.55x slower                                                    |
| python_startup             | 11.4 ms                                                | 21.0 ms: 1.84x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (8): tornado_http, pycparser, asyncio_websockets, json_loads, pidigits, crypto_pyaes, fannkuch, asyncio_tcp
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.22x