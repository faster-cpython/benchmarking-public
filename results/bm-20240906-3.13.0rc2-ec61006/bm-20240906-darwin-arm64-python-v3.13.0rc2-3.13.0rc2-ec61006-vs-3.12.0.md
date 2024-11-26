# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc2
- machine: darwin-arm64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.79x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 162 ms: 1.04x faster                                         |
| chameleon      | 4.70 ms                                                | 4.37 ms: 1.08x faster                                        |
| docutils       | 1.50 sec                                               | 1.47 sec: 1.02x faster                                       |
| tornado_http   | 69.3 ms                                                | 85.1 ms: 1.23x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                         |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                         |
| async_tree_none            | 266 ms                                                 | 214 ms: 1.24x faster                                         |
| async_tree_io_tg           | 669 ms                                                 | 557 ms: 1.20x faster                                         |
| async_tree_io              | 668 ms                                                 | 559 ms: 1.20x faster                                         |
| async_tree_memoization     | 312 ms                                                 | 261 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 473 ms: 1.11x faster                                         |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.3 ms: 1.15x faster                                        |
| nbody          | 68.8 ms                                                | 60.6 ms: 1.14x faster                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.8 ms: 1.13x faster                                        |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                         |
| regex_effbot   | 2.64 ms                                                | 2.61 ms: 1.01x faster                                        |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                         |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                         |
| xml_etree_process    | 39.7 ms                                                | 37.6 ms: 1.05x faster                                        |
| xml_etree_generate   | 55.8 ms                                                | 53.1 ms: 1.05x faster                                        |
| unpickle_list        | 3.02 us                                                | 2.91 us: 1.04x faster                                        |
| json_loads           | 17.2 us                                                | 16.7 us: 1.03x faster                                        |
| xml_etree_iterparse  | 74.0 ms                                                | 73.0 ms: 1.01x faster                                        |
| unpickle             | 9.12 us                                                | 9.21 us: 1.01x slower                                        |
| xml_etree_parse      | 106 ms                                                 | 107 ms: 1.01x slower                                         |
| json_dumps           | 6.22 ms                                                | 6.31 ms: 1.01x slower                                        |
| pickle_dict          | 18.1 us                                                | 18.4 us: 1.02x slower                                        |
| pickle_list          | 2.89 us                                                | 3.01 us: 1.04x slower                                        |
| tomli_loads          | 1.39 sec                                               | 1.46 sec: 1.05x slower                                       |
| pickle               | 7.23 us                                                | 7.70 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.7 ms: 1.46x slower                                        |
| python_startup         | 11.4 ms                                                | 17.2 ms: 1.50x slower                                        |
| Geometric mean         | (ref)                                                  | 1.48x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.8 ms: 1.13x faster                                        |
| mako            | 7.71 ms                                                | 7.08 ms: 1.09x faster                                        |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 149 ms: 1.43x faster                                         |
| comprehensions             | 14.5 us                                                | 10.6 us: 1.37x faster                                        |
| generators                 | 31.1 ms                                                | 22.9 ms: 1.35x faster                                        |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                         |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                         |
| logging_silent             | 76.4 ns                                                | 60.7 ns: 1.26x faster                                        |
| deltablue                  | 2.71 ms                                                | 2.16 ms: 1.25x faster                                        |
| async_tree_none            | 266 ms                                                 | 214 ms: 1.24x faster                                         |
| chaos                      | 42.5 ms                                                | 34.4 ms: 1.24x faster                                        |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                        |
| deepcopy_memo              | 27.7 us                                                | 23.0 us: 1.20x faster                                        |
| async_tree_io_tg           | 669 ms                                                 | 557 ms: 1.20x faster                                         |
| async_tree_io              | 668 ms                                                 | 559 ms: 1.20x faster                                         |
| async_tree_memoization     | 312 ms                                                 | 261 ms: 1.20x faster                                         |
| logging_simple             | 3.69 us                                                | 3.12 us: 1.18x faster                                        |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                         |
| nqueens                    | 62.4 ms                                                | 52.9 ms: 1.18x faster                                        |
| unpack_sequence            | 31.5 ns                                                | 26.7 ns: 1.18x faster                                        |
| logging_format             | 3.98 us                                                | 3.39 us: 1.17x faster                                        |
| float                      | 55.8 ms                                                | 48.3 ms: 1.15x faster                                        |
| deepcopy                   | 235 us                                                 | 204 us: 1.15x faster                                         |
| sqlglot_parse              | 848 us                                                 | 739 us: 1.15x faster                                         |
| spectral_norm              | 76.4 ms                                                | 67.0 ms: 1.14x faster                                        |
| deepcopy_reduce            | 2.07 us                                                | 1.82 us: 1.14x faster                                        |
| nbody                      | 68.8 ms                                                | 60.6 ms: 1.14x faster                                        |
| sqlglot_transpile          | 1.02 ms                                                | 899 us: 1.14x faster                                         |
| regex_compile              | 77.9 ms                                                | 68.8 ms: 1.13x faster                                        |
| django_template            | 22.3 ms                                                | 19.8 ms: 1.13x faster                                        |
| scimark_lu                 | 76.0 ms                                                | 67.6 ms: 1.12x faster                                        |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.81 ms: 1.11x faster                                        |
| mdp                        | 1.58 sec                                               | 1.42 sec: 1.11x faster                                       |
| sympy_sum                  | 77.6 ms                                                | 69.8 ms: 1.11x faster                                        |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 473 ms: 1.11x faster                                         |
| sympy_str                  | 148 ms                                                 | 133 ms: 1.11x faster                                         |
| sqlglot_normalize          | 186 ms                                                 | 168 ms: 1.11x faster                                         |
| asyncio_tcp                | 449 ms                                                 | 408 ms: 1.10x faster                                         |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                         |
| bench_thread_pool          | 504 us                                                 | 460 us: 1.10x faster                                         |
| sympy_integrate            | 11.4 ms                                                | 10.4 ms: 1.10x faster                                        |
| dulwich_log                | 29.8 ms                                                | 27.3 ms: 1.09x faster                                        |
| hexiom                     | 4.54 ms                                                | 4.16 ms: 1.09x faster                                        |
| mako                       | 7.71 ms                                                | 7.08 ms: 1.09x faster                                        |
| sqlglot_optimize           | 34.0 ms                                                | 31.3 ms: 1.09x faster                                        |
| chameleon                  | 4.70 ms                                                | 4.37 ms: 1.08x faster                                        |
| async_generators           | 304 ms                                                 | 285 ms: 1.07x faster                                         |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                         |
| pprint_safe_repr           | 497 ms                                                 | 468 ms: 1.06x faster                                         |
| pprint_pformat             | 1.01 sec                                               | 953 ms: 1.06x faster                                         |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                         |
| sympy_expand               | 241 ms                                                 | 228 ms: 1.06x faster                                         |
| pycparser                  | 677 ms                                                 | 641 ms: 1.06x faster                                         |
| xml_etree_process          | 39.7 ms                                                | 37.6 ms: 1.05x faster                                        |
| scimark_monte_carlo        | 45.0 ms                                                | 42.8 ms: 1.05x faster                                        |
| xml_etree_generate         | 55.8 ms                                                | 53.1 ms: 1.05x faster                                        |
| json                       | 3.09 ms                                                | 2.95 ms: 1.05x faster                                        |
| 2to3                       | 169 ms                                                 | 162 ms: 1.04x faster                                         |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                        |
| crypto_pyaes               | 51.9 ms                                                | 49.9 ms: 1.04x faster                                        |
| unpickle_list              | 3.02 us                                                | 2.91 us: 1.04x faster                                        |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                         |
| typing_runtime_protocols   | 93.0 us                                                | 89.7 us: 1.04x faster                                        |
| json_loads                 | 17.2 us                                                | 16.7 us: 1.03x faster                                        |
| docutils                   | 1.50 sec                                               | 1.47 sec: 1.02x faster                                       |
| richards                   | 32.1 ms                                                | 31.5 ms: 1.02x faster                                        |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                        |
| xml_etree_iterparse        | 74.0 ms                                                | 73.0 ms: 1.01x faster                                        |
| regex_effbot               | 2.64 ms                                                | 2.61 ms: 1.01x faster                                        |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                         |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                         |
| unpickle                   | 9.12 us                                                | 9.21 us: 1.01x slower                                        |
| xml_etree_parse            | 106 ms                                                 | 107 ms: 1.01x slower                                         |
| json_dumps                 | 6.22 ms                                                | 6.31 ms: 1.01x slower                                        |
| pathlib                    | 24.2 ms                                                | 24.6 ms: 1.02x slower                                        |
| pyflate                    | 316 ms                                                 | 322 ms: 1.02x slower                                         |
| pickle_dict                | 18.1 us                                                | 18.4 us: 1.02x slower                                        |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                        |
| fannkuch                   | 248 ms                                                 | 257 ms: 1.03x slower                                         |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                       |
| pickle_list                | 2.89 us                                                | 3.01 us: 1.04x slower                                        |
| tomli_loads                | 1.39 sec                                               | 1.46 sec: 1.05x slower                                       |
| dask                       | 222 ms                                                 | 234 ms: 1.06x slower                                         |
| pickle                     | 7.23 us                                                | 7.70 us: 1.07x slower                                        |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                        |
| bench_mp_pool              | 44.9 ms                                                | 49.0 ms: 1.09x slower                                        |
| scimark_sor                | 87.4 ms                                                | 95.5 ms: 1.09x slower                                        |
| coverage                   | 38.9 ms                                                | 44.7 ms: 1.15x slower                                        |
| tornado_http               | 69.3 ms                                                | 85.1 ms: 1.23x slower                                        |
| mypy2                      | 380 ms                                                 | 479 ms: 1.26x slower                                         |
| telco                      | 3.68 ms                                                | 4.69 ms: 1.27x slower                                        |
| create_gc_cycles           | 701 us                                                 | 898 us: 1.28x slower                                         |
| python_startup_no_site     | 9.37 ms                                                | 13.7 ms: 1.46x slower                                        |
| python_startup             | 11.4 ms                                                | 17.2 ms: 1.50x slower                                        |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                 |

Benchmark hidden because not significant (4): gunicorn, meteor_contest, pidigits, aiohttp
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.064x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.79x