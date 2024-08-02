# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: darwin-arm64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.80x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 163 ms: 1.04x faster                                                            |
| tornado_http   | 69.3 ms                                                | 66.3 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 226 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 258 ms                                                 | 183 ms: 1.41x faster                                                            |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                            |
| async_tree_io_tg           | 669 ms                                                 | 511 ms: 1.31x faster                                                            |
| async_tree_memoization     | 312 ms                                                 | 241 ms: 1.29x faster                                                            |
| async_tree_io              | 668 ms                                                 | 544 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 443 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 452 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.1 ms: 1.17x faster                                                           |
| float          | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 69.1 ms: 1.13x faster                                                           |
| regex_dna      | 154 ms                                                 | 150 ms: 1.03x faster                                                            |
| regex_effbot   | 2.64 ms                                                | 2.64 ms: 1.00x faster                                                           |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 185 us: 1.08x faster                                                            |
| xml_etree_process    | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                           |
| unpickle_pure_python | 151 us                                                 | 145 us: 1.04x faster                                                            |
| xml_etree_generate   | 55.8 ms                                                | 53.7 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 74.0 ms                                                | 73.1 ms: 1.01x faster                                                           |
| json_loads           | 17.2 us                                                | 17.4 us: 1.01x slower                                                           |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                                            |
| json_dumps           | 6.22 ms                                                | 6.45 ms: 1.04x slower                                                           |
| tomli_loads          | 1.39 sec                                               | 1.50 sec: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.5 ms: 1.36x slower                                                           |
| python_startup_no_site | 9.37 ms                                                | 12.8 ms: 1.37x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                           |
| mako            | 7.71 ms                                                | 6.98 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.1 us: 1.62x faster                                                           |
| deepcopy                   | 235 us                                                 | 146 us: 1.61x faster                                                            |
| generators                 | 31.1 ms                                                | 20.6 ms: 1.51x faster                                                           |
| async_tree_memoization_tg  | 323 ms                                                 | 226 ms: 1.42x faster                                                            |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 258 ms                                                 | 183 ms: 1.41x faster                                                            |
| comprehensions             | 14.5 us                                                | 10.4 us: 1.39x faster                                                           |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                            |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                                           |
| async_tree_io_tg           | 669 ms                                                 | 511 ms: 1.31x faster                                                            |
| async_tree_memoization     | 312 ms                                                 | 241 ms: 1.29x faster                                                            |
| logging_silent             | 76.4 ns                                                | 59.5 ns: 1.29x faster                                                           |
| deltablue                  | 2.71 ms                                                | 2.13 ms: 1.27x faster                                                           |
| async_tree_io              | 668 ms                                                 | 544 ms: 1.23x faster                                                            |
| logging_simple             | 3.69 us                                                | 3.05 us: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 443 ms: 1.20x faster                                                            |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                           |
| chaos                      | 42.5 ms                                                | 35.7 ms: 1.19x faster                                                           |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                           |
| nbody                      | 68.8 ms                                                | 59.1 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 452 ms: 1.16x faster                                                            |
| nqueens                    | 62.4 ms                                                | 53.8 ms: 1.16x faster                                                           |
| float                      | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                           |
| sqlglot_parse              | 848 us                                                 | 748 us: 1.13x faster                                                            |
| spectral_norm              | 76.4 ms                                                | 67.6 ms: 1.13x faster                                                           |
| regex_compile              | 77.9 ms                                                | 69.1 ms: 1.13x faster                                                           |
| django_template            | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                           |
| sqlglot_transpile          | 1.02 ms                                                | 908 us: 1.12x faster                                                            |
| bench_thread_pool          | 504 us                                                 | 453 us: 1.11x faster                                                            |
| mako                       | 7.71 ms                                                | 6.98 ms: 1.11x faster                                                           |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.84 ms: 1.10x faster                                                           |
| hexiom                     | 4.54 ms                                                | 4.12 ms: 1.10x faster                                                           |
| dulwich_log                | 29.8 ms                                                | 27.2 ms: 1.10x faster                                                           |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                          |
| sympy_str                  | 148 ms                                                 | 135 ms: 1.09x faster                                                            |
| sympy_sum                  | 77.6 ms                                                | 71.6 ms: 1.08x faster                                                           |
| sqlglot_normalize          | 186 ms                                                 | 171 ms: 1.08x faster                                                            |
| pickle_pure_python         | 200 us                                                 | 185 us: 1.08x faster                                                            |
| sympy_integrate            | 11.4 ms                                                | 10.5 ms: 1.08x faster                                                           |
| scimark_lu                 | 76.0 ms                                                | 70.5 ms: 1.08x faster                                                           |
| sqlglot_optimize           | 34.0 ms                                                | 31.6 ms: 1.08x faster                                                           |
| async_generators           | 304 ms                                                 | 283 ms: 1.07x faster                                                            |
| pycparser                  | 677 ms                                                 | 641 ms: 1.06x faster                                                            |
| sympy_expand               | 241 ms                                                 | 230 ms: 1.05x faster                                                            |
| xml_etree_process          | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                           |
| pprint_pformat             | 1.01 sec                                               | 967 ms: 1.05x faster                                                            |
| pprint_safe_repr           | 497 ms                                                 | 475 ms: 1.05x faster                                                            |
| scimark_fft                | 195 ms                                                 | 187 ms: 1.05x faster                                                            |
| tornado_http               | 69.3 ms                                                | 66.3 ms: 1.04x faster                                                           |
| scimark_monte_carlo        | 45.0 ms                                                | 43.2 ms: 1.04x faster                                                           |
| unpickle_pure_python       | 151 us                                                 | 145 us: 1.04x faster                                                            |
| 2to3                       | 169 ms                                                 | 163 ms: 1.04x faster                                                            |
| xml_etree_generate         | 55.8 ms                                                | 53.7 ms: 1.04x faster                                                           |
| richards_super             | 36.0 ms                                                | 34.8 ms: 1.03x faster                                                           |
| regex_dna                  | 154 ms                                                 | 150 ms: 1.03x faster                                                            |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                           |
| go                         | 102 ms                                                 | 98.8 ms: 1.03x faster                                                           |
| json                       | 3.09 ms                                                | 3.01 ms: 1.03x faster                                                           |
| richards                   | 32.1 ms                                                | 31.5 ms: 1.02x faster                                                           |
| crypto_pyaes               | 51.9 ms                                                | 51.1 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 74.0 ms                                                | 73.1 ms: 1.01x faster                                                           |
| typing_runtime_protocols   | 93.0 us                                                | 92.2 us: 1.01x faster                                                           |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                            |
| regex_effbot               | 2.64 ms                                                | 2.64 ms: 1.00x faster                                                           |
| json_loads                 | 17.2 us                                                | 17.4 us: 1.01x slower                                                           |
| meteor_contest             | 71.7 ms                                                | 72.8 ms: 1.01x slower                                                           |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.02x slower                                                            |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                          |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                           |
| pyflate                    | 316 ms                                                 | 324 ms: 1.03x slower                                                            |
| json_dumps                 | 6.22 ms                                                | 6.45 ms: 1.04x slower                                                           |
| fannkuch                   | 248 ms                                                 | 267 ms: 1.08x slower                                                            |
| tomli_loads                | 1.39 sec                                               | 1.50 sec: 1.08x slower                                                          |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                           |
| bench_mp_pool              | 44.9 ms                                                | 49.0 ms: 1.09x slower                                                           |
| scimark_sor                | 87.4 ms                                                | 97.4 ms: 1.12x slower                                                           |
| coverage                   | 38.9 ms                                                | 45.6 ms: 1.17x slower                                                           |
| create_gc_cycles           | 701 us                                                 | 906 us: 1.29x slower                                                            |
| telco                      | 3.68 ms                                                | 4.79 ms: 1.30x slower                                                           |
| python_startup             | 11.4 ms                                                | 15.5 ms: 1.36x slower                                                           |
| python_startup_no_site     | 9.37 ms                                                | 12.8 ms: 1.37x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): asyncio_tcp, dask, docutils, pidigits
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.80x