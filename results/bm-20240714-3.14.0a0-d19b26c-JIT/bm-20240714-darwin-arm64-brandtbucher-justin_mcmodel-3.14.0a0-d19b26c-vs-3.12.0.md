# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: darwin-arm64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 172 ms: 1.02x slower                                                  |
| docutils       | 1.50 sec                                               | 1.51 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 176 ms: 1.46x faster                                                  |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 232 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 514 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 516 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.4 ms: 1.18x faster                                                 |
| nbody          | 68.8 ms                                                | 64.1 ms: 1.07x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 72.9 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.57 ms: 1.03x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 174 us: 1.15x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.28 sec: 1.09x faster                                                |
| xml_etree_process    | 39.7 ms                                                | 36.6 ms: 1.08x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 52.5 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 70.7 ms: 1.05x faster                                                 |
| json_loads           | 17.2 us                                                | 17.4 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 107 ms: 1.01x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.41 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 12.7 ms: 1.36x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.53 ms: 1.18x faster                                                 |
| django_template | 22.3 ms                                                | 22.2 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.8 us: 1.64x faster                                                 |
| deepcopy                   | 235 us                                                 | 152 us: 1.55x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 176 ms: 1.46x faster                                                  |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 232 ms: 1.35x faster                                                  |
| generators                 | 31.1 ms                                                | 23.2 ms: 1.34x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.34x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 514 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 516 ms: 1.29x faster                                                  |
| raytrace                   | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| logging_silent             | 76.4 ns                                                | 61.9 ns: 1.23x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.03 us: 1.22x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                                  |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                 |
| mako                       | 7.71 ms                                                | 6.53 ms: 1.18x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.18x faster                                                 |
| float                      | 55.8 ms                                                | 47.4 ms: 1.18x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.32 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 174 us: 1.15x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 68.6 ms: 1.11x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.28 sec: 1.09x faster                                                |
| xml_etree_process          | 39.7 ms                                                | 36.6 ms: 1.08x faster                                                 |
| nqueens                    | 62.4 ms                                                | 57.6 ms: 1.08x faster                                                 |
| chaos                      | 42.5 ms                                                | 39.4 ms: 1.08x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.47 sec: 1.08x faster                                                |
| nbody                      | 68.8 ms                                                | 64.1 ms: 1.07x faster                                                 |
| sympy_str                  | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| regex_compile              | 77.9 ms                                                | 72.9 ms: 1.07x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 52.5 ms: 1.06x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 73.0 ms: 1.06x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 475 us: 1.06x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 70.7 ms: 1.05x faster                                                 |
| richards                   | 32.1 ms                                                | 30.7 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                 |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 178 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.02 ms: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.03x faster                                                 |
| async_generators           | 304 ms                                                 | 294 ms: 1.03x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.40 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 33.1 ms: 1.03x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 994 us: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.57 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.9 ms: 1.03x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 827 us: 1.03x faster                                                  |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 488 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 998 ms: 1.01x faster                                                  |
| django_template            | 22.3 ms                                                | 22.2 ms: 1.01x faster                                                 |
| sympy_expand               | 241 ms                                                 | 240 ms: 1.00x faster                                                  |
| go                         | 102 ms                                                 | 101 ms: 1.00x faster                                                  |
| fannkuch                   | 248 ms                                                 | 248 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| pyflate                    | 316 ms                                                 | 318 ms: 1.01x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.51 sec: 1.01x slower                                                |
| json_loads                 | 17.2 us                                                | 17.4 us: 1.01x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 107 ms: 1.01x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 72.7 ms: 1.01x slower                                                 |
| 2to3                       | 169 ms                                                 | 172 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.41 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 95.9 us: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.05x slower                                                |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 82.6 ms: 1.09x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 50.3 ms: 1.12x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 102 ms: 1.17x slower                                                  |
| coverage                   | 38.9 ms                                                | 46.2 ms: 1.19x slower                                                 |
| telco                      | 3.68 ms                                                | 4.61 ms: 1.25x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 913 us: 1.30x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 12.7 ms: 1.36x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (6): asyncio_tcp, tornado_http, pycparser, asyncio_websockets, crypto_pyaes, dask
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.18x