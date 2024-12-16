# Results vs. 3.12.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: darwin-arm64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.061x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 361 ms: 1.86x faster                                                   |
| async_tree_io              | 668 ms                                                 | 378 ms: 1.77x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 154 ms: 1.67x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 193 ms: 1.67x faster                                                   |
| async_tree_none            | 266 ms                                                 | 168 ms: 1.58x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 205 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 419 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 422 ms: 1.25x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.56x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.8 ms: 1.17x faster                                                  |
| nbody          | 68.8 ms                                                | 63.7 ms: 1.08x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.01 ms: 1.31x faster                                                  |
| regex_dna      | 154 ms                                                 | 136 ms: 1.14x faster                                                   |
| regex_compile  | 77.9 ms                                                | 69.5 ms: 1.12x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.0 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 125 us: 1.20x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.21 sec: 1.15x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 49.3 ms: 1.13x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 35.1 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 69.9 ms: 1.06x faster                                                  |
| json_loads           | 17.2 us                                                | 16.5 us: 1.05x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 103 ms: 1.04x faster                                                   |
| pickle_pure_python   | 200 us                                                 | 197 us: 1.01x faster                                                   |
| json_dumps           | 6.22 ms                                                | 7.16 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 16.6 ms: 1.77x slower                                                  |
| python_startup         | 11.4 ms                                                | 21.6 ms: 1.89x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.83x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.26 ms: 1.23x faster                                                  |
| django_template | 22.3 ms                                                | 23.2 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 361 ms: 1.86x faster                                                   |
| async_tree_io              | 668 ms                                                 | 378 ms: 1.77x faster                                                   |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 154 ms: 1.67x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 193 ms: 1.67x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 17.2 us: 1.61x faster                                                  |
| async_tree_none            | 266 ms                                                 | 168 ms: 1.58x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 205 ms: 1.53x faster                                                   |
| deepcopy                   | 235 us                                                 | 158 us: 1.48x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.01 ms: 1.31x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.59 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 419 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 422 ms: 1.25x faster                                                   |
| mako                       | 7.71 ms                                                | 6.26 ms: 1.23x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 62.0 ms: 1.23x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 125 us: 1.20x faster                                                   |
| float                      | 55.8 ms                                                | 47.8 ms: 1.17x faster                                                  |
| raytrace                   | 212 ms                                                 | 184 ms: 1.15x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.21 sec: 1.15x faster                                                 |
| scimark_fft                | 195 ms                                                 | 172 ms: 1.14x faster                                                   |
| regex_dna                  | 154 ms                                                 | 136 ms: 1.14x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 49.3 ms: 1.13x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 35.1 ms: 1.13x faster                                                  |
| regex_compile              | 77.9 ms                                                | 69.5 ms: 1.12x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 68.6 ms: 1.11x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.5 ms: 1.10x faster                                                  |
| generators                 | 31.1 ms                                                | 28.4 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.89 ms: 1.08x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                                  |
| nbody                      | 68.8 ms                                                | 63.7 ms: 1.08x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.43 us: 1.08x faster                                                  |
| json                       | 3.09 ms                                                | 2.88 ms: 1.07x faster                                                  |
| logging_format             | 3.98 us                                                | 3.73 us: 1.07x faster                                                  |
| scimark_sor                | 87.4 ms                                                | 82.2 ms: 1.06x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.55 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 69.9 ms: 1.06x faster                                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.9 ms: 1.06x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.05x faster                                                  |
| comprehensions             | 14.5 us                                                | 14.0 us: 1.04x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 103 ms: 1.04x faster                                                   |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 75.4 ms: 1.03x faster                                                  |
| sympy_str                  | 148 ms                                                 | 144 ms: 1.02x faster                                                   |
| go                         | 102 ms                                                 | 99.7 ms: 1.02x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                  |
| async_generators           | 304 ms                                                 | 300 ms: 1.01x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 197 us: 1.01x faster                                                   |
| logging_silent             | 76.4 ns                                                | 75.7 ns: 1.01x faster                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.64 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 44.8 ms: 1.01x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.57 sec: 1.00x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.01 sec: 1.00x faster                                                 |
| chaos                      | 42.5 ms                                                | 42.4 ms: 1.00x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 498 ms: 1.00x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 34.2 ms: 1.00x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 16.0 ms: 1.00x slower                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                                   |
| sqlglot_parse              | 848 us                                                 | 854 us: 1.01x slower                                                   |
| sqlglot_normalize          | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| pyflate                    | 316 ms                                                 | 319 ms: 1.01x slower                                                   |
| sympy_expand               | 241 ms                                                 | 244 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.03 ms: 1.01x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 72.7 ms: 1.01x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.8 ms: 1.04x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 53.8 ms: 1.04x slower                                                  |
| django_template            | 22.3 ms                                                | 23.2 ms: 1.04x slower                                                  |
| richards_super             | 36.0 ms                                                | 38.4 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 99.5 us: 1.07x slower                                                  |
| richards                   | 32.1 ms                                                | 34.6 ms: 1.08x slower                                                  |
| hexiom                     | 4.54 ms                                                | 4.91 ms: 1.08x slower                                                  |
| fannkuch                   | 248 ms                                                 | 272 ms: 1.09x slower                                                   |
| coverage                   | 38.9 ms                                                | 44.2 ms: 1.14x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.16 ms: 1.15x slower                                                  |
| telco                      | 3.68 ms                                                | 4.46 ms: 1.21x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 3.07 ms: 1.28x slower                                                  |
| mypy2                      | 380 ms                                                 | 526 ms: 1.38x slower                                                   |
| bench_mp_pool              | 44.9 ms                                                | 63.3 ms: 1.41x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 16.6 ms: 1.77x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.28 ms: 1.83x slower                                                  |
| python_startup             | 11.4 ms                                                | 21.6 ms: 1.89x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (4): bench_thread_pool, 2to3, nqueens, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.22x