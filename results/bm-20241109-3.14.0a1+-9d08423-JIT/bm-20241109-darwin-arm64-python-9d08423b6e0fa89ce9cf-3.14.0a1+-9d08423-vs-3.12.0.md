# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.021x faster
- HPT reliability: 85.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 212 ms: 1.25x slower                                                   |
| docutils       | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.34x faster                                                   |
| async_tree_none            | 266 ms                                                 | 206 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.24x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 254 ms: 1.23x faster                                                   |
| async_tree_io              | 668 ms                                                 | 592 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 482 ms: 1.10x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 627 ms: 1.07x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                  |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.33 ms: 1.13x faster                                                  |
| regex_dna      | 154 ms                                                 | 137 ms: 1.12x faster                                                   |
| regex_compile  | 77.9 ms                                                | 76.7 ms: 1.02x faster                                                  |
| regex_v8       | 16.0 ms                                                | 15.9 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                | 49.5 ms: 1.13x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 35.3 ms: 1.12x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                   |
| json_loads           | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| pickle_pure_python   | 200 us                                                 | 194 us: 1.03x faster                                                   |
| xml_etree_iterparse  | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                  |
| json_dumps           | 6.22 ms                                                | 7.10 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.0 ms: 1.49x slower                                                  |
| python_startup         | 11.4 ms                                                | 18.8 ms: 1.65x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.57x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.24 ms: 1.24x faster                                                  |
| django_template | 22.3 ms                                                | 23.5 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 17.6 us: 1.57x faster                                                  |
| deepcopy                   | 235 us                                                 | 157 us: 1.49x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.35x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.34x faster                                                   |
| async_tree_none            | 266 ms                                                 | 206 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.24x faster                                                   |
| mako                       | 7.71 ms                                                | 6.24 ms: 1.24x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 254 ms: 1.23x faster                                                   |
| generators                 | 31.1 ms                                                | 26.9 ms: 1.16x faster                                                  |
| raytrace                   | 212 ms                                                 | 184 ms: 1.15x faster                                                   |
| float                      | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.33 ms: 1.13x faster                                                  |
| async_tree_io              | 668 ms                                                 | 592 ms: 1.13x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 49.5 ms: 1.13x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 35.3 ms: 1.12x faster                                                  |
| regex_dna                  | 154 ms                                                 | 137 ms: 1.12x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.29 us: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 68.7 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 482 ms: 1.10x faster                                                   |
| logging_format             | 3.98 us                                                | 3.61 us: 1.10x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.5 ms: 1.10x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 69.8 ms: 1.09x faster                                                  |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                                  |
| comprehensions             | 14.5 us                                                | 13.5 us: 1.08x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 627 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                   |
| json                       | 3.09 ms                                                | 2.91 ms: 1.06x faster                                                  |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                   |
| logging_silent             | 76.4 ns                                                | 73.5 ns: 1.04x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.6 us: 1.04x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.61 ms: 1.04x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 488 us: 1.03x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 194 us: 1.03x faster                                                   |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.06 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 487 ms: 1.02x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                  |
| regex_compile              | 77.9 ms                                                | 76.7 ms: 1.02x faster                                                  |
| nqueens                    | 62.4 ms                                                | 61.7 ms: 1.01x faster                                                  |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                                   |
| scimark_sor                | 87.4 ms                                                | 87.0 ms: 1.00x faster                                                  |
| regex_v8                   | 16.0 ms                                                | 15.9 ms: 1.00x faster                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.71 ms: 1.00x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.02 sec: 1.00x slower                                                 |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| async_generators           | 304 ms                                                 | 306 ms: 1.01x slower                                                   |
| sqlalchemy_declarative     | 62.3 ms                                                | 63.2 ms: 1.01x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 72.8 ms: 1.01x slower                                                  |
| chaos                      | 42.5 ms                                                | 43.5 ms: 1.02x slower                                                  |
| fannkuch                   | 248 ms                                                 | 257 ms: 1.03x slower                                                   |
| pyflate                    | 316 ms                                                 | 327 ms: 1.03x slower                                                   |
| sqlglot_normalize          | 186 ms                                                 | 193 ms: 1.04x slower                                                   |
| sqlglot_parse              | 848 us                                                 | 882 us: 1.04x slower                                                   |
| sympy_sum                  | 77.6 ms                                                | 80.9 ms: 1.04x slower                                                  |
| richards_super             | 36.0 ms                                                | 37.8 ms: 1.05x slower                                                  |
| sympy_str                  | 148 ms                                                 | 155 ms: 1.05x slower                                                   |
| crypto_pyaes               | 51.9 ms                                                | 54.5 ms: 1.05x slower                                                  |
| django_template            | 22.3 ms                                                | 23.5 ms: 1.05x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                 |
| richards                   | 32.1 ms                                                | 34.0 ms: 1.06x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.08 ms: 1.06x slower                                                  |
| sympy_expand               | 241 ms                                                 | 256 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 93.0 us                                                | 101 us: 1.08x slower                                                   |
| hexiom                     | 4.54 ms                                                | 5.05 ms: 1.11x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 38.1 ms: 1.12x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.8 ms: 1.13x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.10 ms: 1.14x slower                                                  |
| coverage                   | 38.9 ms                                                | 44.6 ms: 1.15x slower                                                  |
| telco                      | 3.68 ms                                                | 4.43 ms: 1.20x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.93 ms: 1.22x slower                                                  |
| 2to3                       | 169 ms                                                 | 212 ms: 1.25x slower                                                   |
| bench_mp_pool              | 44.9 ms                                                | 64.2 ms: 1.43x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 14.0 ms: 1.49x slower                                                  |
| python_startup             | 11.4 ms                                                | 18.8 ms: 1.65x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.32 ms: 1.89x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (4): xml_etree_parse, scimark_monte_carlo, mdp, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (18) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 85.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.27x