# Results vs. 3.12.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: darwin-arm64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 171 ms: 1.01x slower                                                  |
| docutils       | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 176 ms: 1.47x faster                                                  |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 232 ms: 1.34x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 513 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 519 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.2 ms: 1.18x faster                                                 |
| nbody          | 68.8 ms                                                | 64.1 ms: 1.07x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 73.5 ms: 1.06x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                 |
| regex_dna      | 154 ms                                                 | 150 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 175 us: 1.15x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                |
| xml_etree_process    | 39.7 ms                                                | 36.5 ms: 1.09x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 52.5 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 71.3 ms: 1.04x faster                                                 |
| json_loads           | 17.2 us                                                | 17.3 us: 1.00x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.39 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.3 ms: 1.34x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 12.7 ms: 1.35x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.50 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 21.8 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.8 us: 1.64x faster                                                 |
| deepcopy                   | 235 us                                                 | 152 us: 1.55x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 176 ms: 1.47x faster                                                  |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 232 ms: 1.34x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                  |
| generators                 | 31.1 ms                                                | 23.2 ms: 1.34x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.56 us: 1.33x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 513 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 519 ms: 1.29x faster                                                  |
| raytrace                   | 212 ms                                                 | 166 ms: 1.28x faster                                                  |
| logging_silent             | 76.4 ns                                                | 61.7 ns: 1.24x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.04 us: 1.21x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                                 |
| mako                       | 7.71 ms                                                | 6.50 ms: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.37 us: 1.18x faster                                                 |
| float                      | 55.8 ms                                                | 47.2 ms: 1.18x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.4 us: 1.18x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.33 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 175 us: 1.15x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 398 ms: 1.13x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                |
| spectral_norm              | 76.4 ms                                                | 68.7 ms: 1.11x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                |
| xml_etree_process          | 39.7 ms                                                | 36.5 ms: 1.09x faster                                                 |
| chaos                      | 42.5 ms                                                | 39.3 ms: 1.08x faster                                                 |
| nqueens                    | 62.4 ms                                                | 57.9 ms: 1.08x faster                                                 |
| nbody                      | 68.8 ms                                                | 64.1 ms: 1.07x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 52.5 ms: 1.06x faster                                                 |
| regex_compile              | 77.9 ms                                                | 73.5 ms: 1.06x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 476 us: 1.06x faster                                                  |
| sympy_str                  | 148 ms                                                 | 140 ms: 1.06x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 73.7 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                                 |
| richards_super             | 36.0 ms                                                | 34.7 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 71.3 ms: 1.04x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 179 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.03 ms: 1.04x faster                                                 |
| richards                   | 32.1 ms                                                | 31.1 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 481 ms: 1.03x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.40 ms: 1.03x faster                                                 |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.03x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                 |
| regex_dna                  | 154 ms                                                 | 150 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 33.2 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.9 ms: 1.02x faster                                                 |
| django_template            | 22.3 ms                                                | 21.8 ms: 1.02x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 989 ms: 1.02x faster                                                  |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 831 us: 1.02x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.00 ms: 1.02x faster                                                 |
| fannkuch                   | 248 ms                                                 | 244 ms: 1.02x faster                                                  |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| json_loads                 | 17.2 us                                                | 17.3 us: 1.00x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 52.2 ms: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 319 ms: 1.01x slower                                                  |
| 2to3                       | 169 ms                                                 | 171 ms: 1.01x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 72.7 ms: 1.01x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.39 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 96.7 us: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.04x slower                                                |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 82.6 ms: 1.09x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 50.1 ms: 1.12x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 102 ms: 1.17x slower                                                  |
| coverage                   | 38.9 ms                                                | 45.9 ms: 1.18x slower                                                 |
| telco                      | 3.68 ms                                                | 4.64 ms: 1.26x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 913 us: 1.30x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.3 ms: 1.34x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 12.7 ms: 1.35x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (7): tornado_http, pycparser, go, asyncio_websockets, sympy_expand, xml_etree_parse, dask
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.17x