# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 170 ms: 1.00x slower                                           |
| docutils       | 1.50 sec                                               | 1.50 sec: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x slower                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                           |
| async_tree_none_tg         | 258 ms                                                 | 195 ms: 1.32x faster                                           |
| async_tree_memoization_tg  | 323 ms                                                 | 246 ms: 1.31x faster                                           |
| async_tree_io_tg           | 669 ms                                                 | 539 ms: 1.24x faster                                           |
| async_tree_memoization     | 312 ms                                                 | 262 ms: 1.19x faster                                           |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 454 ms: 1.16x faster                                           |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                           |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.2 ms: 1.21x faster                                          |
| nbody          | 68.8 ms                                                | 63.7 ms: 1.08x faster                                          |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 72.0 ms: 1.08x faster                                          |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                           |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.01x faster                                          |
| regex_v8       | 16.0 ms                                                | 17.0 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 33.9 ms: 1.17x faster                                          |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                           |
| pickle_pure_python   | 200 us                                                 | 176 us: 1.13x faster                                           |
| xml_etree_generate   | 55.8 ms                                                | 49.5 ms: 1.13x faster                                          |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.11x faster                                         |
| json_loads           | 17.2 us                                                | 16.4 us: 1.05x faster                                          |
| xml_etree_iterparse  | 74.0 ms                                                | 72.4 ms: 1.02x faster                                          |
| json_dumps           | 6.22 ms                                                | 6.16 ms: 1.01x faster                                          |
| unpickle_list        | 3.02 us                                                | 3.00 us: 1.01x faster                                          |
| unpickle             | 9.12 us                                                | 9.07 us: 1.01x faster                                          |
| pickle               | 7.23 us                                                | 7.29 us: 1.01x slower                                          |
| pickle_dict          | 18.1 us                                                | 18.6 us: 1.03x slower                                          |
| pickle_list          | 2.89 us                                                | 3.11 us: 1.08x slower                                          |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.9 ms: 1.59x slower                                          |
| python_startup         | 11.4 ms                                                | 19.2 ms: 1.69x slower                                          |
| Geometric mean         | (ref)                                                  | 1.64x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.43 ms: 1.20x faster                                          |
| django_template | 22.3 ms                                                | 20.2 ms: 1.10x faster                                          |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                           |
| deepcopy_memo              | 27.7 us                                                | 16.6 us: 1.67x faster                                          |
| deepcopy                   | 235 us                                                 | 149 us: 1.57x faster                                           |
| deepcopy_reduce            | 2.07 us                                                | 1.49 us: 1.39x faster                                          |
| logging_silent             | 76.4 ns                                                | 56.4 ns: 1.36x faster                                          |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                           |
| async_tree_none_tg         | 258 ms                                                 | 195 ms: 1.32x faster                                           |
| async_tree_memoization_tg  | 323 ms                                                 | 246 ms: 1.31x faster                                           |
| generators                 | 31.1 ms                                                | 24.2 ms: 1.29x faster                                          |
| async_tree_io_tg           | 669 ms                                                 | 539 ms: 1.24x faster                                           |
| logging_simple             | 3.69 us                                                | 3.02 us: 1.22x faster                                          |
| float                      | 55.8 ms                                                | 46.2 ms: 1.21x faster                                          |
| mako                       | 7.71 ms                                                | 6.43 ms: 1.20x faster                                          |
| logging_format             | 3.98 us                                                | 3.33 us: 1.19x faster                                          |
| async_tree_memoization     | 312 ms                                                 | 262 ms: 1.19x faster                                           |
| scimark_lu                 | 76.0 ms                                                | 64.0 ms: 1.19x faster                                          |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                          |
| raytrace                   | 212 ms                                                 | 180 ms: 1.18x faster                                           |
| deltablue                  | 2.71 ms                                                | 2.31 ms: 1.17x faster                                          |
| xml_etree_process          | 39.7 ms                                                | 33.9 ms: 1.17x faster                                          |
| comprehensions             | 14.5 us                                                | 12.5 us: 1.17x faster                                          |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 454 ms: 1.16x faster                                           |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                           |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                           |
| pickle_pure_python         | 200 us                                                 | 176 us: 1.13x faster                                           |
| xml_etree_generate         | 55.8 ms                                                | 49.5 ms: 1.13x faster                                          |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.11x faster                                         |
| spectral_norm              | 76.4 ms                                                | 68.6 ms: 1.11x faster                                          |
| django_template            | 22.3 ms                                                | 20.2 ms: 1.10x faster                                          |
| nqueens                    | 62.4 ms                                                | 56.6 ms: 1.10x faster                                          |
| pathlib                    | 24.2 ms                                                | 22.2 ms: 1.09x faster                                          |
| pprint_safe_repr           | 497 ms                                                 | 456 ms: 1.09x faster                                           |
| regex_compile              | 77.9 ms                                                | 72.0 ms: 1.08x faster                                          |
| nbody                      | 68.8 ms                                                | 63.7 ms: 1.08x faster                                          |
| richards_super             | 36.0 ms                                                | 33.4 ms: 1.08x faster                                          |
| richards                   | 32.1 ms                                                | 29.9 ms: 1.07x faster                                          |
| chaos                      | 42.5 ms                                                | 39.8 ms: 1.07x faster                                          |
| json                       | 3.09 ms                                                | 2.89 ms: 1.07x faster                                          |
| sqlglot_normalize          | 186 ms                                                 | 174 ms: 1.07x faster                                           |
| mdp                        | 1.58 sec                                               | 1.48 sec: 1.06x faster                                         |
| pprint_pformat             | 1.01 sec                                               | 952 ms: 1.06x faster                                           |
| bench_thread_pool          | 504 us                                                 | 475 us: 1.06x faster                                           |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                           |
| go                         | 102 ms                                                 | 96.1 ms: 1.06x faster                                          |
| async_generators           | 304 ms                                                 | 288 ms: 1.05x faster                                           |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.97 ms: 1.05x faster                                          |
| sqlglot_parse              | 848 us                                                 | 808 us: 1.05x faster                                           |
| json_loads                 | 17.2 us                                                | 16.4 us: 1.05x faster                                          |
| sympy_sum                  | 77.6 ms                                                | 74.5 ms: 1.04x faster                                          |
| pycparser                  | 677 ms                                                 | 650 ms: 1.04x faster                                           |
| dulwich_log                | 29.8 ms                                                | 28.6 ms: 1.04x faster                                          |
| sympy_str                  | 148 ms                                                 | 142 ms: 1.04x faster                                           |
| sqlglot_transpile          | 1.02 ms                                                | 984 us: 1.04x faster                                           |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                           |
| sqlite_synth               | 1.57 us                                                | 1.53 us: 1.02x faster                                          |
| xml_etree_iterparse        | 74.0 ms                                                | 72.4 ms: 1.02x faster                                          |
| sympy_expand               | 241 ms                                                 | 236 ms: 1.02x faster                                           |
| scimark_sor                | 87.4 ms                                                | 85.8 ms: 1.02x faster                                          |
| hexiom                     | 4.54 ms                                                | 4.47 ms: 1.02x faster                                          |
| scimark_monte_carlo        | 45.0 ms                                                | 44.6 ms: 1.01x faster                                          |
| json_dumps                 | 6.22 ms                                                | 6.16 ms: 1.01x faster                                          |
| unpickle_list              | 3.02 us                                                | 3.00 us: 1.01x faster                                          |
| sqlglot_optimize           | 34.0 ms                                                | 33.8 ms: 1.01x faster                                          |
| pyflate                    | 316 ms                                                 | 314 ms: 1.01x faster                                           |
| unpickle                   | 9.12 us                                                | 9.07 us: 1.01x faster                                          |
| regex_effbot               | 2.64 ms                                                | 2.63 ms: 1.01x faster                                          |
| docutils                   | 1.50 sec                                               | 1.50 sec: 1.00x faster                                         |
| 2to3                       | 169 ms                                                 | 170 ms: 1.00x slower                                           |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                           |
| crypto_pyaes               | 51.9 ms                                                | 52.2 ms: 1.01x slower                                          |
| pickle                     | 7.23 us                                                | 7.29 us: 1.01x slower                                          |
| typing_runtime_protocols   | 93.0 us                                                | 95.0 us: 1.02x slower                                          |
| pickle_dict                | 18.1 us                                                | 18.6 us: 1.03x slower                                          |
| fannkuch                   | 248 ms                                                 | 257 ms: 1.03x slower                                           |
| sympy_integrate            | 11.4 ms                                                | 11.8 ms: 1.04x slower                                          |
| meteor_contest             | 71.7 ms                                                | 74.5 ms: 1.04x slower                                          |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.05x slower                                         |
| regex_v8                   | 16.0 ms                                                | 17.0 ms: 1.06x slower                                          |
| pickle_list                | 2.89 us                                                | 3.11 us: 1.08x slower                                          |
| coverage                   | 38.9 ms                                                | 43.5 ms: 1.12x slower                                          |
| gc_traversal               | 2.40 ms                                                | 2.91 ms: 1.21x slower                                          |
| telco                      | 3.68 ms                                                | 4.56 ms: 1.24x slower                                          |
| bench_mp_pool              | 44.9 ms                                                | 61.0 ms: 1.36x slower                                          |
| python_startup_no_site     | 9.37 ms                                                | 14.9 ms: 1.59x slower                                          |
| python_startup             | 11.4 ms                                                | 19.2 ms: 1.69x slower                                          |
| create_gc_cycles           | 701 us                                                 | 1.29 ms: 1.84x slower                                          |
| unpack_sequence            | 31.5 ns                                                | 75.2 ns: 2.39x slower                                          |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                   |

Benchmark hidden because not significant (3): asyncio_tcp, xml_etree_parse, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.24x