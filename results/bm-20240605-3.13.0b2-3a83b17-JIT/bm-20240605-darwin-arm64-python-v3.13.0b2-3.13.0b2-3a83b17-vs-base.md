# Results vs. base

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                                                               | 173 ms: 1.07x slower                                                                                     |
| chameleon      | 4.27 ms                                                                                              | 4.41 ms: 1.03x slower                                                                                    |
| docutils       | 1.44 sec                                                                                             | 1.51 sec: 1.05x slower                                                                                   |
| Geometric mean | (ref)                                                                                                | 1.04x slower                                                                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                                                               | 334 ms: 1.01x slower                                                                                     |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                                                               | 364 ms: 1.02x slower                                                                                     |
| async_tree_eager_tg              | 41.4 ms                                                                                              | 42.7 ms: 1.03x slower                                                                                    |
| async_tree_eager                 | 60.3 ms                                                                                              | 63.3 ms: 1.05x slower                                                                                    |
| Geometric mean                   | (ref)                                                                                                | 1.01x slower                                                                                             |

Benchmark hidden because not significant (12): async_tree_eager_io, async_tree_eager_io_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| float          | 48.6 ms                                                                                              | 47.4 ms: 1.03x faster                                                                                    |
| nbody          | 59.6 ms                                                                                              | 63.5 ms: 1.06x slower                                                                                    |
| Geometric mean | (ref)                                                                                                | 1.01x slower                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                                                              | 17.3 ms: 1.00x slower                                                                                    |
| regex_compile  | 68.5 ms                                                                                              | 71.9 ms: 1.05x slower                                                                                    |
| Geometric mean | (ref)                                                                                                | 1.01x slower                                                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                                                             | 1.24 sec: 1.18x faster                                                                                   |
| unpickle_pure_python | 141 us                                                                                               | 132 us: 1.07x faster                                                                                     |
| xml_etree_process    | 37.1 ms                                                                                              | 35.8 ms: 1.03x faster                                                                                    |
| pickle_pure_python   | 179 us                                                                                               | 173 us: 1.03x faster                                                                                     |
| xml_etree_generate   | 52.7 ms                                                                                              | 51.6 ms: 1.02x faster                                                                                    |
| xml_etree_iterparse  | 71.5 ms                                                                                              | 70.5 ms: 1.01x faster                                                                                    |
| json_dumps           | 6.23 ms                                                                                              | 6.17 ms: 1.01x faster                                                                                    |
| unpickle_list        | 2.88 us                                                                                              | 2.88 us: 1.00x faster                                                                                    |
| pickle_dict          | 18.3 us                                                                                              | 18.2 us: 1.00x faster                                                                                    |
| json_loads           | 16.8 us                                                                                              | 16.9 us: 1.00x slower                                                                                    |
| pickle               | 7.48 us                                                                                              | 7.52 us: 1.01x slower                                                                                    |
| pickle_list          | 2.96 us                                                                                              | 2.99 us: 1.01x slower                                                                                    |
| Geometric mean       | (ref)                                                                                                | 1.02x faster                                                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                                                              | 16.4 ms: 1.08x slower                                                                                    |
| python_startup_no_site | 12.3 ms                                                                                              | 13.4 ms: 1.09x slower                                                                                    |
| Geometric mean         | (ref)                                                                                                | 1.09x slower                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| mako            | 6.99 ms                                                                                              | 6.40 ms: 1.09x faster                                                                                    |
| django_template | 19.4 ms                                                                                              | 21.3 ms: 1.10x slower                                                                                    |
| genshi_text     | 13.9 ms                                                                                              | 16.4 ms: 1.18x slower                                                                                    |
| genshi_xml      | 29.9 ms                                                                                              | 39.3 ms: 1.31x slower                                                                                    |
| Geometric mean  | (ref)                                                                                                | 1.12x slower                                                                                             |

All benchmarks:
===============

| Benchmark                        | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.47 sec                                                                                             | 1.24 sec: 1.18x faster                                                                                   |
| mako                             | 6.99 ms                                                                                              | 6.40 ms: 1.09x faster                                                                                    |
| mdp                              | 1.53 sec                                                                                             | 1.43 sec: 1.08x faster                                                                                   |
| fannkuch                         | 248 ms                                                                                               | 233 ms: 1.07x faster                                                                                     |
| unpickle_pure_python             | 141 us                                                                                               | 132 us: 1.07x faster                                                                                     |
| deepcopy_memo                    | 22.6 us                                                                                              | 21.5 us: 1.05x faster                                                                                    |
| xml_etree_process                | 37.1 ms                                                                                              | 35.8 ms: 1.03x faster                                                                                    |
| pickle_pure_python               | 179 us                                                                                               | 173 us: 1.03x faster                                                                                     |
| float                            | 48.6 ms                                                                                              | 47.4 ms: 1.03x faster                                                                                    |
| xml_etree_generate               | 52.7 ms                                                                                              | 51.6 ms: 1.02x faster                                                                                    |
| pyflate                          | 321 ms                                                                                               | 315 ms: 1.02x faster                                                                                     |
| xml_etree_iterparse              | 71.5 ms                                                                                              | 70.5 ms: 1.01x faster                                                                                    |
| json_dumps                       | 6.23 ms                                                                                              | 6.17 ms: 1.01x faster                                                                                    |
| logging_simple                   | 3.04 us                                                                                              | 3.02 us: 1.01x faster                                                                                    |
| richards                         | 31.8 ms                                                                                              | 31.7 ms: 1.00x faster                                                                                    |
| unpickle_list                    | 2.88 us                                                                                              | 2.88 us: 1.00x faster                                                                                    |
| pickle_dict                      | 18.3 us                                                                                              | 18.2 us: 1.00x faster                                                                                    |
| regex_v8                         | 17.3 ms                                                                                              | 17.3 ms: 1.00x slower                                                                                    |
| json_loads                       | 16.8 us                                                                                              | 16.9 us: 1.00x slower                                                                                    |
| gc_traversal                     | 2.45 ms                                                                                              | 2.46 ms: 1.01x slower                                                                                    |
| thrift                           | 435 us                                                                                               | 438 us: 1.01x slower                                                                                     |
| pickle                           | 7.48 us                                                                                              | 7.52 us: 1.01x slower                                                                                    |
| logging_format                   | 3.31 us                                                                                              | 3.33 us: 1.01x slower                                                                                    |
| create_gc_cycles                 | 897 us                                                                                               | 903 us: 1.01x slower                                                                                     |
| telco                            | 4.60 ms                                                                                              | 4.64 ms: 1.01x slower                                                                                    |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                                                               | 334 ms: 1.01x slower                                                                                     |
| pickle_list                      | 2.96 us                                                                                              | 2.99 us: 1.01x slower                                                                                    |
| coroutines                       | 15.8 ms                                                                                              | 16.0 ms: 1.01x slower                                                                                    |
| sqlite_synth                     | 1.55 us                                                                                              | 1.57 us: 1.01x slower                                                                                    |
| pprint_pformat                   | 947 ms                                                                                               | 958 ms: 1.01x slower                                                                                     |
| bpe_tokeniser                    | 3.05 sec                                                                                             | 3.09 sec: 1.01x slower                                                                                   |
| richards_super                   | 35.2 ms                                                                                              | 35.7 ms: 1.01x slower                                                                                    |
| go                               | 101 ms                                                                                               | 102 ms: 1.02x slower                                                                                     |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                                                               | 364 ms: 1.02x slower                                                                                     |
| meteor_contest                   | 70.3 ms                                                                                              | 71.4 ms: 1.02x slower                                                                                    |
| spectral_norm                    | 66.4 ms                                                                                              | 67.5 ms: 1.02x slower                                                                                    |
| deepcopy                         | 204 us                                                                                               | 208 us: 1.02x slower                                                                                     |
| scimark_fft                      | 181 ms                                                                                               | 185 ms: 1.03x slower                                                                                     |
| generators                       | 22.9 ms                                                                                              | 23.6 ms: 1.03x slower                                                                                    |
| async_tree_eager_tg              | 41.4 ms                                                                                              | 42.7 ms: 1.03x slower                                                                                    |
| chameleon                        | 4.27 ms                                                                                              | 4.41 ms: 1.03x slower                                                                                    |
| scimark_monte_carlo              | 42.5 ms                                                                                              | 44.0 ms: 1.04x slower                                                                                    |
| sympy_str                        | 131 ms                                                                                               | 137 ms: 1.04x slower                                                                                     |
| dulwich_log                      | 27.6 ms                                                                                              | 28.8 ms: 1.04x slower                                                                                    |
| sympy_expand                     | 226 ms                                                                                               | 236 ms: 1.04x slower                                                                                     |
| crypto_pyaes                     | 49.5 ms                                                                                              | 51.8 ms: 1.05x slower                                                                                    |
| sympy_sum                        | 69.2 ms                                                                                              | 72.4 ms: 1.05x slower                                                                                    |
| regex_compile                    | 68.5 ms                                                                                              | 71.9 ms: 1.05x slower                                                                                    |
| logging_silent                   | 60.1 ns                                                                                              | 63.1 ns: 1.05x slower                                                                                    |
| async_tree_eager                 | 60.3 ms                                                                                              | 63.3 ms: 1.05x slower                                                                                    |
| scimark_sparse_mat_mult          | 2.77 ms                                                                                              | 2.92 ms: 1.05x slower                                                                                    |
| sympy_integrate                  | 10.3 ms                                                                                              | 10.9 ms: 1.05x slower                                                                                    |
| docutils                         | 1.44 sec                                                                                             | 1.51 sec: 1.05x slower                                                                                   |
| async_generators                 | 281 ms                                                                                               | 296 ms: 1.05x slower                                                                                     |
| sqlglot_optimize                 | 30.9 ms                                                                                              | 32.6 ms: 1.06x slower                                                                                    |
| scimark_sor                      | 94.9 ms                                                                                              | 100 ms: 1.06x slower                                                                                     |
| pycparser                        | 632 ms                                                                                               | 672 ms: 1.06x slower                                                                                     |
| nbody                            | 59.6 ms                                                                                              | 63.5 ms: 1.06x slower                                                                                    |
| typing_runtime_protocols         | 87.6 us                                                                                              | 93.5 us: 1.07x slower                                                                                    |
| hexiom                           | 4.06 ms                                                                                              | 4.36 ms: 1.07x slower                                                                                    |
| 2to3                             | 161 ms                                                                                               | 173 ms: 1.07x slower                                                                                     |
| bench_thread_pool                | 447 us                                                                                               | 481 us: 1.08x slower                                                                                     |
| mypy2                            | 379 ms                                                                                               | 408 ms: 1.08x slower                                                                                     |
| python_startup                   | 15.2 ms                                                                                              | 16.4 ms: 1.08x slower                                                                                    |
| nqueens                          | 52.2 ms                                                                                              | 56.8 ms: 1.09x slower                                                                                    |
| bench_mp_pool                    | 47.2 ms                                                                                              | 51.4 ms: 1.09x slower                                                                                    |
| python_startup_no_site           | 12.3 ms                                                                                              | 13.4 ms: 1.09x slower                                                                                    |
| django_template                  | 19.4 ms                                                                                              | 21.3 ms: 1.10x slower                                                                                    |
| aiohttp                          | 997 us                                                                                               | 1.10 ms: 1.10x slower                                                                                    |
| raytrace                         | 147 ms                                                                                               | 163 ms: 1.11x slower                                                                                     |
| gunicorn                         | 1.04 ms                                                                                              | 1.15 ms: 1.11x slower                                                                                    |
| sqlglot_transpile                | 891 us                                                                                               | 1.00 ms: 1.12x slower                                                                                    |
| sqlglot_parse                    | 732 us                                                                                               | 826 us: 1.13x slower                                                                                     |
| chaos                            | 34.0 ms                                                                                              | 38.9 ms: 1.14x slower                                                                                    |
| deltablue                        | 2.14 ms                                                                                              | 2.47 ms: 1.15x slower                                                                                    |
| scimark_lu                       | 66.9 ms                                                                                              | 78.6 ms: 1.18x slower                                                                                    |
| genshi_text                      | 13.9 ms                                                                                              | 16.4 ms: 1.18x slower                                                                                    |
| comprehensions                   | 10.2 us                                                                                              | 12.2 us: 1.21x slower                                                                                    |
| genshi_xml                       | 29.9 ms                                                                                              | 39.3 ms: 1.31x slower                                                                                    |
| Geometric mean                   | (ref)                                                                                                | 1.03x slower                                                                                             |

Benchmark hidden because not significant (30): async_tree_eager_io, xml_etree_parse, coverage, html5lib, pprint_safe_repr, regex_effbot, regex_dna, flaskblogging, deepcopy_reduce, asyncio_websockets, json, pidigits, async_tree_eager_io_tg, pathlib, asyncio_tcp_ssl, unpickle, dask, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_eager_memoization_tg, async_tree_eager_memoization, tornado_http, asyncio_tcp, pylint
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.21x