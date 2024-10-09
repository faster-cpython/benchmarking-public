# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.03x faster
- HPT reliability: 96.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 181 ms: 1.07x slower                                                  |
| docutils       | 1.50 sec                                               | 1.60 sec: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 187 ms: 1.38x faster                                                  |
| async_tree_none            | 266 ms                                                 | 201 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 260 ms: 1.24x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 573 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.7 ms: 1.19x faster                                                 |
| nbody          | 68.8 ms                                                | 63.6 ms: 1.08x faster                                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| regex_compile  | 77.9 ms                                                | 76.0 ms: 1.02x faster                                                 |
| regex_v8       | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 130 us: 1.16x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 34.6 ms: 1.15x faster                                                 |
| pickle_pure_python   | 200 us                                                 | 176 us: 1.14x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 50.1 ms: 1.11x faster                                                 |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                |
| xml_etree_iterparse  | 74.0 ms                                                | 70.7 ms: 1.05x faster                                                 |
| json_loads           | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_dumps           | 6.22 ms                                                | 6.14 ms: 1.01x faster                                                 |
| unpickle             | 9.12 us                                                | 9.01 us: 1.01x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.99 us: 1.01x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.01x slower                                                 |
| pickle               | 7.23 us                                                | 7.43 us: 1.03x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.97 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 18.2 ms: 1.59x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 15.2 ms: 1.63x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.61x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.39 ms: 1.21x faster                                                 |
| django_template | 22.3 ms                                                | 23.4 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 16.5 us: 1.67x faster                                                 |
| deepcopy                   | 235 us                                                 | 157 us: 1.49x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 187 ms: 1.38x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                                 |
| async_tree_none            | 266 ms                                                 | 201 ms: 1.32x faster                                                  |
| logging_silent             | 76.4 ns                                                | 60.7 ns: 1.26x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 260 ms: 1.24x faster                                                  |
| generators                 | 31.1 ms                                                | 25.4 ms: 1.22x faster                                                 |
| mako                       | 7.71 ms                                                | 6.39 ms: 1.21x faster                                                 |
| raytrace                   | 212 ms                                                 | 177 ms: 1.20x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.08 us: 1.20x faster                                                 |
| float                      | 55.8 ms                                                | 46.7 ms: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 64.0 ms: 1.19x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.18x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 573 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 130 us: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.15x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 34.6 ms: 1.15x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.0 ms: 1.14x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 176 us: 1.14x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.9 us: 1.13x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.41 ms: 1.12x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 50.1 ms: 1.11x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                |
| pathlib                    | 24.2 ms                                                | 22.2 ms: 1.09x faster                                                 |
| nbody                      | 68.8 ms                                                | 63.6 ms: 1.08x faster                                                 |
| json                       | 3.09 ms                                                | 2.88 ms: 1.07x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.48 sec: 1.07x faster                                                |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                                  |
| nqueens                    | 62.4 ms                                                | 59.0 ms: 1.06x faster                                                 |
| chaos                      | 42.5 ms                                                | 40.5 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.99 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 70.7 ms: 1.05x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 482 us: 1.05x faster                                                  |
| async_generators           | 304 ms                                                 | 291 ms: 1.04x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.53 us: 1.03x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.03x faster                                                  |
| regex_compile              | 77.9 ms                                                | 76.0 ms: 1.02x faster                                                 |
| json_dumps                 | 6.22 ms                                                | 6.14 ms: 1.01x faster                                                 |
| unpickle                   | 9.12 us                                                | 9.01 us: 1.01x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.99 us: 1.01x faster                                                 |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                                  |
| scimark_sor                | 87.4 ms                                                | 87.3 ms: 1.00x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.01 sec: 1.00x slower                                                |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.1 us: 1.01x slower                                                 |
| pprint_safe_repr           | 497 ms                                                 | 501 ms: 1.01x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 52.3 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 78.9 ms: 1.02x slower                                                 |
| sympy_expand               | 241 ms                                                 | 246 ms: 1.02x slower                                                  |
| sympy_str                  | 148 ms                                                 | 150 ms: 1.02x slower                                                  |
| pyflate                    | 316 ms                                                 | 323 ms: 1.02x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.05 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 95.5 us: 1.03x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                                 |
| pickle                     | 7.23 us                                                | 7.43 us: 1.03x slower                                                 |
| pickle_list                | 2.89 us                                                | 2.97 us: 1.03x slower                                                 |
| hexiom                     | 4.54 ms                                                | 4.70 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.04x slower                                                |
| meteor_contest             | 71.7 ms                                                | 75.1 ms: 1.05x slower                                                 |
| django_template            | 22.3 ms                                                | 23.4 ms: 1.05x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 47.8 ms: 1.06x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.60 sec: 1.07x slower                                                |
| fannkuch                   | 248 ms                                                 | 265 ms: 1.07x slower                                                  |
| 2to3                       | 169 ms                                                 | 181 ms: 1.07x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.6 ms: 1.11x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 37.8 ms: 1.11x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.0 ms: 1.13x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 51.4 ms: 1.14x slower                                                 |
| telco                      | 3.68 ms                                                | 4.49 ms: 1.22x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 899 us: 1.28x slower                                                  |
| richards_super             | 36.0 ms                                                | 46.6 ms: 1.29x slower                                                 |
| richards                   | 32.1 ms                                                | 45.2 ms: 1.41x slower                                                 |
| python_startup             | 11.4 ms                                                | 18.2 ms: 1.59x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 15.2 ms: 1.63x slower                                                 |
| unpack_sequence            | 31.5 ns                                                | 76.8 ns: 2.44x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (5): asyncio_tcp, regex_effbot, sqlglot_parse, pycparser, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.59x