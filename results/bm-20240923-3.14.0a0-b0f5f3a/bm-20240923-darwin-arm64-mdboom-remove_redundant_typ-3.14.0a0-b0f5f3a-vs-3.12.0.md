# Results vs. 3.12.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: darwin-arm64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 162 ms: 1.05x faster                                                  |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                |
| tornado_http   | 69.3 ms                                                | 85.8 ms: 1.24x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                                  |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 548 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.15x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.5 ms: 1.15x faster                                                 |
| nbody          | 68.8 ms                                                | 60.0 ms: 1.15x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.0 ms: 1.16x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 180 us: 1.11x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 140 us: 1.07x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 52.9 ms: 1.06x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.90 us: 1.04x faster                                                 |
| json_loads           | 17.2 us                                                | 16.8 us: 1.02x faster                                                 |
| unpickle             | 9.12 us                                                | 9.07 us: 1.01x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.00x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.30 ms: 1.01x slower                                                 |
| pickle               | 7.23 us                                                | 7.34 us: 1.02x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                                  |
| pickle_list          | 2.89 us                                                | 2.96 us: 1.03x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.1 ms: 1.40x slower                                                 |
| python_startup         | 11.4 ms                                                | 16.0 ms: 1.40x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.40x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.0 ms: 1.11x faster                                                 |
| mako            | 7.71 ms                                                | 7.12 ms: 1.08x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.6 us: 1.67x faster                                                 |
| deepcopy                   | 235 us                                                 | 144 us: 1.63x faster                                                  |
| generators                 | 31.1 ms                                                | 21.1 ms: 1.47x faster                                                 |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                                  |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.34x faster                                                 |
| go                         | 102 ms                                                 | 79.2 ms: 1.28x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.13 ms: 1.27x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                  |
| logging_silent             | 76.4 ns                                                | 60.8 ns: 1.26x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.00 us: 1.23x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 548 ms: 1.22x faster                                                  |
| logging_format             | 3.98 us                                                | 3.28 us: 1.22x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.6 ms: 1.19x faster                                                 |
| unpack_sequence            | 31.5 ns                                                | 26.4 ns: 1.19x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 64.6 ms: 1.18x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.2 ms: 1.17x faster                                                 |
| regex_compile              | 77.9 ms                                                | 67.0 ms: 1.16x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.70 ms: 1.16x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 66.0 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 736 us: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.5 ms: 1.15x faster                                                 |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                  |
| nbody                      | 68.8 ms                                                | 60.0 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.15x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 898 us: 1.14x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 68.7 ms: 1.13x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 448 us: 1.13x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.04 ms: 1.12x faster                                                 |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| django_template            | 22.3 ms                                                | 20.0 ms: 1.11x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 180 us: 1.11x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.11x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                |
| sqlglot_optimize           | 34.0 ms                                                | 31.1 ms: 1.10x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 27.3 ms: 1.09x faster                                                 |
| scimark_fft                | 195 ms                                                 | 179 ms: 1.09x faster                                                  |
| async_generators           | 304 ms                                                 | 278 ms: 1.09x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 457 ms: 1.09x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 930 ms: 1.09x faster                                                  |
| mako                       | 7.71 ms                                                | 7.12 ms: 1.08x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 416 ms: 1.08x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 140 us: 1.07x faster                                                  |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                                  |
| pycparser                  | 677 ms                                                 | 637 ms: 1.06x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 42.4 ms: 1.06x faster                                                 |
| json                       | 3.09 ms                                                | 2.91 ms: 1.06x faster                                                 |
| sympy_expand               | 241 ms                                                 | 227 ms: 1.06x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 52.9 ms: 1.06x faster                                                 |
| 2to3                       | 169 ms                                                 | 162 ms: 1.05x faster                                                  |
| unpickle_list              | 3.02 us                                                | 2.90 us: 1.04x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.0 ms: 1.04x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.8 us: 1.02x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 71.3 ms: 1.01x faster                                                 |
| unpickle                   | 9.12 us                                                | 9.07 us: 1.01x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_dict                | 18.1 us                                                | 18.1 us: 1.00x slower                                                 |
| richards_super             | 36.0 ms                                                | 36.2 ms: 1.01x slower                                                 |
| richards                   | 32.1 ms                                                | 32.4 ms: 1.01x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.30 ms: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 320 ms: 1.01x slower                                                  |
| pickle                     | 7.23 us                                                | 7.34 us: 1.02x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.02x slower                                                  |
| pickle_list                | 2.89 us                                                | 2.96 us: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| fannkuch                   | 248 ms                                                 | 261 ms: 1.05x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                |
| scimark_sor                | 87.4 ms                                                | 92.7 ms: 1.06x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 48.0 ms: 1.07x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.4 ms: 1.14x slower                                                 |
| tornado_http               | 69.3 ms                                                | 85.8 ms: 1.24x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 892 us: 1.27x slower                                                  |
| telco                      | 3.68 ms                                                | 4.81 ms: 1.31x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.1 ms: 1.40x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.0 ms: 1.40x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.092x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.70x