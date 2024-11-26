# Results vs. 3.12.0

- fork: python
- ref: faa3272fb8d63d481a13
- machine: darwin-arm64
- commit hash: faa3272
- commit date: 2024-10-29
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 165 ms: 1.03x faster                                                   |
| docutils       | 1.50 sec                                               | 1.41 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                   |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.26x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 469 ms: 1.14x faster                                                   |
| async_tree_io              | 668 ms                                                 | 596 ms: 1.12x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 618 ms: 1.08x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.5 ms: 1.13x faster                                                  |
| nbody          | 68.8 ms                                                | 65.5 ms: 1.05x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.6 ms: 1.13x faster                                                  |
| regex_dna      | 154 ms                                                 | 141 ms: 1.10x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.44 ms: 1.08x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.7 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 184 us: 1.09x faster                                                   |
| xml_etree_generate   | 55.8 ms                                                | 52.7 ms: 1.06x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                   |
| xml_etree_process    | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                  |
| json_loads           | 17.2 us                                                | 16.5 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 73.6 ms: 1.01x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.26 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.2 ms: 1.30x slower                                                  |
| python_startup         | 11.4 ms                                                | 16.8 ms: 1.47x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.38x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.60 ms: 1.17x faster                                                  |
| django_template | 22.3 ms                                                | 19.7 ms: 1.14x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 17.0 us: 1.63x faster                                                  |
| deepcopy                   | 235 us                                                 | 146 us: 1.61x faster                                                   |
| generators                 | 31.1 ms                                                | 20.2 ms: 1.54x faster                                                  |
| raytrace                   | 212 ms                                                 | 154 ms: 1.38x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                  |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                   |
| comprehensions             | 14.5 us                                                | 11.4 us: 1.28x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.26x faster                                                   |
| go                         | 102 ms                                                 | 82.9 ms: 1.22x faster                                                  |
| logging_silent             | 76.4 ns                                                | 62.6 ns: 1.22x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.06 us: 1.21x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.25 ms: 1.20x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 214 ms: 1.20x faster                                                   |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                                  |
| chaos                      | 42.5 ms                                                | 36.3 ms: 1.17x faster                                                  |
| mako                       | 7.71 ms                                                | 6.60 ms: 1.17x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 438 us: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                   |
| nqueens                    | 62.4 ms                                                | 54.7 ms: 1.14x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 743 us: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 469 ms: 1.14x faster                                                   |
| django_template            | 22.3 ms                                                | 19.7 ms: 1.14x faster                                                  |
| regex_compile              | 77.9 ms                                                | 68.6 ms: 1.13x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 907 us: 1.13x faster                                                   |
| float                      | 55.8 ms                                                | 49.5 ms: 1.13x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 67.6 ms: 1.12x faster                                                  |
| async_tree_io              | 668 ms                                                 | 596 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.82 ms: 1.11x faster                                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 56.1 ms: 1.11x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 69.9 ms: 1.11x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 168 ms: 1.10x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 69.5 ms: 1.10x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 27.2 ms: 1.10x faster                                                  |
| sympy_str                  | 148 ms                                                 | 135 ms: 1.10x faster                                                   |
| hexiom                     | 4.54 ms                                                | 4.14 ms: 1.10x faster                                                  |
| async_generators           | 304 ms                                                 | 277 ms: 1.10x faster                                                   |
| regex_dna                  | 154 ms                                                 | 141 ms: 1.10x faster                                                   |
| pprint_safe_repr           | 497 ms                                                 | 458 ms: 1.09x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 184 us: 1.09x faster                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 31.4 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 618 ms: 1.08x faster                                                   |
| pprint_pformat             | 1.01 sec                                               | 935 ms: 1.08x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.44 ms: 1.08x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.47 sec: 1.07x faster                                                 |
| json                       | 3.09 ms                                                | 2.89 ms: 1.07x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.41 sec: 1.06x faster                                                 |
| pycparser                  | 677 ms                                                 | 638 ms: 1.06x faster                                                   |
| sympy_expand               | 241 ms                                                 | 227 ms: 1.06x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 52.7 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                   |
| nbody                      | 68.8 ms                                                | 65.5 ms: 1.05x faster                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.37 ms: 1.05x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.04x faster                                                  |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.51 us: 1.04x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 43.6 ms: 1.03x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.03x faster                                                  |
| richards                   | 32.1 ms                                                | 31.1 ms: 1.03x faster                                                  |
| 2to3                       | 169 ms                                                 | 165 ms: 1.03x faster                                                   |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                                   |
| crypto_pyaes               | 51.9 ms                                                | 51.2 ms: 1.01x faster                                                  |
| meteor_contest             | 71.7 ms                                                | 71.1 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 73.6 ms: 1.01x faster                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| pyflate                    | 316 ms                                                 | 325 ms: 1.03x slower                                                   |
| regex_v8                   | 16.0 ms                                                | 16.7 ms: 1.04x slower                                                  |
| fannkuch                   | 248 ms                                                 | 265 ms: 1.07x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.49 sec: 1.07x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 96.2 ms: 1.10x slower                                                  |
| coverage                   | 38.9 ms                                                | 44.0 ms: 1.13x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.26 ms: 1.17x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.97 ms: 1.24x slower                                                  |
| telco                      | 3.68 ms                                                | 4.64 ms: 1.26x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 12.2 ms: 1.30x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 58.5 ms: 1.30x slower                                                  |
| python_startup             | 11.4 ms                                                | 16.8 ms: 1.47x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.33 ms: 1.90x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (3): typing_runtime_protocols, xml_etree_parse, tornado_http
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (18) of results/bm-20241029-3.14.0a1+-faa3272/bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.078x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.17x