# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                                  |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                |
| tornado_http   | 69.3 ms                                                | 82.8 ms: 1.19x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 193 ms: 1.38x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 243 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.29x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 573 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 457 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 597 ms: 1.12x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.4 ms: 1.16x faster                                                 |
| float          | 55.8 ms                                                | 48.7 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.5 ms: 1.15x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 146 ms: 1.06x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.5 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 183 us: 1.09x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 53.9 ms: 1.04x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.44 ms: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 110 ms: 1.04x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.5 ms: 1.44x slower                                                 |
| python_startup         | 11.4 ms                                                | 16.6 ms: 1.46x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.0 ms: 1.12x faster                                                 |
| mako            | 7.71 ms                                                | 7.10 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.6 us: 1.66x faster                                                 |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                                  |
| generators                 | 31.1 ms                                                | 20.4 ms: 1.52x faster                                                 |
| comprehensions             | 14.5 us                                                | 10.1 us: 1.45x faster                                                 |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| async_tree_none            | 266 ms                                                 | 193 ms: 1.38x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 243 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.29x faster                                                  |
| go                         | 102 ms                                                 | 79.0 ms: 1.29x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.15 ms: 1.26x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                                  |
| logging_silent             | 76.4 ns                                                | 61.1 ns: 1.25x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.8 ms: 1.19x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.3 ms: 1.17x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 573 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 457 ms: 1.16x faster                                                  |
| nbody                      | 68.8 ms                                                | 59.4 ms: 1.16x faster                                                 |
| logging_format             | 3.98 us                                                | 3.44 us: 1.16x faster                                                 |
| regex_compile              | 77.9 ms                                                | 67.5 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.7 ms: 1.15x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 741 us: 1.14x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.77 ms: 1.13x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.4 ms: 1.13x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 903 us: 1.13x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 69.0 ms: 1.12x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 67.8 ms: 1.12x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 450 us: 1.12x faster                                                  |
| async_tree_io              | 668 ms                                                 | 597 ms: 1.12x faster                                                  |
| django_template            | 22.3 ms                                                | 20.0 ms: 1.12x faster                                                 |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.09 ms: 1.11x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                                |
| sqlglot_normalize          | 186 ms                                                 | 168 ms: 1.11x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 453 ms: 1.10x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 27.2 ms: 1.10x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 183 us: 1.09x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 411 ms: 1.09x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.3 ms: 1.09x faster                                                 |
| mako                       | 7.71 ms                                                | 7.10 ms: 1.09x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 932 ms: 1.08x faster                                                  |
| async_generators           | 304 ms                                                 | 282 ms: 1.08x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                                  |
| pycparser                  | 677 ms                                                 | 639 ms: 1.06x faster                                                  |
| regex_dna                  | 154 ms                                                 | 146 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                  |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                                  |
| sympy_expand               | 241 ms                                                 | 228 ms: 1.06x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.95 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.3 ms: 1.04x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 53.9 ms: 1.04x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                |
| richards_super             | 36.0 ms                                                | 35.1 ms: 1.03x faster                                                 |
| richards                   | 32.1 ms                                                | 31.3 ms: 1.03x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.9 ms: 1.02x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                 |
| pyflate                    | 316 ms                                                 | 324 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| meteor_contest             | 71.7 ms                                                | 74.2 ms: 1.03x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.44 ms: 1.03x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.5 ms: 1.04x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 110 ms: 1.04x slower                                                  |
| fannkuch                   | 248 ms                                                 | 261 ms: 1.05x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| scimark_sor                | 87.4 ms                                                | 92.8 ms: 1.06x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 48.9 ms: 1.09x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.5 ms: 1.14x slower                                                 |
| tornado_http               | 69.3 ms                                                | 82.8 ms: 1.19x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 899 us: 1.28x slower                                                  |
| telco                      | 3.68 ms                                                | 4.75 ms: 1.29x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.5 ms: 1.44x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.6 ms: 1.46x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (5): pathlib, typing_runtime_protocols, xml_etree_iterparse, json_loads, pidigits
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.63x