# Results vs. 3.12.0

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: darwin-arm64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.80x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| docutils       | 1.50 sec                                               | 1.48 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 175 ms: 1.47x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                                  |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 236 ms: 1.32x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.32x faster                                                  |
| async_tree_io              | 668 ms                                                 | 532 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 446 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 60.1 ms: 1.14x faster                                                 |
| float          | 55.8 ms                                                | 49.4 ms: 1.13x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.5 ms: 1.14x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.62 ms: 1.01x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.8 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 183 us: 1.09x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.2 ms: 1.07x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 52.7 ms: 1.06x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 72.5 ms: 1.02x faster                                                 |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.36 ms: 1.02x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.3 ms: 1.31x slower                                                 |
| python_startup         | 11.4 ms                                                | 15.1 ms: 1.32x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.71 ms                                                | 7.19 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.9 us: 1.64x faster                                                 |
| deepcopy                   | 235 us                                                 | 146 us: 1.61x faster                                                  |
| generators                 | 31.1 ms                                                | 20.9 ms: 1.49x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 175 ms: 1.47x faster                                                  |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.6 us: 1.37x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                                  |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 236 ms: 1.32x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.32x faster                                                  |
| logging_silent             | 76.4 ns                                                | 59.3 ns: 1.29x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.12 ms: 1.28x faster                                                 |
| async_tree_io              | 668 ms                                                 | 532 ms: 1.25x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.07 us: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 446 ms: 1.19x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.9 ms: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.38 us: 1.18x faster                                                 |
| nqueens                    | 62.4 ms                                                | 54.0 ms: 1.16x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 66.4 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                  |
| nbody                      | 68.8 ms                                                | 60.1 ms: 1.14x faster                                                 |
| regex_compile              | 77.9 ms                                                | 68.5 ms: 1.14x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 746 us: 1.14x faster                                                  |
| django_template            | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                 |
| float                      | 55.8 ms                                                | 49.4 ms: 1.13x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 909 us: 1.12x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 452 us: 1.12x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.08 ms: 1.12x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.81 ms: 1.11x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                                  |
| sympy_str                  | 148 ms                                                 | 134 ms: 1.11x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 70.3 ms: 1.10x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.10x faster                                                |
| pickle_pure_python         | 200 us                                                 | 183 us: 1.09x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.4 ms: 1.09x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 31.2 ms: 1.09x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 69.8 ms: 1.09x faster                                                 |
| async_generators           | 304 ms                                                 | 281 ms: 1.08x faster                                                  |
| mako                       | 7.71 ms                                                | 7.19 ms: 1.07x faster                                                 |
| scimark_fft                | 195 ms                                                 | 183 ms: 1.07x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.2 ms: 1.07x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 52.7 ms: 1.06x faster                                                 |
| pycparser                  | 677 ms                                                 | 640 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 960 ms: 1.05x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 473 ms: 1.05x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.0 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 42.8 ms: 1.05x faster                                                 |
| sympy_expand               | 241 ms                                                 | 230 ms: 1.05x faster                                                  |
| 2to3                       | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| richards_super             | 36.0 ms                                                | 34.4 ms: 1.05x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| go                         | 102 ms                                                 | 98.3 ms: 1.03x faster                                                 |
| richards                   | 32.1 ms                                                | 31.3 ms: 1.03x faster                                                 |
| json                       | 3.09 ms                                                | 3.01 ms: 1.03x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.6 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 90.8 us: 1.02x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 72.5 ms: 1.02x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.48 sec: 1.02x faster                                                |
| regex_effbot               | 2.64 ms                                                | 2.62 ms: 1.01x faster                                                 |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| meteor_contest             | 71.7 ms                                                | 71.6 ms: 1.00x faster                                                 |
| pyflate                    | 316 ms                                                 | 322 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                |
| json_dumps                 | 6.22 ms                                                | 6.36 ms: 1.02x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 47.2 ms: 1.05x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                |
| fannkuch                   | 248 ms                                                 | 263 ms: 1.06x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 96.1 ms: 1.10x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.8 ms: 1.11x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.2 ms: 1.16x slower                                                 |
| telco                      | 3.68 ms                                                | 4.65 ms: 1.26x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 899 us: 1.28x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 12.3 ms: 1.31x slower                                                 |
| python_startup             | 11.4 ms                                                | 15.1 ms: 1.32x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (4): asyncio_tcp, tornado_http, dask, xml_etree_parse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.80x