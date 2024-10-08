# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 172 ms: 1.01x slower                                                  |
| docutils       | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 175 ms: 1.47x faster                                                  |
| async_tree_none            | 266 ms                                                 | 193 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 233 ms: 1.34x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.33x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.31x faster                                                  |
| async_tree_io              | 668 ms                                                 | 527 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 448 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.8 ms: 1.17x faster                                                 |
| nbody          | 68.8 ms                                                | 64.2 ms: 1.07x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 73.7 ms: 1.06x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_dna      | 154 ms                                                 | 153 ms: 1.01x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 175 us: 1.14x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 133 us: 1.13x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                |
| xml_etree_process    | 39.7 ms                                                | 36.4 ms: 1.09x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 53.5 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 71.4 ms: 1.04x faster                                                 |
| json_loads           | 17.2 us                                                | 17.3 us: 1.00x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.27 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 12.8 ms: 1.36x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.51 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 21.4 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.8 us: 1.64x faster                                                 |
| deepcopy                   | 235 us                                                 | 153 us: 1.53x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 175 ms: 1.47x faster                                                  |
| async_tree_none            | 266 ms                                                 | 193 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 233 ms: 1.34x faster                                                  |
| generators                 | 31.1 ms                                                | 23.2 ms: 1.34x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.33x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.56 us: 1.33x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.31x faster                                                  |
| raytrace                   | 212 ms                                                 | 165 ms: 1.28x faster                                                  |
| async_tree_io              | 668 ms                                                 | 527 ms: 1.27x faster                                                  |
| logging_silent             | 76.4 ns                                                | 61.5 ns: 1.24x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.07 us: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 448 ms: 1.19x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                                 |
| mako                       | 7.71 ms                                                | 6.51 ms: 1.19x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.39 us: 1.18x faster                                                 |
| float                      | 55.8 ms                                                | 47.8 ms: 1.17x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.33 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 175 us: 1.14x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 133 us: 1.13x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 68.8 ms: 1.11x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                |
| asyncio_tcp                | 449 ms                                                 | 407 ms: 1.10x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                |
| xml_etree_process          | 39.7 ms                                                | 36.4 ms: 1.09x faster                                                 |
| chaos                      | 42.5 ms                                                | 39.3 ms: 1.08x faster                                                 |
| nqueens                    | 62.4 ms                                                | 57.8 ms: 1.08x faster                                                 |
| nbody                      | 68.8 ms                                                | 64.2 ms: 1.07x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 72.9 ms: 1.07x faster                                                 |
| sympy_str                  | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 476 us: 1.06x faster                                                  |
| regex_compile              | 77.9 ms                                                | 73.7 ms: 1.06x faster                                                 |
| json                       | 3.09 ms                                                | 2.93 ms: 1.06x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 176 ms: 1.05x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 53.5 ms: 1.04x faster                                                 |
| django_template            | 22.3 ms                                                | 21.4 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 71.4 ms: 1.04x faster                                                 |
| async_generators           | 304 ms                                                 | 293 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 480 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.03 ms: 1.04x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.03x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.42 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 33.2 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 988 ms: 1.02x faster                                                  |
| richards_super             | 36.0 ms                                                | 35.2 ms: 1.02x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 44.1 ms: 1.02x faster                                                 |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                  |
| richards                   | 32.1 ms                                                | 31.5 ms: 1.02x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.00 ms: 1.02x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 834 us: 1.02x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.8 ms: 1.02x faster                                                 |
| regex_dna                  | 154 ms                                                 | 153 ms: 1.01x faster                                                  |
| fannkuch                   | 248 ms                                                 | 247 ms: 1.01x faster                                                  |
| go                         | 102 ms                                                 | 101 ms: 1.00x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 409 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 71.9 ms: 1.00x slower                                                 |
| json_loads                 | 17.2 us                                                | 17.3 us: 1.00x slower                                                 |
| pyflate                    | 316 ms                                                 | 317 ms: 1.01x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 52.2 ms: 1.01x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.27 ms: 1.01x slower                                                 |
| dask                       | 222 ms                                                 | 225 ms: 1.01x slower                                                  |
| 2to3                       | 169 ms                                                 | 172 ms: 1.01x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                |
| typing_runtime_protocols   | 93.0 us                                                | 94.6 us: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.61 ms: 1.09x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 82.8 ms: 1.09x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 50.2 ms: 1.12x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 102 ms: 1.17x slower                                                  |
| coverage                   | 38.9 ms                                                | 45.7 ms: 1.18x slower                                                 |
| telco                      | 3.68 ms                                                | 4.56 ms: 1.24x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 905 us: 1.29x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 12.8 ms: 1.36x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (4): tornado_http, pycparser, sympy_expand, xml_etree_parse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.17x