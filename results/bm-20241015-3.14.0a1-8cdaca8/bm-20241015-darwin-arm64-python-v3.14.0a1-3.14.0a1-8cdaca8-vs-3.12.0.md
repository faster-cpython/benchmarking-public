# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.075x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                       |
| docutils       | 1.50 sec                                               | 1.41 sec: 1.07x faster                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 233 ms: 1.39x faster                                       |
| async_tree_none            | 266 ms                                                 | 196 ms: 1.35x faster                                       |
| async_tree_memoization     | 312 ms                                                 | 243 ms: 1.28x faster                                       |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.16x faster                                       |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                       |
| async_tree_io_tg           | 669 ms                                                 | 611 ms: 1.10x faster                                       |
| Geometric mean             | (ref)                                                  | 1.22x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.7 ms: 1.12x faster                                      |
| nbody          | 68.8 ms                                                | 65.5 ms: 1.05x faster                                      |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.4 ms: 1.14x faster                                      |
| regex_dna      | 154 ms                                                 | 146 ms: 1.06x faster                                       |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                      |
| regex_v8       | 16.0 ms                                                | 16.5 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 186 us: 1.08x faster                                       |
| xml_etree_generate   | 55.8 ms                                                | 52.5 ms: 1.06x faster                                      |
| xml_etree_process    | 39.7 ms                                                | 37.5 ms: 1.06x faster                                      |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                       |
| json_loads           | 17.2 us                                                | 16.4 us: 1.05x faster                                      |
| unpickle             | 9.12 us                                                | 9.03 us: 1.01x faster                                      |
| pickle               | 7.23 us                                                | 7.33 us: 1.01x slower                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 75.1 ms: 1.01x slower                                      |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                       |
| pickle_list          | 2.89 us                                                | 2.98 us: 1.03x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.50 sec: 1.08x slower                                     |
| json_dumps           | 6.22 ms                                                | 7.18 ms: 1.15x slower                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (2): unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.7 ms: 1.57x slower                                      |
| python_startup         | 11.4 ms                                                | 19.0 ms: 1.67x slower                                      |
| Geometric mean         | (ref)                                                  | 1.62x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.8 ms: 1.13x faster                                      |
| mako            | 7.71 ms                                                | 7.01 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.11x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.70x faster                                       |
| deepcopy                   | 235 us                                                 | 146 us: 1.61x faster                                       |
| deepcopy_memo              | 27.7 us                                                | 17.4 us: 1.59x faster                                      |
| generators                 | 31.1 ms                                                | 20.1 ms: 1.54x faster                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 233 ms: 1.39x faster                                       |
| raytrace                   | 212 ms                                                 | 154 ms: 1.38x faster                                       |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                      |
| async_tree_none            | 266 ms                                                 | 196 ms: 1.35x faster                                       |
| comprehensions             | 14.5 us                                                | 11.1 us: 1.31x faster                                      |
| async_tree_memoization     | 312 ms                                                 | 243 ms: 1.28x faster                                       |
| logging_silent             | 76.4 ns                                                | 60.9 ns: 1.25x faster                                      |
| go                         | 102 ms                                                 | 82.1 ms: 1.24x faster                                      |
| deltablue                  | 2.71 ms                                                | 2.23 ms: 1.22x faster                                      |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                       |
| logging_simple             | 3.69 us                                                | 3.08 us: 1.20x faster                                      |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                      |
| unpack_sequence            | 31.5 ns                                                | 26.8 ns: 1.18x faster                                      |
| nqueens                    | 62.4 ms                                                | 53.6 ms: 1.17x faster                                      |
| coroutines                 | 19.2 ms                                                | 16.5 ms: 1.17x faster                                      |
| bench_thread_pool          | 504 us                                                 | 433 us: 1.16x faster                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.16x faster                                       |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                       |
| sqlglot_parse              | 848 us                                                 | 743 us: 1.14x faster                                       |
| regex_compile              | 77.9 ms                                                | 68.4 ms: 1.14x faster                                      |
| chaos                      | 42.5 ms                                                | 37.3 ms: 1.14x faster                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                       |
| sqlglot_transpile          | 1.02 ms                                                | 901 us: 1.13x faster                                       |
| django_template            | 22.3 ms                                                | 19.8 ms: 1.13x faster                                      |
| float                      | 55.8 ms                                                | 49.7 ms: 1.12x faster                                      |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                       |
| sympy_sum                  | 77.6 ms                                                | 69.6 ms: 1.11x faster                                      |
| scimark_lu                 | 76.0 ms                                                | 68.2 ms: 1.11x faster                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.83 ms: 1.11x faster                                      |
| sympy_str                  | 148 ms                                                 | 133 ms: 1.11x faster                                       |
| pathlib                    | 24.2 ms                                                | 22.0 ms: 1.10x faster                                      |
| async_generators           | 304 ms                                                 | 276 ms: 1.10x faster                                       |
| mako                       | 7.71 ms                                                | 7.01 ms: 1.10x faster                                      |
| hexiom                     | 4.54 ms                                                | 4.13 ms: 1.10x faster                                      |
| async_tree_io_tg           | 669 ms                                                 | 611 ms: 1.10x faster                                       |
| sqlglot_optimize           | 34.0 ms                                                | 31.1 ms: 1.09x faster                                      |
| dulwich_log                | 29.8 ms                                                | 27.3 ms: 1.09x faster                                      |
| spectral_norm              | 76.4 ms                                                | 70.2 ms: 1.09x faster                                      |
| mdp                        | 1.58 sec                                               | 1.46 sec: 1.08x faster                                     |
| pprint_pformat             | 1.01 sec                                               | 936 ms: 1.08x faster                                       |
| pickle_pure_python         | 200 us                                                 | 186 us: 1.08x faster                                       |
| pprint_safe_repr           | 497 ms                                                 | 462 ms: 1.08x faster                                       |
| json                       | 3.09 ms                                                | 2.87 ms: 1.07x faster                                      |
| docutils                   | 1.50 sec                                               | 1.41 sec: 1.07x faster                                     |
| pycparser                  | 677 ms                                                 | 635 ms: 1.07x faster                                       |
| xml_etree_generate         | 55.8 ms                                                | 52.5 ms: 1.06x faster                                      |
| sympy_expand               | 241 ms                                                 | 227 ms: 1.06x faster                                       |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                       |
| xml_etree_process          | 39.7 ms                                                | 37.5 ms: 1.06x faster                                      |
| regex_dna                  | 154 ms                                                 | 146 ms: 1.06x faster                                       |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                       |
| nbody                      | 68.8 ms                                                | 65.5 ms: 1.05x faster                                      |
| json_loads                 | 17.2 us                                                | 16.4 us: 1.05x faster                                      |
| richards_super             | 36.0 ms                                                | 34.3 ms: 1.05x faster                                      |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.04x faster                                      |
| richards                   | 32.1 ms                                                | 31.0 ms: 1.04x faster                                      |
| scimark_monte_carlo        | 45.0 ms                                                | 43.6 ms: 1.03x faster                                      |
| sqlite_synth               | 1.57 us                                                | 1.52 us: 1.03x faster                                      |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                       |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                      |
| meteor_contest             | 71.7 ms                                                | 70.5 ms: 1.02x faster                                      |
| unpickle                   | 9.12 us                                                | 9.03 us: 1.01x faster                                      |
| typing_runtime_protocols   | 93.0 us                                                | 92.3 us: 1.01x faster                                      |
| crypto_pyaes               | 51.9 ms                                                | 51.7 ms: 1.00x faster                                      |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| pickle                     | 7.23 us                                                | 7.33 us: 1.01x slower                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 75.1 ms: 1.01x slower                                      |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.02x slower                                       |
| pickle_list                | 2.89 us                                                | 2.98 us: 1.03x slower                                      |
| regex_v8                   | 16.0 ms                                                | 16.5 ms: 1.03x slower                                      |
| pyflate                    | 316 ms                                                 | 327 ms: 1.04x slower                                       |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                     |
| fannkuch                   | 248 ms                                                 | 268 ms: 1.08x slower                                       |
| tomli_loads                | 1.39 sec                                               | 1.50 sec: 1.08x slower                                     |
| scimark_sor                | 87.4 ms                                                | 95.9 ms: 1.10x slower                                      |
| coverage                   | 38.9 ms                                                | 44.8 ms: 1.15x slower                                      |
| json_dumps                 | 6.22 ms                                                | 7.18 ms: 1.15x slower                                      |
| gc_traversal               | 2.40 ms                                                | 2.94 ms: 1.22x slower                                      |
| telco                      | 3.68 ms                                                | 4.53 ms: 1.23x slower                                      |
| bench_mp_pool              | 44.9 ms                                                | 58.9 ms: 1.31x slower                                      |
| python_startup_no_site     | 9.37 ms                                                | 14.7 ms: 1.57x slower                                      |
| python_startup             | 11.4 ms                                                | 19.0 ms: 1.67x slower                                      |
| create_gc_cycles           | 701 us                                                 | 1.30 ms: 1.85x slower                                      |
| Geometric mean             | (ref)                                                  | 1.07x faster                                               |

Benchmark hidden because not significant (4): asyncio_tcp, unpickle_list, pickle_dict, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.075x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.17x