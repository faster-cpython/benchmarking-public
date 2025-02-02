# Results vs. 3.12.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: darwin-arm64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.037x faster
- HPT reliability: 99.20%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 182 ms: 1.07x slower                                                   |
| docutils       | 1.50 sec                                               | 1.55 sec: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.38x faster                                                   |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                                   |
| async_tree_io              | 668 ms                                                 | 581 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 469 ms: 1.13x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 609 ms: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.2 ms: 1.16x faster                                                  |
| nbody          | 68.8 ms                                                | 65.7 ms: 1.05x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 143 ms: 1.08x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.50 ms: 1.06x faster                                                  |
| regex_compile  | 77.9 ms                                                | 74.5 ms: 1.05x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.6 ms: 1.15x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 133 us: 1.13x faster                                                   |
| pickle_pure_python   | 200 us                                                 | 179 us: 1.12x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.12x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 50.4 ms: 1.11x faster                                                  |
| json_loads           | 17.2 us                                                | 16.7 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 72.2 ms: 1.03x faster                                                  |
| json_dumps           | 6.22 ms                                                | 7.15 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.1 ms: 1.61x slower                                                  |
| python_startup         | 11.4 ms                                                | 19.1 ms: 1.68x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.64x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.49 ms: 1.19x faster                                                  |
| django_template | 22.3 ms                                                | 22.7 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 16.8 us: 1.65x faster                                                  |
| deepcopy                   | 235 us                                                 | 153 us: 1.54x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.38x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.34x faster                                                  |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                   |
| raytrace                   | 212 ms                                                 | 169 ms: 1.25x faster                                                   |
| generators                 | 31.1 ms                                                | 25.5 ms: 1.22x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                                   |
| mako                       | 7.71 ms                                                | 6.49 ms: 1.19x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.11 us: 1.18x faster                                                  |
| logging_format             | 3.98 us                                                | 3.39 us: 1.17x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.4 ms: 1.17x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 65.7 ms: 1.16x faster                                                  |
| float                      | 55.8 ms                                                | 48.2 ms: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 581 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 457 ms: 1.15x faster                                                   |
| xml_etree_process          | 39.7 ms                                                | 34.6 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 469 ms: 1.13x faster                                                   |
| unpickle_pure_python       | 151 us                                                 | 133 us: 1.13x faster                                                   |
| deltablue                  | 2.71 ms                                                | 2.39 ms: 1.13x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.12x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.12x faster                                                 |
| comprehensions             | 14.5 us                                                | 13.1 us: 1.11x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 50.4 ms: 1.11x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 609 ms: 1.10x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 69.5 ms: 1.10x faster                                                  |
| logging_silent             | 76.4 ns                                                | 69.9 ns: 1.09x faster                                                  |
| regex_dna                  | 154 ms                                                 | 143 ms: 1.08x faster                                                   |
| pathlib                    | 24.2 ms                                                | 22.5 ms: 1.08x faster                                                  |
| json                       | 3.09 ms                                                | 2.88 ms: 1.07x faster                                                  |
| nqueens                    | 62.4 ms                                                | 58.9 ms: 1.06x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 475 us: 1.06x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.50 ms: 1.06x faster                                                  |
| nbody                      | 68.8 ms                                                | 65.7 ms: 1.05x faster                                                  |
| regex_compile              | 77.9 ms                                                | 74.5 ms: 1.05x faster                                                  |
| async_generators           | 304 ms                                                 | 292 ms: 1.04x faster                                                   |
| json_loads                 | 17.2 us                                                | 16.7 us: 1.03x faster                                                  |
| go                         | 102 ms                                                 | 98.5 ms: 1.03x faster                                                  |
| chaos                      | 42.5 ms                                                | 41.3 ms: 1.03x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 72.2 ms: 1.03x faster                                                  |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                   |
| mdp                        | 1.58 sec                                               | 1.55 sec: 1.02x faster                                                 |
| scimark_sor                | 87.4 ms                                                | 85.9 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.00 sec: 1.01x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 185 ms: 1.00x faster                                                   |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.16 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 45.5 ms: 1.01x slower                                                  |
| django_template            | 22.3 ms                                                | 22.7 ms: 1.01x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 862 us: 1.02x slower                                                   |
| richards_super             | 36.0 ms                                                | 36.7 ms: 1.02x slower                                                  |
| sympy_str                  | 148 ms                                                 | 150 ms: 1.02x slower                                                   |
| sympy_expand               | 241 ms                                                 | 246 ms: 1.02x slower                                                   |
| richards                   | 32.1 ms                                                | 32.9 ms: 1.02x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 79.6 ms: 1.03x slower                                                  |
| pyflate                    | 316 ms                                                 | 324 ms: 1.03x slower                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                  |
| fannkuch                   | 248 ms                                                 | 257 ms: 1.03x slower                                                   |
| docutils                   | 1.50 sec                                               | 1.55 sec: 1.03x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 53.9 ms: 1.04x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 75.1 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 97.5 us: 1.05x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                  |
| 2to3                       | 169 ms                                                 | 182 ms: 1.07x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 37.0 ms: 1.09x slower                                                  |
| hexiom                     | 4.54 ms                                                | 4.99 ms: 1.10x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.5 ms: 1.10x slower                                                  |
| coverage                   | 38.9 ms                                                | 44.1 ms: 1.14x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.15 ms: 1.15x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.94 ms: 1.22x slower                                                  |
| telco                      | 3.68 ms                                                | 4.56 ms: 1.24x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 61.8 ms: 1.38x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 15.1 ms: 1.61x slower                                                  |
| python_startup             | 11.4 ms                                                | 19.1 ms: 1.68x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.31 ms: 1.87x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (4): xml_etree_parse, pycparser, pprint_safe_repr, tornado_http
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 99.20% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x