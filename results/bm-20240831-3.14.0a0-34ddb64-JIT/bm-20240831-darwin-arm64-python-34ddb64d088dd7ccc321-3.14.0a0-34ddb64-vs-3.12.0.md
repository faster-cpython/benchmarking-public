# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.04x faster
- HPT reliability: 94.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.85x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 180 ms: 1.06x slower                                                  |
| docutils       | 1.50 sec                                               | 1.61 sec: 1.07x slower                                                |
| tornado_http   | 69.3 ms                                                | 87.9 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 245 ms: 1.31x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 200 ms: 1.29x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 553 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 463 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                                  |
| async_tree_io              | 668 ms                                                 | 594 ms: 1.13x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.4 ms: 1.20x faster                                                 |
| nbody          | 68.8 ms                                                | 63.8 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.07x faster                                                  |
| regex_compile  | 77.9 ms                                                | 74.9 ms: 1.04x faster                                                 |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.6 ms: 1.15x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 133 us: 1.14x faster                                                  |
| pickle_pure_python   | 200 us                                                 | 177 us: 1.13x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 50.7 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 71.9 ms: 1.03x faster                                                 |
| json_loads           | 17.2 us                                                | 17.3 us: 1.01x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.28 ms: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 110 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.8 ms: 1.48x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 13.9 ms: 1.49x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.48x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 22.1 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.1 us: 1.72x faster                                                 |
| deepcopy                   | 235 us                                                 | 154 us: 1.52x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.49 us: 1.39x faster                                                 |
| async_tree_none            | 266 ms                                                 | 194 ms: 1.37x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 245 ms: 1.31x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 200 ms: 1.29x faster                                                  |
| generators                 | 31.1 ms                                                | 24.6 ms: 1.26x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                                  |
| logging_silent             | 76.4 ns                                                | 62.4 ns: 1.23x faster                                                 |
| raytrace                   | 212 ms                                                 | 174 ms: 1.22x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.03 us: 1.22x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 553 ms: 1.21x faster                                                  |
| float                      | 55.8 ms                                                | 46.4 ms: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                                 |
| logging_format             | 3.98 us                                                | 3.34 us: 1.19x faster                                                 |
| mako                       | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 65.7 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 463 ms: 1.15x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 34.6 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.8 us: 1.14x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 133 us: 1.14x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.39 ms: 1.13x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 177 us: 1.13x faster                                                  |
| async_tree_io              | 668 ms                                                 | 594 ms: 1.13x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                |
| spectral_norm              | 76.4 ms                                                | 68.3 ms: 1.12x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 50.7 ms: 1.10x faster                                                 |
| nbody                      | 68.8 ms                                                | 63.8 ms: 1.08x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.07x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 474 us: 1.06x faster                                                  |
| chaos                      | 42.5 ms                                                | 40.4 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                                 |
| nqueens                    | 62.4 ms                                                | 59.5 ms: 1.05x faster                                                 |
| regex_compile              | 77.9 ms                                                | 74.9 ms: 1.04x faster                                                 |
| async_generators           | 304 ms                                                 | 294 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 71.9 ms: 1.03x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.1 ms: 1.02x faster                                                 |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.07 ms: 1.02x faster                                                 |
| sympy_str                  | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 76.4 ms: 1.02x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.57 sec: 1.01x faster                                                |
| django_template            | 22.3 ms                                                | 22.1 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 184 ms: 1.01x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 409 ms: 1.00x faster                                                  |
| go                         | 102 ms                                                 | 102 ms: 1.00x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 52.1 ms: 1.01x slower                                                 |
| json_loads                 | 17.2 us                                                | 17.3 us: 1.01x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.28 ms: 1.01x slower                                                 |
| sqlglot_parse              | 848 us                                                 | 857 us: 1.01x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 88.7 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 95.0 us: 1.02x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.04 sec: 1.03x slower                                                |
| pprint_safe_repr           | 497 ms                                                 | 511 ms: 1.03x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 73.8 ms: 1.03x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 110 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| sympy_expand               | 241 ms                                                 | 250 ms: 1.04x slower                                                  |
| pyflate                    | 316 ms                                                 | 328 ms: 1.04x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.9 ms: 1.04x slower                                                 |
| hexiom                     | 4.54 ms                                                | 4.78 ms: 1.05x slower                                                 |
| 2to3                       | 169 ms                                                 | 180 ms: 1.06x slower                                                  |
| fannkuch                   | 248 ms                                                 | 264 ms: 1.06x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 36.2 ms: 1.06x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.61 sec: 1.07x slower                                                |
| scimark_monte_carlo        | 45.0 ms                                                | 48.6 ms: 1.08x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 51.6 ms: 1.15x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.2 ms: 1.16x slower                                                 |
| tornado_http               | 69.3 ms                                                | 87.9 ms: 1.27x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 904 us: 1.29x slower                                                  |
| telco                      | 3.68 ms                                                | 4.85 ms: 1.32x slower                                                 |
| richards_super             | 36.0 ms                                                | 49.7 ms: 1.38x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.8 ms: 1.48x slower                                                 |
| richards                   | 32.1 ms                                                | 47.7 ms: 1.49x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.9 ms: 1.49x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (3): asyncio_tcp, pidigits, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 94.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.85x