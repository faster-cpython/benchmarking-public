# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: darwin-arm64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 171 ms: 1.01x slower                                                |
| docutils       | 1.50 sec                                               | 1.49 sec: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                |
| async_tree_none_tg         | 258 ms                                                 | 212 ms: 1.21x faster                                                |
| async_tree_memoization     | 312 ms                                                 | 262 ms: 1.19x faster                                                |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.16x faster                                                |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                                |
| async_tree_io_tg           | 669 ms                                                 | 609 ms: 1.10x faster                                                |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.1 ms: 1.16x faster                                               |
| nbody          | 68.8 ms                                                | 65.6 ms: 1.05x faster                                               |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 71.0 ms: 1.10x faster                                               |
| regex_dna      | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| regex_effbot   | 2.64 ms                                                | 2.45 ms: 1.08x faster                                               |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.2 ms: 1.16x faster                                               |
| unpickle_pure_python | 151 us                                                 | 133 us: 1.14x faster                                                |
| tomli_loads          | 1.39 sec                                               | 1.23 sec: 1.13x faster                                              |
| pickle_pure_python   | 200 us                                                 | 179 us: 1.11x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 50.2 ms: 1.11x faster                                               |
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                               |
| xml_etree_iterparse  | 74.0 ms                                                | 72.7 ms: 1.02x faster                                               |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                                |
| json_dumps           | 6.22 ms                                                | 7.17 ms: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.5 ms: 1.44x slower                                               |
| python_startup         | 11.4 ms                                                | 17.4 ms: 1.53x slower                                               |
| Geometric mean         | (ref)                                                  | 1.48x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.45 ms: 1.20x faster                                               |
| django_template | 22.3 ms                                                | 20.4 ms: 1.09x faster                                               |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.70x faster                                                |
| deepcopy_memo              | 27.7 us                                                | 16.7 us: 1.65x faster                                               |
| deepcopy                   | 235 us                                                 | 148 us: 1.58x faster                                                |
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                |
| deepcopy_reduce            | 2.07 us                                                | 1.53 us: 1.35x faster                                               |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                |
| raytrace                   | 212 ms                                                 | 162 ms: 1.31x faster                                                |
| generators                 | 31.1 ms                                                | 24.1 ms: 1.29x faster                                               |
| async_tree_none_tg         | 258 ms                                                 | 212 ms: 1.21x faster                                                |
| logging_simple             | 3.69 us                                                | 3.04 us: 1.21x faster                                               |
| logging_format             | 3.98 us                                                | 3.33 us: 1.20x faster                                               |
| mako                       | 7.71 ms                                                | 6.45 ms: 1.20x faster                                               |
| async_tree_memoization     | 312 ms                                                 | 262 ms: 1.19x faster                                                |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                               |
| scimark_lu                 | 76.0 ms                                                | 65.0 ms: 1.17x faster                                               |
| deltablue                  | 2.71 ms                                                | 2.32 ms: 1.17x faster                                               |
| xml_etree_process          | 39.7 ms                                                | 34.2 ms: 1.16x faster                                               |
| float                      | 55.8 ms                                                | 48.1 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.16x faster                                                |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                                |
| comprehensions             | 14.5 us                                                | 12.7 us: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                                |
| unpickle_pure_python       | 151 us                                                 | 133 us: 1.14x faster                                                |
| go                         | 102 ms                                                 | 89.9 ms: 1.13x faster                                               |
| tomli_loads                | 1.39 sec                                               | 1.23 sec: 1.13x faster                                              |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.11x faster                                                |
| xml_etree_generate         | 55.8 ms                                                | 50.2 ms: 1.11x faster                                               |
| spectral_norm              | 76.4 ms                                                | 69.3 ms: 1.10x faster                                               |
| logging_silent             | 76.4 ns                                                | 69.4 ns: 1.10x faster                                               |
| async_tree_io_tg           | 669 ms                                                 | 609 ms: 1.10x faster                                                |
| regex_compile              | 77.9 ms                                                | 71.0 ms: 1.10x faster                                               |
| django_template            | 22.3 ms                                                | 20.4 ms: 1.09x faster                                               |
| regex_dna                  | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| pathlib                    | 24.2 ms                                                | 22.3 ms: 1.09x faster                                               |
| json                       | 3.09 ms                                                | 2.84 ms: 1.09x faster                                               |
| pprint_safe_repr           | 497 ms                                                 | 460 ms: 1.08x faster                                                |
| nqueens                    | 62.4 ms                                                | 57.9 ms: 1.08x faster                                               |
| regex_effbot               | 2.64 ms                                                | 2.45 ms: 1.08x faster                                               |
| sqlglot_normalize          | 186 ms                                                 | 173 ms: 1.07x faster                                                |
| bench_thread_pool          | 504 us                                                 | 469 us: 1.07x faster                                                |
| chaos                      | 42.5 ms                                                | 40.3 ms: 1.06x faster                                               |
| nbody                      | 68.8 ms                                                | 65.6 ms: 1.05x faster                                               |
| dulwich_log                | 29.8 ms                                                | 28.5 ms: 1.04x faster                                               |
| async_generators           | 304 ms                                                 | 291 ms: 1.04x faster                                                |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                               |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                               |
| mdp                        | 1.58 sec                                               | 1.52 sec: 1.04x faster                                              |
| pprint_pformat             | 1.01 sec                                               | 974 ms: 1.04x faster                                                |
| richards                   | 32.1 ms                                                | 31.1 ms: 1.03x faster                                               |
| pycparser                  | 677 ms                                                 | 656 ms: 1.03x faster                                                |
| sqlglot_parse              | 848 us                                                 | 822 us: 1.03x faster                                                |
| sympy_str                  | 148 ms                                                 | 143 ms: 1.03x faster                                                |
| sympy_sum                  | 77.6 ms                                                | 75.4 ms: 1.03x faster                                               |
| sqlglot_transpile          | 1.02 ms                                                | 993 us: 1.03x faster                                                |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                                |
| xml_etree_iterparse        | 74.0 ms                                                | 72.7 ms: 1.02x faster                                               |
| sympy_expand               | 241 ms                                                 | 237 ms: 1.02x faster                                                |
| scimark_sor                | 87.4 ms                                                | 86.1 ms: 1.02x faster                                               |
| sqlglot_optimize           | 34.0 ms                                                | 33.6 ms: 1.01x faster                                               |
| pyflate                    | 316 ms                                                 | 312 ms: 1.01x faster                                                |
| hexiom                     | 4.54 ms                                                | 4.49 ms: 1.01x faster                                               |
| docutils                   | 1.50 sec                                               | 1.49 sec: 1.01x faster                                              |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.15 ms: 1.01x slower                                               |
| scimark_monte_carlo        | 45.0 ms                                                | 45.3 ms: 1.01x slower                                               |
| 2to3                       | 169 ms                                                 | 171 ms: 1.01x slower                                                |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.01x slower                                                |
| meteor_contest             | 71.7 ms                                                | 72.9 ms: 1.02x slower                                               |
| fannkuch                   | 248 ms                                                 | 254 ms: 1.02x slower                                                |
| sympy_integrate            | 11.4 ms                                                | 11.8 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 93.0 us                                                | 96.8 us: 1.04x slower                                               |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                               |
| crypto_pyaes               | 51.9 ms                                                | 54.3 ms: 1.05x slower                                               |
| coverage                   | 38.9 ms                                                | 43.7 ms: 1.12x slower                                               |
| json_dumps                 | 6.22 ms                                                | 7.17 ms: 1.15x slower                                               |
| gc_traversal               | 2.40 ms                                                | 2.95 ms: 1.23x slower                                               |
| telco                      | 3.68 ms                                                | 4.54 ms: 1.23x slower                                               |
| bench_mp_pool              | 44.9 ms                                                | 60.1 ms: 1.34x slower                                               |
| python_startup_no_site     | 9.37 ms                                                | 13.5 ms: 1.44x slower                                               |
| python_startup             | 11.4 ms                                                | 17.4 ms: 1.53x slower                                               |
| create_gc_cycles           | 701 us                                                 | 1.32 ms: 1.89x slower                                               |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.24x