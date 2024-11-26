# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.031x faster
- HPT reliability: 94.05%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 184 ms: 1.09x slower                                                   |
| docutils       | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.37x faster                                                   |
| async_tree_none            | 266 ms                                                 | 201 ms: 1.32x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 245 ms: 1.27x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.20x faster                                                   |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 472 ms: 1.13x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 613 ms: 1.09x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.7 ms: 1.15x faster                                                  |
| nbody          | 68.8 ms                                                | 65.9 ms: 1.04x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 143 ms: 1.08x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.48 ms: 1.06x faster                                                  |
| regex_compile  | 77.9 ms                                                | 75.3 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.8 ms: 1.14x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 49.6 ms: 1.13x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 134 us: 1.12x faster                                                   |
| pickle_pure_python   | 200 us                                                 | 179 us: 1.12x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                 |
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                                   |
| json_dumps           | 6.22 ms                                                | 7.13 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.4 ms: 1.54x slower                                                  |
| python_startup         | 11.4 ms                                                | 18.8 ms: 1.65x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.59x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.44 ms: 1.20x faster                                                  |
| django_template | 22.3 ms                                                | 22.9 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 17.1 us: 1.62x faster                                                  |
| deepcopy                   | 235 us                                                 | 155 us: 1.52x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.37x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.55 us: 1.34x faster                                                  |
| async_tree_none            | 266 ms                                                 | 201 ms: 1.32x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 245 ms: 1.27x faster                                                   |
| generators                 | 31.1 ms                                                | 25.3 ms: 1.23x faster                                                  |
| raytrace                   | 212 ms                                                 | 173 ms: 1.23x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.20x faster                                                   |
| mako                       | 7.71 ms                                                | 6.44 ms: 1.20x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.18 us: 1.16x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.6 ms: 1.16x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 65.8 ms: 1.15x faster                                                  |
| logging_format             | 3.98 us                                                | 3.46 us: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                   |
| float                      | 55.8 ms                                                | 48.7 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.14x faster                                                   |
| xml_etree_process          | 39.7 ms                                                | 34.8 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 472 ms: 1.13x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 49.6 ms: 1.13x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.41 ms: 1.12x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 134 us: 1.12x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.12x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                 |
| comprehensions             | 14.5 us                                                | 13.3 us: 1.09x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 613 ms: 1.09x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 70.1 ms: 1.09x faster                                                  |
| regex_dna                  | 154 ms                                                 | 143 ms: 1.08x faster                                                   |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                                  |
| json                       | 3.09 ms                                                | 2.86 ms: 1.08x faster                                                  |
| logging_silent             | 76.4 ns                                                | 70.9 ns: 1.08x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 474 us: 1.06x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.48 ms: 1.06x faster                                                  |
| nqueens                    | 62.4 ms                                                | 58.8 ms: 1.06x faster                                                  |
| nbody                      | 68.8 ms                                                | 65.9 ms: 1.04x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| regex_compile              | 77.9 ms                                                | 75.3 ms: 1.03x faster                                                  |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                                   |
| go                         | 102 ms                                                 | 98.8 ms: 1.03x faster                                                  |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                                   |
| dulwich_log                | 29.8 ms                                                | 29.3 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                  |
| chaos                      | 42.5 ms                                                | 41.9 ms: 1.02x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.56 sec: 1.01x faster                                                 |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.59 ms: 1.01x faster                                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 61.8 ms: 1.01x faster                                                  |
| scimark_sor                | 87.4 ms                                                | 87.0 ms: 1.00x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.02 sec: 1.00x slower                                                 |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| sqlglot_normalize          | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 497 ms                                                 | 502 ms: 1.01x slower                                                   |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.18 ms: 1.01x slower                                                  |
| pycparser                  | 677 ms                                                 | 689 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 45.8 ms: 1.02x slower                                                  |
| django_template            | 22.3 ms                                                | 22.9 ms: 1.02x slower                                                  |
| sympy_str                  | 148 ms                                                 | 152 ms: 1.03x slower                                                   |
| sympy_expand               | 241 ms                                                 | 249 ms: 1.03x slower                                                   |
| sympy_sum                  | 77.6 ms                                                | 80.2 ms: 1.03x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 880 us: 1.04x slower                                                   |
| docutils                   | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.07 ms: 1.05x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 75.2 ms: 1.05x slower                                                  |
| richards_super             | 36.0 ms                                                | 37.8 ms: 1.05x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                  |
| pyflate                    | 316 ms                                                 | 332 ms: 1.05x slower                                                   |
| crypto_pyaes               | 51.9 ms                                                | 54.6 ms: 1.05x slower                                                  |
| fannkuch                   | 248 ms                                                 | 263 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 93.0 us                                                | 98.5 us: 1.06x slower                                                  |
| richards                   | 32.1 ms                                                | 34.0 ms: 1.06x slower                                                  |
| 2to3                       | 169 ms                                                 | 184 ms: 1.09x slower                                                   |
| hexiom                     | 4.54 ms                                                | 5.00 ms: 1.10x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 37.7 ms: 1.11x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.6 ms: 1.11x slower                                                  |
| coverage                   | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.13 ms: 1.15x slower                                                  |
| telco                      | 3.68 ms                                                | 4.45 ms: 1.21x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.94 ms: 1.22x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 62.2 ms: 1.39x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 14.4 ms: 1.54x slower                                                  |
| python_startup             | 11.4 ms                                                | 18.8 ms: 1.65x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.32 ms: 1.88x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 94.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x