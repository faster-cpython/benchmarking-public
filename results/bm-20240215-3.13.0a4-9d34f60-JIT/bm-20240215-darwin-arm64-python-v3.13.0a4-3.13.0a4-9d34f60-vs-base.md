# Results vs. base

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.01x slower
- HPT reliability: 94.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 6.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| 2to3           | 172 ms                                                                                               | 190 ms: 1.11x slower                                                                                     |
| docutils       | 1.45 sec                                                                                             | 1.48 sec: 1.02x slower                                                                                   |
| Geometric mean | (ref)                                                                                                | 1.03x slower                                                                                             |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|--------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg   | 672 ms                                                                                               | 666 ms: 1.01x faster                                                                                     |
| async_tree_io      | 704 ms                                                                                               | 699 ms: 1.01x faster                                                                                     |
| async_tree_none_tg | 260 ms                                                                                               | 259 ms: 1.00x faster                                                                                     |
| Geometric mean     | (ref)                                                                                                | 1.01x faster                                                                                             |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| float          | 56.6 ms                                                                                              | 55.5 ms: 1.02x faster                                                                                    |
| nbody          | 74.3 ms                                                                                              | 75.9 ms: 1.02x slower                                                                                    |
| Geometric mean | (ref)                                                                                                | 1.00x slower                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| regex_v8       | 17.1 ms                                                                                              | 17.4 ms: 1.02x slower                                                                                    |
| regex_compile  | 73.5 ms                                                                                              | 75.1 ms: 1.02x slower                                                                                    |
| regex_effbot   | 2.48 ms                                                                                              | 2.54 ms: 1.02x slower                                                                                    |
| regex_dna      | 145 ms                                                                                               | 150 ms: 1.04x slower                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.03x slower                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.55 sec                                                                                             | 1.40 sec: 1.11x faster                                                                                   |
| xml_etree_process    | 39.9 ms                                                                                              | 38.7 ms: 1.03x faster                                                                                    |
| xml_etree_iterparse  | 76.3 ms                                                                                              | 74.8 ms: 1.02x faster                                                                                    |
| json_loads           | 17.0 us                                                                                              | 16.9 us: 1.00x faster                                                                                    |
| xml_etree_generate   | 56.2 ms                                                                                              | 56.1 ms: 1.00x faster                                                                                    |
| json_dumps           | 6.46 ms                                                                                              | 6.48 ms: 1.00x slower                                                                                    |
| unpickle_list        | 3.06 us                                                                                              | 3.10 us: 1.01x slower                                                                                    |
| pickle               | 7.22 us                                                                                              | 7.33 us: 1.01x slower                                                                                    |
| unpickle_pure_python | 154 us                                                                                               | 158 us: 1.02x slower                                                                                     |
| pickle_list          | 2.89 us                                                                                              | 2.99 us: 1.03x slower                                                                                    |
| Geometric mean       | (ref)                                                                                                | 1.01x faster                                                                                             |

Benchmark hidden because not significant (4): unpickle, pickle_pure_python, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                                                              | 13.1 ms: 1.04x slower                                                                                    |
| python_startup_no_site | 11.0 ms                                                                                              | 11.6 ms: 1.05x slower                                                                                    |
| Geometric mean         | (ref)                                                                                                | 1.04x slower                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-----------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| mako      | 7.58 ms                                                                                              | 7.79 ms: 1.03x slower                                                                                    |

All benchmarks:
===============

| Benchmark                | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|--------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| tomli_loads              | 1.55 sec                                                                                             | 1.40 sec: 1.11x faster                                                                                   |
| richards                 | 33.9 ms                                                                                              | 31.9 ms: 1.06x faster                                                                                    |
| richards_super           | 37.4 ms                                                                                              | 35.7 ms: 1.05x faster                                                                                    |
| pyflate                  | 338 ms                                                                                               | 326 ms: 1.04x faster                                                                                     |
| coverage                 | 48.9 ms                                                                                              | 47.5 ms: 1.03x faster                                                                                    |
| xml_etree_process        | 39.9 ms                                                                                              | 38.7 ms: 1.03x faster                                                                                    |
| xml_etree_iterparse      | 76.3 ms                                                                                              | 74.8 ms: 1.02x faster                                                                                    |
| coroutines               | 19.1 ms                                                                                              | 18.7 ms: 1.02x faster                                                                                    |
| float                    | 56.6 ms                                                                                              | 55.5 ms: 1.02x faster                                                                                    |
| generators               | 28.6 ms                                                                                              | 28.3 ms: 1.01x faster                                                                                    |
| async_tree_io_tg         | 672 ms                                                                                               | 666 ms: 1.01x faster                                                                                     |
| json                     | 2.97 ms                                                                                              | 2.95 ms: 1.01x faster                                                                                    |
| async_tree_io            | 704 ms                                                                                               | 699 ms: 1.01x faster                                                                                     |
| typing_runtime_protocols | 71.4 us                                                                                              | 70.9 us: 1.01x faster                                                                                    |
| json_loads               | 17.0 us                                                                                              | 16.9 us: 1.00x faster                                                                                    |
| sqlglot_parse            | 790 us                                                                                               | 787 us: 1.00x faster                                                                                     |
| gc_traversal             | 2.40 ms                                                                                              | 2.39 ms: 1.00x faster                                                                                    |
| async_tree_none_tg       | 260 ms                                                                                               | 259 ms: 1.00x faster                                                                                     |
| pprint_safe_repr         | 517 ms                                                                                               | 515 ms: 1.00x faster                                                                                     |
| create_gc_cycles         | 707 us                                                                                               | 705 us: 1.00x faster                                                                                     |
| xml_etree_generate       | 56.2 ms                                                                                              | 56.1 ms: 1.00x faster                                                                                    |
| asyncio_websockets       | 408 ms                                                                                               | 409 ms: 1.00x slower                                                                                     |
| json_dumps               | 6.46 ms                                                                                              | 6.48 ms: 1.00x slower                                                                                    |
| logging_format           | 3.74 us                                                                                              | 3.76 us: 1.00x slower                                                                                    |
| scimark_lu               | 74.6 ms                                                                                              | 74.8 ms: 1.00x slower                                                                                    |
| telco                    | 4.49 ms                                                                                              | 4.51 ms: 1.00x slower                                                                                    |
| sqlglot_normalize        | 181 ms                                                                                               | 182 ms: 1.01x slower                                                                                     |
| scimark_sor              | 105 ms                                                                                               | 106 ms: 1.01x slower                                                                                     |
| fannkuch                 | 265 ms                                                                                               | 267 ms: 1.01x slower                                                                                     |
| sympy_expand             | 239 ms                                                                                               | 241 ms: 1.01x slower                                                                                     |
| deltablue                | 2.43 ms                                                                                              | 2.45 ms: 1.01x slower                                                                                    |
| sqlglot_transpile        | 964 us                                                                                               | 973 us: 1.01x slower                                                                                     |
| deepcopy                 | 224 us                                                                                               | 226 us: 1.01x slower                                                                                     |
| unpickle_list            | 3.06 us                                                                                              | 3.10 us: 1.01x slower                                                                                    |
| crypto_pyaes             | 48.5 ms                                                                                              | 49.1 ms: 1.01x slower                                                                                    |
| logging_silent           | 69.4 ns                                                                                              | 70.3 ns: 1.01x slower                                                                                    |
| pickle                   | 7.22 us                                                                                              | 7.33 us: 1.01x slower                                                                                    |
| sympy_str                | 139 ms                                                                                               | 141 ms: 1.01x slower                                                                                     |
| docutils                 | 1.45 sec                                                                                             | 1.48 sec: 1.02x slower                                                                                   |
| sqlglot_optimize         | 33.8 ms                                                                                              | 34.4 ms: 1.02x slower                                                                                    |
| meteor_contest           | 73.0 ms                                                                                              | 74.3 ms: 1.02x slower                                                                                    |
| deepcopy_memo            | 25.8 us                                                                                              | 26.3 us: 1.02x slower                                                                                    |
| dulwich_log              | 29.3 ms                                                                                              | 29.8 ms: 1.02x slower                                                                                    |
| async_generators         | 298 ms                                                                                               | 303 ms: 1.02x slower                                                                                     |
| regex_v8                 | 17.1 ms                                                                                              | 17.4 ms: 1.02x slower                                                                                    |
| regex_compile            | 73.5 ms                                                                                              | 75.1 ms: 1.02x slower                                                                                    |
| nbody                    | 74.3 ms                                                                                              | 75.9 ms: 1.02x slower                                                                                    |
| unpickle_pure_python     | 154 us                                                                                               | 158 us: 1.02x slower                                                                                     |
| regex_effbot             | 2.48 ms                                                                                              | 2.54 ms: 1.02x slower                                                                                    |
| bench_thread_pool        | 492 us                                                                                               | 504 us: 1.02x slower                                                                                     |
| nqueens                  | 60.0 ms                                                                                              | 61.6 ms: 1.03x slower                                                                                    |
| mako                     | 7.58 ms                                                                                              | 7.79 ms: 1.03x slower                                                                                    |
| pathlib                  | 24.7 ms                                                                                              | 25.4 ms: 1.03x slower                                                                                    |
| sympy_integrate          | 10.7 ms                                                                                              | 11.1 ms: 1.03x slower                                                                                    |
| pickle_list              | 2.89 us                                                                                              | 2.99 us: 1.03x slower                                                                                    |
| python_startup           | 12.6 ms                                                                                              | 13.1 ms: 1.04x slower                                                                                    |
| scimark_monte_carlo      | 46.9 ms                                                                                              | 48.5 ms: 1.04x slower                                                                                    |
| comprehensions           | 12.1 us                                                                                              | 12.6 us: 1.04x slower                                                                                    |
| regex_dna                | 145 ms                                                                                               | 150 ms: 1.04x slower                                                                                     |
| sympy_sum                | 72.5 ms                                                                                              | 75.3 ms: 1.04x slower                                                                                    |
| mdp                      | 1.55 sec                                                                                             | 1.61 sec: 1.04x slower                                                                                   |
| chaos                    | 39.5 ms                                                                                              | 41.0 ms: 1.04x slower                                                                                    |
| raytrace                 | 169 ms                                                                                               | 176 ms: 1.04x slower                                                                                     |
| scimark_fft              | 203 ms                                                                                               | 213 ms: 1.05x slower                                                                                     |
| go                       | 105 ms                                                                                               | 110 ms: 1.05x slower                                                                                     |
| python_startup_no_site   | 11.0 ms                                                                                              | 11.6 ms: 1.05x slower                                                                                    |
| spectral_norm            | 74.7 ms                                                                                              | 78.8 ms: 1.05x slower                                                                                    |
| scimark_sparse_mat_mult  | 3.11 ms                                                                                              | 3.31 ms: 1.07x slower                                                                                    |
| hexiom                   | 4.52 ms                                                                                              | 4.91 ms: 1.09x slower                                                                                    |
| 2to3                     | 172 ms                                                                                               | 190 ms: 1.11x slower                                                                                     |
| mypy2                    | 456 ms                                                                                               | 577 ms: 1.26x slower                                                                                     |
| Geometric mean           | (ref)                                                                                                | 1.01x slower                                                                                             |

Benchmark hidden because not significant (20): asyncio_tcp, asyncio_tcp_ssl, async_tree_memoization, unpickle, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, pickle_pure_python, pickle_dict, chameleon, logging_simple, sqlite_synth, pidigits, deepcopy_reduce, pprint_pformat, xml_etree_parse, pycparser, bench_mp_pool, tornado_http
Ignored benchmarks (17) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask, unpack_sequence

# HPT report

- Reliability score: 94.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 6.97x