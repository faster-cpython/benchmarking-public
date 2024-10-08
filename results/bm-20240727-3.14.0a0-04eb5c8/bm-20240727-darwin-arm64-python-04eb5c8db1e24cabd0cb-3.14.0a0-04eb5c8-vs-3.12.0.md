# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.62x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 163 ms: 1.04x faster                                                  |
| docutils       | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                |
| tornado_http   | 69.3 ms                                                | 66.6 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 226 ms: 1.43x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 183 ms: 1.41x faster                                                  |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 508 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 241 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 545 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 441 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 451 ms: 1.17x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.1 ms: 1.16x faster                                                 |
| nbody          | 68.8 ms                                                | 61.7 ms: 1.12x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.4 ms: 1.14x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.54 ms: 1.04x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 53.0 ms: 1.05x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 144 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 72.6 ms: 1.02x faster                                                 |
| json_loads           | 17.2 us                                                | 17.0 us: 1.01x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.37 ms: 1.02x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.2 ms: 1.33x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 12.5 ms: 1.33x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.33x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.71 ms                                                | 7.04 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.0 us: 1.63x faster                                                 |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                                  |
| generators                 | 31.1 ms                                                | 20.6 ms: 1.51x faster                                                 |
| raytrace                   | 212 ms                                                 | 147 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 226 ms: 1.43x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 183 ms: 1.41x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.49 us: 1.38x faster                                                 |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.34x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 508 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 241 ms: 1.30x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.11 ms: 1.28x faster                                                 |
| logging_silent             | 76.4 ns                                                | 59.7 ns: 1.28x faster                                                 |
| async_tree_io              | 668 ms                                                 | 545 ms: 1.22x faster                                                  |
| chaos                      | 42.5 ms                                                | 34.9 ms: 1.22x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 441 ms: 1.21x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.08 us: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.39 us: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 451 ms: 1.17x faster                                                  |
| nqueens                    | 62.4 ms                                                | 53.6 ms: 1.16x faster                                                 |
| float                      | 55.8 ms                                                | 48.1 ms: 1.16x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 65.9 ms: 1.16x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 742 us: 1.14x faster                                                  |
| regex_compile              | 77.9 ms                                                | 68.4 ms: 1.14x faster                                                 |
| django_template            | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 905 us: 1.13x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.79 ms: 1.12x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 449 us: 1.12x faster                                                  |
| nbody                      | 68.8 ms                                                | 61.7 ms: 1.12x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.42 sec: 1.11x faster                                                |
| sympy_sum                  | 77.6 ms                                                | 70.0 ms: 1.11x faster                                                 |
| sympy_str                  | 148 ms                                                 | 133 ms: 1.11x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 168 ms: 1.11x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.12 ms: 1.10x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 27.2 ms: 1.10x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                                  |
| mako                       | 7.71 ms                                                | 7.04 ms: 1.09x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.4 ms: 1.09x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 69.5 ms: 1.09x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 31.2 ms: 1.09x faster                                                 |
| async_generators           | 304 ms                                                 | 281 ms: 1.08x faster                                                  |
| scimark_fft                | 195 ms                                                 | 182 ms: 1.07x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 42.5 ms: 1.06x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 955 ms: 1.06x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 470 ms: 1.06x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 53.0 ms: 1.05x faster                                                 |
| pycparser                  | 677 ms                                                 | 643 ms: 1.05x faster                                                  |
| sympy_expand               | 241 ms                                                 | 229 ms: 1.05x faster                                                  |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 144 us: 1.05x faster                                                  |
| tornado_http               | 69.3 ms                                                | 66.6 ms: 1.04x faster                                                 |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                                 |
| 2to3                       | 169 ms                                                 | 163 ms: 1.04x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.54 ms: 1.04x faster                                                 |
| go                         | 102 ms                                                 | 98.1 ms: 1.04x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.4 ms: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 50.6 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 72.6 ms: 1.02x faster                                                 |
| richards                   | 32.1 ms                                                | 31.6 ms: 1.02x faster                                                 |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.01x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| meteor_contest             | 71.7 ms                                                | 71.9 ms: 1.00x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 93.7 us: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 322 ms: 1.02x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.37 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| bench_mp_pool              | 44.9 ms                                                | 48.1 ms: 1.07x slower                                                 |
| fannkuch                   | 248 ms                                                 | 266 ms: 1.07x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 95.1 ms: 1.09x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.2 ms: 1.14x slower                                                 |
| telco                      | 3.68 ms                                                | 4.55 ms: 1.24x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 903 us: 1.29x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.2 ms: 1.33x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 12.5 ms: 1.33x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (3): asyncio_tcp, xml_etree_parse, dask
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.62x