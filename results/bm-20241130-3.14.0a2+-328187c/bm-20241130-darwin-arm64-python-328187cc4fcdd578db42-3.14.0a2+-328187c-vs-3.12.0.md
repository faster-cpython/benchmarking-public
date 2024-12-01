# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.034x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 203 ms: 1.27x faster                                                   |
| async_tree_none            | 266 ms                                                 | 211 ms: 1.26x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 253 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 476 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 608 ms: 1.10x faster                                                   |
| async_tree_io              | 668 ms                                                 | 611 ms: 1.09x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 53.3 ms: 1.05x faster                                                  |
| nbody          | 68.8 ms                                                | 68.6 ms: 1.00x faster                                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.08 ms: 1.27x faster                                                  |
| regex_dna      | 154 ms                                                 | 134 ms: 1.15x faster                                                   |
| regex_compile  | 77.9 ms                                                | 72.1 ms: 1.08x faster                                                  |
| regex_v8       | 16.0 ms                                                | 15.9 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 54.3 ms: 1.03x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 39.2 ms: 1.01x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 154 us: 1.02x slower                                                   |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.03x slower                                                   |
| pickle_pure_python   | 200 us                                                 | 207 us: 1.04x slower                                                   |
| xml_etree_iterparse  | 74.0 ms                                                | 76.9 ms: 1.04x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.53 sec: 1.10x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.28 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.5 ms: 1.65x slower                                                  |
| python_startup         | 11.4 ms                                                | 20.3 ms: 1.78x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.71x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 7.13 ms: 1.08x faster                                                  |
| django_template | 22.3 ms                                                | 20.8 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy                   | 235 us                                                 | 152 us: 1.55x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 18.2 us: 1.52x faster                                                  |
| generators                 | 31.1 ms                                                | 22.5 ms: 1.38x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.59 us: 1.30x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.08 ms: 1.27x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 203 ms: 1.27x faster                                                   |
| async_tree_none            | 266 ms                                                 | 211 ms: 1.26x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                   |
| raytrace                   | 212 ms                                                 | 171 ms: 1.24x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 253 ms: 1.23x faster                                                   |
| comprehensions             | 14.5 us                                                | 12.5 us: 1.16x faster                                                  |
| go                         | 102 ms                                                 | 87.6 ms: 1.16x faster                                                  |
| regex_dna                  | 154 ms                                                 | 134 ms: 1.15x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.29 us: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 476 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                                   |
| logging_format             | 3.98 us                                                | 3.59 us: 1.11x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 608 ms: 1.10x faster                                                   |
| deltablue                  | 2.71 ms                                                | 2.47 ms: 1.10x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.6 ms: 1.09x faster                                                  |
| async_tree_io              | 668 ms                                                 | 611 ms: 1.09x faster                                                   |
| logging_silent             | 76.4 ns                                                | 70.3 ns: 1.09x faster                                                  |
| mako                       | 7.71 ms                                                | 7.13 ms: 1.08x faster                                                  |
| regex_compile              | 77.9 ms                                                | 72.1 ms: 1.08x faster                                                  |
| chaos                      | 42.5 ms                                                | 39.4 ms: 1.08x faster                                                  |
| json                       | 3.09 ms                                                | 2.87 ms: 1.08x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.5 ms: 1.07x faster                                                  |
| django_template            | 22.3 ms                                                | 20.8 ms: 1.07x faster                                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.6 ms: 1.06x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 73.0 ms: 1.06x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 28.1 ms: 1.06x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 475 us: 1.06x faster                                                   |
| async_generators           | 304 ms                                                 | 287 ms: 1.06x faster                                                   |
| nqueens                    | 62.4 ms                                                | 59.1 ms: 1.06x faster                                                  |
| sympy_str                  | 148 ms                                                 | 140 ms: 1.05x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 72.7 ms: 1.05x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 72.4 ms: 1.05x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 808 us: 1.05x faster                                                   |
| float                      | 55.8 ms                                                | 53.3 ms: 1.05x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 983 us: 1.04x faster                                                   |
| mdp                        | 1.58 sec                                               | 1.52 sec: 1.04x faster                                                 |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.44 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.03 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 33.0 ms: 1.03x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 54.3 ms: 1.03x faster                                                  |
| pycparser                  | 677 ms                                                 | 658 ms: 1.03x faster                                                   |
| sqlglot_normalize          | 186 ms                                                 | 181 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 497 ms                                                 | 484 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.01 sec                                               | 984 ms: 1.03x faster                                                   |
| sympy_expand               | 241 ms                                                 | 236 ms: 1.02x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 39.2 ms: 1.01x faster                                                  |
| regex_v8                   | 16.0 ms                                                | 15.9 ms: 1.00x faster                                                  |
| scimark_fft                | 195 ms                                                 | 195 ms: 1.00x faster                                                   |
| nbody                      | 68.8 ms                                                | 68.6 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                                   |
| meteor_contest             | 71.7 ms                                                | 72.4 ms: 1.01x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.5 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 151 us                                                 | 154 us: 1.02x slower                                                   |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.03x slower                                                   |
| richards_super             | 36.0 ms                                                | 37.0 ms: 1.03x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 46.5 ms: 1.03x slower                                                  |
| pickle_pure_python         | 200 us                                                 | 207 us: 1.04x slower                                                   |
| xml_etree_iterparse        | 74.0 ms                                                | 76.9 ms: 1.04x slower                                                  |
| richards                   | 32.1 ms                                                | 33.5 ms: 1.04x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 54.3 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 98.2 us: 1.06x slower                                                  |
| pyflate                    | 316 ms                                                 | 338 ms: 1.07x slower                                                   |
| fannkuch                   | 248 ms                                                 | 269 ms: 1.08x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.53 sec: 1.10x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.2 ms: 1.14x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 101 ms: 1.15x slower                                                   |
| json_dumps                 | 6.22 ms                                                | 7.28 ms: 1.17x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.95 ms: 1.23x slower                                                  |
| telco                      | 3.68 ms                                                | 4.58 ms: 1.24x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 61.7 ms: 1.38x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 15.5 ms: 1.65x slower                                                  |
| python_startup             | 11.4 ms                                                | 20.3 ms: 1.78x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.30 ms: 1.86x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (2): 2to3, hexiom
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.18x