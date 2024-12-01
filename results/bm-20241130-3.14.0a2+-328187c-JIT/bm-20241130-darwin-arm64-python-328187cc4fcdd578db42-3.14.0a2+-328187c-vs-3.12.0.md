# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.024x faster
- HPT reliability: 93.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 203 ms: 1.20x slower                                                   |
| docutils       | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 201 ms: 1.28x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 257 ms: 1.26x faster                                                   |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.26x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 252 ms: 1.24x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 593 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 476 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 474 ms: 1.11x faster                                                   |
| async_tree_io              | 668 ms                                                 | 609 ms: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                  |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.01 ms: 1.31x faster                                                  |
| regex_dna      | 154 ms                                                 | 135 ms: 1.14x faster                                                   |
| regex_compile  | 77.9 ms                                                | 71.9 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 126 us: 1.20x faster                                                   |
| xml_etree_process    | 39.7 ms                                                | 35.7 ms: 1.11x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.10x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 50.7 ms: 1.10x faster                                                  |
| json_loads           | 17.2 us                                                | 16.5 us: 1.04x faster                                                  |
| pickle_pure_python   | 200 us                                                 | 195 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 74.0 ms                                                | 74.5 ms: 1.01x slower                                                  |
| xml_etree_parse      | 106 ms                                                 | 110 ms: 1.03x slower                                                   |
| json_dumps           | 6.22 ms                                                | 7.21 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.7 ms: 1.67x slower                                                  |
| python_startup         | 11.4 ms                                                | 20.5 ms: 1.80x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.73x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.24 ms: 1.24x faster                                                  |
| django_template | 22.3 ms                                                | 23.0 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 17.5 us: 1.58x faster                                                  |
| deepcopy                   | 235 us                                                 | 161 us: 1.46x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.01 ms: 1.31x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.58 us: 1.31x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 201 ms: 1.28x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 257 ms: 1.26x faster                                                   |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.26x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 252 ms: 1.24x faster                                                   |
| mako                       | 7.71 ms                                                | 6.24 ms: 1.24x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 126 us: 1.20x faster                                                   |
| generators                 | 31.1 ms                                                | 26.8 ms: 1.16x faster                                                  |
| raytrace                   | 212 ms                                                 | 183 ms: 1.16x faster                                                   |
| regex_dna                  | 154 ms                                                 | 135 ms: 1.14x faster                                                   |
| float                      | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 593 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 476 ms: 1.12x faster                                                   |
| xml_etree_process          | 39.7 ms                                                | 35.7 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 474 ms: 1.11x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.10x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 50.7 ms: 1.10x faster                                                  |
| async_tree_io              | 668 ms                                                 | 609 ms: 1.10x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 69.6 ms: 1.10x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.5 ms: 1.10x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 69.3 ms: 1.10x faster                                                  |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                  |
| regex_compile              | 77.9 ms                                                | 71.9 ms: 1.08x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.40 us: 1.08x faster                                                  |
| json                       | 3.09 ms                                                | 2.85 ms: 1.08x faster                                                  |
| logging_format             | 3.98 us                                                | 3.72 us: 1.07x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.7 ms: 1.07x faster                                                  |
| comprehensions             | 14.5 us                                                | 13.7 us: 1.07x faster                                                  |
| scimark_fft                | 195 ms                                                 | 186 ms: 1.05x faster                                                   |
| sqlalchemy_declarative     | 62.3 ms                                                | 59.6 ms: 1.05x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.04x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.61 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 482 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.01 sec                                               | 982 ms: 1.03x faster                                                   |
| bench_thread_pool          | 504 us                                                 | 492 us: 1.02x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 195 us: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.07 ms: 1.02x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 76.9 ms: 1.01x faster                                                  |
| sympy_str                  | 148 ms                                                 | 147 ms: 1.01x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.56 us: 1.00x faster                                                  |
| go                         | 102 ms                                                 | 101 ms: 1.00x faster                                                   |
| nqueens                    | 62.4 ms                                                | 62.6 ms: 1.00x slower                                                  |
| mdp                        | 1.58 sec                                               | 1.59 sec: 1.00x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 87.8 ms: 1.00x slower                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 74.5 ms: 1.01x slower                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 45.3 ms: 1.01x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                 |
| chaos                      | 42.5 ms                                                | 43.4 ms: 1.02x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 73.3 ms: 1.02x slower                                                  |
| sympy_expand               | 241 ms                                                 | 248 ms: 1.03x slower                                                   |
| django_template            | 22.3 ms                                                | 23.0 ms: 1.03x slower                                                  |
| xml_etree_parse            | 106 ms                                                 | 110 ms: 1.03x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 35.3 ms: 1.04x slower                                                  |
| pyflate                    | 316 ms                                                 | 327 ms: 1.04x slower                                                   |
| sqlglot_parse              | 848 us                                                 | 880 us: 1.04x slower                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.06 ms: 1.04x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 54.8 ms: 1.06x slower                                                  |
| sqlglot_normalize          | 186 ms                                                 | 197 ms: 1.06x slower                                                   |
| richards                   | 32.1 ms                                                | 34.2 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 99.1 us: 1.07x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.1 ms: 1.07x slower                                                  |
| richards_super             | 36.0 ms                                                | 38.4 ms: 1.07x slower                                                  |
| hexiom                     | 4.54 ms                                                | 4.97 ms: 1.09x slower                                                  |
| fannkuch                   | 248 ms                                                 | 284 ms: 1.14x slower                                                   |
| coverage                   | 38.9 ms                                                | 44.9 ms: 1.16x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.21 ms: 1.16x slower                                                  |
| 2to3                       | 169 ms                                                 | 203 ms: 1.20x slower                                                   |
| gc_traversal               | 2.40 ms                                                | 2.96 ms: 1.23x slower                                                  |
| telco                      | 3.68 ms                                                | 4.54 ms: 1.23x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 61.9 ms: 1.38x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 15.7 ms: 1.67x slower                                                  |
| python_startup             | 11.4 ms                                                | 20.5 ms: 1.80x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.32 ms: 1.88x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (6): async_generators, logging_silent, regex_v8, sqlalchemy_imperative, dulwich_log, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 93.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.21x