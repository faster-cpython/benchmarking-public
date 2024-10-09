# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 1.50 sec                                               | 1.49 sec: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                           |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                           |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                           |
| async_tree_memoization_tg  | 323 ms                                                 | 259 ms: 1.25x faster                                           |
| async_tree_io_tg           | 669 ms                                                 | 569 ms: 1.18x faster                                           |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 457 ms: 1.17x faster                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                           |
| async_tree_io              | 668 ms                                                 | 587 ms: 1.14x faster                                           |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.3 ms: 1.20x faster                                          |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                          |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 71.6 ms: 1.09x faster                                          |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                           |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 33.7 ms: 1.18x faster                                          |
| unpickle_pure_python | 151 us                                                 | 130 us: 1.16x faster                                           |
| pickle_pure_python   | 200 us                                                 | 175 us: 1.14x faster                                           |
| xml_etree_generate   | 55.8 ms                                                | 49.1 ms: 1.14x faster                                          |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.13x faster                                         |
| json_loads           | 17.2 us                                                | 16.3 us: 1.06x faster                                          |
| xml_etree_iterparse  | 74.0 ms                                                | 71.5 ms: 1.04x faster                                          |
| json_dumps           | 6.22 ms                                                | 6.10 ms: 1.02x faster                                          |
| unpickle             | 9.12 us                                                | 9.07 us: 1.01x faster                                          |
| pickle_list          | 2.89 us                                                | 2.94 us: 1.02x slower                                          |
| pickle               | 7.23 us                                                | 7.44 us: 1.03x slower                                          |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                   |

Benchmark hidden because not significant (3): unpickle_list, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.1 ms: 1.41x slower                                          |
| python_startup_no_site | 9.37 ms                                                | 13.3 ms: 1.42x slower                                          |
| Geometric mean         | (ref)                                                  | 1.42x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.37 ms: 1.21x faster                                          |
| django_template | 22.3 ms                                                | 20.2 ms: 1.11x faster                                          |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.3 us: 1.70x faster                                          |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                           |
| deepcopy                   | 235 us                                                 | 148 us: 1.59x faster                                           |
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                           |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                          |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                           |
| generators                 | 31.1 ms                                                | 24.1 ms: 1.29x faster                                          |
| logging_silent             | 76.4 ns                                                | 60.7 ns: 1.26x faster                                          |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                           |
| async_tree_memoization_tg  | 323 ms                                                 | 259 ms: 1.25x faster                                           |
| raytrace                   | 212 ms                                                 | 171 ms: 1.24x faster                                           |
| mako                       | 7.71 ms                                                | 6.37 ms: 1.21x faster                                          |
| logging_simple             | 3.69 us                                                | 3.04 us: 1.21x faster                                          |
| float                      | 55.8 ms                                                | 46.3 ms: 1.20x faster                                          |
| logging_format             | 3.98 us                                                | 3.31 us: 1.20x faster                                          |
| scimark_lu                 | 76.0 ms                                                | 64.2 ms: 1.18x faster                                          |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                          |
| async_tree_io_tg           | 669 ms                                                 | 569 ms: 1.18x faster                                           |
| xml_etree_process          | 39.7 ms                                                | 33.7 ms: 1.18x faster                                          |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 457 ms: 1.17x faster                                           |
| comprehensions             | 14.5 us                                                | 12.5 us: 1.17x faster                                          |
| unpickle_pure_python       | 151 us                                                 | 130 us: 1.16x faster                                           |
| deltablue                  | 2.71 ms                                                | 2.36 ms: 1.15x faster                                          |
| pickle_pure_python         | 200 us                                                 | 175 us: 1.14x faster                                           |
| spectral_norm              | 76.4 ms                                                | 66.9 ms: 1.14x faster                                          |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                           |
| async_tree_io              | 668 ms                                                 | 587 ms: 1.14x faster                                           |
| xml_etree_generate         | 55.8 ms                                                | 49.1 ms: 1.14x faster                                          |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.13x faster                                         |
| pathlib                    | 24.2 ms                                                | 21.8 ms: 1.11x faster                                          |
| django_template            | 22.3 ms                                                | 20.2 ms: 1.11x faster                                          |
| nqueens                    | 62.4 ms                                                | 57.3 ms: 1.09x faster                                          |
| go                         | 102 ms                                                 | 93.4 ms: 1.09x faster                                          |
| json                       | 3.09 ms                                                | 2.84 ms: 1.09x faster                                          |
| regex_compile              | 77.9 ms                                                | 71.6 ms: 1.09x faster                                          |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                          |
| mdp                        | 1.58 sec                                               | 1.47 sec: 1.08x faster                                         |
| pprint_safe_repr           | 497 ms                                                 | 462 ms: 1.08x faster                                           |
| chaos                      | 42.5 ms                                                | 39.7 ms: 1.07x faster                                          |
| sqlglot_normalize          | 186 ms                                                 | 174 ms: 1.06x faster                                           |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                           |
| json_loads                 | 17.2 us                                                | 16.3 us: 1.06x faster                                          |
| richards_super             | 36.0 ms                                                | 34.0 ms: 1.06x faster                                          |
| bench_thread_pool          | 504 us                                                 | 478 us: 1.06x faster                                           |
| sqlglot_parse              | 848 us                                                 | 804 us: 1.05x faster                                           |
| async_generators           | 304 ms                                                 | 289 ms: 1.05x faster                                           |
| richards                   | 32.1 ms                                                | 30.6 ms: 1.05x faster                                          |
| sympy_sum                  | 77.6 ms                                                | 74.0 ms: 1.05x faster                                          |
| dulwich_log                | 29.8 ms                                                | 28.5 ms: 1.05x faster                                          |
| sympy_str                  | 148 ms                                                 | 141 ms: 1.04x faster                                           |
| pycparser                  | 677 ms                                                 | 649 ms: 1.04x faster                                           |
| sqlglot_transpile          | 1.02 ms                                                | 980 us: 1.04x faster                                           |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                           |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.03 ms: 1.04x faster                                          |
| xml_etree_iterparse        | 74.0 ms                                                | 71.5 ms: 1.04x faster                                          |
| pprint_pformat             | 1.01 sec                                               | 979 ms: 1.03x faster                                           |
| hexiom                     | 4.54 ms                                                | 4.42 ms: 1.03x faster                                          |
| sympy_expand               | 241 ms                                                 | 235 ms: 1.03x faster                                           |
| sqlite_synth               | 1.57 us                                                | 1.53 us: 1.02x faster                                          |
| json_dumps                 | 6.22 ms                                                | 6.10 ms: 1.02x faster                                          |
| docutils                   | 1.50 sec                                               | 1.49 sec: 1.01x faster                                         |
| sqlglot_optimize           | 34.0 ms                                                | 33.8 ms: 1.01x faster                                          |
| unpickle                   | 9.12 us                                                | 9.07 us: 1.01x faster                                          |
| scimark_sor                | 87.4 ms                                                | 87.0 ms: 1.00x faster                                          |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                           |
| pyflate                    | 316 ms                                                 | 317 ms: 1.00x slower                                           |
| typing_runtime_protocols   | 93.0 us                                                | 94.5 us: 1.02x slower                                          |
| pickle_list                | 2.89 us                                                | 2.94 us: 1.02x slower                                          |
| meteor_contest             | 71.7 ms                                                | 73.5 ms: 1.02x slower                                          |
| scimark_monte_carlo        | 45.0 ms                                                | 46.1 ms: 1.02x slower                                          |
| pickle                     | 7.23 us                                                | 7.44 us: 1.03x slower                                          |
| sympy_integrate            | 11.4 ms                                                | 11.7 ms: 1.03x slower                                          |
| gc_traversal               | 2.40 ms                                                | 2.48 ms: 1.03x slower                                          |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                         |
| fannkuch                   | 248 ms                                                 | 260 ms: 1.05x slower                                           |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.06x slower                                          |
| bench_mp_pool              | 44.9 ms                                                | 50.8 ms: 1.13x slower                                          |
| coverage                   | 38.9 ms                                                | 44.6 ms: 1.15x slower                                          |
| telco                      | 3.68 ms                                                | 4.55 ms: 1.24x slower                                          |
| create_gc_cycles           | 701 us                                                 | 899 us: 1.28x slower                                           |
| python_startup             | 11.4 ms                                                | 16.1 ms: 1.41x slower                                          |
| python_startup_no_site     | 9.37 ms                                                | 13.3 ms: 1.42x slower                                          |
| unpack_sequence            | 31.5 ns                                                | 74.9 ns: 2.38x slower                                          |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                   |

Benchmark hidden because not significant (8): asyncio_tcp, 2to3, regex_effbot, unpickle_list, crypto_pyaes, pickle_dict, xml_etree_parse, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.60x