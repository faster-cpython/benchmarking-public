# Results vs. 3.12.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: darwin-arm64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.76x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 190 ms: 1.12x slower                                                  |
| docutils       | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                |
| tornado_http   | 69.3 ms                                                | 82.7 ms: 1.19x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 183 ms: 1.41x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 229 ms: 1.41x faster                                                  |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 243 ms: 1.28x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 543 ms: 1.23x faster                                                  |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 445 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.5 ms: 1.16x faster                                                 |
| float          | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 69.2 ms: 1.12x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 187 us: 1.07x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 145 us: 1.04x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 54.0 ms: 1.03x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 38.6 ms: 1.03x faster                                                 |
| json_loads           | 17.2 us                                                | 17.2 us: 1.00x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 74.8 ms: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 110 ms: 1.04x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.52 ms: 1.05x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.4 ms: 1.43x slower                                                 |
| python_startup         | 11.4 ms                                                | 16.4 ms: 1.44x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.2 ms: 1.11x faster                                                 |
| mako            | 7.71 ms                                                | 7.20 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.4 us: 1.59x faster                                                 |
| deepcopy                   | 235 us                                                 | 148 us: 1.59x faster                                                  |
| generators                 | 31.1 ms                                                | 20.7 ms: 1.50x faster                                                 |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 183 ms: 1.41x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 229 ms: 1.41x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.33x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 243 ms: 1.28x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.15 ms: 1.26x faster                                                 |
| logging_silent             | 76.4 ns                                                | 62.0 ns: 1.23x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 543 ms: 1.23x faster                                                  |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.21x faster                                                  |
| chaos                      | 42.5 ms                                                | 35.5 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 445 ms: 1.20x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.39 us: 1.17x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.4 ms: 1.17x faster                                                 |
| nbody                      | 68.8 ms                                                | 59.5 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 746 us: 1.14x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.79 ms: 1.13x faster                                                 |
| regex_compile              | 77.9 ms                                                | 69.2 ms: 1.12x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 448 us: 1.12x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 68.1 ms: 1.12x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 67.9 ms: 1.12x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 913 us: 1.12x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 406 ms: 1.11x faster                                                  |
| django_template            | 22.3 ms                                                | 20.2 ms: 1.11x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 27.0 ms: 1.10x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.14 ms: 1.10x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                |
| sympy_str                  | 148 ms                                                 | 135 ms: 1.09x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 71.5 ms: 1.09x faster                                                 |
| async_generators           | 304 ms                                                 | 282 ms: 1.08x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 173 ms: 1.08x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.6 ms: 1.07x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 187 us: 1.07x faster                                                  |
| mako                       | 7.71 ms                                                | 7.20 ms: 1.07x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                                  |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                                  |
| pycparser                  | 677 ms                                                 | 640 ms: 1.06x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 32.2 ms: 1.06x faster                                                 |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 145 us: 1.04x faster                                                  |
| go                         | 102 ms                                                 | 98.1 ms: 1.04x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 54.0 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 481 ms: 1.03x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 43.5 ms: 1.03x faster                                                 |
| richards_super             | 36.0 ms                                                | 34.9 ms: 1.03x faster                                                 |
| sympy_expand               | 241 ms                                                 | 233 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 980 ms: 1.03x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 38.6 ms: 1.03x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.6 ms: 1.03x faster                                                 |
| richards                   | 32.1 ms                                                | 31.7 ms: 1.01x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                |
| json_loads                 | 17.2 us                                                | 17.2 us: 1.00x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| meteor_contest             | 71.7 ms                                                | 72.4 ms: 1.01x slower                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 74.8 ms: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.48 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 96.2 us: 1.03x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 110 ms: 1.04x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.52 ms: 1.05x slower                                                 |
| fannkuch                   | 248 ms                                                 | 262 ms: 1.05x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 93.6 ms: 1.07x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                |
| bench_mp_pool              | 44.9 ms                                                | 48.8 ms: 1.09x slower                                                 |
| 2to3                       | 169 ms                                                 | 190 ms: 1.12x slower                                                  |
| coverage                   | 38.9 ms                                                | 45.2 ms: 1.16x slower                                                 |
| tornado_http               | 69.3 ms                                                | 82.7 ms: 1.19x slower                                                 |
| telco                      | 3.68 ms                                                | 4.59 ms: 1.25x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 896 us: 1.28x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.4 ms: 1.43x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.4 ms: 1.44x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.76x