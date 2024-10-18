# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: darwin-arm64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.02x faster
- HPT reliability: 94.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 183 ms: 1.08x slower                                                    |
| docutils       | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.37x faster                                                    |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                    |
| async_tree_memoization     | 312 ms                                                 | 245 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                    |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 471 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 669 ms                                                 | 613 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                   |
| nbody          | 68.8 ms                                                | 65.5 ms: 1.05x faster                                                   |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 148 ms: 1.05x faster                                                    |
| regex_compile  | 77.9 ms                                                | 75.8 ms: 1.03x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.00x faster                                                   |
| regex_v8       | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                    |
| xml_etree_process    | 39.7 ms                                                | 35.0 ms: 1.13x faster                                                   |
| pickle_pure_python   | 200 us                                                 | 180 us: 1.11x faster                                                    |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 50.8 ms: 1.10x faster                                                   |
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                   |
| unpickle_list        | 3.02 us                                                | 2.96 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 74.0 ms                                                | 72.9 ms: 1.02x faster                                                   |
| pickle_list          | 2.89 us                                                | 2.86 us: 1.01x faster                                                   |
| xml_etree_parse      | 106 ms                                                 | 107 ms: 1.01x slower                                                    |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                   |
| pickle               | 7.23 us                                                | 7.32 us: 1.01x slower                                                   |
| json_dumps           | 6.22 ms                                                | 7.14 ms: 1.15x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.8 ms: 1.58x slower                                                   |
| python_startup         | 11.4 ms                                                | 19.2 ms: 1.68x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.63x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.48 ms: 1.19x faster                                                   |
| django_template | 22.3 ms                                                | 22.8 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.69x faster                                                    |
| deepcopy_memo              | 27.7 us                                                | 16.9 us: 1.64x faster                                                   |
| deepcopy                   | 235 us                                                 | 156 us: 1.51x faster                                                    |
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.37x faster                                                    |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                    |
| deepcopy_reduce            | 2.07 us                                                | 1.56 us: 1.33x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 245 ms: 1.27x faster                                                    |
| generators                 | 31.1 ms                                                | 25.2 ms: 1.23x faster                                                   |
| raytrace                   | 212 ms                                                 | 173 ms: 1.23x faster                                                    |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.21x faster                                                    |
| mako                       | 7.71 ms                                                | 6.48 ms: 1.19x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                                   |
| scimark_lu                 | 76.0 ms                                                | 64.6 ms: 1.18x faster                                                   |
| logging_format             | 3.98 us                                                | 3.40 us: 1.17x faster                                                   |
| coroutines                 | 19.2 ms                                                | 16.6 ms: 1.16x faster                                                   |
| float                      | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                    |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                    |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                    |
| xml_etree_process          | 39.7 ms                                                | 35.0 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 471 ms: 1.13x faster                                                    |
| deltablue                  | 2.71 ms                                                | 2.41 ms: 1.12x faster                                                   |
| comprehensions             | 14.5 us                                                | 12.9 us: 1.12x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 180 us: 1.11x faster                                                    |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 50.8 ms: 1.10x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 69.8 ms: 1.09x faster                                                   |
| logging_silent             | 76.4 ns                                                | 69.9 ns: 1.09x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 613 ms: 1.09x faster                                                    |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                                   |
| nqueens                    | 62.4 ms                                                | 58.2 ms: 1.07x faster                                                   |
| json                       | 3.09 ms                                                | 2.88 ms: 1.07x faster                                                   |
| bench_thread_pool          | 504 us                                                 | 475 us: 1.06x faster                                                    |
| nbody                      | 68.8 ms                                                | 65.5 ms: 1.05x faster                                                   |
| regex_dna                  | 154 ms                                                 | 148 ms: 1.05x faster                                                    |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                   |
| dulwich_log                | 29.8 ms                                                | 28.8 ms: 1.03x faster                                                   |
| go                         | 102 ms                                                 | 98.2 ms: 1.03x faster                                                   |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                                    |
| regex_compile              | 77.9 ms                                                | 75.8 ms: 1.03x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                   |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                    |
| unpickle_list              | 3.02 us                                                | 2.96 us: 1.02x faster                                                   |
| mdp                        | 1.58 sec                                               | 1.55 sec: 1.02x faster                                                  |
| chaos                      | 42.5 ms                                                | 41.8 ms: 1.02x faster                                                   |
| scimark_sor                | 87.4 ms                                                | 86.1 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 74.0 ms                                                | 72.9 ms: 1.02x faster                                                   |
| pickle_list                | 2.89 us                                                | 2.86 us: 1.01x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.63 ms: 1.00x faster                                                   |
| sqlglot_normalize          | 186 ms                                                 | 186 ms: 1.00x slower                                                    |
| pprint_pformat             | 1.01 sec                                               | 1.02 sec: 1.00x slower                                                  |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                                    |
| xml_etree_parse            | 106 ms                                                 | 107 ms: 1.01x slower                                                    |
| pycparser                  | 677 ms                                                 | 683 ms: 1.01x slower                                                    |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                   |
| pickle                     | 7.23 us                                                | 7.32 us: 1.01x slower                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.19 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 45.9 ms: 1.02x slower                                                   |
| django_template            | 22.3 ms                                                | 22.8 ms: 1.02x slower                                                   |
| sympy_sum                  | 77.6 ms                                                | 79.3 ms: 1.02x slower                                                   |
| sympy_expand               | 241 ms                                                 | 247 ms: 1.02x slower                                                    |
| sympy_str                  | 148 ms                                                 | 151 ms: 1.03x slower                                                    |
| sqlglot_parse              | 848 us                                                 | 873 us: 1.03x slower                                                    |
| pyflate                    | 316 ms                                                 | 327 ms: 1.04x slower                                                    |
| meteor_contest             | 71.7 ms                                                | 74.6 ms: 1.04x slower                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.07 ms: 1.04x slower                                                   |
| crypto_pyaes               | 51.9 ms                                                | 54.1 ms: 1.04x slower                                                   |
| docutils                   | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.31 sec: 1.05x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 97.9 us: 1.05x slower                                                   |
| regex_v8                   | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                   |
| fannkuch                   | 248 ms                                                 | 266 ms: 1.07x slower                                                    |
| richards_super             | 36.0 ms                                                | 38.7 ms: 1.08x slower                                                   |
| 2to3                       | 169 ms                                                 | 183 ms: 1.08x slower                                                    |
| hexiom                     | 4.54 ms                                                | 4.95 ms: 1.09x slower                                                   |
| richards                   | 32.1 ms                                                | 35.2 ms: 1.09x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 37.5 ms: 1.10x slower                                                   |
| sympy_integrate            | 11.4 ms                                                | 12.6 ms: 1.11x slower                                                   |
| coverage                   | 38.9 ms                                                | 43.5 ms: 1.12x slower                                                   |
| json_dumps                 | 6.22 ms                                                | 7.14 ms: 1.15x slower                                                   |
| gc_traversal               | 2.40 ms                                                | 2.95 ms: 1.23x slower                                                   |
| telco                      | 3.68 ms                                                | 4.67 ms: 1.27x slower                                                   |
| bench_mp_pool              | 44.9 ms                                                | 61.8 ms: 1.38x slower                                                   |
| python_startup_no_site     | 9.37 ms                                                | 14.8 ms: 1.58x slower                                                   |
| python_startup             | 11.4 ms                                                | 19.2 ms: 1.68x slower                                                   |
| create_gc_cycles           | 701 us                                                 | 1.31 ms: 1.86x slower                                                   |
| unpack_sequence            | 31.5 ns                                                | 77.0 ns: 2.45x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (4): pprint_safe_repr, unpickle, asyncio_tcp, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 94.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x