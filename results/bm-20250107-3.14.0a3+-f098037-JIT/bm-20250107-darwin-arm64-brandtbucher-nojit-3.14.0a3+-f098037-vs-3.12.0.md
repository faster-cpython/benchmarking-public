# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.079x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 165 ms: 1.03x faster                                          |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.04x faster                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 352 ms: 1.90x faster                                          |
| async_tree_io              | 668 ms                                                 | 366 ms: 1.82x faster                                          |
| async_tree_none_tg         | 258 ms                                                 | 149 ms: 1.73x faster                                          |
| async_tree_memoization_tg  | 323 ms                                                 | 188 ms: 1.72x faster                                          |
| async_tree_none            | 266 ms                                                 | 159 ms: 1.67x faster                                          |
| async_tree_memoization     | 312 ms                                                 | 200 ms: 1.56x faster                                          |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 408 ms: 1.31x faster                                          |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 420 ms: 1.25x faster                                          |
| Geometric mean             | (ref)                                                  | 1.60x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.6 ms: 1.25x faster                                         |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                         |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.01 ms: 1.31x faster                                         |
| regex_compile  | 77.9 ms                                                | 67.6 ms: 1.15x faster                                         |
| regex_dna      | 154 ms                                                 | 136 ms: 1.14x faster                                          |
| regex_v8       | 16.0 ms                                                | 15.9 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 124 us: 1.22x faster                                          |
| tomli_loads          | 1.39 sec                                               | 1.18 sec: 1.18x faster                                        |
| xml_etree_generate   | 55.8 ms                                                | 50.0 ms: 1.12x faster                                         |
| xml_etree_process    | 39.7 ms                                                | 35.5 ms: 1.12x faster                                         |
| pickle_pure_python   | 200 us                                                 | 187 us: 1.07x faster                                          |
| xml_etree_iterparse  | 74.0 ms                                                | 70.0 ms: 1.06x faster                                         |
| json_loads           | 17.2 us                                                | 16.4 us: 1.05x faster                                         |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.04x faster                                          |
| json_dumps           | 6.22 ms                                                | 7.12 ms: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.8 ms: 1.48x slower                                         |
| python_startup         | 11.4 ms                                                | 18.8 ms: 1.65x slower                                         |
| Geometric mean         | (ref)                                                  | 1.56x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.26 ms: 1.23x faster                                         |
| django_template | 22.3 ms                                                | 22.7 ms: 1.02x slower                                         |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 352 ms: 1.90x faster                                          |
| async_tree_io              | 668 ms                                                 | 366 ms: 1.82x faster                                          |
| async_tree_none_tg         | 258 ms                                                 | 149 ms: 1.73x faster                                          |
| async_tree_memoization_tg  | 323 ms                                                 | 188 ms: 1.72x faster                                          |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                          |
| async_tree_none            | 266 ms                                                 | 159 ms: 1.67x faster                                          |
| deepcopy_memo              | 27.7 us                                                | 17.1 us: 1.61x faster                                         |
| async_tree_memoization     | 312 ms                                                 | 200 ms: 1.56x faster                                          |
| deepcopy                   | 235 us                                                 | 156 us: 1.51x faster                                          |
| deepcopy_reduce            | 2.07 us                                                | 1.55 us: 1.34x faster                                         |
| regex_effbot               | 2.64 ms                                                | 2.01 ms: 1.31x faster                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 408 ms: 1.31x faster                                          |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 420 ms: 1.25x faster                                          |
| float                      | 55.8 ms                                                | 44.6 ms: 1.25x faster                                         |
| spectral_norm              | 76.4 ms                                                | 62.0 ms: 1.23x faster                                         |
| mako                       | 7.71 ms                                                | 6.26 ms: 1.23x faster                                         |
| coroutines                 | 19.2 ms                                                | 15.8 ms: 1.22x faster                                         |
| unpickle_pure_python       | 151 us                                                 | 124 us: 1.22x faster                                          |
| tomli_loads                | 1.39 sec                                               | 1.18 sec: 1.18x faster                                        |
| regex_compile              | 77.9 ms                                                | 67.6 ms: 1.15x faster                                         |
| raytrace                   | 212 ms                                                 | 185 ms: 1.15x faster                                          |
| generators                 | 31.1 ms                                                | 27.1 ms: 1.15x faster                                         |
| scimark_fft                | 195 ms                                                 | 170 ms: 1.15x faster                                          |
| regex_dna                  | 154 ms                                                 | 136 ms: 1.14x faster                                          |
| xml_etree_generate         | 55.8 ms                                                | 50.0 ms: 1.12x faster                                         |
| xml_etree_process          | 39.7 ms                                                | 35.5 ms: 1.12x faster                                         |
| scimark_lu                 | 76.0 ms                                                | 68.7 ms: 1.10x faster                                         |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.87 ms: 1.09x faster                                         |
| deltablue                  | 2.71 ms                                                | 2.49 ms: 1.09x faster                                         |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                         |
| json                       | 3.09 ms                                                | 2.85 ms: 1.08x faster                                         |
| logging_simple             | 3.69 us                                                | 3.40 us: 1.08x faster                                         |
| pickle_pure_python         | 200 us                                                 | 187 us: 1.07x faster                                          |
| scimark_sor                | 87.4 ms                                                | 81.7 ms: 1.07x faster                                         |
| logging_format             | 3.98 us                                                | 3.74 us: 1.06x faster                                         |
| pathlib                    | 24.2 ms                                                | 22.8 ms: 1.06x faster                                         |
| xml_etree_iterparse        | 74.0 ms                                                | 70.0 ms: 1.06x faster                                         |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.9 ms: 1.06x faster                                         |
| go                         | 102 ms                                                 | 96.1 ms: 1.06x faster                                         |
| comprehensions             | 14.5 us                                                | 13.8 us: 1.05x faster                                         |
| dulwich_log                | 29.8 ms                                                | 28.4 ms: 1.05x faster                                         |
| json_loads                 | 17.2 us                                                | 16.4 us: 1.05x faster                                         |
| xml_etree_parse            | 106 ms                                                 | 102 ms: 1.04x faster                                          |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.04x faster                                        |
| pprint_pformat             | 1.01 sec                                               | 977 ms: 1.03x faster                                          |
| sympy_sum                  | 77.6 ms                                                | 75.1 ms: 1.03x faster                                         |
| sympy_str                  | 148 ms                                                 | 143 ms: 1.03x faster                                          |
| nqueens                    | 62.4 ms                                                | 60.5 ms: 1.03x faster                                         |
| 2to3                       | 169 ms                                                 | 165 ms: 1.03x faster                                          |
| pprint_safe_repr           | 497 ms                                                 | 484 ms: 1.03x faster                                          |
| pyflate                    | 316 ms                                                 | 308 ms: 1.03x faster                                          |
| chaos                      | 42.5 ms                                                | 41.9 ms: 1.02x faster                                         |
| bench_thread_pool          | 504 us                                                 | 497 us: 1.01x faster                                          |
| sqlglot_parse              | 848 us                                                 | 837 us: 1.01x faster                                          |
| async_generators           | 304 ms                                                 | 301 ms: 1.01x faster                                          |
| sqlite_synth               | 1.57 us                                                | 1.56 us: 1.01x faster                                         |
| logging_silent             | 76.4 ns                                                | 75.8 ns: 1.01x faster                                         |
| scimark_monte_carlo        | 45.0 ms                                                | 44.7 ms: 1.01x faster                                         |
| sqlglot_transpile          | 1.02 ms                                                | 1.02 ms: 1.00x faster                                         |
| regex_v8                   | 16.0 ms                                                | 15.9 ms: 1.00x faster                                         |
| sympy_expand               | 241 ms                                                 | 242 ms: 1.00x slower                                          |
| sqlglot_optimize           | 34.0 ms                                                | 34.2 ms: 1.00x slower                                         |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                          |
| sqlglot_normalize          | 186 ms                                                 | 188 ms: 1.01x slower                                          |
| meteor_contest             | 71.7 ms                                                | 72.5 ms: 1.01x slower                                         |
| sympy_integrate            | 11.4 ms                                                | 11.5 ms: 1.01x slower                                         |
| mdp                        | 1.58 sec                                               | 1.60 sec: 1.01x slower                                        |
| django_template            | 22.3 ms                                                | 22.7 ms: 1.02x slower                                         |
| crypto_pyaes               | 51.9 ms                                                | 53.3 ms: 1.03x slower                                         |
| richards_super             | 36.0 ms                                                | 37.1 ms: 1.03x slower                                         |
| richards                   | 32.1 ms                                                | 33.4 ms: 1.04x slower                                         |
| typing_runtime_protocols   | 93.0 us                                                | 98.2 us: 1.06x slower                                         |
| hexiom                     | 4.54 ms                                                | 4.87 ms: 1.07x slower                                         |
| fannkuch                   | 248 ms                                                 | 269 ms: 1.08x slower                                          |
| json_dumps                 | 6.22 ms                                                | 7.12 ms: 1.14x slower                                         |
| coverage                   | 38.9 ms                                                | 45.9 ms: 1.18x slower                                         |
| telco                      | 3.68 ms                                                | 4.44 ms: 1.21x slower                                         |
| gc_traversal               | 2.40 ms                                                | 3.07 ms: 1.28x slower                                         |
| bench_mp_pool              | 44.9 ms                                                | 60.5 ms: 1.35x slower                                         |
| mypy2                      | 380 ms                                                 | 521 ms: 1.37x slower                                          |
| python_startup_no_site     | 9.37 ms                                                | 13.8 ms: 1.48x slower                                         |
| python_startup             | 11.4 ms                                                | 18.8 ms: 1.65x slower                                         |
| create_gc_cycles           | 701 us                                                 | 1.27 ms: 1.81x slower                                         |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                  |

Benchmark hidden because not significant (2): pycparser, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.22x