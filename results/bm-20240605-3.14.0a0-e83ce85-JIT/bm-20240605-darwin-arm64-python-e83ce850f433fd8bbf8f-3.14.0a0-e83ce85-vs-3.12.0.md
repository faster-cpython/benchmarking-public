# Results vs. 3.12.0

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: darwin-arm64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.62x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 170 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 238 ms: 1.35x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                  |
| async_tree_none            | 266 ms                                                 | 215 ms: 1.24x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 555 ms: 1.21x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 452 ms: 1.18x faster                                                  |
| async_tree_io              | 668 ms                                                 | 571 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 473 ms: 1.11x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.7 ms: 1.17x faster                                                 |
| nbody          | 68.8 ms                                                | 64.0 ms: 1.08x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 72.4 ms: 1.08x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 172 us: 1.16x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.12x faster                                                |
| xml_etree_process    | 39.7 ms                                                | 35.6 ms: 1.11x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.85 us: 1.06x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 70.1 ms: 1.06x faster                                                 |
| json_loads           | 17.2 us                                                | 17.0 us: 1.02x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                                  |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.32 ms: 1.02x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.94 us: 1.02x slower                                                 |
| unpickle             | 9.12 us                                                | 9.30 us: 1.02x slower                                                 |
| pickle               | 7.23 us                                                | 7.45 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 12.7 ms: 1.35x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.36 ms: 1.21x faster                                                 |
| django_template | 22.3 ms                                                | 21.5 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 238 ms: 1.35x faster                                                  |
| generators                 | 31.1 ms                                                | 23.5 ms: 1.32x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 21.3 us: 1.30x faster                                                 |
| raytrace                   | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| async_tree_none            | 266 ms                                                 | 215 ms: 1.24x faster                                                  |
| coroutines                 | 19.2 ms                                                | 15.8 ms: 1.21x faster                                                 |
| mako                       | 7.71 ms                                                | 6.36 ms: 1.21x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 555 ms: 1.21x faster                                                  |
| logging_silent             | 76.4 ns                                                | 63.8 ns: 1.20x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.18x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 452 ms: 1.18x faster                                                  |
| async_tree_io              | 668 ms                                                 | 571 ms: 1.17x faster                                                  |
| float                      | 55.8 ms                                                | 47.7 ms: 1.17x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 172 us: 1.16x faster                                                  |
| logging_format             | 3.98 us                                                | 3.44 us: 1.16x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                  |
| deepcopy                   | 235 us                                                 | 206 us: 1.14x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.82 us: 1.14x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.3 ms: 1.14x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.12x faster                                                |
| xml_etree_process          | 39.7 ms                                                | 35.6 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 473 ms: 1.11x faster                                                  |
| pathlib                    | 24.2 ms                                                | 21.9 ms: 1.11x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                |
| deltablue                  | 2.71 ms                                                | 2.47 ms: 1.09x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 460 ms: 1.08x faster                                                  |
| nbody                      | 68.8 ms                                                | 64.0 ms: 1.08x faster                                                 |
| regex_compile              | 77.9 ms                                                | 72.4 ms: 1.08x faster                                                 |
| chaos                      | 42.5 ms                                                | 39.7 ms: 1.07x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 72.6 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 947 ms: 1.07x faster                                                  |
| sympy_str                  | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.95 ms: 1.06x faster                                                 |
| nqueens                    | 62.4 ms                                                | 58.9 ms: 1.06x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.85 us: 1.06x faster                                                 |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 70.1 ms: 1.06x faster                                                 |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                                 |
| async_generators           | 304 ms                                                 | 289 ms: 1.05x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 483 us: 1.04x faster                                                  |
| fannkuch                   | 248 ms                                                 | 239 ms: 1.04x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.9 ms: 1.04x faster                                                 |
| django_template            | 22.3 ms                                                | 21.5 ms: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.41 ms: 1.03x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 33.2 ms: 1.03x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 830 us: 1.02x faster                                                  |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.02x faster                                                 |
| richards                   | 32.1 ms                                                | 31.6 ms: 1.02x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 105 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 44.5 ms: 1.01x faster                                                 |
| richards_super             | 36.0 ms                                                | 35.6 ms: 1.01x faster                                                 |
| sympy_expand               | 241 ms                                                 | 239 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.23 sec: 1.01x faster                                                |
| pyflate                    | 316 ms                                                 | 314 ms: 1.01x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.56 us: 1.00x faster                                                 |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| 2to3                       | 169 ms                                                 | 170 ms: 1.00x slower                                                  |
| go                         | 102 ms                                                 | 102 ms: 1.01x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 72.5 ms: 1.01x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.32 ms: 1.02x slower                                                 |
| pickle_list                | 2.89 us                                                | 2.94 us: 1.02x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.30 us: 1.02x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 95.3 us: 1.02x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                                 |
| pickle                     | 7.23 us                                                | 7.45 us: 1.03x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 79.1 ms: 1.04x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 49.4 ms: 1.10x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 102 ms: 1.16x slower                                                  |
| coverage                   | 38.9 ms                                                | 45.6 ms: 1.17x slower                                                 |
| telco                      | 3.68 ms                                                | 4.47 ms: 1.22x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 914 us: 1.30x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 12.7 ms: 1.35x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (7): tornado_http, crypto_pyaes, docutils, asyncio_websockets, dask, pycparser, asyncio_tcp
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (13) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.62x