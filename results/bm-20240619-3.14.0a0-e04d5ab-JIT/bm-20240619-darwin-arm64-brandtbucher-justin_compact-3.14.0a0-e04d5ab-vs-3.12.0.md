# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: darwin-arm64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.02x faster
- HPT reliability: 96.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 176 ms: 1.04x slower                                                  |
| docutils       | 1.50 sec                                               | 1.55 sec: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 266 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 563 ms: 1.19x faster                                                  |
| async_tree_none            | 266 ms                                                 | 228 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 466 ms: 1.14x faster                                                  |
| async_tree_io              | 668 ms                                                 | 597 ms: 1.12x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 282 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 489 ms: 1.07x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.4 ms: 1.18x faster                                                 |
| nbody          | 68.8 ms                                                | 63.3 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 74.1 ms: 1.05x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.03x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 181 us: 1.10x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.29 sec: 1.08x faster                                                |
| unpickle_pure_python | 151 us                                                 | 140 us: 1.08x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.7 ms: 1.05x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 53.4 ms: 1.05x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.91 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.32 ms: 1.02x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.98 us: 1.03x slower                                                 |
| unpickle             | 9.12 us                                                | 9.51 us: 1.04x slower                                                 |
| pickle               | 7.23 us                                                | 7.55 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.4 ms: 1.44x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 13.6 ms: 1.45x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.51 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 23.1 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.0 us: 1.63x faster                                                 |
| deepcopy                   | 235 us                                                 | 158 us: 1.49x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.62 us: 1.28x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 266 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 563 ms: 1.19x faster                                                  |
| mako                       | 7.71 ms                                                | 6.51 ms: 1.19x faster                                                 |
| generators                 | 31.1 ms                                                | 26.3 ms: 1.18x faster                                                 |
| float                      | 55.8 ms                                                | 47.4 ms: 1.18x faster                                                 |
| logging_silent             | 76.4 ns                                                | 65.4 ns: 1.17x faster                                                 |
| raytrace                   | 212 ms                                                 | 182 ms: 1.17x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.5 us: 1.17x faster                                                 |
| async_tree_none            | 266 ms                                                 | 228 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 466 ms: 1.14x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 67.1 ms: 1.14x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.26 us: 1.13x faster                                                 |
| logging_format             | 3.98 us                                                | 3.55 us: 1.12x faster                                                 |
| async_tree_io              | 668 ms                                                 | 597 ms: 1.12x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 282 ms: 1.11x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 181 us: 1.10x faster                                                  |
| nbody                      | 68.8 ms                                                | 63.3 ms: 1.09x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.29 sec: 1.08x faster                                                |
| unpickle_pure_python       | 151 us                                                 | 140 us: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 489 ms: 1.07x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.49 sec: 1.06x faster                                                |
| deltablue                  | 2.71 ms                                                | 2.57 ms: 1.05x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 37.7 ms: 1.05x faster                                                 |
| regex_compile              | 77.9 ms                                                | 74.1 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                                 |
| coroutines                 | 19.2 ms                                                | 18.3 ms: 1.05x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.1 ms: 1.05x faster                                                 |
| scimark_fft                | 195 ms                                                 | 187 ms: 1.05x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 53.4 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.00 ms: 1.04x faster                                                 |
| nqueens                    | 62.4 ms                                                | 60.0 ms: 1.04x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.91 us: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 489 us: 1.03x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.41 ms: 1.03x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 75.4 ms: 1.03x faster                                                 |
| chaos                      | 42.5 ms                                                | 41.5 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 485 ms: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 988 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                 |
| sympy_str                  | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| fannkuch                   | 248 ms                                                 | 243 ms: 1.02x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 44.5 ms: 1.01x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.58 us: 1.01x slower                                                 |
| async_generators           | 304 ms                                                 | 306 ms: 1.01x slower                                                  |
| pyflate                    | 316 ms                                                 | 318 ms: 1.01x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 52.5 ms: 1.01x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 72.7 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 34.5 ms: 1.01x slower                                                 |
| pycparser                  | 677 ms                                                 | 687 ms: 1.01x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.32 ms: 1.02x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| sqlglot_parse              | 848 us                                                 | 871 us: 1.03x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.55 sec: 1.03x slower                                                |
| pickle_list                | 2.89 us                                                | 2.98 us: 1.03x slower                                                 |
| django_template            | 22.3 ms                                                | 23.1 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| go                         | 102 ms                                                 | 106 ms: 1.04x slower                                                  |
| dask                       | 222 ms                                                 | 231 ms: 1.04x slower                                                  |
| 2to3                       | 169 ms                                                 | 176 ms: 1.04x slower                                                  |
| unpickle                   | 9.12 us                                                | 9.51 us: 1.04x slower                                                 |
| pickle                     | 7.23 us                                                | 7.55 us: 1.05x slower                                                 |
| sympy_expand               | 241 ms                                                 | 252 ms: 1.05x slower                                                  |
| richards                   | 32.1 ms                                                | 33.9 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 98.8 us: 1.06x slower                                                 |
| richards_super             | 36.0 ms                                                | 38.5 ms: 1.07x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.61 ms: 1.09x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 86.3 ms: 1.14x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 51.5 ms: 1.15x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 107 ms: 1.23x slower                                                  |
| coverage                   | 38.9 ms                                                | 48.0 ms: 1.23x slower                                                 |
| telco                      | 3.68 ms                                                | 4.63 ms: 1.26x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 912 us: 1.30x slower                                                  |
| python_startup             | 11.4 ms                                                | 16.4 ms: 1.44x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.6 ms: 1.45x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (6): asyncio_tcp, json_loads, sympy_integrate, pidigits, tornado_http, xml_etree_parse
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (14) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x