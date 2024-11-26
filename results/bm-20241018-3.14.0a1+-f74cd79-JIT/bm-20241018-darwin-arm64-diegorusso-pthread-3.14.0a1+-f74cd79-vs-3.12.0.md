# Results vs. 3.12.0

- fork: diegorusso
- ref: pthread
- machine: darwin-arm64
- commit hash: f74cd79
- commit date: 2024-10-18
- overall geometric mean: 1.039x faster
- HPT reliability: 98.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 182 ms: 1.07x slower                                          |
| docutils       | 1.50 sec                                               | 1.57 sec: 1.04x slower                                        |
| Geometric mean | (ref)                                                  | 1.08x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                          |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                          |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                          |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                          |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                          |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                          |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 469 ms: 1.13x faster                                          |
| async_tree_io_tg           | 669 ms                                                 | 610 ms: 1.10x faster                                          |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.4 ms: 1.15x faster                                         |
| nbody          | 68.8 ms                                                | 65.3 ms: 1.05x faster                                         |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 74.4 ms: 1.05x faster                                         |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                          |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.01x faster                                         |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.8 ms: 1.14x faster                                         |
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                          |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                        |
| pickle_pure_python   | 200 us                                                 | 180 us: 1.11x faster                                          |
| xml_etree_generate   | 55.8 ms                                                | 50.5 ms: 1.11x faster                                         |
| json_loads           | 17.2 us                                                | 16.4 us: 1.05x faster                                         |
| xml_etree_iterparse  | 74.0 ms                                                | 72.7 ms: 1.02x faster                                         |
| json_dumps           | 6.22 ms                                                | 7.08 ms: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.9 ms: 1.27x slower                                         |
| python_startup         | 11.4 ms                                                | 15.7 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.32x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.46 ms: 1.19x faster                                         |
| django_template | 22.3 ms                                                | 22.6 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.70x faster                                          |
| deepcopy_memo              | 27.7 us                                                | 16.9 us: 1.64x faster                                         |
| deepcopy                   | 235 us                                                 | 152 us: 1.55x faster                                          |
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                          |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.34x faster                                         |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                          |
| generators                 | 31.1 ms                                                | 25.3 ms: 1.23x faster                                         |
| raytrace                   | 212 ms                                                 | 173 ms: 1.22x faster                                          |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                          |
| mako                       | 7.71 ms                                                | 6.46 ms: 1.19x faster                                         |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                         |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                          |
| logging_format             | 3.98 us                                                | 3.38 us: 1.18x faster                                         |
| scimark_lu                 | 76.0 ms                                                | 65.0 ms: 1.17x faster                                         |
| coroutines                 | 19.2 ms                                                | 16.5 ms: 1.17x faster                                         |
| float                      | 55.8 ms                                                | 48.4 ms: 1.15x faster                                         |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                          |
| xml_etree_process          | 39.7 ms                                                | 34.8 ms: 1.14x faster                                         |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                          |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                          |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 469 ms: 1.13x faster                                          |
| deltablue                  | 2.71 ms                                                | 2.39 ms: 1.13x faster                                         |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                        |
| pickle_pure_python         | 200 us                                                 | 180 us: 1.11x faster                                          |
| comprehensions             | 14.5 us                                                | 13.1 us: 1.11x faster                                         |
| xml_etree_generate         | 55.8 ms                                                | 50.5 ms: 1.11x faster                                         |
| spectral_norm              | 76.4 ms                                                | 69.3 ms: 1.10x faster                                         |
| async_tree_io_tg           | 669 ms                                                 | 610 ms: 1.10x faster                                          |
| pathlib                    | 24.2 ms                                                | 22.2 ms: 1.09x faster                                         |
| logging_silent             | 76.4 ns                                                | 70.1 ns: 1.09x faster                                         |
| json                       | 3.09 ms                                                | 2.84 ms: 1.09x faster                                         |
| nqueens                    | 62.4 ms                                                | 58.7 ms: 1.06x faster                                         |
| bench_thread_pool          | 504 us                                                 | 476 us: 1.06x faster                                          |
| nbody                      | 68.8 ms                                                | 65.3 ms: 1.05x faster                                         |
| json_loads                 | 17.2 us                                                | 16.4 us: 1.05x faster                                         |
| regex_compile              | 77.9 ms                                                | 74.4 ms: 1.05x faster                                         |
| async_generators           | 304 ms                                                 | 293 ms: 1.04x faster                                          |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                          |
| go                         | 102 ms                                                 | 98.4 ms: 1.03x faster                                         |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                         |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                          |
| chaos                      | 42.5 ms                                                | 41.7 ms: 1.02x faster                                         |
| xml_etree_iterparse        | 74.0 ms                                                | 72.7 ms: 1.02x faster                                         |
| mdp                        | 1.58 sec                                               | 1.55 sec: 1.02x faster                                        |
| scimark_sor                | 87.4 ms                                                | 86.1 ms: 1.01x faster                                         |
| regex_effbot               | 2.64 ms                                                | 2.63 ms: 1.01x faster                                         |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                          |
| django_template            | 22.3 ms                                                | 22.6 ms: 1.01x slower                                         |
| pprint_safe_repr           | 497 ms                                                 | 504 ms: 1.01x slower                                          |
| sympy_sum                  | 77.6 ms                                                | 78.8 ms: 1.01x slower                                         |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.18 ms: 1.02x slower                                         |
| scimark_monte_carlo        | 45.0 ms                                                | 45.8 ms: 1.02x slower                                         |
| sqlglot_parse              | 848 us                                                 | 865 us: 1.02x slower                                          |
| sympy_str                  | 148 ms                                                 | 151 ms: 1.02x slower                                          |
| sympy_expand               | 241 ms                                                 | 247 ms: 1.02x slower                                          |
| pyflate                    | 316 ms                                                 | 325 ms: 1.03x slower                                          |
| sqlglot_transpile          | 1.02 ms                                                | 1.05 ms: 1.03x slower                                         |
| meteor_contest             | 71.7 ms                                                | 74.5 ms: 1.04x slower                                         |
| crypto_pyaes               | 51.9 ms                                                | 53.9 ms: 1.04x slower                                         |
| docutils                   | 1.50 sec                                               | 1.57 sec: 1.04x slower                                        |
| typing_runtime_protocols   | 93.0 us                                                | 97.4 us: 1.05x slower                                         |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                         |
| 2to3                       | 169 ms                                                 | 182 ms: 1.07x slower                                          |
| fannkuch                   | 248 ms                                                 | 268 ms: 1.08x slower                                          |
| sqlglot_optimize           | 34.0 ms                                                | 36.7 ms: 1.08x slower                                         |
| hexiom                     | 4.54 ms                                                | 4.96 ms: 1.09x slower                                         |
| richards_super             | 36.0 ms                                                | 39.5 ms: 1.10x slower                                         |
| sympy_integrate            | 11.4 ms                                                | 12.5 ms: 1.10x slower                                         |
| richards                   | 32.1 ms                                                | 35.7 ms: 1.11x slower                                         |
| coverage                   | 38.9 ms                                                | 43.5 ms: 1.12x slower                                         |
| json_dumps                 | 6.22 ms                                                | 7.08 ms: 1.14x slower                                         |
| gc_traversal               | 2.40 ms                                                | 2.94 ms: 1.23x slower                                         |
| telco                      | 3.68 ms                                                | 4.58 ms: 1.25x slower                                         |
| python_startup_no_site     | 9.37 ms                                                | 11.9 ms: 1.27x slower                                         |
| bench_mp_pool              | 44.9 ms                                                | 60.5 ms: 1.35x slower                                         |
| python_startup             | 11.4 ms                                                | 15.7 ms: 1.38x slower                                         |
| create_gc_cycles           | 701 us                                                 | 1.33 ms: 1.89x slower                                         |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (5): pprint_pformat, sqlglot_normalize, pycparser, xml_etree_parse, tornado_http
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241018-3.14.0a1+-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.039x faster
# HPT report

- Reliability score: 98.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x