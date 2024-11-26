# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.088x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 162 ms: 1.04x faster                                                  |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                |
| tornado_http   | 69.3 ms                                                | 83.1 ms: 1.20x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 193 ms: 1.38x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 243 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.29x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 574 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 595 ms: 1.12x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.5 ms: 1.16x faster                                                 |
| float          | 55.8 ms                                                | 48.7 ms: 1.14x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.8 ms: 1.15x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 147 ms: 1.05x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.5 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 183 us: 1.09x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.8 ms: 1.05x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 53.4 ms: 1.05x faster                                                 |
| json_loads           | 17.2 us                                                | 17.3 us: 1.00x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.03x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.43 ms: 1.03x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.6 ms: 1.45x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 13.7 ms: 1.46x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.6 ms: 1.14x faster                                                 |
| mako            | 7.71 ms                                                | 6.94 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.5 us: 1.68x faster                                                 |
| deepcopy                   | 235 us                                                 | 144 us: 1.63x faster                                                  |
| generators                 | 31.1 ms                                                | 20.4 ms: 1.52x faster                                                 |
| comprehensions             | 14.5 us                                                | 9.96 us: 1.46x faster                                                 |
| raytrace                   | 212 ms                                                 | 149 ms: 1.43x faster                                                  |
| async_tree_none            | 266 ms                                                 | 193 ms: 1.38x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 243 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.29x faster                                                  |
| go                         | 102 ms                                                 | 79.2 ms: 1.28x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.15 ms: 1.26x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                                  |
| logging_silent             | 76.4 ns                                                | 61.3 ns: 1.25x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.7 ms: 1.19x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.09 us: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.41 us: 1.17x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 574 ms: 1.17x faster                                                  |
| nqueens                    | 62.4 ms                                                | 53.6 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                  |
| nbody                      | 68.8 ms                                                | 59.5 ms: 1.16x faster                                                 |
| regex_compile              | 77.9 ms                                                | 67.8 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.8 ms: 1.15x faster                                                 |
| float                      | 55.8 ms                                                | 48.7 ms: 1.14x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 741 us: 1.14x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 66.7 ms: 1.14x faster                                                 |
| django_template            | 22.3 ms                                                | 19.6 ms: 1.14x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 902 us: 1.13x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 67.5 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.79 ms: 1.12x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 69.1 ms: 1.12x faster                                                 |
| sympy_str                  | 148 ms                                                 | 131 ms: 1.12x faster                                                  |
| async_tree_io              | 668 ms                                                 | 595 ms: 1.12x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 451 us: 1.12x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.07 ms: 1.12x faster                                                 |
| mako                       | 7.71 ms                                                | 6.94 ms: 1.11x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                                |
| dulwich_log                | 29.8 ms                                                | 27.0 ms: 1.11x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 450 ms: 1.10x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 922 ms: 1.10x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.2 ms: 1.09x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 183 us: 1.09x faster                                                  |
| async_generators           | 304 ms                                                 | 281 ms: 1.08x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 418 ms: 1.07x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                 |
| sympy_expand               | 241 ms                                                 | 227 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                  |
| pycparser                  | 677 ms                                                 | 641 ms: 1.06x faster                                                  |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                  |
| regex_dna                  | 154 ms                                                 | 147 ms: 1.05x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.8 ms: 1.05x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 53.4 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                 |
| 2to3                       | 169 ms                                                 | 162 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 43.2 ms: 1.04x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                |
| richards_super             | 36.0 ms                                                | 35.1 ms: 1.03x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.6 ms: 1.02x faster                                                 |
| richards                   | 32.1 ms                                                | 31.4 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 91.6 us: 1.02x faster                                                 |
| pathlib                    | 24.2 ms                                                | 24.0 ms: 1.01x faster                                                 |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| json_loads                 | 17.2 us                                                | 17.3 us: 1.00x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 72.4 ms: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.03x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.43 ms: 1.03x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.5 ms: 1.04x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.05x slower                                                |
| fannkuch                   | 248 ms                                                 | 263 ms: 1.06x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 93.1 ms: 1.07x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 48.9 ms: 1.09x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.0 ms: 1.16x slower                                                 |
| tornado_http               | 69.3 ms                                                | 83.1 ms: 1.20x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 905 us: 1.29x slower                                                  |
| telco                      | 3.68 ms                                                | 4.84 ms: 1.31x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.6 ms: 1.45x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.7 ms: 1.46x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.088x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.65x