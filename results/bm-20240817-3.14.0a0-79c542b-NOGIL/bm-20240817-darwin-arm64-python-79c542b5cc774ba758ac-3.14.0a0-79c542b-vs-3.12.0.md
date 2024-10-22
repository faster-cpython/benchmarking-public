# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.40x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x slower
- Memory change: 0.47x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 258 ms: 1.52x slower                                                  |
| docutils       | 1.50 sec                                               | 1.88 sec: 1.25x slower                                                |
| tornado_http   | 69.3 ms                                                | 109 ms: 1.57x slower                                                  |
| Geometric mean | (ref)                                                  | 1.44x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 540 ms: 1.24x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 216 ms: 1.20x faster                                                  |
| async_tree_io              | 668 ms                                                 | 566 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 279 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 476 ms: 1.12x faster                                                  |
| async_tree_none            | 266 ms                                                 | 243 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 503 ms: 1.04x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 307 ms: 1.02x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 103 ms: 1.85x slower                                                  |
| nbody          | 68.8 ms                                                | 158 ms: 2.29x slower                                                  |
| Geometric mean | (ref)                                                  | 1.62x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_v8       | 16.0 ms                                                | 18.0 ms: 1.13x slower                                                 |
| regex_compile  | 77.9 ms                                                | 137 ms: 1.76x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 17.2 us                                                | 19.5 us: 1.13x slower                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 84.8 ms: 1.15x slower                                                 |
| json_dumps           | 6.22 ms                                                | 8.50 ms: 1.37x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 77.8 ms: 1.39x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 2.19 sec: 1.57x slower                                                |
| xml_etree_process    | 39.7 ms                                                | 66.5 ms: 1.68x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 375 us: 1.88x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 293 us: 1.94x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.42x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.6 ms: 1.45x slower                                                 |
| python_startup         | 11.4 ms                                                | 17.1 ms: 1.50x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.47x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 39.3 ms: 1.76x slower                                                 |
| mako            | 7.71 ms                                                | 14.5 ms: 1.89x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.82x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize          | 186 ms                                                 | 121 ms: 1.54x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 352 ms: 1.28x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 540 ms: 1.24x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 216 ms: 1.20x faster                                                  |
| async_tree_io              | 668 ms                                                 | 566 ms: 1.18x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.04 ms: 1.18x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 279 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 476 ms: 1.12x faster                                                  |
| regex_dna                  | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| async_tree_none            | 266 ms                                                 | 243 ms: 1.09x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 503 ms: 1.04x faster                                                  |
| create_gc_cycles           | 701 us                                                 | 673 us: 1.04x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 307 ms: 1.02x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 405 ms: 1.01x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pathlib                    | 24.2 ms                                                | 26.6 ms: 1.10x slower                                                 |
| json                       | 3.09 ms                                                | 3.45 ms: 1.12x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 18.0 ms: 1.13x slower                                                 |
| generators                 | 31.1 ms                                                | 35.1 ms: 1.13x slower                                                 |
| json_loads                 | 17.2 us                                                | 19.5 us: 1.13x slower                                                 |
| async_generators           | 304 ms                                                 | 345 ms: 1.13x slower                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 84.8 ms: 1.15x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.88 sec: 1.19x slower                                                |
| deepcopy                   | 235 us                                                 | 285 us: 1.22x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 55.6 ms: 1.24x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.88 sec: 1.25x slower                                                |
| nqueens                    | 62.4 ms                                                | 79.1 ms: 1.27x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 92.3 ms: 1.29x slower                                                 |
| deepcopy_memo              | 27.7 us                                                | 36.6 us: 1.32x slower                                                 |
| coroutines                 | 19.2 ms                                                | 25.6 ms: 1.33x slower                                                 |
| comprehensions             | 14.5 us                                                | 19.4 us: 1.33x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.26 ms: 1.36x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 8.50 ms: 1.37x slower                                                 |
| deepcopy_reduce            | 2.07 us                                                | 2.87 us: 1.39x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 77.8 ms: 1.39x slower                                                 |
| scimark_fft                | 195 ms                                                 | 276 ms: 1.42x slower                                                  |
| fannkuch                   | 248 ms                                                 | 355 ms: 1.43x slower                                                  |
| dulwich_log                | 29.8 ms                                                | 42.7 ms: 1.43x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 16.3 ms: 1.43x slower                                                 |
| pycparser                  | 677 ms                                                 | 974 ms: 1.44x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.6 ms: 1.45x slower                                                 |
| python_startup             | 11.4 ms                                                | 17.1 ms: 1.50x slower                                                 |
| 2to3                       | 169 ms                                                 | 258 ms: 1.52x slower                                                  |
| coverage                   | 38.9 ms                                                | 59.2 ms: 1.52x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 79.5 ms: 1.53x slower                                                 |
| tornado_http               | 69.3 ms                                                | 109 ms: 1.57x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 2.19 sec: 1.57x slower                                                |
| pyflate                    | 316 ms                                                 | 498 ms: 1.58x slower                                                  |
| telco                      | 3.68 ms                                                | 5.91 ms: 1.61x slower                                                 |
| bench_thread_pool          | 504 us                                                 | 811 us: 1.61x slower                                                  |
| sympy_str                  | 148 ms                                                 | 247 ms: 1.68x slower                                                  |
| xml_etree_process          | 39.7 ms                                                | 66.5 ms: 1.68x slower                                                 |
| django_template            | 22.3 ms                                                | 39.3 ms: 1.76x slower                                                 |
| regex_compile              | 77.9 ms                                                | 137 ms: 1.76x slower                                                  |
| hexiom                     | 4.54 ms                                                | 8.06 ms: 1.77x slower                                                 |
| logging_simple             | 3.69 us                                                | 6.57 us: 1.78x slower                                                 |
| logging_silent             | 76.4 ns                                                | 136 ns: 1.78x slower                                                  |
| logging_format             | 3.98 us                                                | 7.12 us: 1.79x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 60.9 ms: 1.79x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 81.3 ms: 1.81x slower                                                 |
| raytrace                   | 212 ms                                                 | 387 ms: 1.83x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 172 us: 1.85x slower                                                  |
| float                      | 55.8 ms                                                | 103 ms: 1.85x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.89 sec: 1.87x slower                                                |
| spectral_norm              | 76.4 ms                                                | 143 ms: 1.87x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 930 ms: 1.87x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 145 ms: 1.87x slower                                                  |
| pickle_pure_python         | 200 us                                                 | 375 us: 1.88x slower                                                  |
| chaos                      | 42.5 ms                                                | 80.1 ms: 1.88x slower                                                 |
| mako                       | 7.71 ms                                                | 14.5 ms: 1.89x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 165 ms: 1.89x slower                                                  |
| richards                   | 32.1 ms                                                | 61.8 ms: 1.92x slower                                                 |
| sympy_expand               | 241 ms                                                 | 464 ms: 1.92x slower                                                  |
| unpickle_pure_python       | 151 us                                                 | 293 us: 1.94x slower                                                  |
| richards_super             | 36.0 ms                                                | 70.3 ms: 1.95x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 2.01 ms: 1.97x slower                                                 |
| go                         | 102 ms                                                 | 205 ms: 2.02x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 1.75 ms: 2.07x slower                                                 |
| deltablue                  | 2.71 ms                                                | 5.90 ms: 2.18x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 174 ms: 2.29x slower                                                  |
| nbody                      | 68.8 ms                                                | 158 ms: 2.29x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.40x slower                                                          |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, xml_etree_parse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.30x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.22x

# Memory
- memory change: 0.47x