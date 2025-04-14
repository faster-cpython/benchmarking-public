# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.024x faster
- HPT reliability: 82.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 190 ms: 1.01x slower                                       |
| chameleon      | 5.08 ms                                                | 4.81 ms: 1.06x faster                                      |
| docutils       | 1.44 sec                                               | 1.48 sec: 1.03x slower                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 19.8 ms                                                | 18.7 ms: 1.05x faster                                      |
| async_generators           | 295 ms                                                 | 303 ms: 1.03x slower                                       |
| async_tree_memoization_tg  | 288 ms                                                 | 322 ms: 1.12x slower                                       |
| async_tree_cpu_io_mixed    | 460 ms                                                 | 519 ms: 1.13x slower                                       |
| async_tree_none            | 215 ms                                                 | 252 ms: 1.17x slower                                       |
| async_tree_cpu_io_mixed_tg | 448 ms                                                 | 530 ms: 1.18x slower                                       |
| async_tree_memoization     | 268 ms                                                 | 328 ms: 1.22x slower                                       |
| async_tree_none_tg         | 198 ms                                                 | 259 ms: 1.31x slower                                       |
| async_tree_io_tg           | 497 ms                                                 | 666 ms: 1.34x slower                                       |
| async_tree_io              | 507 ms                                                 | 699 ms: 1.38x slower                                       |
| asyncio_websockets         | 242 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean             | (ref)                                                  | 1.21x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.0 ms                                                | 55.5 ms: 1.01x faster                                      |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| nbody          | 74.0 ms                                                | 75.9 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 75.1 ms: 1.05x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.54 ms: 1.04x faster                                      |
| regex_dna      | 149 ms                                                 | 150 ms: 1.01x slower                                       |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.40 sec: 1.12x faster                                     |
| pickle_pure_python   | 214 us                                                 | 196 us: 1.10x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 38.7 ms: 1.06x faster                                      |
| unpickle_pure_python | 164 us                                                 | 158 us: 1.04x faster                                       |
| xml_etree_generate   | 57.0 ms                                                | 56.1 ms: 1.02x faster                                      |
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| json_dumps           | 6.52 ms                                                | 6.48 ms: 1.01x faster                                      |
| json_loads           | 17.0 us                                                | 16.9 us: 1.00x faster                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 74.8 ms: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 13.1 ms: 1.44x faster                                      |
| python_startup_no_site | 14.5 ms                                                | 11.6 ms: 1.25x faster                                      |
| Geometric mean         | (ref)                                                  | 1.35x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.68 ms                                                | 7.79 ms: 1.01x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| dask                       | 790 ms                                                 | 335 ms: 2.36x faster                                       |
| create_gc_cycles           | 1.17 ms                                                | 705 us: 1.66x faster                                       |
| python_startup             | 18.9 ms                                                | 13.1 ms: 1.44x faster                                      |
| typing_runtime_protocols   | 101 us                                                 | 70.9 us: 1.43x faster                                      |
| bench_mp_pool              | 62.5 ms                                                | 45.9 ms: 1.36x faster                                      |
| python_startup_no_site     | 14.5 ms                                                | 11.6 ms: 1.25x faster                                      |
| gc_traversal               | 2.91 ms                                                | 2.39 ms: 1.22x faster                                      |
| mypy2                      | 701 ms                                                 | 577 ms: 1.22x faster                                       |
| tomli_loads                | 1.57 sec                                               | 1.40 sec: 1.12x faster                                     |
| generators                 | 31.5 ms                                                | 28.3 ms: 1.11x faster                                      |
| crypto_pyaes               | 54.2 ms                                                | 49.1 ms: 1.10x faster                                      |
| richards                   | 35.2 ms                                                | 31.9 ms: 1.10x faster                                      |
| richards_super             | 39.1 ms                                                | 35.7 ms: 1.10x faster                                      |
| pickle_pure_python         | 214 us                                                 | 196 us: 1.10x faster                                       |
| deltablue                  | 2.68 ms                                                | 2.45 ms: 1.09x faster                                      |
| sqlglot_parse              | 856 us                                                 | 787 us: 1.09x faster                                       |
| pyflate                    | 351 ms                                                 | 326 ms: 1.08x faster                                       |
| fannkuch                   | 284 ms                                                 | 267 ms: 1.06x faster                                       |
| xml_etree_process          | 41.0 ms                                                | 38.7 ms: 1.06x faster                                      |
| telco                      | 4.76 ms                                                | 4.51 ms: 1.06x faster                                      |
| chameleon                  | 5.08 ms                                                | 4.81 ms: 1.06x faster                                      |
| coroutines                 | 19.8 ms                                                | 18.7 ms: 1.05x faster                                      |
| sqlglot_transpile          | 1.02 ms                                                | 973 us: 1.05x faster                                       |
| regex_compile              | 78.6 ms                                                | 75.1 ms: 1.05x faster                                      |
| deepcopy                   | 237 us                                                 | 226 us: 1.05x faster                                       |
| logging_simple             | 3.60 us                                                | 3.45 us: 1.04x faster                                      |
| go                         | 115 ms                                                 | 110 ms: 1.04x faster                                       |
| deepcopy_reduce            | 2.07 us                                                | 1.98 us: 1.04x faster                                      |
| deepcopy_memo              | 27.4 us                                                | 26.3 us: 1.04x faster                                      |
| unpickle_pure_python       | 164 us                                                 | 158 us: 1.04x faster                                       |
| scimark_monte_carlo        | 50.4 ms                                                | 48.5 ms: 1.04x faster                                      |
| sqlglot_normalize          | 189 ms                                                 | 182 ms: 1.04x faster                                       |
| logging_format             | 3.89 us                                                | 3.76 us: 1.04x faster                                      |
| regex_effbot               | 2.63 ms                                                | 2.54 ms: 1.04x faster                                      |
| pprint_safe_repr           | 533 ms                                                 | 515 ms: 1.03x faster                                       |
| pprint_pformat             | 1.08 sec                                               | 1.05 sec: 1.03x faster                                     |
| sympy_str                  | 145 ms                                                 | 141 ms: 1.03x faster                                       |
| json                       | 3.03 ms                                                | 2.95 ms: 1.03x faster                                      |
| raytrace                   | 181 ms                                                 | 176 ms: 1.03x faster                                       |
| scimark_lu                 | 76.7 ms                                                | 74.8 ms: 1.02x faster                                      |
| sympy_expand               | 246 ms                                                 | 241 ms: 1.02x faster                                       |
| sympy_integrate            | 11.3 ms                                                | 11.1 ms: 1.02x faster                                      |
| pycparser                  | 705 ms                                                 | 693 ms: 1.02x faster                                       |
| xml_etree_generate         | 57.0 ms                                                | 56.1 ms: 1.02x faster                                      |
| nqueens                    | 62.5 ms                                                | 61.6 ms: 1.02x faster                                      |
| xml_etree_parse            | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| sqlglot_optimize           | 34.9 ms                                                | 34.4 ms: 1.01x faster                                      |
| float                      | 56.0 ms                                                | 55.5 ms: 1.01x faster                                      |
| json_dumps                 | 6.52 ms                                                | 6.48 ms: 1.01x faster                                      |
| chaos                      | 41.2 ms                                                | 41.0 ms: 1.00x faster                                      |
| pidigits                   | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| json_loads                 | 17.0 us                                                | 16.9 us: 1.00x faster                                      |
| logging_silent             | 70.1 ns                                                | 70.3 ns: 1.00x slower                                      |
| meteor_contest             | 74.0 ms                                                | 74.3 ms: 1.00x slower                                      |
| regex_dna                  | 149 ms                                                 | 150 ms: 1.01x slower                                       |
| hexiom                     | 4.86 ms                                                | 4.91 ms: 1.01x slower                                      |
| mako                       | 7.68 ms                                                | 7.79 ms: 1.01x slower                                      |
| 2to3                       | 187 ms                                                 | 190 ms: 1.01x slower                                       |
| xml_etree_iterparse        | 73.6 ms                                                | 74.8 ms: 1.02x slower                                      |
| regex_v8                   | 17.0 ms                                                | 17.4 ms: 1.02x slower                                      |
| nbody                      | 74.0 ms                                                | 75.9 ms: 1.03x slower                                      |
| comprehensions             | 12.3 us                                                | 12.6 us: 1.03x slower                                      |
| async_generators           | 295 ms                                                 | 303 ms: 1.03x slower                                       |
| docutils                   | 1.44 sec                                               | 1.48 sec: 1.03x slower                                     |
| spectral_norm              | 76.3 ms                                                | 78.8 ms: 1.03x slower                                      |
| coverage                   | 46.0 ms                                                | 47.5 ms: 1.03x slower                                      |
| dulwich_log                | 28.5 ms                                                | 29.8 ms: 1.05x slower                                      |
| scimark_fft                | 201 ms                                                 | 213 ms: 1.06x slower                                       |
| mdp                        | 1.49 sec                                               | 1.61 sec: 1.08x slower                                     |
| pathlib                    | 23.4 ms                                                | 25.4 ms: 1.09x slower                                      |
| scimark_sparse_mat_mult    | 2.99 ms                                                | 3.31 ms: 1.11x slower                                      |
| async_tree_memoization_tg  | 288 ms                                                 | 322 ms: 1.12x slower                                       |
| async_tree_cpu_io_mixed    | 460 ms                                                 | 519 ms: 1.13x slower                                       |
| async_tree_none            | 215 ms                                                 | 252 ms: 1.17x slower                                       |
| async_tree_cpu_io_mixed_tg | 448 ms                                                 | 530 ms: 1.18x slower                                       |
| async_tree_memoization     | 268 ms                                                 | 328 ms: 1.22x slower                                       |
| async_tree_none_tg         | 198 ms                                                 | 259 ms: 1.31x slower                                       |
| async_tree_io_tg           | 497 ms                                                 | 666 ms: 1.34x slower                                       |
| async_tree_io              | 507 ms                                                 | 699 ms: 1.38x slower                                       |
| asyncio_websockets         | 242 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (4): tornado_http, bench_thread_pool, sympy_sum, scimark_sor
Ignored benchmarks (22) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (9) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.024x faster
# HPT report

- Reliability score: 82.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x