# Results vs. 3.12.0

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: darwin-arm64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 163 ms: 1.04x faster                                                  |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                |
| tornado_http   | 69.3 ms                                                | 66.4 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 175 ms: 1.48x faster                                                  |
| async_tree_none            | 266 ms                                                 | 191 ms: 1.39x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 231 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.35x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.32x faster                                                  |
| async_tree_io              | 668 ms                                                 | 532 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 445 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 451 ms: 1.17x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                 |
| nbody          | 68.8 ms                                                | 62.2 ms: 1.11x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.3 ms: 1.14x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.57 ms: 1.03x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.1 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 181 us: 1.10x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 37.8 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                 |
| json_loads           | 17.2 us                                                | 17.2 us: 1.00x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.53 ms: 1.05x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 10.8 ms: 1.15x slower                                                 |
| python_startup         | 11.4 ms                                                | 13.6 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.8 ms: 1.13x faster                                                 |
| mako            | 7.71 ms                                                | 7.05 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.8 us: 1.65x faster                                                 |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 175 ms: 1.48x faster                                                  |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| async_tree_none            | 266 ms                                                 | 191 ms: 1.39x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| generators                 | 31.1 ms                                                | 22.7 ms: 1.37x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 231 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.35x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.8 us: 1.34x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.32x faster                                                  |
| logging_silent             | 76.4 ns                                                | 59.1 ns: 1.29x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.10 ms: 1.29x faster                                                 |
| async_tree_io              | 668 ms                                                 | 532 ms: 1.26x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.04 us: 1.21x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 445 ms: 1.20x faster                                                  |
| chaos                      | 42.5 ms                                                | 35.7 ms: 1.19x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 451 ms: 1.17x faster                                                  |
| nqueens                    | 62.4 ms                                                | 54.0 ms: 1.16x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 739 us: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                 |
| regex_compile              | 77.9 ms                                                | 68.3 ms: 1.14x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 899 us: 1.14x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 67.2 ms: 1.14x faster                                                 |
| django_template            | 22.3 ms                                                | 19.8 ms: 1.13x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.42 sec: 1.11x faster                                                |
| bench_thread_pool          | 504 us                                                 | 453 us: 1.11x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.11 ms: 1.11x faster                                                 |
| nbody                      | 68.8 ms                                                | 62.2 ms: 1.11x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 181 us: 1.10x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 70.5 ms: 1.10x faster                                                 |
| sympy_str                  | 148 ms                                                 | 134 ms: 1.10x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 169 ms: 1.10x faster                                                  |
| mako                       | 7.71 ms                                                | 7.05 ms: 1.09x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.4 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.89 ms: 1.09x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 414 ms: 1.08x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.4 ms: 1.08x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 70.7 ms: 1.07x faster                                                 |
| async_generators           | 304 ms                                                 | 283 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 467 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 952 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                  |
| pycparser                  | 677 ms                                                 | 643 ms: 1.05x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 37.8 ms: 1.05x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.1 ms: 1.05x faster                                                 |
| richards_super             | 36.0 ms                                                | 34.3 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                 |
| tornado_http               | 69.3 ms                                                | 66.4 ms: 1.04x faster                                                 |
| scimark_fft                | 195 ms                                                 | 187 ms: 1.04x faster                                                  |
| sympy_expand               | 241 ms                                                 | 232 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 43.3 ms: 1.04x faster                                                 |
| 2to3                       | 169 ms                                                 | 163 ms: 1.04x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                |
| regex_effbot               | 2.64 ms                                                | 2.57 ms: 1.03x faster                                                 |
| go                         | 102 ms                                                 | 98.9 ms: 1.03x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.6 ms: 1.03x faster                                                 |
| richards                   | 32.1 ms                                                | 31.4 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 71.2 ms: 1.01x faster                                                 |
| json_loads                 | 17.2 us                                                | 17.2 us: 1.00x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.01x slower                                                  |
| pyflate                    | 316 ms                                                 | 320 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 94.7 us: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 45.9 ms: 1.02x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.53 ms: 1.05x slower                                                 |
| fannkuch                   | 248 ms                                                 | 262 ms: 1.05x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                |
| regex_v8                   | 16.0 ms                                                | 17.1 ms: 1.07x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 96.5 ms: 1.10x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 10.8 ms: 1.15x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.1 ms: 1.16x slower                                                 |
| python_startup             | 11.4 ms                                                | 13.6 ms: 1.19x slower                                                 |
| telco                      | 3.68 ms                                                | 4.59 ms: 1.25x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 896 us: 1.28x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240717-3.14.0a0-f4bc84d/bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x