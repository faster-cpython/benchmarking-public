# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: darwin-arm64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 172 ms: 1.01x slower                                                   |
| chameleon      | 4.70 ms                                                | 4.41 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 238 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                   |
| async_tree_none            | 266 ms                                                 | 209 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 550 ms: 1.22x faster                                                   |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.21x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 259 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 466 ms: 1.13x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.4 ms: 1.18x faster                                                  |
| nbody          | 68.8 ms                                                | 63.6 ms: 1.08x faster                                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 72.7 ms: 1.07x faster                                                  |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 173 us: 1.15x faster                                                   |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 35.9 ms: 1.11x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 51.4 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 70.3 ms: 1.05x faster                                                  |
| unpickle_list        | 3.02 us                                                | 2.88 us: 1.05x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.05x faster                                                   |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| json_dumps           | 6.22 ms                                                | 6.11 ms: 1.02x faster                                                  |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                  |
| pickle               | 7.23 us                                                | 7.49 us: 1.04x slower                                                  |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.7 ms: 1.35x slower                                                  |
| python_startup         | 11.4 ms                                                | 15.6 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.37 ms: 1.21x faster                                                  |
| django_template | 22.3 ms                                                | 21.3 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 238 ms: 1.35x faster                                                   |
| generators                 | 31.1 ms                                                | 23.0 ms: 1.35x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                   |
| raytrace                   | 212 ms                                                 | 164 ms: 1.29x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 21.7 us: 1.28x faster                                                  |
| async_tree_none            | 266 ms                                                 | 209 ms: 1.27x faster                                                   |
| logging_silent             | 76.4 ns                                                | 62.2 ns: 1.23x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 550 ms: 1.22x faster                                                   |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.21x faster                                                   |
| mako                       | 7.71 ms                                                | 6.37 ms: 1.21x faster                                                  |
| coroutines                 | 19.2 ms                                                | 15.9 ms: 1.21x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 259 ms: 1.21x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.07 us: 1.20x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.2 us: 1.19x faster                                                  |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                   |
| float                      | 55.8 ms                                                | 47.4 ms: 1.18x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 173 us: 1.15x faster                                                   |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.82 us: 1.14x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 67.1 ms: 1.14x faster                                                  |
| deepcopy                   | 235 us                                                 | 207 us: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 466 ms: 1.13x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 35.9 ms: 1.11x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                 |
| nqueens                    | 62.4 ms                                                | 56.8 ms: 1.10x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.48 ms: 1.09x faster                                                  |
| chaos                      | 42.5 ms                                                | 39.1 ms: 1.09x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 51.4 ms: 1.09x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 459 ms: 1.08x faster                                                   |
| nbody                      | 68.8 ms                                                | 63.6 ms: 1.08x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 71.9 ms: 1.08x faster                                                  |
| sympy_str                  | 148 ms                                                 | 137 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.92 ms: 1.07x faster                                                  |
| regex_compile              | 77.9 ms                                                | 72.7 ms: 1.07x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.7 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 947 ms: 1.07x faster                                                   |
| chameleon                  | 4.70 ms                                                | 4.41 ms: 1.07x faster                                                  |
| fannkuch                   | 248 ms                                                 | 235 ms: 1.06x faster                                                   |
| bench_thread_pool          | 504 us                                                 | 478 us: 1.06x faster                                                   |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 70.3 ms: 1.05x faster                                                  |
| scimark_fft                | 195 ms                                                 | 186 ms: 1.05x faster                                                   |
| unpickle_list              | 3.02 us                                                | 2.88 us: 1.05x faster                                                  |
| django_template            | 22.3 ms                                                | 21.3 ms: 1.05x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 102 ms: 1.05x faster                                                   |
| sympy_integrate            | 11.4 ms                                                | 10.9 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 32.7 ms: 1.04x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.37 ms: 1.04x faster                                                  |
| aiohttp                    | 1.08 ms                                                | 1.04 ms: 1.04x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| gunicorn                   | 1.15 ms                                                | 1.11 ms: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                  |
| async_generators           | 304 ms                                                 | 296 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 44.0 ms: 1.02x faster                                                  |
| richards_super             | 36.0 ms                                                | 35.2 ms: 1.02x faster                                                  |
| sympy_expand               | 241 ms                                                 | 236 ms: 1.02x faster                                                   |
| sqlglot_parse              | 848 us                                                 | 831 us: 1.02x faster                                                   |
| richards                   | 32.1 ms                                                | 31.5 ms: 1.02x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| json_dumps                 | 6.22 ms                                                | 6.11 ms: 1.02x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.02x faster                                                  |
| pycparser                  | 677 ms                                                 | 672 ms: 1.01x faster                                                   |
| pyflate                    | 316 ms                                                 | 314 ms: 1.00x faster                                                   |
| meteor_contest             | 71.7 ms                                                | 71.5 ms: 1.00x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                   |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                                   |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                  |
| 2to3                       | 169 ms                                                 | 172 ms: 1.01x slower                                                   |
| go                         | 102 ms                                                 | 103 ms: 1.02x slower                                                   |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                  |
| pickle                     | 7.23 us                                                | 7.49 us: 1.04x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 78.7 ms: 1.04x slower                                                  |
| pickle_list                | 2.89 us                                                | 2.99 us: 1.04x slower                                                  |
| mypy2                      | 380 ms                                                 | 404 ms: 1.06x slower                                                   |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 49.9 ms: 1.11x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 101 ms: 1.16x slower                                                   |
| coverage                   | 38.9 ms                                                | 45.1 ms: 1.16x slower                                                  |
| telco                      | 3.68 ms                                                | 4.55 ms: 1.24x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 909 us: 1.30x slower                                                   |
| python_startup_no_site     | 9.37 ms                                                | 12.7 ms: 1.35x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.6 ms: 1.37x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (9): asyncio_tcp, tornado_http, asyncio_tcp_ssl, dask, sqlite_synth, crypto_pyaes, docutils, unpickle, typing_runtime_protocols
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (14) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.70x