# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc1
- machine: darwin-arm64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.071x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                         |
| chameleon      | 4.70 ms                                                | 4.36 ms: 1.08x faster                                        |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.03x faster                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.35x faster                                         |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                         |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.27x faster                                         |
| async_tree_io              | 668 ms                                                 | 555 ms: 1.20x faster                                         |
| async_tree_memoization     | 312 ms                                                 | 260 ms: 1.20x faster                                         |
| async_tree_io_tg           | 669 ms                                                 | 564 ms: 1.19x faster                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 452 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 468 ms: 1.12x faster                                         |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.5 ms: 1.15x faster                                        |
| nbody          | 68.8 ms                                                | 60.6 ms: 1.14x faster                                        |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 69.3 ms: 1.12x faster                                        |
| regex_dna      | 154 ms                                                 | 151 ms: 1.02x faster                                         |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                        |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                         |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                         |
| xml_etree_generate   | 55.8 ms                                                | 53.2 ms: 1.05x faster                                        |
| xml_etree_process    | 39.7 ms                                                | 38.0 ms: 1.04x faster                                        |
| xml_etree_iterparse  | 74.0 ms                                                | 72.0 ms: 1.03x faster                                        |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                        |
| xml_etree_parse      | 106 ms                                                 | 106 ms: 1.01x faster                                         |
| tomli_loads          | 1.39 sec                                               | 1.46 sec: 1.05x slower                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.4 ms: 1.35x slower                                        |
| python_startup_no_site | 9.37 ms                                                | 12.7 ms: 1.35x slower                                        |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.0 ms: 1.12x faster                                        |
| mako            | 7.71 ms                                                | 7.23 ms: 1.07x faster                                        |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 148 ms: 1.43x faster                                         |
| comprehensions             | 14.5 us                                                | 10.6 us: 1.37x faster                                        |
| generators                 | 31.1 ms                                                | 22.9 ms: 1.36x faster                                        |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.35x faster                                         |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                         |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.27x faster                                         |
| deltablue                  | 2.71 ms                                                | 2.15 ms: 1.26x faster                                        |
| logging_silent             | 76.4 ns                                                | 60.9 ns: 1.25x faster                                        |
| chaos                      | 42.5 ms                                                | 34.5 ms: 1.23x faster                                        |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                        |
| async_tree_io              | 668 ms                                                 | 555 ms: 1.20x faster                                         |
| async_tree_memoization     | 312 ms                                                 | 260 ms: 1.20x faster                                         |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                        |
| deepcopy_memo              | 27.7 us                                                | 23.2 us: 1.19x faster                                        |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                        |
| async_tree_io_tg           | 669 ms                                                 | 564 ms: 1.19x faster                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 452 ms: 1.18x faster                                         |
| nqueens                    | 62.4 ms                                                | 53.3 ms: 1.17x faster                                        |
| float                      | 55.8 ms                                                | 48.5 ms: 1.15x faster                                        |
| sqlglot_parse              | 848 us                                                 | 741 us: 1.14x faster                                         |
| deepcopy                   | 235 us                                                 | 205 us: 1.14x faster                                         |
| nbody                      | 68.8 ms                                                | 60.6 ms: 1.14x faster                                        |
| spectral_norm              | 76.4 ms                                                | 67.4 ms: 1.13x faster                                        |
| deepcopy_reduce            | 2.07 us                                                | 1.83 us: 1.13x faster                                        |
| sqlglot_transpile          | 1.02 ms                                                | 904 us: 1.13x faster                                         |
| regex_compile              | 77.9 ms                                                | 69.3 ms: 1.12x faster                                        |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 468 ms: 1.12x faster                                         |
| django_template            | 22.3 ms                                                | 20.0 ms: 1.12x faster                                        |
| scimark_lu                 | 76.0 ms                                                | 67.9 ms: 1.12x faster                                        |
| sympy_str                  | 148 ms                                                 | 133 ms: 1.11x faster                                         |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                         |
| hexiom                     | 4.54 ms                                                | 4.10 ms: 1.11x faster                                        |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                       |
| sympy_sum                  | 77.6 ms                                                | 70.2 ms: 1.11x faster                                        |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.84 ms: 1.10x faster                                        |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                         |
| dulwich_log                | 29.8 ms                                                | 27.3 ms: 1.09x faster                                        |
| sympy_integrate            | 11.4 ms                                                | 10.4 ms: 1.09x faster                                        |
| bench_thread_pool          | 504 us                                                 | 463 us: 1.09x faster                                         |
| sqlglot_optimize           | 34.0 ms                                                | 31.3 ms: 1.09x faster                                        |
| asyncio_tcp                | 449 ms                                                 | 414 ms: 1.08x faster                                         |
| chameleon                  | 4.70 ms                                                | 4.36 ms: 1.08x faster                                        |
| async_generators           | 304 ms                                                 | 283 ms: 1.07x faster                                         |
| mako                       | 7.71 ms                                                | 7.23 ms: 1.07x faster                                        |
| json                       | 3.09 ms                                                | 2.90 ms: 1.07x faster                                        |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                         |
| pprint_pformat             | 1.01 sec                                               | 953 ms: 1.06x faster                                         |
| pycparser                  | 677 ms                                                 | 638 ms: 1.06x faster                                         |
| pprint_safe_repr           | 497 ms                                                 | 469 ms: 1.06x faster                                         |
| sympy_expand               | 241 ms                                                 | 228 ms: 1.06x faster                                         |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                         |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                         |
| typing_runtime_protocols   | 93.0 us                                                | 88.5 us: 1.05x faster                                        |
| scimark_monte_carlo        | 45.0 ms                                                | 42.9 ms: 1.05x faster                                        |
| xml_etree_generate         | 55.8 ms                                                | 53.2 ms: 1.05x faster                                        |
| xml_etree_process          | 39.7 ms                                                | 38.0 ms: 1.04x faster                                        |
| richards_super             | 36.0 ms                                                | 34.7 ms: 1.04x faster                                        |
| crypto_pyaes               | 51.9 ms                                                | 50.0 ms: 1.04x faster                                        |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.03x faster                                       |
| xml_etree_iterparse        | 74.0 ms                                                | 72.0 ms: 1.03x faster                                        |
| regex_dna                  | 154 ms                                                 | 151 ms: 1.02x faster                                         |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                        |
| pathlib                    | 24.2 ms                                                | 23.8 ms: 1.02x faster                                        |
| meteor_contest             | 71.7 ms                                                | 70.4 ms: 1.02x faster                                        |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                        |
| richards                   | 32.1 ms                                                | 31.6 ms: 1.02x faster                                        |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                         |
| xml_etree_parse            | 106 ms                                                 | 106 ms: 1.01x faster                                         |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                         |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                         |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                       |
| fannkuch                   | 248 ms                                                 | 254 ms: 1.02x slower                                         |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                        |
| tomli_loads                | 1.39 sec                                               | 1.46 sec: 1.05x slower                                       |
| bench_mp_pool              | 44.9 ms                                                | 47.9 ms: 1.07x slower                                        |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.08x slower                                        |
| scimark_sor                | 87.4 ms                                                | 95.2 ms: 1.09x slower                                        |
| coverage                   | 38.9 ms                                                | 45.0 ms: 1.16x slower                                        |
| mypy2                      | 380 ms                                                 | 455 ms: 1.20x slower                                         |
| create_gc_cycles           | 701 us                                                 | 880 us: 1.26x slower                                         |
| telco                      | 3.68 ms                                                | 4.64 ms: 1.26x slower                                        |
| python_startup             | 11.4 ms                                                | 15.4 ms: 1.35x slower                                        |
| python_startup_no_site     | 9.37 ms                                                | 12.7 ms: 1.35x slower                                        |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (4): tornado_http, dask, asyncio_websockets, json_dumps
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.071x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.59x