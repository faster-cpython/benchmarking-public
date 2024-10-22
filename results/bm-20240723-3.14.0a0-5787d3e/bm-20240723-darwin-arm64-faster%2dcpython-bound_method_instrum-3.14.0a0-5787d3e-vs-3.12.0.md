# Results vs. 3.12.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: darwin-arm64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 162 ms: 1.05x faster                                                            |
| docutils       | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                          |
| tornado_http   | 69.3 ms                                                | 65.1 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 173 ms: 1.49x faster                                                            |
| async_tree_io_tg           | 669 ms                                                 | 496 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 239 ms: 1.35x faster                                                            |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                            |
| async_tree_memoization     | 312 ms                                                 | 235 ms: 1.33x faster                                                            |
| async_tree_io              | 668 ms                                                 | 530 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 444 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 456 ms: 1.15x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.3 ms: 1.15x faster                                                           |
| nbody          | 68.8 ms                                                | 62.2 ms: 1.11x faster                                                           |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.0 ms: 1.14x faster                                                           |
| regex_effbot   | 2.64 ms                                                | 2.54 ms: 1.04x faster                                                           |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                            |
| regex_v8       | 16.0 ms                                                | 17.7 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                                            |
| xml_etree_generate   | 55.8 ms                                                | 52.3 ms: 1.07x faster                                                           |
| xml_etree_process    | 39.7 ms                                                | 37.2 ms: 1.06x faster                                                           |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                            |
| xml_etree_iterparse  | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                           |
| json_loads           | 17.2 us                                                | 17.0 us: 1.02x faster                                                           |
| json_dumps           | 6.22 ms                                                | 6.41 ms: 1.03x slower                                                           |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.3 ms: 1.31x slower                                                           |
| python_startup         | 11.4 ms                                                | 14.9 ms: 1.31x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                           |
| mako            | 7.71 ms                                                | 6.93 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.7 us: 1.66x faster                                                           |
| deepcopy                   | 235 us                                                 | 146 us: 1.60x faster                                                            |
| generators                 | 31.1 ms                                                | 20.7 ms: 1.50x faster                                                           |
| async_tree_none_tg         | 258 ms                                                 | 173 ms: 1.49x faster                                                            |
| raytrace                   | 212 ms                                                 | 146 ms: 1.45x faster                                                            |
| deepcopy_reduce            | 2.07 us                                                | 1.49 us: 1.39x faster                                                           |
| async_tree_io_tg           | 669 ms                                                 | 496 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 239 ms: 1.35x faster                                                            |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                            |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.34x faster                                                           |
| async_tree_memoization     | 312 ms                                                 | 235 ms: 1.33x faster                                                            |
| deltablue                  | 2.71 ms                                                | 2.09 ms: 1.29x faster                                                           |
| logging_silent             | 76.4 ns                                                | 59.3 ns: 1.29x faster                                                           |
| async_tree_io              | 668 ms                                                 | 530 ms: 1.26x faster                                                            |
| chaos                      | 42.5 ms                                                | 34.8 ms: 1.22x faster                                                           |
| logging_simple             | 3.69 us                                                | 3.03 us: 1.22x faster                                                           |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 444 ms: 1.20x faster                                                            |
| logging_format             | 3.98 us                                                | 3.33 us: 1.20x faster                                                           |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                           |
| nqueens                    | 62.4 ms                                                | 53.8 ms: 1.16x faster                                                           |
| spectral_norm              | 76.4 ms                                                | 66.0 ms: 1.16x faster                                                           |
| float                      | 55.8 ms                                                | 48.3 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 456 ms: 1.15x faster                                                            |
| sqlglot_parse              | 848 us                                                 | 741 us: 1.14x faster                                                            |
| regex_compile              | 77.9 ms                                                | 68.0 ms: 1.14x faster                                                           |
| sqlglot_transpile          | 1.02 ms                                                | 902 us: 1.13x faster                                                            |
| django_template            | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                           |
| mdp                        | 1.58 sec                                               | 1.41 sec: 1.12x faster                                                          |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.80 ms: 1.12x faster                                                           |
| bench_thread_pool          | 504 us                                                 | 453 us: 1.11x faster                                                            |
| mako                       | 7.71 ms                                                | 6.93 ms: 1.11x faster                                                           |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                                            |
| sympy_sum                  | 77.6 ms                                                | 70.0 ms: 1.11x faster                                                           |
| sympy_str                  | 148 ms                                                 | 133 ms: 1.11x faster                                                            |
| nbody                      | 68.8 ms                                                | 62.2 ms: 1.11x faster                                                           |
| hexiom                     | 4.54 ms                                                | 4.11 ms: 1.11x faster                                                           |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                                            |
| scimark_lu                 | 76.0 ms                                                | 69.3 ms: 1.10x faster                                                           |
| sympy_integrate            | 11.4 ms                                                | 10.4 ms: 1.09x faster                                                           |
| sqlglot_optimize           | 34.0 ms                                                | 31.2 ms: 1.09x faster                                                           |
| async_generators           | 304 ms                                                 | 280 ms: 1.09x faster                                                            |
| pprint_safe_repr           | 497 ms                                                 | 464 ms: 1.07x faster                                                            |
| scimark_fft                | 195 ms                                                 | 183 ms: 1.07x faster                                                            |
| xml_etree_generate         | 55.8 ms                                                | 52.3 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.01 sec                                               | 948 ms: 1.07x faster                                                            |
| tornado_http               | 69.3 ms                                                | 65.1 ms: 1.07x faster                                                           |
| xml_etree_process          | 39.7 ms                                                | 37.2 ms: 1.06x faster                                                           |
| pathlib                    | 24.2 ms                                                | 22.9 ms: 1.06x faster                                                           |
| pycparser                  | 677 ms                                                 | 639 ms: 1.06x faster                                                            |
| scimark_monte_carlo        | 45.0 ms                                                | 42.7 ms: 1.06x faster                                                           |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                            |
| richards_super             | 36.0 ms                                                | 34.3 ms: 1.05x faster                                                           |
| sympy_expand               | 241 ms                                                 | 230 ms: 1.05x faster                                                            |
| json                       | 3.09 ms                                                | 2.95 ms: 1.05x faster                                                           |
| 2to3                       | 169 ms                                                 | 162 ms: 1.05x faster                                                            |
| regex_effbot               | 2.64 ms                                                | 2.54 ms: 1.04x faster                                                           |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                            |
| richards                   | 32.1 ms                                                | 31.2 ms: 1.03x faster                                                           |
| crypto_pyaes               | 51.9 ms                                                | 50.5 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                           |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.02x faster                                                           |
| docutils                   | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                          |
| meteor_contest             | 71.7 ms                                                | 71.5 ms: 1.00x faster                                                           |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                            |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                          |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                           |
| pyflate                    | 316 ms                                                 | 324 ms: 1.03x slower                                                            |
| go                         | 102 ms                                                 | 104 ms: 1.03x slower                                                            |
| json_dumps                 | 6.22 ms                                                | 6.41 ms: 1.03x slower                                                           |
| bench_mp_pool              | 44.9 ms                                                | 46.9 ms: 1.05x slower                                                           |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                          |
| fannkuch                   | 248 ms                                                 | 267 ms: 1.07x slower                                                            |
| scimark_sor                | 87.4 ms                                                | 96.1 ms: 1.10x slower                                                           |
| regex_v8                   | 16.0 ms                                                | 17.7 ms: 1.11x slower                                                           |
| coverage                   | 38.9 ms                                                | 44.7 ms: 1.15x slower                                                           |
| telco                      | 3.68 ms                                                | 4.61 ms: 1.25x slower                                                           |
| create_gc_cycles           | 701 us                                                 | 893 us: 1.27x slower                                                            |
| python_startup_no_site     | 9.37 ms                                                | 12.3 ms: 1.31x slower                                                           |
| python_startup             | 11.4 ms                                                | 14.9 ms: 1.31x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (4): asyncio_tcp, dask, typing_runtime_protocols, xml_etree_parse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.61x