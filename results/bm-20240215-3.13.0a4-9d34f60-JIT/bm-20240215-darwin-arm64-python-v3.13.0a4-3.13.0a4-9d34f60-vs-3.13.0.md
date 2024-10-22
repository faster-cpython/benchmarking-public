# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.00x slower
- HPT reliability: 56.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 5.78x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 190 ms: 1.07x slower                                       |
| chameleon      | 5.08 ms                                                | 4.81 ms: 1.06x faster                                      |
| docutils       | 1.44 sec                                               | 1.48 sec: 1.02x slower                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_tcp                | 457 ms                                                 | 401 ms: 1.14x faster                                       |
| coroutines                 | 19.8 ms                                                | 18.7 ms: 1.06x faster                                      |
| async_generators           | 294 ms                                                 | 303 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.26 sec                                               | 1.31 sec: 1.03x slower                                     |
| async_tree_memoization_tg  | 291 ms                                                 | 322 ms: 1.11x slower                                       |
| async_tree_cpu_io_mixed    | 460 ms                                                 | 519 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed_tg | 447 ms                                                 | 530 ms: 1.19x slower                                       |
| async_tree_none            | 212 ms                                                 | 252 ms: 1.19x slower                                       |
| async_tree_memoization     | 270 ms                                                 | 328 ms: 1.21x slower                                       |
| async_tree_none_tg         | 198 ms                                                 | 259 ms: 1.30x slower                                       |
| async_tree_io_tg           | 500 ms                                                 | 666 ms: 1.33x slower                                       |
| async_tree_io              | 507 ms                                                 | 699 ms: 1.38x slower                                       |
| asyncio_websockets         | 241 ms                                                 | 409 ms: 1.70x slower                                       |
| Geometric mean             | (ref)                                                  | 1.17x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.2 ms                                                | 55.5 ms: 1.01x faster                                      |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| nbody          | 73.9 ms                                                | 75.9 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 75.1 ms: 1.05x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.54 ms: 1.04x faster                                      |
| regex_dna      | 148 ms                                                 | 150 ms: 1.02x slower                                       |
| regex_v8       | 16.9 ms                                                | 17.4 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.40 sec: 1.11x faster                                     |
| pickle_pure_python   | 213 us                                                 | 196 us: 1.09x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 38.7 ms: 1.06x faster                                      |
| unpickle_pure_python | 163 us                                                 | 158 us: 1.03x faster                                       |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.03x faster                                       |
| json_dumps           | 6.56 ms                                                | 6.48 ms: 1.01x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 56.1 ms: 1.01x faster                                      |
| pickle               | 7.36 us                                                | 7.33 us: 1.00x faster                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 74.8 ms: 1.01x slower                                      |
| unpickle_list        | 2.93 us                                                | 3.10 us: 1.06x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (4): pickle_list, pickle_dict, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 13.1 ms: 1.30x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 11.6 ms: 1.18x faster                                      |
| Geometric mean         | (ref)                                                  | 1.24x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.68 ms                                                | 7.79 ms: 1.01x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 101 us                                                 | 70.9 us: 1.42x faster                                      |
| python_startup             | 17.0 ms                                                | 13.1 ms: 1.30x faster                                      |
| unpack_sequence            | 36.1 ns                                                | 28.4 ns: 1.27x faster                                      |
| python_startup_no_site     | 13.7 ms                                                | 11.6 ms: 1.18x faster                                      |
| asyncio_tcp                | 457 ms                                                 | 401 ms: 1.14x faster                                       |
| create_gc_cycles           | 803 us                                                 | 705 us: 1.14x faster                                       |
| generators                 | 31.5 ms                                                | 28.3 ms: 1.11x faster                                      |
| tomli_loads                | 1.56 sec                                               | 1.40 sec: 1.11x faster                                     |
| richards                   | 35.4 ms                                                | 31.9 ms: 1.11x faster                                      |
| bench_mp_pool              | 50.9 ms                                                | 45.9 ms: 1.11x faster                                      |
| crypto_pyaes               | 54.0 ms                                                | 49.1 ms: 1.10x faster                                      |
| richards_super             | 39.1 ms                                                | 35.7 ms: 1.10x faster                                      |
| deltablue                  | 2.68 ms                                                | 2.45 ms: 1.09x faster                                      |
| sqlglot_parse              | 856 us                                                 | 787 us: 1.09x faster                                       |
| pickle_pure_python         | 213 us                                                 | 196 us: 1.09x faster                                       |
| pyflate                    | 351 ms                                                 | 326 ms: 1.08x faster                                       |
| telco                      | 4.80 ms                                                | 4.51 ms: 1.07x faster                                      |
| chameleon                  | 5.08 ms                                                | 4.81 ms: 1.06x faster                                      |
| fannkuch                   | 282 ms                                                 | 267 ms: 1.06x faster                                       |
| coroutines                 | 19.8 ms                                                | 18.7 ms: 1.06x faster                                      |
| xml_etree_process          | 40.9 ms                                                | 38.7 ms: 1.06x faster                                      |
| sqlglot_transpile          | 1.02 ms                                                | 973 us: 1.05x faster                                       |
| regex_compile              | 78.5 ms                                                | 75.1 ms: 1.05x faster                                      |
| go                         | 115 ms                                                 | 110 ms: 1.04x faster                                       |
| scimark_monte_carlo        | 50.4 ms                                                | 48.5 ms: 1.04x faster                                      |
| gc_traversal               | 2.48 ms                                                | 2.39 ms: 1.04x faster                                      |
| deepcopy_reduce            | 2.06 us                                                | 1.98 us: 1.04x faster                                      |
| sqlglot_normalize          | 189 ms                                                 | 182 ms: 1.04x faster                                       |
| regex_effbot               | 2.63 ms                                                | 2.54 ms: 1.04x faster                                      |
| logging_simple             | 3.57 us                                                | 3.45 us: 1.04x faster                                      |
| deepcopy_memo              | 27.2 us                                                | 26.3 us: 1.04x faster                                      |
| unpickle_pure_python       | 163 us                                                 | 158 us: 1.03x faster                                       |
| sympy_str                  | 145 ms                                                 | 141 ms: 1.03x faster                                       |
| xml_etree_parse            | 109 ms                                                 | 105 ms: 1.03x faster                                       |
| raytrace                   | 182 ms                                                 | 176 ms: 1.03x faster                                       |
| pprint_safe_repr           | 531 ms                                                 | 515 ms: 1.03x faster                                       |
| pprint_pformat             | 1.08 sec                                               | 1.05 sec: 1.03x faster                                     |
| deepcopy                   | 232 us                                                 | 226 us: 1.03x faster                                       |
| logging_format             | 3.85 us                                                | 3.76 us: 1.03x faster                                      |
| sympy_integrate            | 11.3 ms                                                | 11.1 ms: 1.02x faster                                      |
| scimark_lu                 | 76.5 ms                                                | 74.8 ms: 1.02x faster                                      |
| sympy_expand               | 246 ms                                                 | 241 ms: 1.02x faster                                       |
| nqueens                    | 62.9 ms                                                | 61.6 ms: 1.02x faster                                      |
| pycparser                  | 706 ms                                                 | 693 ms: 1.02x faster                                       |
| sqlglot_optimize           | 34.9 ms                                                | 34.4 ms: 1.02x faster                                      |
| float                      | 56.2 ms                                                | 55.5 ms: 1.01x faster                                      |
| json_dumps                 | 6.56 ms                                                | 6.48 ms: 1.01x faster                                      |
| xml_etree_generate         | 56.6 ms                                                | 56.1 ms: 1.01x faster                                      |
| chaos                      | 41.3 ms                                                | 41.0 ms: 1.01x faster                                      |
| pickle                     | 7.36 us                                                | 7.33 us: 1.00x faster                                      |
| bench_thread_pool          | 506 us                                                 | 504 us: 1.00x faster                                       |
| sympy_sum                  | 75.6 ms                                                | 75.3 ms: 1.00x faster                                      |
| pidigits                   | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| scimark_sor                | 106 ms                                                 | 106 ms: 1.00x faster                                       |
| logging_silent             | 69.9 ns                                                | 70.3 ns: 1.01x slower                                      |
| meteor_contest             | 73.8 ms                                                | 74.3 ms: 1.01x slower                                      |
| xml_etree_iterparse        | 74.2 ms                                                | 74.8 ms: 1.01x slower                                      |
| hexiom                     | 4.85 ms                                                | 4.91 ms: 1.01x slower                                      |
| mako                       | 7.68 ms                                                | 7.79 ms: 1.01x slower                                      |
| regex_dna                  | 148 ms                                                 | 150 ms: 1.02x slower                                       |
| spectral_norm              | 77.3 ms                                                | 78.8 ms: 1.02x slower                                      |
| docutils                   | 1.44 sec                                               | 1.48 sec: 1.02x slower                                     |
| regex_v8                   | 16.9 ms                                                | 17.4 ms: 1.03x slower                                      |
| nbody                      | 73.9 ms                                                | 75.9 ms: 1.03x slower                                      |
| coverage                   | 46.1 ms                                                | 47.5 ms: 1.03x slower                                      |
| sqlite_synth               | 1.54 us                                                | 1.59 us: 1.03x slower                                      |
| async_generators           | 294 ms                                                 | 303 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.26 sec                                               | 1.31 sec: 1.03x slower                                     |
| comprehensions             | 12.2 us                                                | 12.6 us: 1.03x slower                                      |
| dulwich_log                | 28.7 ms                                                | 29.8 ms: 1.04x slower                                      |
| unpickle_list              | 2.93 us                                                | 3.10 us: 1.06x slower                                      |
| scimark_fft                | 201 ms                                                 | 213 ms: 1.06x slower                                       |
| 2to3                       | 178 ms                                                 | 190 ms: 1.07x slower                                       |
| mdp                        | 1.50 sec                                               | 1.61 sec: 1.08x slower                                     |
| scimark_sparse_mat_mult    | 2.99 ms                                                | 3.31 ms: 1.11x slower                                      |
| async_tree_memoization_tg  | 291 ms                                                 | 322 ms: 1.11x slower                                       |
| pathlib                    | 22.8 ms                                                | 25.4 ms: 1.11x slower                                      |
| async_tree_cpu_io_mixed    | 460 ms                                                 | 519 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed_tg | 447 ms                                                 | 530 ms: 1.19x slower                                       |
| async_tree_none            | 212 ms                                                 | 252 ms: 1.19x slower                                       |
| async_tree_memoization     | 270 ms                                                 | 328 ms: 1.21x slower                                       |
| async_tree_none_tg         | 198 ms                                                 | 259 ms: 1.30x slower                                       |
| dask                       | 255 ms                                                 | 335 ms: 1.31x slower                                       |
| async_tree_io_tg           | 500 ms                                                 | 666 ms: 1.33x slower                                       |
| async_tree_io              | 507 ms                                                 | 699 ms: 1.38x slower                                       |
| mypy2                      | 396 ms                                                 | 577 ms: 1.46x slower                                       |
| asyncio_websockets         | 241 ms                                                 | 409 ms: 1.70x slower                                       |
| Geometric mean             | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (6): tornado_http, pickle_list, pickle_dict, json_loads, json, unpickle
Ignored benchmarks (18) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift

# HPT report

- Reliability score: 56.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 5.78x