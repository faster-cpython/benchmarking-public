# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backoff
- machine: darwin-arm64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.030x faster
- HPT reliability: 99.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 177 ms: 1.05x slower                                                 |
| docutils       | 1.50 sec                                               | 1.55 sec: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                                 |
| async_tree_none            | 266 ms                                                 | 206 ms: 1.29x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 254 ms: 1.23x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 218 ms: 1.18x faster                                                 |
| async_tree_io              | 668 ms                                                 | 591 ms: 1.13x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 468 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 479 ms: 1.11x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 627 ms: 1.07x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                |
| nbody          | 68.8 ms                                                | 63.0 ms: 1.09x faster                                                |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.33 ms: 1.13x faster                                                |
| regex_dna      | 154 ms                                                 | 136 ms: 1.13x faster                                                 |
| regex_compile  | 77.9 ms                                                | 73.4 ms: 1.06x faster                                                |
| regex_v8       | 16.0 ms                                                | 15.8 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 122 us: 1.23x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 35.3 ms: 1.12x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 49.8 ms: 1.12x faster                                                |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.11x faster                                               |
| json_loads           | 17.2 us                                                | 16.5 us: 1.04x faster                                                |
| pickle_pure_python   | 200 us                                                 | 194 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 72.0 ms: 1.03x faster                                                |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                                 |
| json_dumps           | 6.22 ms                                                | 7.11 ms: 1.14x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.0 ms: 1.60x slower                                                |
| python_startup         | 11.4 ms                                                | 19.7 ms: 1.72x slower                                                |
| Geometric mean         | (ref)                                                  | 1.66x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 7.71 ms                                                | 6.23 ms: 1.24x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                 |
| deepcopy_memo              | 27.7 us                                                | 17.6 us: 1.57x faster                                                |
| deepcopy                   | 235 us                                                 | 158 us: 1.49x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.34x faster                                                |
| async_tree_none            | 266 ms                                                 | 206 ms: 1.29x faster                                                 |
| mako                       | 7.71 ms                                                | 6.23 ms: 1.24x faster                                                |
| unpickle_pure_python       | 151 us                                                 | 122 us: 1.23x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 254 ms: 1.23x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 218 ms: 1.18x faster                                                 |
| generators                 | 31.1 ms                                                | 26.7 ms: 1.16x faster                                                |
| float                      | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                |
| raytrace                   | 212 ms                                                 | 186 ms: 1.14x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.33 ms: 1.13x faster                                                |
| regex_dna                  | 154 ms                                                 | 136 ms: 1.13x faster                                                 |
| async_tree_io              | 668 ms                                                 | 591 ms: 1.13x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 35.3 ms: 1.12x faster                                                |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 468 ms: 1.12x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 49.8 ms: 1.12x faster                                                |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 479 ms: 1.11x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.11x faster                                               |
| logging_simple             | 3.69 us                                                | 3.33 us: 1.11x faster                                                |
| coroutines                 | 19.2 ms                                                | 17.4 ms: 1.10x faster                                                |
| scimark_lu                 | 76.0 ms                                                | 68.9 ms: 1.10x faster                                                |
| spectral_norm              | 76.4 ms                                                | 69.8 ms: 1.09x faster                                                |
| nbody                      | 68.8 ms                                                | 63.0 ms: 1.09x faster                                                |
| logging_format             | 3.98 us                                                | 3.66 us: 1.09x faster                                                |
| json                       | 3.09 ms                                                | 2.86 ms: 1.08x faster                                                |
| async_tree_io_tg           | 669 ms                                                 | 627 ms: 1.07x faster                                                 |
| comprehensions             | 14.5 us                                                | 13.7 us: 1.06x faster                                                |
| regex_compile              | 77.9 ms                                                | 73.4 ms: 1.06x faster                                                |
| pathlib                    | 24.2 ms                                                | 22.9 ms: 1.06x faster                                                |
| scimark_fft                | 195 ms                                                 | 186 ms: 1.05x faster                                                 |
| sqlalchemy_declarative     | 62.3 ms                                                | 59.4 ms: 1.05x faster                                                |
| bench_thread_pool          | 504 us                                                 | 482 us: 1.05x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.59 ms: 1.04x faster                                                |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.04x faster                                                |
| logging_silent             | 76.4 ns                                                | 73.8 ns: 1.04x faster                                                |
| pprint_safe_repr           | 497 ms                                                 | 480 ms: 1.04x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 194 us: 1.03x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 982 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 72.0 ms: 1.03x faster                                                |
| dulwich_log                | 29.8 ms                                                | 29.1 ms: 1.02x faster                                                |
| sympy_sum                  | 77.6 ms                                                | 75.8 ms: 1.02x faster                                                |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.08 ms: 1.02x faster                                                |
| nqueens                    | 62.4 ms                                                | 61.3 ms: 1.02x faster                                                |
| go                         | 102 ms                                                 | 99.9 ms: 1.02x faster                                                |
| xml_etree_parse            | 106 ms                                                 | 105 ms: 1.01x faster                                                 |
| regex_v8                   | 16.0 ms                                                | 15.8 ms: 1.01x faster                                                |
| pycparser                  | 677 ms                                                 | 672 ms: 1.01x faster                                                 |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.64 ms: 1.01x faster                                                |
| scimark_sor                | 87.4 ms                                                | 87.2 ms: 1.00x faster                                                |
| mdp                        | 1.58 sec                                               | 1.59 sec: 1.00x slower                                               |
| scimark_monte_carlo        | 45.0 ms                                                | 45.2 ms: 1.00x slower                                                |
| async_generators           | 304 ms                                                 | 306 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 72.6 ms: 1.01x slower                                                |
| chaos                      | 42.5 ms                                                | 43.4 ms: 1.02x slower                                                |
| sqlglot_optimize           | 34.0 ms                                                | 34.9 ms: 1.02x slower                                                |
| sqlglot_parse              | 848 us                                                 | 873 us: 1.03x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.55 sec: 1.03x slower                                               |
| sqlglot_transpile          | 1.02 ms                                                | 1.06 ms: 1.03x slower                                                |
| richards_super             | 36.0 ms                                                | 37.3 ms: 1.03x slower                                                |
| pyflate                    | 316 ms                                                 | 328 ms: 1.04x slower                                                 |
| richards                   | 32.1 ms                                                | 33.4 ms: 1.04x slower                                                |
| 2to3                       | 169 ms                                                 | 177 ms: 1.05x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 12.0 ms: 1.05x slower                                                |
| crypto_pyaes               | 51.9 ms                                                | 54.8 ms: 1.06x slower                                                |
| sympy_expand               | 241 ms                                                 | 255 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 99.2 us: 1.07x slower                                                |
| hexiom                     | 4.54 ms                                                | 4.93 ms: 1.08x slower                                                |
| fannkuch                   | 248 ms                                                 | 278 ms: 1.12x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.3 ms: 1.14x slower                                                |
| json_dumps                 | 6.22 ms                                                | 7.11 ms: 1.14x slower                                                |
| telco                      | 3.68 ms                                                | 4.48 ms: 1.22x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.93 ms: 1.22x slower                                                |
| bench_mp_pool              | 44.9 ms                                                | 62.2 ms: 1.39x slower                                                |
| python_startup_no_site     | 9.37 ms                                                | 15.0 ms: 1.60x slower                                                |
| python_startup             | 11.4 ms                                                | 19.7 ms: 1.72x slower                                                |
| create_gc_cycles           | 701 us                                                 | 1.33 ms: 1.90x slower                                                |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (2): sympy_str, django_template
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (18) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.26% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.21x