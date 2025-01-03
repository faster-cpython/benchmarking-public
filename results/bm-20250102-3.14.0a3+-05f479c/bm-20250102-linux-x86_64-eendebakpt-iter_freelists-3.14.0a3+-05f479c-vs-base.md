# Results vs. base

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-x86_64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.010x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 253 ms: 1.01x faster                                                 |
| docutils       | 2.60 sec                                                               | 2.57 sec: 1.01x faster                                               |
| html5lib       | 62.7 ms                                                                | 60.6 ms: 1.03x faster                                                |
| sphinx         | 1.01 sec                                                               | 989 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                 | 25.0 ms                                                                | 23.3 ms: 1.07x faster                                                |
| async_tree_cpu_io_mixed    | 488 ms                                                                 | 480 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 472 ms                                                                 | 467 ms: 1.01x faster                                                 |
| async_tree_memoization     | 326 ms                                                                 | 323 ms: 1.01x faster                                                 |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (7): async_tree_none, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.6 ms                                                                | 94.1 ms: 1.04x faster                                                |
| pidigits       | 190 ms                                                                 | 189 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                 | 204 ms: 1.09x faster                                                 |
| regex_effbot   | 3.47 ms                                                                | 3.32 ms: 1.05x faster                                                |
| regex_compile  | 127 ms                                                                 | 125 ms: 1.01x faster                                                 |
| regex_v8       | 25.4 ms                                                                | 25.1 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process    | 59.4 ms                                                                | 58.0 ms: 1.02x faster                                                |
| xml_etree_generate   | 85.1 ms                                                                | 83.2 ms: 1.02x faster                                                |
| xml_etree_iterparse  | 97.4 ms                                                                | 96.0 ms: 1.01x faster                                                |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                 |
| xml_etree_parse      | 138 ms                                                                 | 137 ms: 1.01x faster                                                 |
| tomli_loads          | 1.97 sec                                                               | 1.96 sec: 1.01x faster                                               |
| json_dumps           | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                |
| json_loads           | 26.3 us                                                                | 26.9 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.02 ms: 1.00x faster                                                |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.7 ms                                                                | 21.9 ms: 1.03x faster                                                |
| genshi_xml      | 50.2 ms                                                                | 49.4 ms: 1.02x faster                                                |
| django_template | 31.6 ms                                                                | 31.4 ms: 1.00x faster                                                |
| mako            | 11.4 ms                                                                | 11.8 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna                  | 221 ms                                                                 | 204 ms: 1.09x faster                                                 |
| coroutines                 | 25.0 ms                                                                | 23.3 ms: 1.07x faster                                                |
| regex_effbot               | 3.47 ms                                                                | 3.32 ms: 1.05x faster                                                |
| gc_traversal               | 4.97 ms                                                                | 4.78 ms: 1.04x faster                                                |
| sqlglot_optimize           | 52.7 ms                                                                | 50.8 ms: 1.04x faster                                                |
| nbody                      | 97.6 ms                                                                | 94.1 ms: 1.04x faster                                                |
| html5lib                   | 62.7 ms                                                                | 60.6 ms: 1.03x faster                                                |
| genshi_text                | 22.7 ms                                                                | 21.9 ms: 1.03x faster                                                |
| sqlglot_normalize          | 104 ms                                                                 | 101 ms: 1.03x faster                                                 |
| bpe_tokeniser              | 4.57 sec                                                               | 4.45 sec: 1.03x faster                                               |
| xml_etree_process          | 59.4 ms                                                                | 58.0 ms: 1.02x faster                                                |
| hexiom                     | 6.39 ms                                                                | 6.24 ms: 1.02x faster                                                |
| fannkuch                   | 413 ms                                                                 | 403 ms: 1.02x faster                                                 |
| sphinx                     | 1.01 sec                                                               | 989 ms: 1.02x faster                                                 |
| xml_etree_generate         | 85.1 ms                                                                | 83.2 ms: 1.02x faster                                                |
| deltablue                  | 3.27 ms                                                                | 3.21 ms: 1.02x faster                                                |
| generators                 | 28.0 ms                                                                | 27.4 ms: 1.02x faster                                                |
| sqlite_synth               | 2.85 us                                                                | 2.80 us: 1.02x faster                                                |
| sympy_expand               | 456 ms                                                                 | 447 ms: 1.02x faster                                                 |
| logging_format             | 6.30 us                                                                | 6.19 us: 1.02x faster                                                |
| pathlib                    | 16.1 ms                                                                | 15.8 ms: 1.02x faster                                                |
| telco                      | 7.77 ms                                                                | 7.64 ms: 1.02x faster                                                |
| go                         | 117 ms                                                                 | 115 ms: 1.02x faster                                                 |
| sympy_integrate            | 19.9 ms                                                                | 19.5 ms: 1.02x faster                                                |
| deepcopy_reduce            | 2.66 us                                                                | 2.61 us: 1.02x faster                                                |
| genshi_xml                 | 50.2 ms                                                                | 49.4 ms: 1.02x faster                                                |
| comprehensions             | 17.0 us                                                                | 16.7 us: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 488 ms                                                                 | 480 ms: 1.02x faster                                                 |
| chaos                      | 60.8 ms                                                                | 59.8 ms: 1.02x faster                                                |
| spectral_norm              | 105 ms                                                                 | 104 ms: 1.02x faster                                                 |
| connected_components       | 442 ms                                                                 | 435 ms: 1.02x faster                                                 |
| richards_super             | 51.4 ms                                                                | 50.6 ms: 1.02x faster                                                |
| richards                   | 44.8 ms                                                                | 44.2 ms: 1.02x faster                                                |
| regex_compile              | 127 ms                                                                 | 125 ms: 1.01x faster                                                 |
| xml_etree_iterparse        | 97.4 ms                                                                | 96.0 ms: 1.01x faster                                                |
| regex_v8                   | 25.4 ms                                                                | 25.1 ms: 1.01x faster                                                |
| pyflate                    | 478 ms                                                                 | 472 ms: 1.01x faster                                                 |
| nqueens                    | 80.0 ms                                                                | 78.9 ms: 1.01x faster                                                |
| crypto_pyaes               | 72.2 ms                                                                | 71.2 ms: 1.01x faster                                                |
| docutils                   | 2.60 sec                                                               | 2.57 sec: 1.01x faster                                               |
| typing_runtime_protocols   | 159 us                                                                 | 158 us: 1.01x faster                                                 |
| shortest_path              | 478 ms                                                                 | 473 ms: 1.01x faster                                                 |
| many_optionals             | 948 us                                                                 | 937 us: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 472 ms                                                                 | 467 ms: 1.01x faster                                                 |
| logging_simple             | 5.71 us                                                                | 5.66 us: 1.01x faster                                                |
| mdp                        | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                               |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                 |
| sqlglot_transpile          | 1.59 ms                                                                | 1.58 ms: 1.01x faster                                                |
| pprint_pformat             | 1.50 sec                                                               | 1.48 sec: 1.01x faster                                               |
| sympy_sum                  | 148 ms                                                                 | 147 ms: 1.01x faster                                                 |
| async_tree_memoization     | 326 ms                                                                 | 323 ms: 1.01x faster                                                 |
| xml_etree_parse            | 138 ms                                                                 | 137 ms: 1.01x faster                                                 |
| 2to3                       | 254 ms                                                                 | 253 ms: 1.01x faster                                                 |
| deepcopy                   | 259 us                                                                 | 257 us: 1.01x faster                                                 |
| sympy_str                  | 269 ms                                                                 | 267 ms: 1.01x faster                                                 |
| dulwich_log                | 64.1 ms                                                                | 63.7 ms: 1.01x faster                                                |
| tomli_loads                | 1.97 sec                                                               | 1.96 sec: 1.01x faster                                               |
| bench_thread_pool          | 864 us                                                                 | 859 us: 1.01x faster                                                 |
| logging_silent             | 107 ns                                                                 | 107 ns: 1.00x faster                                                 |
| django_template            | 31.6 ms                                                                | 31.4 ms: 1.00x faster                                                |
| sqlglot_parse              | 1.27 ms                                                                | 1.27 ms: 1.00x faster                                                |
| python_startup_no_site     | 7.05 ms                                                                | 7.02 ms: 1.00x faster                                                |
| raytrace                   | 271 ms                                                                 | 270 ms: 1.00x faster                                                 |
| pidigits                   | 190 ms                                                                 | 189 ms: 1.00x faster                                                 |
| sqlalchemy_declarative     | 128 ms                                                                 | 128 ms: 1.00x faster                                                 |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| create_gc_cycles           | 2.45 ms                                                                | 2.46 ms: 1.00x slower                                                |
| scimark_lu                 | 116 ms                                                                 | 117 ms: 1.01x slower                                                 |
| deepcopy_memo              | 30.6 us                                                                | 30.9 us: 1.01x slower                                                |
| json_dumps                 | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                |
| json                       | 4.91 ms                                                                | 4.98 ms: 1.01x slower                                                |
| scimark_fft                | 348 ms                                                                 | 355 ms: 1.02x slower                                                 |
| coverage                   | 82.9 ms                                                                | 84.6 ms: 1.02x slower                                                |
| json_loads                 | 26.3 us                                                                | 26.9 us: 1.02x slower                                                |
| mako                       | 11.4 ms                                                                | 11.8 ms: 1.03x slower                                                |
| scimark_sparse_mat_mult    | 4.71 ms                                                                | 4.94 ms: 1.05x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (22): async_tree_none, async_tree_io, mypy2, pylint, float, k_core, async_tree_io_tg, bench_mp_pool, djangocms, pickle_pure_python, async_tree_memoization_tg, scimark_sor, pprint_safe_repr, subparsers, sqlalchemy_imperative, asyncio_websockets, meteor_contest, async_tree_none_tg, async_generators, thrift, scimark_monte_carlo, pycparser

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x