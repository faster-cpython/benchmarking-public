# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: darwin-arm64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 172 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.29x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 549 ms: 1.22x faster                                                  |
| async_tree_none            | 266 ms                                                 | 219 ms: 1.21x faster                                                  |
| async_tree_io              | 668 ms                                                 | 573 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 271 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 480 ms: 1.10x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.5 ms: 1.20x faster                                                 |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 71.5 ms: 1.09x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 173 us: 1.16x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                |
| xml_etree_process    | 39.7 ms                                                | 36.1 ms: 1.10x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 52.1 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 70.6 ms: 1.05x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.90 us: 1.04x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.02x faster                                                  |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                | 9.28 us: 1.02x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.40 ms: 1.03x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.97 us: 1.03x slower                                                 |
| pickle               | 7.23 us                                                | 7.50 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.3 ms: 1.21x slower                                                 |
| python_startup         | 11.4 ms                                                | 14.2 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.23x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.46 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 21.6 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.9 us: 1.64x faster                                                 |
| deepcopy                   | 235 us                                                 | 151 us: 1.55x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.34x faster                                                 |
| generators                 | 31.1 ms                                                | 23.3 ms: 1.34x faster                                                 |
| raytrace                   | 212 ms                                                 | 162 ms: 1.31x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.29x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.01 us: 1.22x faster                                                 |
| logging_silent             | 76.4 ns                                                | 62.6 ns: 1.22x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 549 ms: 1.22x faster                                                  |
| async_tree_none            | 266 ms                                                 | 219 ms: 1.21x faster                                                  |
| logging_format             | 3.98 us                                                | 3.31 us: 1.20x faster                                                 |
| float                      | 55.8 ms                                                | 46.5 ms: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                                 |
| mako                       | 7.71 ms                                                | 6.46 ms: 1.19x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.4 us: 1.17x faster                                                 |
| async_tree_io              | 668 ms                                                 | 573 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 173 us: 1.16x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 271 ms: 1.15x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.35 ms: 1.15x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.0 ms: 1.14x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                |
| xml_etree_process          | 39.7 ms                                                | 36.1 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 480 ms: 1.10x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                |
| regex_compile              | 77.9 ms                                                | 71.5 ms: 1.09x faster                                                 |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                 |
| chaos                      | 42.5 ms                                                | 39.4 ms: 1.08x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 52.1 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.93 ms: 1.07x faster                                                 |
| nqueens                    | 62.4 ms                                                | 58.5 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 467 ms: 1.06x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 475 us: 1.06x faster                                                  |
| sympy_str                  | 148 ms                                                 | 140 ms: 1.05x faster                                                  |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                                 |
| scimark_fft                | 195 ms                                                 | 186 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 962 ms: 1.05x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 74.0 ms: 1.05x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 177 ms: 1.05x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 70.6 ms: 1.05x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.34 ms: 1.05x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.2 ms: 1.04x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.90 us: 1.04x faster                                                 |
| django_template            | 22.3 ms                                                | 21.6 ms: 1.03x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| async_generators           | 304 ms                                                 | 294 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 33.0 ms: 1.03x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.1 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.9 ms: 1.03x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 827 us: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                 |
| richards                   | 32.1 ms                                                | 31.6 ms: 1.02x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.02x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 105 ms: 1.02x faster                                                  |
| richards_super             | 36.0 ms                                                | 35.5 ms: 1.02x faster                                                 |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                                  |
| fannkuch                   | 248 ms                                                 | 246 ms: 1.01x faster                                                  |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                                 |
| pycparser                  | 677 ms                                                 | 671 ms: 1.01x faster                                                  |
| pyflate                    | 316 ms                                                 | 314 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 52.2 ms: 1.01x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| 2to3                       | 169 ms                                                 | 172 ms: 1.01x slower                                                  |
| unpickle                   | 9.12 us                                                | 9.28 us: 1.02x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 95.0 us: 1.02x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.40 ms: 1.03x slower                                                 |
| pickle_list                | 2.89 us                                                | 2.97 us: 1.03x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.48 ms: 1.03x slower                                                 |
| pickle                     | 7.23 us                                                | 7.50 us: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.04x slower                                                |
| scimark_lu                 | 76.0 ms                                                | 80.5 ms: 1.06x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 49.2 ms: 1.10x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.3 ms: 1.17x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 103 ms: 1.18x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 11.3 ms: 1.21x slower                                                 |
| telco                      | 3.68 ms                                                | 4.58 ms: 1.24x slower                                                 |
| python_startup             | 11.4 ms                                                | 14.2 ms: 1.25x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 906 us: 1.29x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (8): tornado_http, meteor_contest, sympy_expand, sqlite_synth, asyncio_websockets, docutils, asyncio_tcp, dask
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (14) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.27x