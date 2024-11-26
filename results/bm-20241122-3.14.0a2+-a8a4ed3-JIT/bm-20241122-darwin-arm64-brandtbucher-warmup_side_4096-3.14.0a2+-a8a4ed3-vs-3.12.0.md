# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: darwin-arm64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.035x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 208 ms: 1.28x faster                                                     |
| async_tree_none_tg         | 258 ms                                                 | 203 ms: 1.27x faster                                                     |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                     |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 669 ms                                                 | 595 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 469 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 479 ms: 1.11x faster                                                     |
| async_tree_io              | 668 ms                                                 | 606 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                    |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                    |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.02 ms: 1.31x faster                                                    |
| regex_dna      | 154 ms                                                 | 135 ms: 1.14x faster                                                     |
| regex_compile  | 77.9 ms                                                | 70.4 ms: 1.11x faster                                                    |
| regex_v8       | 16.0 ms                                                | 15.8 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.13x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 122 us: 1.23x faster                                                     |
| xml_etree_process    | 39.7 ms                                                | 35.3 ms: 1.12x faster                                                    |
| xml_etree_generate   | 55.8 ms                                                | 49.9 ms: 1.12x faster                                                    |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                   |
| json_loads           | 17.2 us                                                | 16.5 us: 1.05x faster                                                    |
| pickle_pure_python   | 200 us                                                 | 193 us: 1.03x faster                                                     |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                                     |
| json_dumps           | 6.22 ms                                                | 7.13 ms: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.1 ms: 1.61x slower                                                    |
| python_startup         | 11.4 ms                                                | 19.8 ms: 1.73x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.67x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.21 ms: 1.24x faster                                                    |
| django_template | 22.3 ms                                                | 23.1 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                     |
| deepcopy_memo              | 27.7 us                                                | 17.5 us: 1.58x faster                                                    |
| deepcopy                   | 235 us                                                 | 157 us: 1.49x faster                                                     |
| deepcopy_reduce            | 2.07 us                                                | 1.56 us: 1.33x faster                                                    |
| regex_effbot               | 2.64 ms                                                | 2.02 ms: 1.31x faster                                                    |
| async_tree_none            | 266 ms                                                 | 208 ms: 1.28x faster                                                     |
| async_tree_none_tg         | 258 ms                                                 | 203 ms: 1.27x faster                                                     |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                     |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                                     |
| mako                       | 7.71 ms                                                | 6.21 ms: 1.24x faster                                                    |
| unpickle_pure_python       | 151 us                                                 | 122 us: 1.23x faster                                                     |
| raytrace                   | 212 ms                                                 | 182 ms: 1.16x faster                                                     |
| generators                 | 31.1 ms                                                | 27.1 ms: 1.14x faster                                                    |
| float                      | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                    |
| regex_dna                  | 154 ms                                                 | 135 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 669 ms                                                 | 595 ms: 1.12x faster                                                     |
| xml_etree_process          | 39.7 ms                                                | 35.3 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 469 ms: 1.12x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                | 49.9 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 479 ms: 1.11x faster                                                     |
| scimark_lu                 | 76.0 ms                                                | 68.5 ms: 1.11x faster                                                    |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                   |
| regex_compile              | 77.9 ms                                                | 70.4 ms: 1.11x faster                                                    |
| async_tree_io              | 668 ms                                                 | 606 ms: 1.10x faster                                                     |
| coroutines                 | 19.2 ms                                                | 17.6 ms: 1.09x faster                                                    |
| spectral_norm              | 76.4 ms                                                | 70.1 ms: 1.09x faster                                                    |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                    |
| comprehensions             | 14.5 us                                                | 13.5 us: 1.08x faster                                                    |
| pathlib                    | 24.2 ms                                                | 22.6 ms: 1.07x faster                                                    |
| json                       | 3.09 ms                                                | 2.88 ms: 1.07x faster                                                    |
| logging_simple             | 3.69 us                                                | 3.46 us: 1.07x faster                                                    |
| logging_format             | 3.98 us                                                | 3.75 us: 1.06x faster                                                    |
| sqlalchemy_declarative     | 62.3 ms                                                | 59.0 ms: 1.06x faster                                                    |
| deltablue                  | 2.71 ms                                                | 2.56 ms: 1.06x faster                                                    |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                     |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.05x faster                                                    |
| sympy_sum                  | 77.6 ms                                                | 74.4 ms: 1.04x faster                                                    |
| pickle_pure_python         | 200 us                                                 | 193 us: 1.03x faster                                                     |
| bench_thread_pool          | 504 us                                                 | 489 us: 1.03x faster                                                     |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.05 ms: 1.03x faster                                                    |
| sympy_str                  | 148 ms                                                 | 144 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.01 sec                                               | 990 ms: 1.02x faster                                                     |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                                     |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.60 ms: 1.01x faster                                                    |
| docutils                   | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                   |
| nqueens                    | 62.4 ms                                                | 61.7 ms: 1.01x faster                                                    |
| dulwich_log                | 29.8 ms                                                | 29.5 ms: 1.01x faster                                                    |
| pprint_safe_repr           | 497 ms                                                 | 492 ms: 1.01x faster                                                     |
| sqlite_synth               | 1.57 us                                                | 1.56 us: 1.01x faster                                                    |
| regex_v8                   | 16.0 ms                                                | 15.8 ms: 1.01x faster                                                    |
| logging_silent             | 76.4 ns                                                | 75.9 ns: 1.01x faster                                                    |
| scimark_sor                | 87.4 ms                                                | 87.0 ms: 1.00x faster                                                    |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 34.0 ms                                                | 34.3 ms: 1.01x slower                                                    |
| sympy_expand               | 241 ms                                                 | 243 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                | 1.03 ms: 1.01x slower                                                    |
| mdp                        | 1.58 sec                                               | 1.60 sec: 1.01x slower                                                   |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.01x slower                                                     |
| sqlglot_parse              | 848 us                                                 | 862 us: 1.02x slower                                                     |
| meteor_contest             | 71.7 ms                                                | 73.2 ms: 1.02x slower                                                    |
| pyflate                    | 316 ms                                                 | 323 ms: 1.02x slower                                                     |
| chaos                      | 42.5 ms                                                | 43.6 ms: 1.02x slower                                                    |
| sympy_integrate            | 11.4 ms                                                | 11.7 ms: 1.03x slower                                                    |
| django_template            | 22.3 ms                                                | 23.1 ms: 1.03x slower                                                    |
| crypto_pyaes               | 51.9 ms                                                | 54.6 ms: 1.05x slower                                                    |
| richards_super             | 36.0 ms                                                | 38.1 ms: 1.06x slower                                                    |
| richards                   | 32.1 ms                                                | 34.2 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 93.0 us                                                | 99.1 us: 1.07x slower                                                    |
| fannkuch                   | 248 ms                                                 | 266 ms: 1.07x slower                                                     |
| hexiom                     | 4.54 ms                                                | 4.87 ms: 1.07x slower                                                    |
| json_dumps                 | 6.22 ms                                                | 7.13 ms: 1.15x slower                                                    |
| coverage                   | 38.9 ms                                                | 45.5 ms: 1.17x slower                                                    |
| telco                      | 3.68 ms                                                | 4.47 ms: 1.22x slower                                                    |
| gc_traversal               | 2.40 ms                                                | 2.96 ms: 1.23x slower                                                    |
| bench_mp_pool              | 44.9 ms                                                | 61.6 ms: 1.37x slower                                                    |
| python_startup_no_site     | 9.37 ms                                                | 15.1 ms: 1.61x slower                                                    |
| python_startup             | 11.4 ms                                                | 19.8 ms: 1.73x slower                                                    |
| create_gc_cycles           | 701 us                                                 | 1.32 ms: 1.88x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_iterparse, sqlglot_normalize, scimark_monte_carlo, pycparser, async_generators, 2to3
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.20x