# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| docutils       | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                |
| tornado_http   | 69.3 ms                                                | 66.9 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 176 ms: 1.47x faster                                                  |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 232 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.31x faster                                                  |
| async_tree_io              | 668 ms                                                 | 534 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 454 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 60.6 ms: 1.14x faster                                                 |
| float          | 55.8 ms                                                | 50.1 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.5 ms: 1.14x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 181 us: 1.10x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 53.8 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 72.2 ms: 1.02x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.40 ms: 1.03x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.7 ms: 1.36x slower                                                 |
| python_startup         | 11.4 ms                                                | 15.6 ms: 1.37x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                 |
| mako            | 7.71 ms                                                | 7.14 ms: 1.08x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.0 us: 1.62x faster                                                 |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 176 ms: 1.47x faster                                                  |
| raytrace                   | 212 ms                                                 | 151 ms: 1.41x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| generators                 | 31.1 ms                                                | 22.8 ms: 1.36x faster                                                 |
| comprehensions             | 14.5 us                                                | 10.7 us: 1.36x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 232 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.31x faster                                                  |
| logging_silent             | 76.4 ns                                                | 59.4 ns: 1.29x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.11 ms: 1.28x faster                                                 |
| async_tree_io              | 668 ms                                                 | 534 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                                 |
| chaos                      | 42.5 ms                                                | 36.1 ms: 1.18x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.39 us: 1.18x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 454 ms: 1.16x faster                                                  |
| nqueens                    | 62.4 ms                                                | 54.2 ms: 1.15x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 746 us: 1.14x faster                                                  |
| nbody                      | 68.8 ms                                                | 60.6 ms: 1.14x faster                                                 |
| regex_compile              | 77.9 ms                                                | 68.5 ms: 1.14x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 906 us: 1.13x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 68.0 ms: 1.12x faster                                                 |
| django_template            | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.08 ms: 1.11x faster                                                 |
| float                      | 55.8 ms                                                | 50.1 ms: 1.11x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.42 sec: 1.11x faster                                                |
| bench_thread_pool          | 504 us                                                 | 455 us: 1.11x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 181 us: 1.10x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 169 ms: 1.10x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 70.6 ms: 1.10x faster                                                 |
| sympy_str                  | 148 ms                                                 | 135 ms: 1.09x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 412 ms: 1.09x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.5 ms: 1.09x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 31.5 ms: 1.08x faster                                                 |
| mako                       | 7.71 ms                                                | 7.14 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.91 ms: 1.08x faster                                                 |
| async_generators           | 304 ms                                                 | 283 ms: 1.08x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 70.8 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 465 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 948 ms: 1.07x faster                                                  |
| pycparser                  | 677 ms                                                 | 639 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                  |
| 2to3                       | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                 |
| sympy_expand               | 241 ms                                                 | 231 ms: 1.04x faster                                                  |
| json                       | 3.09 ms                                                | 2.97 ms: 1.04x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 53.8 ms: 1.04x faster                                                 |
| tornado_http               | 69.3 ms                                                | 66.9 ms: 1.04x faster                                                 |
| scimark_fft                | 195 ms                                                 | 189 ms: 1.03x faster                                                  |
| richards_super             | 36.0 ms                                                | 34.8 ms: 1.03x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.7 ms: 1.03x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.5 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 72.2 ms: 1.02x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| richards                   | 32.1 ms                                                | 31.6 ms: 1.02x faster                                                 |
| go                         | 102 ms                                                 | 100 ms: 1.02x faster                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 91.9 us: 1.01x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 71.2 ms: 1.01x faster                                                 |
| pyflate                    | 316 ms                                                 | 322 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.40 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.03x slower                                                |
| fannkuch                   | 248 ms                                                 | 261 ms: 1.05x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                |
| bench_mp_pool              | 44.9 ms                                                | 48.4 ms: 1.08x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 96.3 ms: 1.10x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.3 ms: 1.16x slower                                                 |
| telco                      | 3.68 ms                                                | 4.62 ms: 1.26x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 900 us: 1.28x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 12.7 ms: 1.36x slower                                                 |
| python_startup             | 11.4 ms                                                | 15.6 ms: 1.37x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (5): dask, json_loads, asyncio_websockets, pidigits, xml_etree_parse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.07x