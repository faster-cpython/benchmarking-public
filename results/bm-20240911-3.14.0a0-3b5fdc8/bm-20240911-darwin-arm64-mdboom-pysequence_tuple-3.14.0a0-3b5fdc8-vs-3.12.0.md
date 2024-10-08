# Results vs. 3.12.0

- fork: mdboom
- ref: pysequence_tuple
- machine: darwin-arm64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 158 ms: 1.07x faster                                              |
| docutils       | 1.50 sec                                               | 1.43 sec: 1.05x faster                                            |
| tornado_http   | 69.3 ms                                                | 81.7 ms: 1.18x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 188 ms: 1.37x faster                                              |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                              |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.26x faster                                              |
| async_tree_memoization_tg  | 323 ms                                                 | 257 ms: 1.25x faster                                              |
| async_tree_io_tg           | 669 ms                                                 | 543 ms: 1.23x faster                                              |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 463 ms: 1.15x faster                                              |
| async_tree_io              | 668 ms                                                 | 581 ms: 1.15x faster                                              |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                              |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.2 ms: 1.13x faster                                             |
| nbody          | 68.8 ms                                                | 60.7 ms: 1.13x faster                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.2 ms: 1.16x faster                                             |
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                             |
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                              |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                              |
| unpickle_pure_python | 151 us                                                 | 141 us: 1.07x faster                                              |
| xml_etree_process    | 39.7 ms                                                | 37.4 ms: 1.06x faster                                             |
| xml_etree_generate   | 55.8 ms                                                | 53.1 ms: 1.05x faster                                             |
| unpickle_list        | 3.02 us                                                | 2.91 us: 1.04x faster                                             |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                             |
| unpickle             | 9.12 us                                                | 9.21 us: 1.01x slower                                             |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                             |
| pickle               | 7.23 us                                                | 7.38 us: 1.02x slower                                             |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                              |
| pickle_list          | 2.89 us                                                | 2.95 us: 1.02x slower                                             |
| json_dumps           | 6.22 ms                                                | 6.41 ms: 1.03x slower                                             |
| tomli_loads          | 1.39 sec                                               | 1.50 sec: 1.08x slower                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.7 ms: 1.46x slower                                             |
| python_startup         | 11.4 ms                                                | 17.0 ms: 1.49x slower                                             |
| Geometric mean         | (ref)                                                  | 1.47x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.6 ms: 1.14x faster                                             |
| mako            | 7.71 ms                                                | 7.00 ms: 1.10x faster                                             |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.5 us: 1.68x faster                                             |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                              |
| generators                 | 31.1 ms                                                | 20.4 ms: 1.53x faster                                             |
| comprehensions             | 14.5 us                                                | 10.0 us: 1.45x faster                                             |
| raytrace                   | 212 ms                                                 | 148 ms: 1.43x faster                                              |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.38x faster                                             |
| async_tree_none_tg         | 258 ms                                                 | 188 ms: 1.37x faster                                              |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                              |
| go                         | 102 ms                                                 | 79.2 ms: 1.28x faster                                             |
| deltablue                  | 2.71 ms                                                | 2.13 ms: 1.27x faster                                             |
| logging_silent             | 76.4 ns                                                | 60.5 ns: 1.26x faster                                             |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.26x faster                                              |
| async_tree_memoization_tg  | 323 ms                                                 | 257 ms: 1.25x faster                                              |
| async_tree_io_tg           | 669 ms                                                 | 543 ms: 1.23x faster                                              |
| logging_simple             | 3.69 us                                                | 3.01 us: 1.22x faster                                             |
| chaos                      | 42.5 ms                                                | 34.9 ms: 1.22x faster                                             |
| logging_format             | 3.98 us                                                | 3.32 us: 1.20x faster                                             |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                             |
| nqueens                    | 62.4 ms                                                | 53.3 ms: 1.17x faster                                             |
| regex_compile              | 77.9 ms                                                | 67.2 ms: 1.16x faster                                             |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 463 ms: 1.15x faster                                              |
| async_tree_io              | 668 ms                                                 | 581 ms: 1.15x faster                                              |
| unpack_sequence            | 31.5 ns                                                | 27.4 ns: 1.15x faster                                             |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                              |
| django_template            | 22.3 ms                                                | 19.6 ms: 1.14x faster                                             |
| sqlglot_parse              | 848 us                                                 | 744 us: 1.14x faster                                              |
| spectral_norm              | 76.4 ms                                                | 67.3 ms: 1.14x faster                                             |
| float                      | 55.8 ms                                                | 49.2 ms: 1.13x faster                                             |
| nbody                      | 68.8 ms                                                | 60.7 ms: 1.13x faster                                             |
| sympy_sum                  | 77.6 ms                                                | 68.9 ms: 1.13x faster                                             |
| sqlglot_transpile          | 1.02 ms                                                | 907 us: 1.13x faster                                              |
| sympy_str                  | 148 ms                                                 | 131 ms: 1.12x faster                                              |
| bench_thread_pool          | 504 us                                                 | 449 us: 1.12x faster                                              |
| scimark_lu                 | 76.0 ms                                                | 67.7 ms: 1.12x faster                                             |
| mdp                        | 1.58 sec                                               | 1.42 sec: 1.12x faster                                            |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                              |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.82 ms: 1.11x faster                                             |
| pprint_safe_repr           | 497 ms                                                 | 448 ms: 1.11x faster                                              |
| hexiom                     | 4.54 ms                                                | 4.11 ms: 1.11x faster                                             |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.11x faster                                             |
| mako                       | 7.71 ms                                                | 7.00 ms: 1.10x faster                                             |
| pprint_pformat             | 1.01 sec                                               | 919 ms: 1.10x faster                                              |
| dulwich_log                | 29.8 ms                                                | 27.1 ms: 1.10x faster                                             |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                              |
| sqlglot_optimize           | 34.0 ms                                                | 31.2 ms: 1.09x faster                                             |
| async_generators           | 304 ms                                                 | 279 ms: 1.09x faster                                              |
| richards_super             | 36.0 ms                                                | 33.5 ms: 1.08x faster                                             |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                             |
| 2to3                       | 169 ms                                                 | 158 ms: 1.07x faster                                              |
| asyncio_tcp                | 449 ms                                                 | 419 ms: 1.07x faster                                              |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.07x faster                                              |
| unpickle_pure_python       | 151 us                                                 | 141 us: 1.07x faster                                              |
| pycparser                  | 677 ms                                                 | 636 ms: 1.06x faster                                              |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                              |
| richards                   | 32.1 ms                                                | 30.3 ms: 1.06x faster                                             |
| xml_etree_process          | 39.7 ms                                                | 37.4 ms: 1.06x faster                                             |
| docutils                   | 1.50 sec                                               | 1.43 sec: 1.05x faster                                            |
| xml_etree_generate         | 55.8 ms                                                | 53.1 ms: 1.05x faster                                             |
| scimark_fft                | 195 ms                                                 | 186 ms: 1.05x faster                                              |
| json                       | 3.09 ms                                                | 2.97 ms: 1.04x faster                                             |
| scimark_monte_carlo        | 45.0 ms                                                | 43.4 ms: 1.04x faster                                             |
| unpickle_list              | 3.02 us                                                | 2.91 us: 1.04x faster                                             |
| crypto_pyaes               | 51.9 ms                                                | 50.2 ms: 1.03x faster                                             |
| pathlib                    | 24.2 ms                                                | 23.8 ms: 1.02x faster                                             |
| typing_runtime_protocols   | 93.0 us                                                | 91.7 us: 1.01x faster                                             |
| sqlite_synth               | 1.57 us                                                | 1.56 us: 1.01x faster                                             |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                             |
| meteor_contest             | 71.7 ms                                                | 71.5 ms: 1.00x faster                                             |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                              |
| unpickle                   | 9.12 us                                                | 9.21 us: 1.01x slower                                             |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                             |
| pyflate                    | 316 ms                                                 | 322 ms: 1.02x slower                                              |
| pickle                     | 7.23 us                                                | 7.38 us: 1.02x slower                                             |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                             |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.02x slower                                              |
| pickle_list                | 2.89 us                                                | 2.95 us: 1.02x slower                                             |
| json_dumps                 | 6.22 ms                                                | 6.41 ms: 1.03x slower                                             |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                            |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                             |
| fannkuch                   | 248 ms                                                 | 260 ms: 1.05x slower                                              |
| scimark_sor                | 87.4 ms                                                | 93.2 ms: 1.07x slower                                             |
| tomli_loads                | 1.39 sec                                               | 1.50 sec: 1.08x slower                                            |
| bench_mp_pool              | 44.9 ms                                                | 49.2 ms: 1.10x slower                                             |
| coverage                   | 38.9 ms                                                | 44.4 ms: 1.14x slower                                             |
| tornado_http               | 69.3 ms                                                | 81.7 ms: 1.18x slower                                             |
| create_gc_cycles           | 701 us                                                 | 892 us: 1.27x slower                                              |
| telco                      | 3.68 ms                                                | 4.81 ms: 1.31x slower                                             |
| python_startup_no_site     | 9.37 ms                                                | 13.7 ms: 1.46x slower                                             |
| python_startup             | 11.4 ms                                                | 17.0 ms: 1.49x slower                                             |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                      |

Benchmark hidden because not significant (2): xml_etree_iterparse, pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.70x