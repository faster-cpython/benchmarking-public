# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.85x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 174 ms: 1.02x slower                                                  |
| docutils       | 1.50 sec                                               | 1.54 sec: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.42x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 228 ms: 1.42x faster                                                  |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 506 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 239 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 544 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 443 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.7 ms: 1.20x faster                                                 |
| nbody          | 68.8 ms                                                | 62.7 ms: 1.10x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 71.2 ms: 1.09x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                 |
| regex_dna      | 154 ms                                                 | 153 ms: 1.01x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 174 us: 1.15x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.12x faster                                                |
| xml_etree_process    | 39.7 ms                                                | 35.8 ms: 1.11x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 51.7 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.35 ms: 1.02x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.1 ms: 1.40x slower                                                 |
| python_startup         | 11.4 ms                                                | 16.1 ms: 1.41x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.40x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.46 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 21.6 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.2 us: 1.61x faster                                                 |
| deepcopy                   | 235 us                                                 | 154 us: 1.52x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.42x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 228 ms: 1.42x faster                                                  |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.34x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 506 ms: 1.32x faster                                                  |
| raytrace                   | 212 ms                                                 | 160 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 239 ms: 1.30x faster                                                  |
| generators                 | 31.1 ms                                                | 24.6 ms: 1.26x faster                                                 |
| logging_silent             | 76.4 ns                                                | 61.0 ns: 1.25x faster                                                 |
| logging_simple             | 3.69 us                                                | 2.99 us: 1.23x faster                                                 |
| async_tree_io              | 668 ms                                                 | 544 ms: 1.23x faster                                                  |
| logging_format             | 3.98 us                                                | 3.30 us: 1.21x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 443 ms: 1.20x faster                                                  |
| float                      | 55.8 ms                                                | 46.7 ms: 1.20x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.2 us: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                 |
| mako                       | 7.71 ms                                                | 6.46 ms: 1.19x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.32 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 174 us: 1.15x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 66.2 ms: 1.15x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 68.3 ms: 1.12x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.12x faster                                                |
| xml_etree_process          | 39.7 ms                                                | 35.8 ms: 1.11x faster                                                 |
| nbody                      | 68.8 ms                                                | 62.7 ms: 1.10x faster                                                 |
| chaos                      | 42.5 ms                                                | 38.8 ms: 1.10x faster                                                 |
| regex_compile              | 77.9 ms                                                | 71.2 ms: 1.09x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 413 ms: 1.09x faster                                                  |
| nqueens                    | 62.4 ms                                                | 57.8 ms: 1.08x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 51.7 ms: 1.08x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.46 sec: 1.08x faster                                                |
| bench_thread_pool          | 504 us                                                 | 472 us: 1.07x faster                                                  |
| json                       | 3.09 ms                                                | 2.91 ms: 1.06x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 28.2 ms: 1.06x faster                                                 |
| richards_super             | 36.0 ms                                                | 34.2 ms: 1.05x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 74.2 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.01 ms: 1.04x faster                                                 |
| sympy_str                  | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| richards                   | 32.1 ms                                                | 30.9 ms: 1.04x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 179 ms: 1.04x faster                                                  |
| django_template            | 22.3 ms                                                | 21.6 ms: 1.04x faster                                                 |
| scimark_fft                | 195 ms                                                 | 189 ms: 1.03x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                 |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 483 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 982 ms: 1.03x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 43.8 ms: 1.03x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.43 ms: 1.03x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 33.4 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 71.0 ms: 1.01x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.3 ms: 1.01x faster                                                 |
| regex_dna                  | 154 ms                                                 | 153 ms: 1.01x faster                                                  |
| pyflate                    | 316 ms                                                 | 313 ms: 1.01x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 51.6 ms: 1.01x faster                                                 |
| go                         | 102 ms                                                 | 101 ms: 1.00x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pycparser                  | 677 ms                                                 | 684 ms: 1.01x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 88.4 ms: 1.01x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.35 ms: 1.02x slower                                                 |
| sympy_expand               | 241 ms                                                 | 246 ms: 1.02x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.54 sec: 1.02x slower                                                |
| 2to3                       | 169 ms                                                 | 174 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| dask                       | 222 ms                                                 | 233 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 97.8 us: 1.05x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 51.0 ms: 1.14x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.7 ms: 1.15x slower                                                 |
| telco                      | 3.68 ms                                                | 4.56 ms: 1.24x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 904 us: 1.29x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.1 ms: 1.40x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.1 ms: 1.41x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (5): tornado_http, sqlglot_transpile, sqlglot_parse, fannkuch, json_loads
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.85x