# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.076x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                                   |
| docutils       | 1.50 sec                                               | 1.40 sec: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 236 ms: 1.37x faster                                                   |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 249 ms: 1.25x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 217 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                   |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 469 ms: 1.14x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 611 ms: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.8 ms: 1.12x faster                                                  |
| nbody          | 68.8 ms                                                | 66.0 ms: 1.04x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.1 ms: 1.14x faster                                                  |
| regex_dna      | 154 ms                                                 | 142 ms: 1.09x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 183 us: 1.09x faster                                                   |
| xml_etree_generate   | 55.8 ms                                                | 52.3 ms: 1.07x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.2 ms: 1.07x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                   |
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                  |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                                   |
| tomli_loads          | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.18 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.3 ms: 1.53x slower                                                  |
| python_startup         | 11.4 ms                                                | 18.9 ms: 1.66x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.59x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                  |
| mako            | 7.71 ms                                                | 6.97 ms: 1.11x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 17.0 us: 1.63x faster                                                  |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                                   |
| generators                 | 31.1 ms                                                | 20.1 ms: 1.55x faster                                                  |
| raytrace                   | 212 ms                                                 | 154 ms: 1.38x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 236 ms: 1.37x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.35x faster                                                  |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                   |
| comprehensions             | 14.5 us                                                | 11.4 us: 1.28x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 249 ms: 1.25x faster                                                   |
| logging_silent             | 76.4 ns                                                | 60.9 ns: 1.25x faster                                                  |
| go                         | 102 ms                                                 | 82.4 ms: 1.23x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.03 us: 1.21x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.24 ms: 1.21x faster                                                  |
| logging_format             | 3.98 us                                                | 3.31 us: 1.21x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 217 ms: 1.19x faster                                                   |
| coroutines                 | 19.2 ms                                                | 16.5 ms: 1.16x faster                                                  |
| chaos                      | 42.5 ms                                                | 36.8 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                   |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.15x faster                                                   |
| regex_compile              | 77.9 ms                                                | 68.1 ms: 1.14x faster                                                  |
| nqueens                    | 62.4 ms                                                | 54.8 ms: 1.14x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 746 us: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 469 ms: 1.14x faster                                                   |
| scimark_lu                 | 76.0 ms                                                | 67.0 ms: 1.13x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 902 us: 1.13x faster                                                   |
| django_template            | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                  |
| float                      | 55.8 ms                                                | 49.8 ms: 1.12x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                                   |
| sqlalchemy_declarative     | 62.3 ms                                                | 56.0 ms: 1.11x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 453 us: 1.11x faster                                                   |
| sympy_sum                  | 77.6 ms                                                | 69.8 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.82 ms: 1.11x faster                                                  |
| mako                       | 7.71 ms                                                | 6.97 ms: 1.11x faster                                                  |
| sympy_str                  | 148 ms                                                 | 134 ms: 1.10x faster                                                   |
| pathlib                    | 24.2 ms                                                | 22.0 ms: 1.10x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.13 ms: 1.10x faster                                                  |
| async_generators           | 304 ms                                                 | 277 ms: 1.10x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 611 ms: 1.10x faster                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 31.1 ms: 1.09x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 183 us: 1.09x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 70.0 ms: 1.09x faster                                                  |
| regex_dna                  | 154 ms                                                 | 142 ms: 1.09x faster                                                   |
| pprint_safe_repr           | 497 ms                                                 | 459 ms: 1.08x faster                                                   |
| pprint_pformat             | 1.01 sec                                               | 935 ms: 1.08x faster                                                   |
| dulwich_log                | 29.8 ms                                                | 27.6 ms: 1.08x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.40 sec: 1.07x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.48 sec: 1.07x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 52.3 ms: 1.07x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.2 ms: 1.07x faster                                                  |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.07x faster                                                   |
| pycparser                  | 677 ms                                                 | 635 ms: 1.07x faster                                                   |
| json                       | 3.09 ms                                                | 2.90 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                   |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                                   |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.36 ms: 1.05x faster                                                  |
| nbody                      | 68.8 ms                                                | 66.0 ms: 1.04x faster                                                  |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.03x faster                                                  |
| richards                   | 32.1 ms                                                | 31.1 ms: 1.03x faster                                                  |
| scimark_fft                | 195 ms                                                 | 192 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 44.2 ms: 1.02x faster                                                  |
| meteor_contest             | 71.7 ms                                                | 70.6 ms: 1.02x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 51.7 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                  |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.01x slower                                                   |
| pyflate                    | 316 ms                                                 | 326 ms: 1.03x slower                                                   |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                 |
| fannkuch                   | 248 ms                                                 | 267 ms: 1.08x slower                                                   |
| scimark_sor                | 87.4 ms                                                | 96.1 ms: 1.10x slower                                                  |
| coverage                   | 38.9 ms                                                | 43.7 ms: 1.13x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.18 ms: 1.15x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.93 ms: 1.22x slower                                                  |
| telco                      | 3.68 ms                                                | 4.59 ms: 1.25x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 59.9 ms: 1.33x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 14.3 ms: 1.53x slower                                                  |
| python_startup             | 11.4 ms                                                | 18.9 ms: 1.66x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.31 ms: 1.87x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (2): typing_runtime_protocols, tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.076x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.17x